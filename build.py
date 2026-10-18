#!/usr/bin/env python3
"""Build the static GitHub Pages catalog from the official-source event audit.

The source of truth is data/events.json.  Only rows that are both `verified` and
assigned to the recurring or special bucket can be rendered in public catalog
tables.  Everything else is rendered on Flagged for Review instead.

Design rules implemented here
-----------------------------
* Date-first ordering.  Every list is ordered "upcoming first, soonest first",
  so the events closest to today are at the top.  A client-side script re-sorts
  and re-badges every row against the visitor's real current date, so the page
  stays correct after the static build.
* Cost is always visible.  The Admission value is classified from the sourced
  text only (free / paid / mixed / not stated) and rendered as an explicit cost
  label.  "Not stated" is never shown as, or treated as, free.
* Every row carries an official source link.
"""
from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).parent
DATA_PATH = ROOT / "data" / "events.json"

FREE_ADMISSION = "Free"

NAV_ITEMS = [
    ("index.html", "Dashboard"),
    ("upcoming.html", "Upcoming"),
    ("free.html", "Free upcoming"),
    ("paid.html", "Paid & partly free"),
    ("recurring.html", "Regularly occurring"),
    ("special.html", "Special events"),
    ("categories.html", "Categories"),
    ("all-events.html", "All events"),
    ("flagged.html", "Flagged for Review"),
    ("method.html", "Method & sources"),
]


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
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


# --------------------------------------------------------------------------- #
# cost classification — derived from the sourced admission text only
# --------------------------------------------------------------------------- #
# Markers taken only from the wording of the sourced admission text.
FREE_HINTS = ("free", "no-cost", "no cost", "suggested")
PAID_HINTS = ("$", "tickets sold", "pass", "paid entry")
# A free statement that also names a ticketed/paid option is "mixed", not "free".
TICKETED_HINTS = ("ticketed", "tickets sold", "reserved", "seating tickets", "hospitality packages")


def cost_class(admission: str) -> str:
    """Classify sourced admission wording; registration alone is not a price."""
    text = (admission or "").strip().lower()
    if not text or "no fundraising minimum" in text:
        # A waived fundraising minimum is not proof that admission costs $0.
        return "not-stated"
    has_free = any(hint in text for hint in FREE_HINTS)
    if has_free:
        if "$" in text or any(hint in text for hint in TICKETED_HINTS):
            return "mixed"
        return "free"
    if any(hint in text for hint in PAID_HINTS):
        return "paid"
    # Do not turn an unfamiliar non-empty description into an invented price.
    return "not-stated"


COST_LABELS = {
    "free": "Free",
    "paid": "Paid / ticketed",
    "mixed": "Free or partly ticketed",
    "not-stated": "Not stated",
}


def cost_cell(event: dict) -> str:
    admission = (event.get("admission") or "").strip()
    kind = cost_class(admission)
    label = COST_LABELS[kind]
    if kind == "not-stated":
        return (
            '<span class="cost cost-unknown" title="Free admission is not confirmed by the linked source">'
            "Not stated</span>" + (f'<span class="cost-detail">{esc(admission)}</span>' if admission else "")
        )
    text = f'<span class="cost cost-{kind}">{esc(label)}</span>'
    if admission:
        text += f'<span class="cost-detail">{esc(admission)}</span>'
    if event.get("admission_source_url"):
        text += f'<a class="evidence-link" href="{esc(event["admission_source_url"])}" target="_blank" rel="noopener noreferrer">Admission evidence ↗</a>'
    return text


# --------------------------------------------------------------------------- #
# date status — build-time value from the audit date, refreshed live in the browser
# --------------------------------------------------------------------------- #
def event_status(event: dict, as_of: date) -> str:
    end = event.get("end_date") or event.get("start_date") or ""
    if not end:
        return "undated"
    try:
        end_date = date.fromisoformat(end)
    except ValueError:
        return "undated"
    return "upcoming" if end_date >= as_of else "completed"


STATUS_LABELS = {
    "upcoming": "Upcoming",
    "completed": "Completed",
    "undated": "Date not published",
}


def status_badge(event: dict, as_of: date) -> str:
    status = event_status(event, as_of)
    label = STATUS_LABELS[status]
    return f'<span class="badge status-{status}">{esc(label)}</span>'


def sort_key(event: dict, as_of: date) -> tuple:
    """Upcoming first, then soonest start date, then name."""
    status = event_status(event, as_of)
    group = 0 if status == "upcoming" else (1 if status == "undated" else 2)
    start = event.get("start_date") or event.get("end_date") or ""
    return (group, start or "9999-99-99", event.get("name", "").lower())


def sort_regular(event: dict) -> tuple:
    ranks = {"weekly": 0, "monthly": 1, "seasonal": 2, "annual": 3}
    return (ranks.get(event.get("cadence"), 9), event.get("name", "").lower())


def source_cell(event: dict) -> str:
    return (
        f'<a class="source-link" href="{esc(event["source_url"])}" target="_blank" '
        f'rel="noopener noreferrer">Source ↗</a>'
        f'<span class="source-meta">{esc(event["source_label"])}</span>'
        f'<span class="authority">{esc(event["source_authority"])}</span>'
    )


def review_badge(status: str) -> str:
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
    return f'<span class="badge badge-{esc(bucket)}">{esc(label)}</span>'


# --------------------------------------------------------------------------- #
# tables
# --------------------------------------------------------------------------- #
def event_table(events: list[dict], *, as_of: date, include_bucket: bool = False) -> str:
    headers = ["Event", "Cadence", "Category", "Date / cadence", "Time", "SF location", "Cost", "Source"]
    if include_bucket:
        headers.insert(1, "List")
    output = [
        '<div class="table-wrap">',
        "<table>",
        "<caption>Official-source event catalog, ordered with upcoming dates first. "
        "An em dash means the linked source did not state that optional field in the captured audit; "
        "“Not stated” in the Cost column means admission cost was not established (it does not mean free).</caption>",
        "<thead><tr>" + "".join(f'<th scope="col">{header}</th>' for header in headers) + "</tr></thead>",
        "<tbody>",
    ]
    for event in events:
        start = event.get("start_date") or ""
        end = event.get("end_date") or ""
        rel = f'<span class="rel" data-start="{esc(start)}" data-end="{esc(end)}"></span>'
        cells = [
            f'<td data-label="Event"><strong>{esc(event["name"])}</strong>'
            f'<span class="organizer">{esc(event["organizer"])}</span>'
            f"{status_badge(event, as_of)}</td>",
            f'<td data-label="Cadence">{esc(pretty(event["cadence"]))}</td>',
            f'<td data-label="Category">{esc(event["category"])}</td>',
            f'<td data-label="Date">{esc(event.get("date_text", ""))}{rel}</td>',
            f'<td data-label="Time">{esc(event.get("time_text", "")) or "<span class=empty>—</span>"}</td>',
            f'<td data-label="Location">{esc(event.get("location", ""))}</td>',
            f'<td data-label="Cost">{cost_cell(event)}</td>',
            f'<td data-label="Source">{source_cell(event)}</td>',
        ]
        if include_bucket:
            cells.insert(1, f'<td data-label="List">{bucket_badge(event["bucket"])}</td>')
        output.append("<tr>" + "".join(cells) + "</tr>")
    output.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(output)


