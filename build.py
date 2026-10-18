#!/usr/bin/env python3
"""Build the static GitHub Pages catalog from the official-source event audit.

The source of truth is data/events.json.  Only rows that are both `verified` and
assigned to the recurring or special bucket can be rendered in public catalog
tables.  Everything else is rendered on Flagged for Review instead.
"""
from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent
DATA_PATH = ROOT / "data" / "events.json"


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def pretty(value: str) -> str:
    return (value or "").replace("-", " ").replace("_", " ").title()


def read_data() -> tuple[dict, list[dict], list[dict]]:
    document = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if not isinstance(document, dict) or not isinstance(document.get("catalog"), dict):
        raise ValueError("data/events.json must contain a catalog object")
    events = document.get("events")
    if not isinstance(events, list):
        raise ValueError("data/events.json must contain an events array")
    flags = document.get("flags", [])
    if not isinstance(flags, list):
        raise ValueError("data/events.json flags must be an array")
    return document["catalog"], events, flags


def validate(catalog: dict, events: list[dict]) -> None:
    required_for_all = {
        "id", "name", "bucket", "category", "source_url", "source_label",
        "source_authority", "status", "review_reason",
    }
    required_for_published = {
        "name", "cadence", "date_text", "location", "organizer",
        "source_url", "source_label", "source_authority",
    }
    ids: set[str] = set()
    for event in events:
        missing = [field for field in required_for_all if field not in event]
        if missing:
            raise ValueError(f"{event.get('id', '<unknown>')} missing {', '.join(missing)}")
        if event["id"] in ids:
            raise ValueError(f"duplicate event id: {event['id']}")
        ids.add(event["id"])
        if not event["source_url"].startswith("https://"):
            raise ValueError(f"{event['id']} does not have an HTTPS source URL")
        is_published = event["status"] == "verified"
        if is_published:
            missing = [field for field in required_for_published if not event.get(field)]
            if missing:
                raise ValueError(f"published {event['id']} missing {', '.join(missing)}")
            if event["bucket"] not in {"recurring", "special"}:
                raise ValueError(f"published {event['id']} has invalid bucket")
        else:
            if event["bucket"] != "review" or not event["review_reason"]:
                raise ValueError(f"review record {event['id']} needs review bucket and reason")
    if catalog.get("geography") != "City and County of San Francisco only":
        raise ValueError("catalog geography statement has changed unexpectedly")


def sort_regular(event: dict) -> tuple:
    ranks = {"weekly": 0, "seasonal": 1, "annual": 2}
    return (ranks.get(event.get("cadence"), 9), event["category"], event["name"])


def sort_special(event: dict) -> tuple:
    return (event.get("start_date") or "9999-99-99", event["name"])


def sort_all(event: dict) -> tuple:
    return (0 if event["bucket"] == "recurring" else 1, event["category"], event["name"])


def empty_cell() -> str:
    return '<span class="empty" title="Not stated in the linked source">—</span>'


def value_cell(value: str) -> str:
    return esc(value) if value else empty_cell()


def source_cell(event: dict) -> str:
    return (
        f'<a class="source-link" href="{esc(event["source_url"])}" target="_blank" '
        f'rel="noopener noreferrer">Official source ↗</a>'
        f'<span class="source-meta">{esc(event["source_label"])}</span>'
        f'<span class="authority">{esc(event["source_authority"])}</span>'
    )


def status_badge(status: str) -> str:
    labels = {
        "partial_sf_program": "Partial SF program",
        "needs_review": "Needs review",
        "cancelled": "Cancelled",
        "outside_city_excluded": "Outside city — excluded",
    }
    label = labels.get(status, pretty(status))
    return f'<span class="badge badge-{esc(status)}">{esc(label)}</span>'


def bucket_badge(bucket: str) -> str:
    label = "Regularly occurring" if bucket == "recurring" else "Special"
    return f'<span class="badge badge-{esc(bucket)}">{label}</span>'