def review_table(events: list[dict]) -> str:
    output = [
        '<div class="table-wrap">',
        '<table class="review-table">',
        "<caption>Items intentionally excluded from the city-only event tables until the noted issue is resolved.</caption>",
        '<thead><tr><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Captured date</th>'
        '<th scope="col">Captured location</th><th scope="col">Why it is flagged</th><th scope="col">Source</th></tr></thead>',
        "<tbody>",
    ]
    for event in events:
        output.append(
            "<tr>"
            f'<td data-label="Item"><strong>{esc(event["name"])}</strong><span class="organizer">{esc(event["organizer"])}</span></td>'
            f'<td data-label="Status">{review_badge(event["status"])}</td>'
            f'<td data-label="Captured date">{esc(event.get("date_text", "")) or "<span class=empty>—</span>"}</td>'
            f'<td data-label="Captured location">{esc(event.get("location", "")) or "<span class=empty>—</span>"}</td>'
            f'<td data-label="Why it is flagged">{esc(event["review_reason"])}</td>'
            f'<td data-label="Source">{source_cell(event)}</td>'
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
        "<caption>Field-level flags on published and excluded rows: corrections applied, source problems, "
        "and residual discrepancies. Sources are linked so every flag can be checked manually.</caption>",
        '<thead><tr><th scope="col">Event</th><th scope="col">Finding</th><th scope="col">Sources to check</th>'
        '<th scope="col">Disposition</th></tr></thead>',
        "<tbody>",
    ]
    for flag in flags:
        sources = "".join(
            f'<a class="source-link" href="{html.escape(source["url"], quote=True)}" target="_blank" '
            f'rel="noopener noreferrer">{esc(source["label"])}</a>'
            for source in flag.get("sources", [])
        )
        output.append(
            "<tr>"
            f'<td data-label="Event"><strong>{esc(flag["event"])}</strong></td>'
            f'<td data-label="Finding">{esc(flag["issue"])}</td>'
            f'<td data-label="Sources to check">{sources}</td>'
            f'<td data-label="Disposition">{esc(flag["disposition"])}</td>'
            "</tr>"
        )
    output.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(output)


def cost_not_stated_table(events: list[dict]) -> str:
    rows = [event for event in events if cost_class(event.get("admission", "")) == "not-stated"]
    if not rows:
        return ""
    output = [
        '<div class="table-wrap">',
        '<table class="review-table">',
        "<caption>Published rows whose linked official page did not establish an admission price. The cost cell on these rows "
        "reads “Not stated”. A fundraising minimum is not an admission price. Check the source before assuming entry is free.</caption>",
        '<thead><tr><th scope="col">Event</th><th scope="col">Date</th><th scope="col">Available wording</th><th scope="col">Source</th></tr></thead>',
        "<tbody>",
    ]
    for event in rows:
        output.append(
            "<tr>"
            f'<td data-label="Event"><strong>{esc(event["name"])}</strong>'
            f'<span class="organizer">{esc(event["organizer"])}</span></td>'
            f'<td data-label="Date">{esc(event.get("date_text", ""))}</td>'
            f'<td data-label="Available wording">{esc(event.get("admission", "")) or "<span class=empty>—</span>"}</td>'
            f'<td data-label="Source">{source_cell(event)}</td>'
            "</tr>"
        )
    output.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(output)


# --------------------------------------------------------------------------- #
# stylesheet
# --------------------------------------------------------------------------- #
STYLE = """
:root{--ink:#17212b;--muted:#526171;--paper:#fff;--mist:#f4f7fa;--line:#d9e2ea;--navy:#103c5b;--blue:#126da6;--teal:#0e766e;--gold:#8f6200;--rose:#9a3131;--shadow:0 8px 24px rgba(19,48,71,.08)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--mist);line-height:1.5}a{color:#075f99}a:hover{color:#064b78}.site-header{color:#fff;background:linear-gradient(120deg,#0d314a,#155d83 55%,#168178);padding:2.4rem 1.25rem 2rem}.shell{max-width:1240px;margin:0 auto;padding:0 1.25rem}.site-header .shell{padding:0;position:relative}.eyebrow{font-size:.77rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#b9e9e4;margin:0 0 .4rem}.site-header h1{margin:0;font-size:clamp(2rem,5vw,3.5rem);letter-spacing:-.045em}.lede{max-width:850px;margin:.7rem 0 0;font-size:1.06rem;color:#e7f4f5}.main{padding-top:1.2rem;padding-bottom:2rem}.nav{display:flex;gap:.55rem;flex-wrap:wrap;margin:0 0 1.5rem}.nav a{text-decoration:none;color:var(--navy);background:var(--paper);border:1px solid var(--line);border-radius:99px;padding:.48rem .77rem;font-weight:700;font-size:.9rem}.nav a.active,.nav a:hover{background:var(--navy);border-color:var(--navy);color:#fff}.hero{display:grid;gap:1rem;grid-template-columns:minmax(0,1.65fr) minmax(260px,.85fr);margin-bottom:1.25rem}.panel,.card{background:var(--paper);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow)}.panel{padding:1.35rem}.panel h2,.panel h3{margin-top:0}.panel p:last-child{margin-bottom:0}.snapshot{background:#eaf5f4;border-color:#bde0dc}.snapshot strong{display:block;font-size:2rem;color:var(--teal);letter-spacing:-.04em}.snapshot small{color:var(--muted)}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.85rem;margin:1rem 0 1.4rem}.card{padding:1rem;text-decoration:none;color:inherit;transition:transform .15s ease,box-shadow .15s ease}.card:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(19,48,71,.14)}.metric{font-size:2rem;font-weight:800;letter-spacing:-.06em;color:var(--navy);display:block}.card-label{display:block;font-weight:750}.card-note{display:block;color:var(--muted);font-size:.85rem;margin-top:.25rem}.notice{padding:1rem 1.1rem;background:#fff7dc;border:1px solid #efd58c;border-radius:12px;margin:1rem 0}.notice strong{color:#715200}.notice a{font-weight:700}.section-head{display:flex;gap:1rem;align-items:baseline;justify-content:space-between;flex-wrap:wrap;margin-top:1.75rem}.section-head h2{margin:0}.section-head p{margin:0;color:var(--muted)}.filterbar{display:flex;gap:.65rem;align-items:center;flex-wrap:wrap;background:var(--paper);border:1px solid var(--line);padding:.8rem;border-radius:12px;margin:.85rem 0}.filterbar label{font-weight:700;font-size:.9rem}.filterbar input,.filterbar select{font:inherit;padding:.55rem .65rem;border:1px solid #aebdc9;border-radius:8px;background:#fff;min-height:2.6rem}.filterbar input{min-width:min(100%,320px);flex:1}.filterbar select{max-width:100%}.table-wrap{overflow:auto;border:1px solid var(--line);border-radius:14px;background:#fff}.table-wrap table{width:100%;min-width:940px;border-collapse:collapse;font-size:.88rem}.table-wrap caption{padding:.8rem 1rem;text-align:left;color:var(--muted);background:#f8fafb;border-bottom:1px solid var(--line);font-size:.82rem}.table-wrap th,.table-wrap td{padding:.72rem .72rem;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}.table-wrap th{font-size:.75rem;letter-spacing:.04em;text-transform:uppercase;color:#405262;background:#edf3f7;position:sticky;top:0;z-index:1}.table-wrap tr:last-child td{border-bottom:0}.table-wrap tbody tr:hover{background:#f7fbfd}.organizer,.source-meta,.authority{display:block;font-size:.78rem;color:var(--muted);margin-top:.16rem}.source-link{font-weight:800;white-space:nowrap}.authority{font-size:.72rem}.empty{color:#6d7a87}.rel{display:block;font-size:.76rem;font-weight:700;color:var(--teal);margin-top:.2rem}.badge{display:inline-block;border-radius:999px;padding:.22rem .5rem;font-size:.74rem;font-weight:800;line-height:1.2;margin-top:.3rem}.badge-recurring{color:#075b54;background:#dff5ef}.badge-special{color:#6e4700;background:#fff0c5}.badge-partial_sf_program{color:#634201;background:#fff0c5}.badge-needs_review{color:#80430a;background:#ffe8cf}.badge-cancelled{color:#892d2d;background:#ffe1e1}.badge-outside_city_excluded{color:#5d4a75;background:#eee8f8}.status-upcoming{color:#075b54;background:#dff5ef}.status-completed{color:#5c6672;background:#eceff2}.status-undated{color:#5d4a75;background:#eee8f8}.cost{display:inline-block;border-radius:6px;padding:.16rem .45rem;font-size:.8rem;font-weight:800}.cost-free{color:#075b54;background:#dff5ef}.cost-paid{color:#6e4700;background:#fff0c5}.cost-mixed{color:#2b4c7e;background:#e2ecfa}.cost-unknown{color:#5c6672;background:#eceff2}.evidence-link{display:block;font-size:.78rem;font-weight:750;margin-top:.2rem}.cost-detail{display:block;font-size:.78rem;color:var(--muted);margin-top:.22rem}.review-table td:nth-child(5){min-width:280px}.category-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.85rem}.category-card{padding:1.05rem;background:#fff;border:1px solid var(--line);border-radius:14px;text-decoration:none;color:inherit}.category-card:hover{box-shadow:var(--shadow);border-color:#9fb9cb}.category-card .metric{font-size:1.6rem}.definition{margin:.4rem 0 0;color:var(--muted);font-size:.9rem}.analysis-list{padding-left:1.2rem}.analysis-list li{margin:.5rem 0}.site-footer{border-top:1px solid var(--line);background:#fff;padding:1.5rem 0 2rem;color:var(--muted);font-size:.88rem}.site-footer p{max-width:1000px;margin:.2rem 0}[hidden]{display:none!important}.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;padding:.6rem;background:#fff;color:#000;z-index:10}
.focus-links{display:flex;gap:.5rem;flex-wrap:wrap;margin:1rem 0}.focus-links a{display:inline-block;border:1px solid #a5ccc7;background:#ecf8f5;border-radius:30px;padding:.4rem .8rem;text-decoration:none;font-weight:750}.focus-links a:hover{background:#d2f0e9}.nextup{list-style:none;margin:0;padding:0}.nextup li{display:flex;gap:.85rem;align-items:flex-start;padding:.7rem 0;border-bottom:1px solid var(--line)}.nextup li:last-child{border-bottom:0}.nextup .when{flex:0 0 8.6rem;font-weight:800;color:var(--navy);font-size:.88rem}.nextup .when small{display:block;font-weight:700;color:var(--teal);font-size:.78rem}.nextup .what{flex:1}.nextup .what a{font-weight:750;text-decoration:none}.nextup .meta{display:block;font-size:.78rem;color:var(--muted);margin-top:.15rem}.today-strip{display:flex;gap:.6rem;flex-wrap:wrap;margin:.6rem 0 1rem}.today-pill{background:#eaf5f4;border:1px solid #bde0dc;border-radius:999px;padding:.4rem .8rem;font-size:.85rem;font-weight:700;color:var(--teal)}.legend{display:flex;gap:.6rem;flex-wrap:wrap;font-size:.82rem;color:var(--muted);margin:.4rem 0 0}.legend .cost{margin-right:.2rem}
@media(max-width:760px){.hero{grid-template-columns:1fr}.site-header{padding:1.5rem 1rem 1.4rem}.shell{padding:0 1rem}.main{padding-top:.9rem}.nav{gap:.4rem;margin-bottom:1rem}.nav{flex-wrap:nowrap;overflow-x:auto;padding-bottom:.25rem}.nav a{white-space:nowrap;font-size:.8rem;padding:.42rem .6rem}.section-head{margin-top:1.3rem}.panel{padding:1rem}.cards{grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.6rem}.metric{font-size:1.6rem}.nextup li{flex-direction:column;gap:.2rem}.nextup .when{flex:none}.filterbar{padding:.7rem}.filterbar input,.filterbar select{min-width:0;width:100%;flex:1 1 100%}.table-wrap{border-radius:12px}.table-wrap table{min-width:0;display:block}.table-wrap caption{font-size:.8rem}.table-wrap thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}.table-wrap tbody,.table-wrap tr,.table-wrap td{display:block;width:100%}.table-wrap tr{border-bottom:1px solid var(--line);padding:.55rem .8rem}.table-wrap tr:last-child{border-bottom:0}.table-wrap td{border:0;padding:.22rem 0;display:flex;gap:.6rem;align-items:flex-start}.table-wrap td::before{content:attr(data-label);font-weight:800;font-size:.7rem;letter-spacing:.05em;text-transform:uppercase;color:#5b6b7a;flex:0 0 6.6em}.table-wrap td[data-label="Event"]{display:block}.table-wrap td[data-label="Event"]::before{display:none}.table-wrap td[data-label="Source"],.table-wrap td[data-label="Cost"]{display:block}.table-wrap td[data-label="Source"]::before,.table-wrap td[data-label="Cost"]::before{display:block;margin-bottom:.2rem}.site-footer{font-size:.85rem}}
""".strip()


# --------------------------------------------------------------------------- #
# page shell
# --------------------------------------------------------------------------- #
def nav(active: str, prefix: str = "") -> str:
    return '<nav class="nav" aria-label="Primary">' + "".join(
        f'<a class="{"active" if href == active else ""}" {"aria-current=page" if href == active else ""} href="{prefix}{href}">{label}</a>'
        for href, label in NAV_ITEMS
    ) + "</nav>"