def event_table(events: list[dict], *, include_bucket: bool = False) -> str:
    headers = ["Event", "Cadence", "Category", "Date / cadence", "Time", "SF location", "Admission", "Official source"]
    if include_bucket:
        headers.insert(1, "List")
    output = [
        '<div class="table-wrap">',
        '<table>',
        '<caption>Official-source event catalog. Optional values show an em dash when not stated in the linked source.</caption>',
        '<thead><tr>' + "".join(f"<th scope=\"col\">{header}</th>" for header in headers) + "</tr></thead>",
        "<tbody>",
    ]
    for event in events:
        cells = [
            f'<td><strong>{esc(event["name"])}</strong><span class="organizer">{esc(event["organizer"])}</span></td>',
            f'<td>{esc(pretty(event["cadence"]))}</td>',
            f'<td>{esc(event["category"])}</td>',
            f'<td>{value_cell(event.get("date_text", ""))}</td>',
            f'<td>{value_cell(event.get("time_text", ""))}</td>',
            f'<td>{value_cell(event.get("location", ""))}</td>',
            f'<td>{value_cell(event.get("admission", ""))}</td>',
            f'<td>{source_cell(event)}</td>',
        ]
        if include_bucket:
            cells.insert(1, f'<td>{bucket_badge(event["bucket"])}</td>')
        output.append("<tr>" + "".join(cells) + "</tr>")
    output.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(output)


def review_table(events: list[dict]) -> str:
    output = [
        '<div class="table-wrap">',
        '<table class="review-table">',
        '<caption>Items intentionally excluded from the city-only event tables until the noted issue is resolved.</caption>',
        '<thead><tr><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Captured date</th><th scope="col">Captured location</th><th scope="col">Why it is flagged</th><th scope="col">Official source</th></tr></thead>',
        "<tbody>",
    ]
    for event in events:
        output.append(
            "<tr>"
            f'<td><strong>{esc(event["name"])}</strong><span class="organizer">{esc(event["organizer"])}</span></td>'
            f'<td>{status_badge(event["status"])}</td>'
            f'<td>{value_cell(event.get("date_text", ""))}</td>'
            f'<td>{value_cell(event.get("location", ""))}</td>'
            f'<td>{esc(event["review_reason"])}</td>'
            f'<td>{source_cell(event)}</td>'
            "</tr>"
        )
    output.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(output)


def flags_table(flags: list[dict]) -> str:
    if not flags:
        return ""
    output = [
        '<div class="table-wrap">',
        '<table class="review-table">',
        '<caption>Field-level flags on published and excluded rows: corrections applied, source problems, and residual discrepancies. Sources are linked so every flag can be checked manually.</caption>',
        '<thead><tr><th scope="col">Event</th><th scope="col">Finding</th><th scope="col">Sources to check</th><th scope="col">Disposition</th></tr></thead>',
        "<tbody>",
    ]
    for flag in flags:
        sources = "".join(
            f'<a class="source-link" href="{html.escape(source["url"], quote=True)}" target="_blank" rel="noopener">{esc(source["label"])}</a>'
            for source in flag.get("sources", [])
        )
        output.append(
            "<tr>"
            f'<td><strong>{esc(flag["event"])}</strong></td>'
            f'<td>{esc(flag["issue"])}</td>'
            f"<td>{sources}</td>"
            f'<td>{esc(flag["disposition"])}</td>'
            "</tr>"
        )
    output.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(output)