SCRIPT = """
const DATA = (() => { try { return JSON.parse(document.getElementById('sf-events-data').textContent); } catch (e) { return []; } })();
const TODAY = new Date(); TODAY.setHours(0, 0, 0, 0);
const dayDiff = (iso) => { if (!iso) return null; const d = new Date(iso + 'T00:00:00'); return Math.round((d - TODAY) / 86400000); };
const fmtDay = (iso) => { if (!iso) return ''; const d = new Date(iso + 'T00:00:00');
  return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' }); };
const H = (text) => String(text || '').replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const A = (url, text) => '<a href=' + JSON.stringify(H(url)) + ' target=_blank rel="noopener noreferrer">' + H(text) + '</a>';
const relative = (start, end) => {
  const s = dayDiff(start), e = dayDiff(end || start);
  if (s === null && e === null) return '';
  if (e !== null && e < 0) return 'past';
  if (s !== null && s === 0) return 'today';
  if (s !== null && s === 1) return 'tomorrow';
  if (s !== null && s > 0) return 'in ' + s + ' days';
  if (e !== null) return 'ongoing — ends ' + fmtDay(end);
  return '';
};
// Update status and ordering from the visitor's local date, not the build date.
for (const row of document.querySelectorAll('tbody tr')) {
  const rel = row.querySelector('.rel');
  if (!rel) continue;
  const label = relative(rel.dataset.start, rel.dataset.end);
  rel.textContent = label;
  const status = label === 'past' ? 'completed' : (label === '' ? 'undated' : 'upcoming');
  row.dataset.status = status;
  row.dataset.daterank = (status === 'upcoming' ? '0' : status === 'undated' ? '1' : '2') + '-' + (rel.dataset.start || rel.dataset.end || '9999-99-99');
  const badge = row.querySelector('.badge.status-upcoming, .badge.status-completed, .badge.status-undated');
  if (badge) {
    badge.textContent = status === 'completed' ? 'Completed' : status === 'undated' ? 'Date not published'
      : label.startsWith('ongoing') ? 'Ongoing now' : 'Upcoming';
    badge.className = 'badge status-' + status;
  }
}
// The executive summary is strictly free AND upcoming; undated traditions are not future dates.
const freeDated = DATA.filter((r) => r.cost_class === 'free' && (r.end || r.start) && dayDiff(r.end || r.start) >= 0);
const startsSoon = freeDated.filter((r) => dayDiff(r.start) >= 0)
  .sort((a, b) => a.start.localeCompare(b.start) || a.name.localeCompare(b.name));
const ongoing = freeDated.filter((r) => dayDiff(r.start) < 0)
  .sort((a, b) => (a.end || '').localeCompare(b.end || '') || a.name.localeCompare(b.name));
const strip = document.getElementById('today-strip');
if (strip) {
  const horizons = [7, 30, 90].map((h) => startsSoon.filter((r) => dayDiff(r.start) <= h).length);
  strip.innerHTML = '<span class="today-pill">Today: ' + H(TODAY.toLocaleDateString(undefined, {year:'numeric',month:'long',day:'numeric'})) + '</span>'
    + '<span class="today-pill">Free starts in 7 days: ' + horizons[0] + '</span>'
    + '<span class="today-pill">In 30 days: ' + horizons[1] + '</span>'
    + '<span class="today-pill">In 90 days: ' + horizons[2] + '</span>'
    + '<span class="today-pill">Free programs ongoing: ' + ongoing.length + '</span>';
}
const count = document.getElementById('free-count');
if (count) count.textContent = freeDated.length;
const nextUp = document.getElementById('next-up-list');
if (nextUp) {
  const rowHtml = (r) => '<li><span class="when">' + H(fmtDay(r.start))
    + '<small>' + H(relative(r.start, r.end)) + '</small></span><span class="what">'
    + A(r.source_url, r.name) + '<span class="meta">' + H(r.category) + ' · ' + H(r.bucket_label)
    + ' · ' + H(r.location) + ' · <span class="cost cost-free">Free</span></span></span></li>';
  const nearest = startsSoon.slice(0, 10).concat(ongoing.slice(0, 3));
  nextUp.innerHTML = nearest.length ? nearest.map(rowHtml).join('')
    : '<li>No confirmed free upcoming dates remain in this snapshot. Check the linked recurring catalog for new announcements.</li>';
}
// 3. Search / category / cost filters.
for (const table of document.querySelectorAll('[data-filter-table]')) {
  const input = document.querySelector('#' + table.dataset.searchControl);
  const select = document.querySelector('#' + table.dataset.categoryControl);
  const cost = document.querySelector('#' + (table.dataset.costControl || 'missing-cost-control'));
  const when = document.querySelector('#' + (table.dataset.whenControl || 'missing-when-control'));
  const sorter = document.querySelector('#' + (table.dataset.sortControl || 'missing-sort-control'));
  const apply = () => {
    const term = (input?.value || '').toLowerCase();
    const category = select?.value || '';
    const costFilter = cost?.value || '';
    const whenFilter = when?.value || '';
    for (const row of table.tBodies[0].rows) {
      const matchText = !term || row.textContent.toLowerCase().includes(term);
      const matchCategory = !category || row.dataset.category === category;
      const matchCost = !costFilter || row.dataset.cost === costFilter;
      const matchWhen = !whenFilter || row.dataset.status === whenFilter;
      const liveMatch = !table.hasAttribute('data-live-upcoming') || row.dataset.status === 'upcoming';
      row.hidden = !(matchText && matchCategory && matchCost && matchWhen && liveMatch);
    }
  };
  // Date-first ordering must be recomputed even if the visitor never touches Sort.
  const tbody = table.tBodies[0];
  if (tbody) Array.from(tbody.rows).sort((a, b) =>
    (a.dataset.daterank + '|' + (a.dataset.name || '')).localeCompare(b.dataset.daterank + '|' + (b.dataset.name || ''))
  ).forEach((row) => tbody.appendChild(row));
  apply();
  if (table.hasAttribute('data-live-upcoming')) {
    const note = table.closest('section')?.querySelector('.live-empty') || table.parentElement.nextElementSibling;
    const visible = Array.from(table.tBodies[0].rows).filter((row) => !row.hidden).length;
    if (note?.classList.contains('live-empty')) note.hidden = visible > 0;
    const focusCount = table.closest('.focus-group')?.querySelector('.focus-count');
    if (focusCount) focusCount.textContent = visible + ' free upcoming on ' + TODAY.toLocaleDateString();
    const total = document.querySelector('[data-live-total]');
    if (total) total.textContent = document.querySelectorAll('table[data-live-upcoming] tbody tr:not([hidden])').length + ' dated free upcoming';
  }
  input?.addEventListener('input', apply); select?.addEventListener('change', apply);
  cost?.addEventListener('change', apply); when?.addEventListener('change', apply);
  if (sorter) {
    const tbody = table.tBodies[0];
    sorter.addEventListener('change', () => {
      const mode = sorter.value;
      const rows = Array.from(tbody.rows);
      const key = (row) => {
        if (mode === 'name') return row.dataset.name || '';
        if (mode === 'category') return row.dataset.category || '';
        if (mode === 'cost') return row.dataset.costrank + '|' + (row.dataset.name || '');
        return row.dataset.daterank + '|' + (row.dataset.name || '');
      };
      rows.sort((a, b) => key(a).localeCompare(key(b)));
      rows.forEach((row) => tbody.appendChild(row));
      apply();
    });
  }
}
"""


def page(title: str, body: str, active: str, catalog: dict, *, prefix: str = "",
         data_block: str = "") -> str:
    audit_href = f"{prefix}research/official-source-audit.md"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Official-source San Francisco city events catalog, ordered by date with upcoming events first, with admission cost shown for every row.">
  <title>{esc(title)} · San Francisco Events</title>
  <link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<header class="site-header"><div class="shell">
  <p class="eyebrow">Official-source catalog · {esc(catalog['as_of'])}</p>
  <h1>San Francisco Events</h1>
  <p class="lede">City and County of San Francisco only. Free upcoming events first. Other admission types, past editions and research records are separated and clearly labeled; every event table row links its source.</p>
</div></header>
<main id="content" class="shell main">
{nav(active, prefix)}
<noscript><p class="notice">Dates on this no-JavaScript view are a snapshot as of {esc(catalog["as_of"])}. Some may have passed; confirm with the linked organizer before attending.</p></noscript>
{body}
</main>
<footer class="site-footer"><div class="shell">
  <p><strong>Scope:</strong> {esc(catalog['coverage'])}</p>
  <p>{esc(catalog['field_policy'])} Read the <a href="{prefix}method.html">method and findings</a> or the row-level <a href="{audit_href}">source audit</a>.</p>
</div></footer>
{data_block}
<script>
{SCRIPT}
</script>
</body>
</html>"""


# --------------------------------------------------------------------------- #
# filter controls
# --------------------------------------------------------------------------- #
def filter_controls(categories: list[str], *, key: str, with_cost: bool = True,
                    with_when: bool = True, with_sort: bool = True) -> str:
    options = "".join(f'<option value="{esc(category)}">{esc(category)}</option>' for category in categories)
    cost_options = "".join(
        f'<option value="{value}">{label}</option>'
        for value, label in (
            ("free", "Free"),
            ("mixed", "Free or partly free"),
            ("paid", "Paid / ticketed"),
            ("not-stated", "Cost not stated"),
        )
    )
    when_options = "".join(
        f'<option value="{value}">{label}</option>'
        for value, label in (("upcoming", "Upcoming only"), ("completed", "Completed only"))
    )
    sort_options = "".join(
        f'<option value="{value}">{label}</option>'
        for value, label in (
            ("date", "Date — upcoming first"),
            ("name", "Name A–Z"),
            ("category", "Category"),
            ("cost", "Cost — free first"),
        )
    )
    parts = [
        '<div class="filterbar" aria-label="Filter events">',
        f'<label for="search-{key}">Search</label>',
        f'<input id="search-{key}" type="search" placeholder="Event, organizer, place, or category">',
        f'<label for="category-{key}">Category</label>',
        f'<select id="category-{key}"><option value="">All categories</option>{options}</select>',
    ]
    if with_cost:
        parts.append(f'<label for="cost-{key}">Cost</label>')
        parts.append(f'<select id="cost-{key}"><option value="">Any cost</option>{cost_options}</select>')
    if with_when:
        parts.append(f'<label for="when-{key}">When</label>')
        parts.append(f'<select id="when-{key}"><option value="">All dates</option>{when_options}</select>')
    if with_sort:
        parts.append(f'<label for="sort-{key}">Sort</label>')
        parts.append(f'<select id="sort-{key}">{sort_options}</select>')
    parts.append("</div>")
    return "".join(parts)


def mark_filter_table(markup: str, *, key: str, with_cost: bool = True,
                      with_when: bool = True, with_sort: bool = True) -> str:
    attributes = f'<table data-filter-table data-search-control="search-{key}" data-category-control="category-{key}"'
    if with_cost:
        attributes += f' data-cost-control="cost-{key}"'
    if with_when:
        attributes += f' data-when-control="when-{key}"'
    if with_sort:
        attributes += f' data-sort-control="sort-{key}"'
    attributes += ">"
    return markup.replace("<table>", attributes, 1)


def table_with_filter_rows(events: list[dict], *, key: str, as_of: date,
                            include_bucket: bool = False, with_cost: bool = True,
                            with_when: bool = True, with_sort: bool = True) -> str:
    markup = event_table(events, as_of=as_of, include_bucket=include_bucket)
    for event in events:
        needle = f'<tr><td data-label="Event"><strong>{esc(event["name"])}</strong>'
        replacement = (
            f'<tr data-category="{esc(event["category"])}"'
            f' data-name="{esc(event["name"].lower())}"'
            f' data-cost="{cost_class(event.get("admission", ""))}"'
            f' data-costrank="{"0" if cost_class(event.get("admission", "")) == "free" else ("1" if cost_class(event.get("admission", "")) == "mixed" else "2")}"'
            f' data-status="{event_status(event, as_of)}"'
            f' data-daterank="{sort_key(event, as_of)[0]}-{event.get("start_date") or event.get("end_date") or "9999-99-99"}">'
            f'<td data-label="Event"><strong>{esc(event["name"])}</strong>'
        )
        markup = markup.replace(needle, replacement, 1)
    return mark_filter_table(
        markup, key=key, with_cost=with_cost, with_when=with_when, with_sort=with_sort
    )


def embed_data(published: list[dict]) -> str:
    payload = []
    for event in published:
        payload.append({
            "id": event["id"],
            "name": event["name"],
            "category": event["category"],
            "bucket_label": "Regularly occurring" if event["bucket"] == "recurring" else "Special",
            "location": event.get("location", ""),
            "start": event.get("start_date", ""),
            "end": event.get("end_date", ""),
            "cost_class": cost_class(event.get("admission", "")),
            "source_url": event["source_url"],
        })
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return f'<script type="application/json" id="sf-events-data">{blob}</script>'


# --------------------------------------------------------------------------- #
# CSV export
# --------------------------------------------------------------------------- #
def write_csv(events: list[dict]) -> None:
    fields = [
        "id", "name", "bucket", "cadence", "category", "date_text", "start_date", "end_date",
        "time_text", "location", "organizer", "admission", "admission_source_url", "cost_class", "source_label", "source_url",
        "source_authority", "status", "review_reason", "notes",
    ]
    with (ROOT / "data" / "events.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for event in events:
            row = {field: event.get(field, "") for field in fields}
            row["cost_class"] = cost_class(event.get("admission", ""))
            writer.writerow(row)


# --------------------------------------------------------------------------- #
# build
# --------------------------------------------------------------------------- #
def build() -> None:
    catalog, events, flags = read_data()
    validate(catalog, events)
    as_of = date.fromisoformat(catalog["as_of"])

    published = [event for event in events if event["status"] == "verified"]
    recurring = sorted(
        [event for event in published if event["bucket"] == "recurring"],
        key=lambda event: sort_key(event, as_of),
    )
    special = sorted(
        [event for event in published if event["bucket"] == "special"],
        key=lambda event: sort_key(event, as_of),
    )
    all_events = sorted(published, key=lambda event: sort_key(event, as_of))
    review = sorted(
        [event for event in events if event["status"] != "verified"],
        key=lambda event: (event["status"], event["name"]),
    )
    categories = sorted({event["category"] for event in published})
    category_counts = Counter(event["category"] for event in published)
    cadence_counts = Counter(event["cadence"] for event in recurring)
    authority_counts = Counter(event["source_authority"] for event in published)
    cost_counts = Counter(cost_class(event.get("admission", "")) for event in published)
    upcoming = [event for event in published if event_status(event, as_of) == "upcoming"]
    upcoming_soon = sorted(
        [event for event in upcoming if not event.get("start_date") or event["start_date"] >= catalog["as_of"]],
        key=lambda event: (event.get("start_date") or "9999-99-99", event.get("name", "").lower()),
    )
    upcoming_ongoing = sorted(
        [event for event in upcoming if event.get("start_date") and event["start_date"] < catalog["as_of"]],
        key=lambda event: (event.get("end_date") or "9999-99-99", event.get("name", "").lower()),
    )
    fallback_next_up = upcoming_soon[:10] + upcoming_ongoing[:3]
    # Only dated, still-current, unambiguously $0-admission rows enter the main view.
    # An undated weekly cadence is not a confirmed occurrence on a particular day.
    free_upcoming = sorted(
        (event for event in published if cost_class(event.get("admission", "")) == "free"
         and event_status(event, as_of) == "upcoming"),
        key=lambda event: sort_key(event, as_of),
    )
    paid_rows = [event for event in all_events if cost_class(event.get("admission", "")) == "paid"]
    mixed_rows = [event for event in all_events if cost_class(event.get("admission", "")) == "mixed"]

    def focus_group(event: dict) -> str:
        # Bhangra & Beats is explicitly described as music by its linked organizer.
        if event["category"] == "Music & performing arts" or event["id"] == "bhangra-beats-night-market-2026":
            return "Music"
        if event["category"] == "Technology, AI & gaming":
            name = event["name"].lower()
            if "game" in name or "devs" in name:
                return "Gaming"
            if "ai" in name or "artificial intelligence" in name:
                return "AI"
        return "Everything else"

    def focus_tables(events: list[dict], *, key_prefix: str) -> str:
        blocks = []
        for key, heading in (("Gaming", "Gaming"), ("Music", "Music"),
                             ("AI", "AI"), ("Everything else", "Everything else")):
            group = [event for event in events if focus_group(event) == key]
            slug = slugify(key)
            table = table_with_filter_rows(group, key=key_prefix + slug, as_of=as_of,
                                           include_bucket=True, with_cost=False,
                                           with_when=False, with_sort=False)
            table = table.replace('<table data-filter-table', '<table data-live-upcoming data-filter-table', 1)
            blocks.append(f'<section class="focus-group" aria-labelledby="{key_prefix}{slug}">'
                          f'<div class="section-head"><h3 id="{key_prefix}{slug}">{heading}</h3>'
                          f'<p class="focus-count">{len(group)} confirmed free upcoming as of {esc(catalog["as_of"])}</p></div>'
                          + (table + '<p class="notice live-empty" hidden>No confirmed free upcoming dates remain in this snapshot.</p>' if group else '<p class="notice">No dated, free upcoming event in this focus area is confirmed in this snapshot. '
                             'Paid or cost-unknown events are not presented as free.</p>')
                          + '</section>')
        return "\n".join(blocks)


    cadence_order = ("weekly", "monthly", "seasonal", "annual")
    cadence_summary = ", ".join(
        f"<strong>{cadence_counts[cadence]} {cadence}</strong>"
        for cadence in cadence_order if cadence_counts.get(cadence)
    )
    top_categories = ", ".join(
        f"<strong>{esc(category)} ({count})</strong>"
        for category, count in category_counts.most_common(3)
    )
    authority_summary = ", ".join(
        f"<strong>{count} {esc(authority.lower())}</strong>"
        for authority, count in sorted(authority_counts.items(), key=lambda item: (-item[1], item[0]))
    )
    cost_summary = ", ".join(
        f"<strong>{cost_counts[kind]} {label.lower()}</strong>"
        for kind, label in COST_LABELS.items() if cost_counts.get(kind)
    )

    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "style.css").write_text(STYLE + "\n", encoding="utf-8")
    (ROOT / "categories").mkdir(exist_ok=True)

    data_block = embed_data(published)

    category_cards = "".join(
        f'<a class="card" href="categories/{slugify(category)}.html">'
        f'<span class="metric">{category_counts[category]}</span>'
        f'<span class="card-label">{esc(category)}</span>'
        f'<span class="card-note">Open category page →</span></a>'
        for category in categories
    )

    fallback_free = sorted(
        free_upcoming, key=lambda event: (event.get("start_date") < catalog["as_of"],
                                         event.get("start_date") if event.get("start_date") >= catalog["as_of"]
                                         else event.get("end_date"), event["name"])
    )[:10]
    home = f"""