STYLE = """
:root{--ink:#17212b;--muted:#526171;--paper:#fff;--mist:#f4f7fa;--line:#d9e2ea;--navy:#103c5b;--blue:#126da6;--teal:#0e766e;--gold:#8f6200;--rose:#9a3131;--shadow:0 8px 24px rgba(19,48,71,.08)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--mist);line-height:1.5}a{color:#075f99}a:hover{color:#064b78}.site-header{color:#fff;background:linear-gradient(120deg,#0d314a,#155d83 55%,#168178);padding:2.4rem 1.25rem 2rem}.shell{max-width:1240px;margin:0 auto;padding:0 1.25rem}.site-header .shell{padding:0;position:relative}.eyebrow{font-size:.77rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#b9e9e4;margin:0 0 .4rem}.site-header h1{margin:0;font-size:clamp(2rem,5vw,3.5rem);letter-spacing:-.045em}.lede{max-width:850px;margin:.7rem 0 0;font-size:1.06rem;color:#e7f4f5}.main{padding-top:1.2rem;padding-bottom:2rem}.nav{display:flex;gap:.55rem;flex-wrap:wrap;margin:0 0 1.5rem}.nav a{text-decoration:none;color:var(--navy);background:var(--paper);border:1px solid var(--line);border-radius:99px;padding:.48rem .77rem;font-weight:700;font-size:.9rem}.nav a.active,.nav a:hover{background:var(--navy);border-color:var(--navy);color:#fff}.hero{display:grid;gap:1rem;grid-template-columns:minmax(0,1.65fr) minmax(260px,.85fr);margin-bottom:1.25rem}.panel,.card{background:var(--paper);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow)}.panel{padding:1.35rem}.panel h2,.panel h3{margin-top:0}.panel p:last-child{margin-bottom:0}.snapshot{background:#eaf5f4;border-color:#bde0dc}.snapshot strong{display:block;font-size:2rem;color:var(--teal);letter-spacing:-.04em}.snapshot small{color:var(--muted)}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.85rem;margin:1rem 0 1.4rem}.card{padding:1rem;text-decoration:none;color:inherit;transition:transform .15s ease,box-shadow .15s ease}.card:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(19,48,71,.14)}.metric{font-size:2rem;font-weight:800;letter-spacing:-.06em;color:var(--navy);display:block}.card-label{display:block;font-weight:750}.card-note{display:block;color:var(--muted);font-size:.85rem;margin-top:.25rem}.notice{padding:1rem 1.1rem;background:#fff7dc;border:1px solid #efd58c;border-radius:12px;margin:1rem 0}.notice strong{color:#715200}.notice a{font-weight:700}.section-head{display:flex;gap:1rem;align-items:baseline;justify-content:space-between;flex-wrap:wrap;margin-top:1.75rem}.section-head h2{margin:0}.section-head p{margin:0;color:var(--muted)}.filterbar{display:flex;gap:.65rem;align-items:center;flex-wrap:wrap;background:var(--paper);border:1px solid var(--line);padding:.8rem;border-radius:12px;margin:.85rem 0}.filterbar label{font-weight:700;font-size:.9rem}.filterbar input,.filterbar select{font:inherit;padding:.55rem .65rem;border:1px solid #aebdc9;border-radius:8px;background:#fff}.filterbar input{min-width:min(100%,360px);flex:1}.filterbar select{max-width:100%}.table-wrap{overflow:auto;border:1px solid var(--line);border-radius:14px;background:#fff}.table-wrap table{width:100%;min-width:960px;border-collapse:collapse;font-size:.88rem}.table-wrap caption{padding:.8rem 1rem;text-align:left;color:var(--muted);background:#f8fafb;border-bottom:1px solid var(--line);font-size:.82rem}.table-wrap th,.table-wrap td{padding:.72rem .72rem;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}.table-wrap th{font-size:.75rem;letter-spacing:.04em;text-transform:uppercase;color:#405262;background:#edf3f7;position:sticky;top:0;z-index:1}.table-wrap tr:last-child td{border-bottom:0}.table-wrap tbody tr:hover{background:#f7fbfd}.organizer,.source-meta,.authority{display:block;font-size:.78rem;color:var(--muted);margin-top:.16rem}.source-link{font-weight:800;white-space:nowrap}.authority{font-size:.72rem}.empty{color:#6d7a87}.badge{display:inline-block;border-radius:999px;padding:.22rem .5rem;font-size:.74rem;font-weight:800;line-height:1.2}.badge-recurring{color:#075b54;background:#dff5ef}.badge-special{color:#6e4700;background:#fff0c5}.badge-partial_sf_program{color:#634201;background:#fff0c5}.badge-needs_review{color:#80430a;background:#ffe8cf}.badge-cancelled{color:#892d2d;background:#ffe1e1}.badge-outside_city_excluded{color:#5d4a75;background:#eee8f8}.review-table td:nth-child(5){min-width:280px}.category-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.85rem}.category-card{padding:1.05rem;background:#fff;border:1px solid var(--line);border-radius:14px;text-decoration:none;color:inherit}.category-card:hover{box-shadow:var(--shadow);border-color:#9fb9cb}.category-card .metric{font-size:1.6rem}.definition{margin:.4rem 0 0;color:var(--muted);font-size:.9rem}.analysis-list{padding-left:1.2rem}.analysis-list li{margin:.5rem 0}.site-footer{border-top:1px solid var(--line);background:#fff;padding:1.5rem 0 2rem;color:var(--muted);font-size:.88rem}.site-footer p{max-width:1000px;margin:.2rem 0}.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;padding:.6rem;background:#fff;color:#000;z-index:10}@media(max-width:720px){.hero{grid-template-columns:1fr}.site-header{padding-top:1.7rem}.shell{padding:0 1rem}.table-wrap table{font-size:.84rem}.nav{gap:.4rem}.nav a{font-size:.82rem;padding:.42rem .62rem}}
""".strip()