<section class="hero">
  <div class="panel">
    <p class="eyebrow" style="color:#0e766e">SF only · source-audited snapshot · {esc(catalog['as_of'])}</p>
    <h2>Find your next free event</h2>
    <p>Only events with a source-confirmed <strong>free admission</strong> and a confirmed date that has not passed appear below. Dates, locations and costs are linked to the publisher for your own check. No price, partly free, or paid? Those are <em>not</em> in this main list.</p>
    <p><a href="free.html"><strong>Browse free upcoming by focus →</strong></a> &nbsp;·&nbsp;
       <a href="paid.html">Paid &amp; partly free →</a> &nbsp;·&nbsp;
       <a href="flagged.html">Unverified costs →</a></p>
  </div>
  <aside class="panel snapshot"><strong id="free-count">{len(free_upcoming)}</strong><span>dated free upcoming events</span><br>
  <small>As of {esc(catalog['as_of'])}; refreshed in your browser. Not an exhaustive city calendar.</small></aside>
</section>
<section aria-labelledby="summary-title">
  <div class="section-head"><h2 id="summary-title">Executive summary · free events near today</h2>
  <p>Nearest confirmed free dates first; ongoing programs follow. All entries have publisher links.</p></div>
  <div class="today-strip" id="today-strip"><span class="today-pill">Snapshot: {esc(catalog['as_of'])}</span></div>
  <div class="panel"><ul class="nextup" id="next-up-list">{''.join(
      f'<li><span class="when">{esc(event.get("date_text", ""))}</span><span class="what">'
      f'<a href="{esc(event["source_url"])}" target="_blank" rel="noopener noreferrer">{esc(event["name"])}</a>'
      f'<span class="meta">{esc(event["category"])} · {esc(event.get("location", ""))} · Free</span></span></li>'
      for event in fallback_free
  ) or '<li>No confirmed free upcoming dates in this snapshot.</li>'}</ul></div>
</section>
<section aria-labelledby="free-table-title">
  <div class="section-head"><h2 id="free-table-title">Free upcoming · by focus</h2>
  <p>Gaming, music and AI first; everything else after. Each table row links its official source.</p></div>
  <nav class="focus-links" aria-label="Jump to free event focus">
    <a href="#home-gaming">Gaming</a><a href="#home-music">Music</a>
    <a href="#home-ai">AI</a><a href="#home-everything-else">Everything else</a>
  </nav>
  {focus_tables(free_upcoming, key_prefix='home-')}
</section>
<section aria-labelledby="explore-title">
  <div class="section-head"><h2 id="explore-title">Explore the audited catalog</h2>
  <p>These secondary views include older editions and non-free admission; they are not free-event recommendations.</p></div>
  <div class="cards">
    <a class="card" href="recurring.html"><span class="metric">{len(recurring)}</span><span class="card-label">Recurring</span><span class="card-note">Weekly, monthly, seasonal, annual</span></a>
    <a class="card" href="special.html"><span class="metric">{len(special)}</span><span class="card-label">Special</span><span class="card-note">Dated one-offs and programs</span></a>
    <a class="card" href="categories.html"><span class="metric">{len(categories)}</span><span class="card-label">Categories</span><span class="card-note">Audited rows by subject</span></a>
    <a class="card" href="all-events.html"><span class="metric">{len(published)}</span><span class="card-label">All source-linked rows</span><span class="card-note">Including past and non-free</span></a>
    <a class="card" href="flagged.html"><span class="metric">{len(review)}</span><span class="card-label">Flagged for Review</span><span class="card-note">Plus costs not confirmed</span></a>
  </div>
</section>
<section class="panel" aria-labelledby="findings"><h2 id="findings">What the evidence shows</h2>
<p>Among {len(published)} audited city-only rows, {len(free_upcoming)} have confirmed free admission and a dated occurrence still current as of {esc(catalog['as_of'])}. Other admission classifications: {cost_summary}. A free fundraising minimum does not establish free entry; any unknown price is treated as unverified.</p>
<p>Recurring records: {cadence_summary}. Largest audited categories: {top_categories}. Source types: {authority_summary}.</p>
<p>This is a limited snapshot, <strong>not every San Francisco event</strong>. Check the linked publisher immediately before visiting. Weekly programs without a dated occurrence remain in the <a href="recurring.html">recurring catalog</a>, not the upcoming list.</p></section>
"""
    (ROOT / "index.html").write_text(
        page("Dashboard", home, "index.html", catalog, data_block=data_block), encoding="utf-8"
    )

    # --- free dated upcoming is the primary view; paid is isolated --------
    upcoming_body = f"""