def nav(active: str, prefix: str = "") -> str:
    items = [
        ("index.html", "Dashboard"),
        ("recurring.html", "Regularly occurring"),
        ("special.html", "Special events"),
        ("categories.html", "Categories"),
        ("all-events.html", "All events"),
        ("flagged.html", "Flagged for Review"),
        ("method.html", "Method & sources"),
    ]
    return '<nav class="nav" aria-label="Primary">' + "".join(
        f'<a class="{"active" if href == active else ""}" href="{prefix}{href}">{label}</a>'
        for href, label in items
    ) + "</nav>"


def page(title: str, body: str, active: str, catalog: dict, *, prefix: str = "") -> str:
    audit_href = f"{prefix}research/official-source-audit.md"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Official-source San Francisco city events catalog, separated into regularly occurring and special events.">
  <title>{esc(title)} · San Francisco Events</title>
  <link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="site-header"><div class="shell">
  <p class="eyebrow">Official-source catalog · {esc(catalog['as_of'])}</p>
  <h1>San Francisco Events</h1>
  <p class="lede">City and County of San Francisco only. Regularly occurring events are separated from one-off or dated special events; every listed row links to the source used for verification.</p>
</div></header>
<main id="content" class="shell main">
{nav(active, prefix)}
{body}
</main>
<footer class="site-footer"><div class="shell">
  <p><strong>Scope:</strong> {esc(catalog['coverage'])}</p>
  <p>{esc(catalog['field_policy'])} Read the <a href="{prefix}method.html">method and findings</a> or the row-level <a href="{audit_href}">source audit</a>.</p>
</div></footer>
<script>
for (const table of document.querySelectorAll('[data-filter-table]')) {{
  const input = document.querySelector(`#${{table.dataset.search}}`);
  const select = document.querySelector(`#${{table.dataset.category}}`);
  const filter = () => {{
    const term = (input?.value || '').toLowerCase();
    const category = select?.value || '';
    for (const row of table.tBodies[0].rows) {{
      const matchText = !term || row.textContent.toLowerCase().includes(term);
      const matchCategory = !category || row.dataset.category === category;
      row.hidden = !(matchText && matchCategory);
    }}
  }};
  input?.addEventListener('input', filter); select?.addEventListener('change', filter);
}}
</script>
</body>
</html>"""


def filter_controls(categories: list[str], *, key: str) -> str:
    options = "".join(f'<option value="{esc(category)}">{esc(category)}</option>' for category in categories)
    return f"""<div class="filterbar" aria-label="Filter events">
  <label for="search-{key}">Search</label>
  <input id="search-{key}" type="search" placeholder="Event, organizer, place, or category">
  <label for="category-{key}">Category</label>
  <select id="category-{key}"><option value="">All categories</option>{options}</select>