<section class="section-head"><div><h2>Upcoming free events · chronological</h2>
<p>Only confirmed free admission and confirmed, not-yet-past dates as of {esc(catalog['as_of'])}.
No paid, partly free, unstated cost, undated tradition or past edition appears here. This snapshot
is rechecked against your local date in the browser; consult sources before travelling.</p></div>
<p data-live-total>{len(free_upcoming)} dated rows as of {esc(catalog["as_of"])}</p></section>
{table_with_filter_rows(free_upcoming, key='upcoming', as_of=as_of, include_bucket=True, with_cost=False, with_when=False, with_sort=False).replace('<table data-filter-table', '<table data-live-upcoming data-filter-table', 1)}
<p class="notice live-empty" hidden>No confirmed free upcoming dates remain in this snapshot.</p>
"""
    (ROOT / "upcoming.html").write_text(
        page("Upcoming free by date", upcoming_body, "upcoming.html", catalog, data_block=data_block), encoding="utf-8"
    )
    free_body = f"""
<section class="section-head"><div><h2>Free upcoming · by focus</h2>
<p>Only dated events still current and <strong>confirmed free</strong> by the linked publisher. Gaming,
music and AI appear first, then everything else. No confirmed free upcoming gaming or AI date? We say so
rather than treat a paid conference as free. Other free traditions without a confirmed dated occurrence
are listed in <a href="recurring.html">recurring events</a>.</p></div><p data-live-total>{len(free_upcoming)} dated rows as of {esc(catalog["as_of"])}</p></section>
<nav class="focus-links" aria-label="Jump to free event focus"><a href="#free-gaming">Gaming</a>
<a href="#free-music">Music</a><a href="#free-ai">AI</a><a href="#free-everything-else">Everything else</a></nav>
{focus_tables(free_upcoming, key_prefix='free-')}
"""
    (ROOT / "free.html").write_text(
        page("Free upcoming by focus", free_body, "free.html", catalog, data_block=data_block), encoding="utf-8"
    )
    paid_body = f"""
<section class="section-head"><div><h2>Paid &amp; partly free · separate catalog</h2>
<p>These rows are <strong>not</strong> in the free upcoming lists. A ticket, price,
or a free portion alongside paid options is labeled in its source-stated wording. Completed editions
remain for historical reference. For unknown prices see <a href="flagged.html">Flagged for Review</a>.</p></div>
<p>{len(paid_rows)} paid · {len(mixed_rows)} partly free</p></section>
<section class="section-head"><h3>Paid / ticketed</h3></section>
{table_with_filter_rows(paid_rows, key='paid', as_of=as_of, include_bucket=True, with_cost=False, with_when=False)}
<section class="section-head"><h3>Partly free / conditional / suggested contribution</h3></section>
{table_with_filter_rows(mixed_rows, key='mixed', as_of=as_of, include_bucket=True, with_cost=False, with_when=False)}
"""
    (ROOT / "paid.html").write_text(
        page("Paid & partly free", paid_body, "paid.html", catalog, data_block=data_block), encoding="utf-8"
    )

    recurring_body = f"""
<section class="section-head"><div><h2>Regularly occurring events</h2>
<p>Weekly, monthly, seasonal, and annual programs with a recurring cadence stated by the source,
ordered with upcoming dates first.</p></div><p>{len(recurring)} verified rows</p></section>
{filter_controls(categories, key='recurring')}
{table_with_filter_rows(recurring, key='recurring', as_of=as_of)}
<section class="notice"><strong>Why annual events are here:</strong> the brief separates regular patterns from dated
special events. A tradition is listed here only when the source supports a weekly/monthly/seasonal/annual cadence;
the exact audited date remains in the row.</section>
"""
    (ROOT / "recurring.html").write_text(
        page("Regularly occurring events", recurring_body, "recurring.html", catalog, data_block=data_block),
        encoding="utf-8",
    )

    special_body = f"""
<section class="section-head"><div><h2>Special events</h2>
<p>Dated programs, single-event conferences, and one-off calendar listings, ordered with upcoming dates first.
No recurrence is inferred.</p></div><p>{len(special)} verified rows</p></section>
{filter_controls(categories, key='special')}
{table_with_filter_rows(special, key='special', as_of=as_of)}
"""
    special_markup = page("Special events", special_body, "special.html", catalog, data_block=data_block)
    (ROOT / "special.html").write_text(special_markup, encoding="utf-8")
    alias_body = f"""
<section class="notice"><strong>Alias page.</strong> This is the same list as <a href="special.html">Special events</a>,
kept at the <code>annual-special.html</code> address for older links. Annual traditions are not listed here;
they are on <a href="recurring.html">Regularly occurring events</a>.</section>
{special_body}"""
    (ROOT / "annual-special.html").write_text(
        page("Special events (alias)", alias_body, "special.html", catalog, data_block=data_block),
        encoding="utf-8",
    )

    all_body = f"""
<section class="section-head"><div><h2>All published city-only events</h2>
<p>Search across the {len(all_events)} records, narrow by category or cost, and sort by date, name, category or cost.
Every row has a source link.</p></div><p>{len(all_events)} verified rows</p></section>
{filter_controls(categories, key='all')}
{table_with_filter_rows(all_events, key='all', as_of=as_of, include_bucket=True)}
"""
    (ROOT / "all-events.html").write_text(
        page("All published events", all_body, "all-events.html", catalog, data_block=data_block),
        encoding="utf-8",
    )

    categories_body = "".join(
        f'<a class="category-card" href="categories/{slugify(category)}.html">'
        f'<span class="metric">{category_counts[category]}</span><strong>{esc(category)}</strong>'
        f'<p class="definition">Source-linked city event rows in this category, upcoming first.</p></a>'
        for category in categories
    )
    (ROOT / "categories.html").write_text(
        page(
            "Categories",
            f'<section class="section-head"><div><h2>Category pages</h2>'
            f'<p>Open a category to review its source-linked city-only event rows, ordered with upcoming dates first.</p>'
            f'</div></section><div class="category-grid">{categories_body}</div>',
            "categories.html", catalog, data_block=data_block,
        ),
        encoding="utf-8",
    )

    for category in categories:
        category_events = sorted(
            [event for event in all_events if event["category"] == category],
            key=lambda event: sort_key(event, as_of),
        )
        category_body = f"""
<section class="section-head"><div><p><a href="../categories.html">← All categories</a></p><h2>{esc(category)}</h2>
<p>{len(category_events)} verified city-only event rows, each with its own source link, ordered with upcoming dates first.</p></div></section>
{filter_controls(categories, key='cat-' + slugify(category))}
{table_with_filter_rows(category_events, key='cat-' + slugify(category), as_of=as_of, include_bucket=True)}
"""
        (ROOT / "categories" / f"{slugify(category)}.html").write_text(
            page(category, category_body, "categories.html", catalog, prefix="../", data_block=data_block),
            encoding="utf-8",
        )

    flagged_body = f"""
<section class="section-head"><div><h2>Flagged for Review</h2>
<p>These records are intentionally excluded from the city-only recurring and special tables.</p></div>
<p>{len(review)} review records · {len(flags)} field-level flags</p></section>
<section class="notice"><strong>What a flag means:</strong> a source may be official and still be unsuitable for a
city-only row — for example a multi-city program, an official cancellation, or an unresolved schedule. Fields stay
blank when not confirmed; nothing below is silently promoted into the catalog.</section>
{review_table(review)}
<section class="section-head"><div><h2>Field-level flags and source findings</h2>
<p>Corrections applied to published rows, source-availability problems, and residual discrepancies that merit manual
review. Each finding links the sources used.</p></div><p>{len(flags)} findings</p></section>
{flags_table(flags)}
<section class="section-head"><div><h2>Admission cost not established by the linked source</h2>
<p>The brief asks that every row state what it costs to attend. Where the official page did not establish a price, the cost
cell reads “Not stated” rather than being filled with an assumption. A waived fundraising minimum is not proof of free entry. Every such row is listed here with its source
link so it can be checked by hand. Blank never means free.</p></div>
<p>{sum(1 for event in published if cost_class(event.get('admission', '')) == 'not-stated')} rows</p></section>
{cost_not_stated_table(published)}
"""
    (ROOT / "flagged.html").write_text(
        page("Flagged for Review", flagged_body, "flagged.html", catalog), encoding="utf-8"
    )

    method_body = f"""
<section class="section-head"><div><h2>Method, sources, and findings</h2>
<p>A reproducible snapshot of publicly advertised San Francisco city events.</p></div></section>
<section class="panel"><h3>Publish rule</h3><ol>
<li>Each active row needs a title, source-stated date/cadence, San Francisco city location, organizer, and HTTPS source link.</li>
<li>Accepted sources are official organizers, official venues, government sources, and clearly labeled trusted civic sources. The source type is visible in every row.</li>
<li>Optional time and admission fields are not inferred. An em dash means the captured source did not state that optional value; “Not stated” in the Cost column means admission cost is not confirmed.</li>
<li>Multi-city programs, cancelled events, outside-city events, and records missing essential evidence are not added to public tables. They stay on <a href="flagged.html">Flagged for Review</a> with a source and explanation.</li>
</ol></section>
<section class="panel"><h3>How date ordering and the executive summary work</h3><ul class="analysis-list">
<li>Primary dashboard, Upcoming and Free pages contain only dated confirmed-free rows still current as of the audit. Secondary research views include completed and non-free rows; those tables place upcoming first and completed editions last.</li>
<li>A small script re-computes each row's status against the visitor's actual current date, so the "Upcoming" / "Completed" badge and the "in N days" label stay correct after the static build date.</li>
<li>The dashboard shows only confirmed-free dated events not yet past. Its nearest-events panel and 7/30/90-day counts use the visitor's local date; paid, mixed, unknown cost and undated rows stay out. The no-JavaScript view is explicitly dated to the audit snapshot.</li>
</ul></section>
<section class="panel"><h3>How cost is labelled</h3><p>Cost classes are derived only from the admission text that the
linked official page stated. Nothing is inferred from an event's type. A waived fundraising minimum by itself does not establish free entry.</p>
<div class="legend">
<span class="cost cost-free">Free</span> the source states no charge
<span class="cost cost-mixed">Free or partly free</span> some programmes free, others ticketed
<span class="cost cost-paid">Paid / ticketed</span> the source states a charge, ticket sale or paid pass
<span class="cost cost-unknown">Not stated</span> a free or paid admission price was not confirmed — <strong>never</strong> treated as free
</div>
<p>Current split: {cost_summary}. The rows without a confirmed cost are listed, with their source links, on the
<a href="flagged.html">Flagged for Review</a> page.</p></section>
<section class="panel"><h3>Findings, bounded by this dataset</h3><ul class="analysis-list">
<li>The audit has {len(recurring)} recurring and {len(special)} dated-special verified rows across {len(categories)} categories; {len(upcoming)} of the {len(published)} published rows are still upcoming as of {esc(catalog['as_of'])}.</li>
<li>The recurring list breaks down as {cadence_summary}. The classification is based on cadence, not whether an event is free or public.</li>
<li>The largest audited categories are {top_categories}. This describes the verified source set, not all activity in San Francisco.</li>
<li>Most 2026 editions in this snapshot had already taken place by the October 18, 2026 check date, while several rows document confirmed 2027 editions. Rows record the audited edition, not a promise that the same dates repeat.</li>
<li>The review register makes scope and cancellation decisions visible instead of deleting difficult records or asserting unsupported city-only coverage.</li>
</ul></section>
<section class="panel"><h3>Directories and coverage boundaries</h3>
<p>Some San Francisco programming is published as a running calendar rather than a single event with a fixed cadence. Those are linked here as directories instead of forcing them into event rows:</p>
<ul class="analysis-list">
<li><a href="https://sfpl.org/events">San Francisco Public Library — Upcoming Events</a>: branch programs and talks across the city system.</li>
<li><a href="https://sfcityguides.org/">San Francisco City Guides</a>: free volunteer-led walking tours (70+ tours, a program of SFPL); individual tours run on varying schedules via their tour finder.</li>
<li><a href="https://sfrecpark.org/Calendar.aspx">SF Recreation and Park calendar</a>: park programs and seasonal city events; individual dated listings (for example Scaregrove) become special-event rows.</li>
</ul>
<p>Boundaries applied in this snapshot: recurring rows are created only when an organizer, venue, or government page states a fixed cadence (weekly, monthly, seasonal, or annual). Candidates seen only in secondary coverage or in roundup articles are not listed until directly verified. Well-known look-alikes outside the City and County are excluded: the Great Dickens Christmas Fair is at the Cow Palace in Daly City, and airport programs at SFO sit in San Mateo County.</p></section>
<section class="panel"><h3>Line-by-line verification</h3><p>The eight primary free-upcoming rows were rechecked for this session with field-level source evidence in
<a href="research/review-f65449c5.md">research/review-f65449c5.md</a>. Prior catalog-wide auditing is recorded in
<a href="research/verification-e79e0de2.md">research/verification-e79e0de2.md</a>, with earlier passes in
<a href="research/reverification-2088b727.md">research/reverification-2088b727.md</a>,
<a href="research/verification-e969f4df.md">research/verification-e969f4df.md</a> and
<a href="research/reverification-55c58947.md">research/reverification-55c58947.md</a>. Values not stated by a source
were blanked and flagged rather than inferred. Static link checks do not live-fetch external sites; consult the organizer for changes.</p></section>
<section class="panel"><h3>Audit trail and maintenance</h3><p>The complete row-level research matrix is in
<a href="research/official-source-audit.md">research/official-source-audit.md</a>. The machine-readable source of truth is
<a href="data/events.json">data/events.json</a>; <a href="data/events.csv">data/events.csv</a> is an export. Before changing
a row, re-check the official source and update the review reason when evidence is incomplete or conflicting.</p>
<p>This site is intentionally not an exhaustive claim: private, newly announced, or unlisted events can exist outside this dated source audit.</p></section>
"""
    (ROOT / "method.html").write_text(
        page("Method & sources", method_body, "method.html", catalog), encoding="utf-8"
    )

    write_csv(events)
    print(
        f"Built {len(published)} published events: {len(recurring)} recurring, {len(special)} special, "
        f"{len(categories)} categories; {len(review)} review records; {len(upcoming)} upcoming; "
        f"{cost_counts['free'] + cost_counts['mixed']} free or partly free."
    )


if __name__ == "__main__":
    build()