</div>"""


def mark_filter_table(markup: str, *, key: str) -> str:
    # The generated table has one tbody and event category values are inserted by the builder below.
    markup = markup.replace('<table>', f'<table data-filter-table data-search="search-{key}" data-category="category-{key}">', 1)
    return markup


def table_with_filter_rows(events: list[dict], *, key: str, include_bucket: bool = False) -> str:
    markup = event_table(events, include_bucket=include_bucket)
    for event in events:
        needle = f'<tr><td><strong>{esc(event["name"])}</strong>'
        replacement = f'<tr data-category="{esc(event["category"])}"><td><strong>{esc(event["name"])}</strong>'
        markup = markup.replace(needle, replacement, 1)
    return mark_filter_table(markup, key=key)


def write_csv(events: list[dict]) -> None:
    fields = [
        "id", "name", "bucket", "cadence", "category", "date_text", "start_date", "end_date",
        "time_text", "location", "organizer", "admission", "source_label", "source_url",
        "source_authority", "status", "review_reason", "notes",
    ]
    with (ROOT / "data" / "events.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows([{field: event.get(field, "") for field in fields} for event in events])


def build() -> None:
    catalog, events, flags = read_data()
    validate(catalog, events)
    published = [event for event in events if event["status"] == "verified"]
    recurring = sorted([event for event in published if event["bucket"] == "recurring"], key=sort_regular)
    special = sorted([event for event in published if event["bucket"] == "special"], key=sort_special)
    all_events = sorted(published, key=sort_all)
    review = sorted([event for event in events if event["status"] != "verified"], key=lambda event: (event["status"], event["name"]))
    categories = sorted({event["category"] for event in published})
    category_counts = Counter(event["category"] for event in published)
    cadence_counts = Counter(event["cadence"] for event in recurring)
    authority_counts = Counter(event["source_authority"] for event in published)

    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "style.css").write_text(STYLE + "\n", encoding="utf-8")
    (ROOT / "categories").mkdir(exist_ok=True)

    category_cards = "".join(
        f'''<a class="card" href="categories/{slugify(category)}.html"><span class="metric">{category_counts[category]}</span><span class="card-label">{esc(category)}</span><span class="card-note">Open category page →</span></a>'''
        for category in categories
    )
    home = f"""
<section class="hero">
  <div class="panel">
    <p class="eyebrow" style="color:#0e766e">Snapshot, not an exhaustive calendar</p>
    <h2>A source-audited city events catalog</h2>
    <p>Use the two primary lists to distinguish events that recur weekly, seasonally, or annually from dated special events. Every active row has its own official source link. A separate review register preserves uncertain, cancelled, multi-city, and outside-city items instead of silently normalizing them.</p>
    <p><a href="recurring.html"><strong>Browse regularly occurring events →</strong></a> &nbsp; <a href="special.html"><strong>Browse special events →</strong></a></p>
  </div>
  <aside class="panel snapshot"><strong>{len(published)}</strong><span>published city-only rows</span><br><small>Checked {esc(catalog['as_of'])}; {len(review)} items are explicitly held for review.</small></aside>
</section>
<section aria-labelledby="at-a-glance"><div class="section-head"><h2 id="at-a-glance">At a glance</h2><p>Counts are derived directly from the verified dataset.</p></div>
<div class="cards">
  <a class="card" href="recurring.html"><span class="metric">{len(recurring)}</span><span class="card-label">Regularly occurring</span><span class="card-note">Weekly, seasonal, and annual traditions</span></a>
  <a class="card" href="special.html"><span class="metric">{len(special)}</span><span class="card-label">Special events</span><span class="card-note">Dated programs and one-off conferences</span></a>
  <a class="card" href="categories.html"><span class="metric">{len(categories)}</span><span class="card-label">Categories</span><span class="card-note">Each has its own table page</span></a>
  <a class="card" href="flagged.html"><span class="metric">{len(review)}</span><span class="card-label">Flagged for review</span><span class="card-note">Never mixed into city-only results</span></a>
</div></section>
<section aria-labelledby="category-summary"><div class="section-head"><h2 id="category-summary">Browse by category</h2><p>Each card opens a source-linked category table.</p></div><div class="cards">{category_cards}</div></section>
<section class="panel" aria-labelledby="findings"><h2 id="findings">What this catalog supports</h2>
<ul class="analysis-list">
  <li><strong>{cadence_counts['weekly']} weekly</strong>, <strong>{cadence_counts['seasonal']} seasonal</strong>, and <strong>{cadence_counts['annual']} annual</strong> entries make up the regularly occurring list; it is not limited to weekly events.</li>
  <li><strong>Community &amp; culture ({category_counts['Community & culture']})</strong>, <strong>Food &amp; markets ({category_counts['Food & markets']})</strong>, and <strong>Music &amp; performing arts ({category_counts['Music & performing arts']})</strong> are the largest documented categories in this audit snapshot.</li>
  <li>The rows link to <strong>{authority_counts['Official organizer']} official organizer</strong>, <strong>{authority_counts['Government source']} government</strong>, <strong>{authority_counts['Official venue / federal trust']} official-venue/federal-trust</strong>, and <strong>{authority_counts['Trusted civic source']} trusted civic</strong> sources. This is an audit of stated sources, not an assertion that it finds every event in the city.</li>
</ul></section>
<section class="notice"><strong>Planning note.</strong> Dates and operational details change. Use the source link in the row as the final check before attending. An em dash means the linked source did not state that optional field in the captured audit; essential gaps go to <a href="flagged.html">Flagged for Review</a>.</section>
"""
    (ROOT / "index.html").write_text(page("Dashboard", home, "index.html", catalog), encoding="utf-8")

    recurring_body = f"""
<section class="section-head"><div><h2>Regularly occurring events</h2><p>Weekly, seasonal, and annual programs with a recurring cadence stated by the source.</p></div><p>{len(recurring)} verified rows</p></section>
{filter_controls(categories, key='recurring')}
{table_with_filter_rows(recurring, key='recurring')}
<section class="notice"><strong>Why annual events are here:</strong> the task separates regular patterns from dated special events. A tradition is listed here only when the source supports an annual/weekly/seasonal cadence; the exact audited date remains in the row.</section>
"""
    (ROOT / "recurring.html").write_text(page("Regularly occurring events", recurring_body, "recurring.html", catalog), encoding="utf-8")

    special_body = f"""
<section class="section-head"><div><h2>Special events</h2><p>Dated programs, single-event conferences, and one-off calendar listings. No recurrence is inferred.</p></div><p>{len(special)} verified rows</p></section>
{filter_controls(categories, key='special')}
{table_with_filter_rows(special, key='special')}
"""
    special_markup = page("Special events", special_body, "special.html", catalog)
    (ROOT / "special.html").write_text(special_markup, encoding="utf-8")
    (ROOT / "annual-special.html").write_text(page("Annual / Special events", special_body, "special.html", catalog), encoding="utf-8")

    all_body = f"""
<section class="section-head"><div><h2>All published city-only events</h2><p>Search across the {len(all_events)} records or narrow by category.</p></div><p>Every row has a source link.</p></section>
{filter_controls(categories, key='all')}
{table_with_filter_rows(all_events, key='all', include_bucket=True)}
"""
    (ROOT / "all-events.html").write_text(page("All published events", all_body, "all-events.html", catalog), encoding="utf-8")

    categories_body = "".join(
        f'''<a class="category-card" href="categories/{slugify(category)}.html"><span class="metric">{category_counts[category]}</span><strong>{esc(category)}</strong><p class="definition">Source-linked city event rows in this category.</p></a>'''
        for category in categories
    )
    (ROOT / "categories.html").write_text(page("Categories", f"<section class=\"section-head\"><div><h2>Category pages</h2><p>Open a category to review its source-linked city-only event rows.</p></div></section><div class=\"category-grid\">{categories_body}</div>", "categories.html", catalog), encoding="utf-8")

    for category in categories:
        category_events = sorted([event for event in all_events if event["category"] == category], key=lambda event: event["name"])
        category_body = f"""
<section class="section-head"><div><p><a href="../categories.html">← All categories</a></p><h2>{esc(category)}</h2><p>{len(category_events)} verified city-only event rows, each with its own official source link.</p></div></section>
{event_table(category_events, include_bucket=True)}
"""
        (ROOT / "categories" / f"{slugify(category)}.html").write_text(
            page(category, category_body, "categories.html", catalog, prefix="../"), encoding="utf-8"
        )

    flagged_body = f"""
<section class="section-head"><div><h2>Flagged for Review</h2><p>These records are intentionally excluded from the city-only recurring and special tables.</p></div><p>{len(review)} review records · {len(flags)} field-level flags</p></section>
<section class="notice"><strong>What a flag means:</strong> a source may be official and still be unsuitable for a city-only row — for example, a multi-city program, an official cancellation, or an unresolved schedule. Fields stay blank when not confirmed; nothing below is silently promoted into the catalog.</section>
{review_table(review)}
<section class="section-head"><div><h2>Field-level flags and source findings</h2><p>Corrections applied to published rows, source-availability problems, and residual discrepancies that merit manual review. Each finding links the sources used.</p></div><p>{len(flags)} findings</p></section>
{flags_table(flags)}
"""
    (ROOT / "flagged.html").write_text(page("Flagged for Review", flagged_body, "flagged.html", catalog), encoding="utf-8")

    method_body = f"""
<section class="section-head"><div><h2>Method, sources, and findings</h2><p>A reproducible snapshot of publicly advertised San Francisco city events.</p></div></section>
<section class="panel"><h3>Publish rule</h3><ol>
<li>Each active row needs a title, source-stated date/cadence, San Francisco city location, organizer, and HTTPS source link.</li>
<li>Accepted sources are official organizers, official venues, government sources, and clearly labeled trusted civic sources. The source type is visible in every row.</li>
<li>Optional time and admission fields are not inferred. An em dash means the captured source did not state that optional value.</li>
<li>Multi-city programs, cancelled events, outside-city events, and records missing essential evidence are not added to public tables. They stay on <a href="flagged.html">Flagged for Review</a> with a source and explanation.</li>
</ol></section>
<section class="panel"><h3>Findings, bounded by this dataset</h3><ul class="analysis-list">
<li>The audit has {len(recurring)} recurring and {len(special)} dated-special verified rows across {len(categories)} categories.</li>
<li>{cadence_counts['annual']} recurring rows are annual traditions, alongside {cadence_counts['weekly']} weekly and {cadence_counts['seasonal']} seasonal programs. The classification is based on cadence, not whether an event is free or public.</li>
<li>The catalog has the most audited rows in Community &amp; culture, Food &amp; markets, and Music &amp; performing arts. This describes the verified source set, not all activity in San Francisco.</li>
<li>The review register makes scope and cancellation decisions visible instead of deleting difficult records or asserting unsupported city-only coverage.</li>
</ul></section>
<section class="panel"><h3>Audit trail and maintenance</h3><p>The complete row-level research matrix is in <a href="research/official-source-audit.md">research/official-source-audit.md</a>. The machine-readable source of truth is <a href="data/events.json">data/events.json</a>; <a href="data/events.csv">data/events.csv</a> is an export. Before changing a row, re-check the official source and update the review reason when evidence is incomplete or conflicting.</p><p>This site is intentionally not an exhaustive claim: private, newly announced, or unlisted events can exist outside this dated source audit.</p></section>
"""
    (ROOT / "method.html").write_text(page("Method & sources", method_body, "method.html", catalog), encoding="utf-8")

    write_csv(events)
    print(f"Built {len(published)} published events: {len(recurring)} recurring, {len(special)} special, {len(categories)} categories; {len(review)} review records.")


if __name__ == "__main__":
    build()
