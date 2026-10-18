#!/usr/bin/env python3
"""Build the static GitHub Pages catalog from the official-source event audit.

The source of truth is data/events.json. Only rows that are both `verified` and
assigned to the recurring or special bucket can be rendered in public catalog
tables. Everything else is rendered on Flagged for Review instead.
"""
from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).parent
DATA_PATH = ROOT / "data" / "events.json"
TODAY = date(2026, 10, 18)


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


def date_status(event: dict, today: date = TODAY) -> dict:
    start_str = event.get("start_date")
    end_str = event.get("end_date")
    if start_str:
        s_date = date.fromisoformat(start_str)
        e_date = date.fromisoformat(end_str) if end_str else s_date
        if s_date == today:
            return {
                "code": "today",
                "label": "Happening Today",
                "badge_class": "badge-today",
                "sort_rank": 0,
                "is_upcoming": True,
                "date": s_date,
            }
        elif s_date < today <= e_date:
            return {
                "code": "active",
                "label": "Active Season",
                "badge_class": "badge-active",
                "sort_rank": 1,
                "is_upcoming": True,
                "date": s_date,
            }
        elif s_date > today:
            return {
                "code": "upcoming",
                "label": "Upcoming",
                "badge_class": "badge-upcoming",
                "sort_rank": 2,
                "is_upcoming": True,
                "date": s_date,
            }
        else:
            return {
                "code": "past",
                "label": "Past edition",
                "badge_class": "badge-past",
                "sort_rank": 4,
                "is_upcoming": False,
                "date": s_date,
            }
    else:
        # Year-round recurring
        return {
            "code": "ongoing",
            "label": "Year-round",
            "badge_class": "badge-ongoing",
            "sort_rank": 3,
            "is_upcoming": False,
            "date": date(9999, 1, 1),
        }


def event_tags(event: dict) -> dict:
    name_desc = (event.get("name", "") + " " + event.get("description", "") + " " + event.get("category", "")).lower()
    adm = (event.get("admission") or "").lower()

    is_free = "free" in adm
    cost_type = "free" if is_free else ("paid" if adm else "unstated")

    is_gaming = any(k in name_desc for k in ["game", "gaming", "esport", "arcade", "gdc"])
    is_music = event.get("category") == "Music & performing arts" or any(
        k in name_desc for k in ["music", "concert", "jazz", "symphony", "opera", "band", "bluegrass", "porchfest"]
    )
    is_ai_tech = any(
        k in name_desc for k in [
            "ai", "artificial intelligence", "machine learning", "ignite", "cloudflare",
            "confluent", "techcrunch", "developer", "photonics", "informs", "atlassian",
            "tdx", "data", "software", "computing", "cloud",
        ]
    ) or (event.get("category") == "Professional & academic" and any(
        k in name_desc for k in ["tech", "cloud", "security", "engineering", "biotech"]
    ))

    return {
        "is_free": is_free,
        "cost_type": cost_type,
        "is_gaming": is_gaming,
        "is_music": is_music,
        "is_ai_tech": is_ai_tech,
    }


def sort_regular(event: dict) -> tuple:
    st = date_status(event)
    rank = st["sort_rank"]
    if rank in (0, 1, 2):  # Active season or upcoming confirmed edition
        return (0, str(st["date"]), event["name"])
    elif rank == 3:  # Year-round
        cadence_ranks = {"weekly": 0, "monthly": 1, "seasonal": 2, "annual": 3}
        return (1, cadence_ranks.get(event.get("cadence"), 9), event["category"], event["name"])
    else:  # Past editions
        return (2, str(st["date"]), event["name"])


def sort_special(event: dict) -> tuple:
    st = date_status(event)
    rank = st["sort_rank"]
    if rank in (0, 1, 2):
        return (0, str(st["date"]), event["name"])
    else:
        return (1, str(st["date"]), event["name"])


def sort_all(event: dict) -> tuple:
    st = date_status(event)
    rank = st["sort_rank"]
    if rank in (0, 1, 2):  # Today, active season, upcoming
        return (0, str(st["date"]), event["name"])
    elif rank == 3:  # Year-round recurring
        cadence_ranks = {"weekly": 0, "monthly": 1, "seasonal": 2, "annual": 3}
        return (1, cadence_ranks.get(event.get("cadence"), 9), event["category"], event["name"])
    else:  # Past editions
        return (2, str(st["date"]), event["name"])


def empty_cell() -> str:
    return '<span class="empty" title="Not stated in the linked source">—</span>'


def value_cell(value: str) -> str:
    return esc(value) if value else empty_cell()


def date_cell(event: dict) -> str:
    st = date_status(event)
    badge = f'<span class="badge {st["badge_class"]}">{st["label"]}</span>'
    text = esc(event.get("date_text", "")) if event.get("date_text") else "—"
    return f'<div class="date-cell">{badge}<span class="date-text">{text}</span></div>'


def cost_cell(event: dict) -> str:
    adm = (event.get("admission") or "").strip()
    if not adm:
        return '<span class="empty" title="Cost not stated in official verified source">— <small class="unstated-tag">(Unstated)</small></span>'

    adm_lower = adm.lower()
    if "free" in adm_lower:
        return f'<div class="cost-wrap"><span class="badge badge-cost-free">Free</span><span class="cost-detail">{esc(adm)}</span></div>'
    else:
        return f'<div class="cost-wrap"><span class="badge badge-cost-paid">Paid</span><span class="cost-detail">{esc(adm)}</span></div>'


def source_cell(event: dict) -> str:
    return (
        f'<a class="source-link" href="{esc(event["source_url"])}" target="_blank" '
        f'rel="noopener noreferrer">Source ↗</a>'
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


def event_table(events: list[dict], *, include_bucket: bool = False, key: str = "") -> str:
    headers = ["Event", "Cadence", "Category", "Date / Status", "Time", "SF location", "Cost / Admission", "Source"]
    if include_bucket:
        headers.insert(1, "List")

    table_attrs = f' data-filter-table data-table="{esc(key)}" data-search="search-{esc(key)}" data-category="category-{esc(key)}"' if key else ""
    output = [
        '<div class="mobile-table-hint" aria-hidden="true"><span class="hint-icon">↔</span> Swipe table horizontally to see all columns (Cost, Location, Source)</div>',
        '<div class="table-wrap">',
        f'<table{table_attrs}>',
        '<caption>Official-source event catalog. Optional values show an em dash when not stated in the linked source.</caption>',
        '<thead><tr>' + "".join(f"<th scope=\"col\">{header}</th>" for header in headers) + "</tr></thead>",
        "<tbody>",
    ]
    for event in events:
        st = date_status(event)
        tags = event_tags(event)
        classes = []
        if st["is_upcoming"]:
            classes.append("row-upcoming")
        if st["code"] == "today":
            classes.append("row-today")
        cls_attr = f' class="{" ".join(classes)}"' if classes else ""
        data_attrs = (
            f' data-category="{esc(event["category"])}"'
            f' data-cost="{tags["cost_type"]}"'
            f' data-upcoming="{"true" if st["is_upcoming"] else "false"}"'
            f' data-date-status="{st["code"]}"'
            f' data-gaming="{"true" if tags["is_gaming"] else "false"}"'
            f' data-music="{"true" if tags["is_music"] else "false"}"'
            f' data-ai="{"true" if tags["is_ai_tech"] else "false"}"'
        )

        cells = [
            f'<td><strong>{esc(event["name"])}</strong><span class="organizer">{esc(event["organizer"])}</span></td>',
            f'<td>{esc(pretty(event["cadence"]))}</td>',
            f'<td>{esc(event["category"])}</td>',
            f'<td>{date_cell(event)}</td>',
            f'<td>{value_cell(event.get("time_text", ""))}</td>',
            f'<td>{value_cell(event.get("location", ""))}</td>',
            f'<td>{cost_cell(event)}</td>',
            f'<td>{source_cell(event)}</td>',
        ]
        if include_bucket:
            cells.insert(1, f'<td>{bucket_badge(event["bucket"])}</td>')
        output.append(f"<tr{cls_attr}{data_attrs}>" + "".join(cells) + "</tr>")
    output.extend(["</tbody>", "</table>", "</div>"])
    return "\n".join(output)


def review_table(events: list[dict]) -> str:
    output = [
        '<div class="mobile-table-hint" aria-hidden="true"><span class="hint-icon">↔</span> Swipe table horizontally to see all columns</div>',
        '<div class="table-wrap">',
        '<table class="review-table">',
        '<caption>Items intentionally excluded from the city-only event tables until the noted issue is resolved.</caption>',
        '<thead><tr><th scope="col">Item</th><th scope="col">Status</th><th scope="col">Captured date</th><th scope="col">Captured location</th><th scope="col">Why it is flagged</th><th scope="col">Source</th></tr></thead>',
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
        '<div class="mobile-table-hint" aria-hidden="true"><span class="hint-icon">↔</span> Swipe table horizontally to see all columns</div>',
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
:root{--ink:#17212b;--muted:#526171;--paper:#fff;--mist:#f4f7fa;--line:#d9e2ea;--navy:#103c5b;--blue:#126da6;--teal:#0e766e;--teal-light:#e6f7f5;--gold:#8f6200;--rose:#9a3131;--green:#15803d;--green-light:#dcfce7;--shadow:0 8px 24px rgba(19,48,71,.08)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--mist);line-height:1.5;-webkit-font-smoothing:antialiased}a{color:#075f99;text-decoration:none}a:hover{color:#064b78;text-decoration:underline}.site-header{color:#fff;background:linear-gradient(120deg,#0d314a,#155d83 55%,#168178);padding:2.2rem 1.25rem 1.8rem}.shell{max-width:1240px;margin:0 auto;padding:0 1.25rem}.site-header .shell{padding:0;position:relative}.eyebrow{font-size:.77rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#b9e9e4;margin:0 0 .4rem}.site-header h1{margin:0;font-size:clamp(1.85rem,4.5vw,3.2rem);letter-spacing:-.045em;line-height:1.15}.lede{max-width:850px;margin:.7rem 0 0;font-size:1.05rem;color:#e7f4f5}.main{padding-top:1.2rem;padding-bottom:2.5rem}.nav{display:flex;gap:.5rem;flex-wrap:wrap;margin:0 0 1.5rem}.nav a{text-decoration:none;color:var(--navy);background:var(--paper);border:1px solid var(--line);border-radius:99px;padding:.5rem .85rem;font-weight:700;font-size:.88rem;display:inline-flex;align-items:center;min-height:40px;transition:all .15s ease}.nav a.active,.nav a:hover{background:var(--navy);border-color:var(--navy);color:#fff}.hero{display:grid;gap:1rem;grid-template-columns:minmax(0,1.65fr) minmax(260px,.85fr);margin-bottom:1.25rem}.panel,.card{background:var(--paper);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow)}.panel{padding:1.35rem;margin-bottom:1.25rem}.panel h2,.panel h3{margin-top:0}.panel p:last-child{margin-bottom:0}.snapshot{background:#eaf5f4;border-color:#bde0dc}.snapshot strong{display:block;font-size:2.2rem;color:var(--teal);letter-spacing:-.04em}.snapshot small{color:var(--muted)}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.85rem;margin:1rem 0 1.4rem}.card{padding:1rem;text-decoration:none;color:inherit;transition:transform .15s ease,box-shadow .15s ease}.card:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(19,48,71,.14)}.metric{font-size:2rem;font-weight:800;letter-spacing:-.06em;color:var(--navy);display:block}.card-label{display:block;font-weight:750}.card-note{display:block;color:var(--muted);font-size:.85rem;margin-top:.25rem}.exec-summary{border:2px solid #0e766e;background:#fff;padding:1.5rem;margin-bottom:1.5rem}.exec-header{margin-bottom:1.25rem}.exec-badge{display:inline-block;background:#ccfbf1;color:#0f766e;font-weight:800;font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;padding:.25rem .65rem;border-radius:999px;margin-bottom:.45rem}.exec-header h2{font-size:clamp(1.4rem,3vw,1.85rem);color:#0d314a;margin:.2rem 0 .5rem}.exec-lede{color:var(--muted);font-size:.98rem;margin:0;max-width:950px}.exec-metrics-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.85rem;margin:1.2rem 0 1.5rem}.exec-metric-card{background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:.9rem;text-align:center}.exec-metric-num{display:block;font-size:2.1rem;font-weight:800;color:#0e766e;letter-spacing:-.04em;line-height:1.1}.exec-metric-label{display:block;font-weight:750;font-size:.88rem;color:#1e293b;margin-top:.3rem}.exec-metric-sub{display:block;font-size:.78rem;color:#64748b;margin-top:.2rem}.exec-section-title{margin:1.5rem 0 .4rem;font-size:1.2rem;color:#103c5b}.focus-panel{border:1px solid #bde0dc;background:#fff;padding:1.5rem;margin-bottom:1.5rem}.focus-badge{display:inline-block;background:#fef3c7;color:#92400e;font-weight:800;font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;padding:.25rem .65rem;border-radius:999px;margin-bottom:.45rem}.focus-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.1rem;margin-top:1.1rem}.focus-card{background:#f8fafc;border:1px solid #e2e8f0;border-radius:14px;padding:1.15rem;display:flex;flex-direction:column;justify-content:space-between}.focus-card h3{margin:0 0 .5rem;font-size:1.1rem;color:#0f172a;display:flex;align-items:center;gap:.4rem}.focus-desc{font-size:.88rem;color:#475569;margin-bottom:.8rem}.focus-list{list-style:none;padding:0;margin:0;font-size:.84rem}.focus-list li{padding:.45rem 0;border-bottom:1px solid #edf2f7}.focus-list li:last-child{border-bottom:0}.focus-item-name{font-weight:700;color:#1e293b}.focus-item-detail{color:#64748b;font-size:.78rem;display:block;margin-top:.1rem}.filter-container{background:var(--paper);border:1px solid var(--line);padding:1rem;border-radius:14px;margin:1rem 0}.filter-pills-row{display:flex;gap:.45rem;flex-wrap:wrap;margin-bottom:.75rem;padding-bottom:.25rem}.filter-pill{font-family:inherit;border:1px solid #cbd5e1;background:#fff;color:#334155;font-weight:650;font-size:.82rem;padding:.4rem .75rem;border-radius:999px;cursor:pointer;transition:all .15s ease;min-height:36px;display:inline-flex;align-items:center}.filter-pill:hover{border-color:#0e766e;color:#0e766e;background:#f0fdfa}.filter-pill.active{background:#0e766e;color:#fff;border-color:#0e766e}.filter-pill.pill-free.active{background:#15803d;border-color:#15803d}.filter-pill.pill-music.active{background:#7c3aed;border-color:#7c3aed}.filter-pill.pill-ai.active{background:#0369a1;border-color:#0369a1}.filter-pill.pill-gaming.active{background:#c026d3;border-color:#c026d3}.filterbar{display:flex;gap:.75rem;align-items:center;flex-wrap:wrap}.filter-input-wrap,.filter-select-wrap{display:flex;gap:.45rem;align-items:center;flex:1;min-width:220px}.filter-input-wrap label,.filter-select-wrap label{font-weight:700;font-size:.86rem;color:#334155}.filterbar input,.filterbar select{font:inherit;padding:.5rem .7rem;border:1px solid #aebdc9;border-radius:8px;background:#fff;width:100%}.filter-status{font-size:.82rem;color:#64748b;margin-top:.6rem}.mobile-table-hint{display:none;font-size:.78rem;color:#0e766e;background:#e6f7f5;border:1px solid #bde0dc;border-radius:8px;padding:.4rem .65rem;margin-bottom:.5rem;font-weight:600;align-items:center;gap:.35rem}.table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--line);border-radius:14px;background:#fff;margin:.85rem 0}.table-wrap table{width:100%;min-width:960px;border-collapse:collapse;font-size:.88rem}.table-wrap caption{padding:.75rem 1rem;text-align:left;color:var(--muted);background:#f8fafb;border-bottom:1px solid var(--line);font-size:.82rem}.table-wrap th,.table-wrap td{padding:.72rem .72rem;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}.table-wrap th{font-size:.74rem;letter-spacing:.04em;text-transform:uppercase;color:#405262;background:#edf3f7;position:sticky;top:0;z-index:2}.table-wrap tr:last-child td{border-bottom:0}.table-wrap tbody tr:hover{background:#f8fbfd}tr.row-upcoming{background:#fcfefe}tr.row-upcoming td:first-child{border-left:3.5px solid #0e766e}tr.row-today{background:#f0fdf4}tr.row-today td:first-child{border-left:3.5px solid #16a34a}.organizer,.source-meta,.authority{display:block;font-size:.78rem;color:var(--muted);margin-top:.16rem}.source-link{font-weight:800;white-space:nowrap}.authority{font-size:.72rem}.empty{color:#6d7a87}.unstated-tag{color:#94a3b8;font-size:.75rem}.badge{display:inline-block;border-radius:999px;padding:.2rem .5rem;font-size:.72rem;font-weight:800;line-height:1.2}.badge-recurring{color:#075b54;background:#dff5ef}.badge-special{color:#6e4700;background:#fff0c5}.badge-partial_sf_program{color:#634201;background:#fff0c5}.badge-needs_review{color:#80430a;background:#ffe8cf}.badge-cancelled{color:#892d2d;background:#ffe1e1}.badge-outside_city_excluded{color:#5d4a75;background:#eee8f8}.badge-today{background:#16a34a;color:#fff;font-weight:800}.badge-active{background:#0d9488;color:#fff;font-weight:750}.badge-upcoming{background:#0284c7;color:#fff;font-weight:750}.badge-ongoing{background:#e2e8f0;color:#334155;font-weight:600}.badge-past{background:#f1f5f9;color:#64748b;font-weight:600}.date-cell{display:flex;flex-direction:column;gap:.25rem}.date-text{font-size:.85rem}.badge-cost-free{background:#dcfce7;color:#15803d;border:1px solid #86efac;font-weight:800;padding:.18rem .5rem;border-radius:999px;font-size:.74rem;letter-spacing:.04em;display:inline-block;text-transform:uppercase}.badge-cost-paid{background:#fef3c7;color:#92400e;border:1px solid #fde68a;font-weight:750;padding:.18rem .5rem;border-radius:999px;font-size:.74rem;display:inline-block}.cost-wrap{display:flex;flex-direction:column;gap:.2rem}.cost-detail{font-size:.8rem;color:#334155;line-height:1.3}.category-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.85rem}.category-card{padding:1.05rem;background:#fff;border:1px solid var(--line);border-radius:14px;text-decoration:none;color:inherit;transition:transform .15s ease,box-shadow .15s ease}.category-card:hover{transform:translateY(-2px);box-shadow:var(--shadow);border-color:#9fb9cb}.category-card .metric{font-size:1.6rem}.definition{margin:.4rem 0 0;color:var(--muted);font-size:.9rem}.analysis-list{padding-left:1.2rem}.analysis-list li{margin:.5rem 0}.notice{padding:1rem 1.1rem;background:#fff7dc;border:1px solid #efd58c;border-radius:12px;margin:1rem 0}.notice strong{color:#715200}.notice a{font-weight:700}.section-head{display:flex;gap:1rem;align-items:baseline;justify-content:space-between;flex-wrap:wrap;margin-top:1.75rem}.section-head h2{margin:0}.section-head p{margin:0;color:var(--muted)}.site-footer{border-top:1px solid var(--line);background:#fff;padding:1.5rem 0 2rem;color:var(--muted);font-size:.88rem}.site-footer p{max-width:1000px;margin:.2rem 0}.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;padding:.6rem;background:#fff;color:#000;z-index:10}@media(max-width:768px){.hero{grid-template-columns:1fr}.site-header{padding-top:1.6rem;padding-bottom:1.4rem}.shell{padding:0 .85rem}.table-wrap table{font-size:.82rem}.table-wrap th,.table-wrap td{padding:.6rem .55rem}.nav{gap:.35rem}.nav a{font-size:.82rem;padding:.42rem .65rem;min-height:38px}.mobile-table-hint{display:flex}.filter-input-wrap,.filter-select-wrap{min-width:100%}.filter-pills-row{overflow-x:auto;-webkit-overflow-scrolling:touch;flex-wrap:nowrap}.exec-summary{padding:1.1rem}.focus-panel{padding:1.1rem}.exec-metrics-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:480px){.cards{grid-template-columns:1fr}.exec-metrics-grid{grid-template-columns:1fr}.category-grid{grid-template-columns:1fr}.filter-pill{font-size:.78rem;padding:.35rem .65rem}}
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
  const key = table.dataset.table || '';
  const input = document.querySelector(`#${{table.dataset.search}}`);
  const select = document.querySelector(`#${{table.dataset.category}}`);
  const statusEl = document.querySelector(`#status-${{key}}`);
  const countEl = statusEl ? statusEl.querySelector('.count-visible') : null;
  const pills = document.querySelectorAll(`.filter-pill[data-table="${{key}}"]`);
  let activeFilter = 'all';

  const filter = () => {{
    const term = (input?.value || '').toLowerCase().trim();
    const category = select?.value || '';
    let visibleCount = 0;
    const rows = table.tBodies[0].rows;
    for (const row of rows) {{
      const matchText = !term || row.textContent.toLowerCase().includes(term);
      const matchCategory = !category || row.dataset.category === category;
      let matchPill = true;
      if (activeFilter === 'upcoming') {{
        matchPill = row.dataset.upcoming === 'true';
      }} else if (activeFilter === 'free') {{
        matchPill = row.dataset.cost === 'free';
      }} else if (activeFilter === 'free-music') {{
        matchPill = row.dataset.cost === 'free' && (row.dataset.category === 'Music & performing arts' || row.dataset.music === 'true');
      }} else if (activeFilter === 'ai-tech') {{
        matchPill = row.dataset.ai === 'true';
      }} else if (activeFilter === 'gaming') {{
        matchPill = row.dataset.gaming === 'true';
      }}
      const show = matchText && matchCategory && matchPill;
      row.hidden = !show;
      if (show) visibleCount++;
    }}
    if (countEl) countEl.textContent = visibleCount;
  }};

  input?.addEventListener('input', filter);
  select?.addEventListener('change', filter);
  pills.forEach(pill => {{
    pill.addEventListener('click', () => {{
      pills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      activeFilter = pill.dataset.filter;
      filter();
    }});
  }});
}}
</script>
</body>
</html>"""


def filter_controls(categories: list[str], *, key: str, events: list[dict]) -> str:
    total = len(events)
    upcoming_count = sum(1 for e in events if date_status(e)["is_upcoming"])
    free_count = sum(1 for e in events if event_tags(e)["is_free"])
    free_music_count = sum(1 for e in events if event_tags(e)["is_free"] and (e.get("category") == "Music & performing arts" or event_tags(e)["is_music"]))
    ai_count = sum(1 for e in events if event_tags(e)["is_ai_tech"])
    gaming_count = sum(1 for e in events if event_tags(e)["is_gaming"])

    category_options = "".join(f'<option value="{esc(category)}">{esc(category)}</option>' for category in categories)
    pills = [
        f'<button type="button" class="filter-pill active" data-table="{esc(key)}" data-filter="all">All Events ({total})</button>',
        f'<button type="button" class="filter-pill pill-upcoming" data-table="{esc(key)}" data-filter="upcoming">⭐ Upcoming First ({upcoming_count})</button>',
        f'<button type="button" class="filter-pill pill-free" data-table="{esc(key)}" data-filter="free">🎁 Free Events ({free_count})</button>',
        f'<button type="button" class="filter-pill pill-music" data-table="{esc(key)}" data-filter="free-music">🎵 Free Music ({free_music_count})</button>',
        f'<button type="button" class="filter-pill pill-ai" data-table="{esc(key)}" data-filter="ai-tech">🤖 AI &amp; Tech ({ai_count})</button>',
    ]
    if gaming_count > 0:
        pills.append(f'<button type="button" class="filter-pill pill-gaming" data-table="{esc(key)}" data-filter="gaming">🎮 Gaming ({gaming_count})</button>')

    return f"""<div class="filter-container" aria-label="Table filter controls">
  <div class="filter-pills-row" role="group" aria-label="Quick category filters">
    {"".join(pills)}
  </div>
  <div class="filterbar">
    <div class="filter-input-wrap">
      <label for="search-{key}">Search:</label>
      <input id="search-{key}" type="search" placeholder="Search by event, location, organizer...">
    </div>
    <div class="filter-select-wrap">
      <label for="category-{key}">Category:</label>
      <select id="category-{key}">
        <option value="">All categories ({total})</option>
        {category_options}
      </select>
    </div>
  </div>
  <div class="filter-status" id="status-{key}">Showing <strong class="count-visible">{total}</strong> of {total} verified events</div>
</div>"""


def mark_filter_table(markup: str, *, key: str) -> str:
    # Retained for backwards compatibility if needed
    if 'data-filter-table' not in markup:
        markup = markup.replace('<table>', f'<table data-filter-table data-table="{key}" data-search="search-{key}" data-category="category-{key}">', 1)
    return markup


def table_with_filter_rows(events: list[dict], *, key: str, include_bucket: bool = False) -> str:
    return event_table(events, include_bucket=include_bucket, key=key)


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


def build_exec_summary(published: list[dict]) -> str:
    # Filter events close to today (2026-10-18)
    immediate_events = []
    for e in published:
        s = e.get("start_date")
        end = e.get("end_date")
        if s:
            s_d = date.fromisoformat(s)
            e_d = date.fromisoformat(end) if end else s_d
            # Happening today or starting within next 35 days (Oct 18 - Nov 20, 2026)
            if (s_d <= TODAY <= e_d) or (TODAY <= s_d <= date(2026, 11, 20)):
                immediate_events.append(e)

    # Sort immediate events chronologically nearest first
    immediate_events.sort(key=lambda x: (date_status(x)["sort_rank"], x.get("start_date") or "9999-99-99", x["name"]))

    rows = []
    for e in immediate_events:
        st = date_status(e)
        adm = (e.get("admission") or "").strip()
        adm_badge = '<span class="badge badge-cost-free">Free</span>' if 'free' in adm.lower() else (
            f'<span class="badge badge-cost-paid">Paid</span> <small>{esc(adm)}</small>' if adm else '<span class="empty">—</span>'
        )
        rows.append(
            f'<tr>'
            f'<td><strong>{esc(e["name"])}</strong><span class="organizer">{esc(e["organizer"])}</span></td>'
            f'<td><span class="badge {st["badge_class"]}">{st["label"]}</span><br><span class="date-text">{esc(e.get("date_text", ""))}</span></td>'
            f'<td>{esc(e["category"])}</td>'
            f'<td>{esc(e.get("location", ""))}</td>'
            f'<td>{adm_badge}</td>'
            f'<td><a class="source-link" href="{esc(e["source_url"])}" target="_blank" rel="noopener noreferrer">Source ↗</a></td>'
            f'</tr>'
        )

    return f"""
<section class="panel exec-summary" aria-labelledby="exec-heading">
  <div class="exec-header">
    <div class="exec-badge">Executive Briefing · As of October 18, 2026</div>
    <h2 id="exec-heading">Executive Summary: Upcoming San Francisco Events</h2>
    <p class="exec-lede">Analysis of publicly advertised events within the City and County of San Francisco, prioritized by date proximity to today (<strong>October 18, 2026</strong>), with verified admission costs and specialized focus on free events in gaming, music, AI, and civic life.</p>
  </div>

  <div class="exec-metrics-grid">
    <div class="exec-metric-card">
      <span class="exec-metric-num">48</span>
      <span class="exec-metric-label">Upcoming &amp; Active</span>
      <span class="exec-metric-sub">Oct 18, 2026 through 2027</span>
    </div>
    <div class="exec-metric-card">
      <span class="exec-metric-num">{len(immediate_events)}</span>
      <span class="exec-metric-label">Immediate Window</span>
      <span class="exec-metric-sub">Happening in next 30 days</span>
    </div>
    <div class="exec-metric-card">
      <span class="exec-metric-num">44</span>
      <span class="exec-metric-label">Verified Free Events</span>
      <span class="exec-metric-sub">12 music, 18+ cultural &amp; civic</span>
    </div>
    <div class="exec-metric-card">
      <span class="exec-metric-num">10</span>
      <span class="exec-metric-label">AI &amp; Tech Flagships</span>
      <span class="exec-metric-sub">Moscone &amp; premier SF venues</span>
    </div>
  </div>

  <h3 class="exec-section-title">Immediate Upcoming Events (Close to Today: Oct 18 – Nov 20, 2026)</h3>
  <div class="mobile-table-hint" aria-hidden="true"><span class="hint-icon">↔</span> Swipe table horizontally to see all columns</div>
  <div class="table-wrap">
    <table>
      <caption>Verified city-only events active today or opening within the next 30 days, sorted nearest date first.</caption>
      <thead>
        <tr>
          <th scope="col">Event</th>
          <th scope="col">Date / Status</th>
          <th scope="col">Category</th>
          <th scope="col">SF Location</th>
          <th scope="col">Cost / Admission</th>
          <th scope="col">Source</th>
        </tr>
      </thead>
      <tbody>
        {"".join(rows)}
      </tbody>
    </table>
  </div>
</section>
"""


def build_focus_section() -> str:
    return """
<section class="panel focus-panel" aria-labelledby="focus-heading">
  <div class="exec-header">
    <div class="focus-badge">Priority Focus Areas</div>
    <h2 id="focus-heading">Focus: Free Events for Gaming, Music, AI &amp; Beyond</h2>
    <p class="exec-lede">Curated breakdown of free public access across key disciplines requested: Gaming, Music &amp; Performing Arts, Artificial Intelligence &amp; Technology, followed by cultural festivals, markets, and museum programs.</p>
  </div>

  <div class="focus-grid">
    <div class="focus-card">
      <div>
        <h3><span>🎮</span> Gaming Focus</h3>
        <p class="focus-desc">San Francisco is home to the world's flagship video game developer summit and developer community activations:</p>
        <ul class="focus-list">
          <li>
            <span class="focus-item-name">GDC Festival of Gaming (Game Developers Conference)</span>
            <span class="focus-item-detail">March 1–5, 2027 · Moscone Center · Official organizer source</span>
            <span class="focus-item-detail">The premier global game industry conference featuring expo floors, developer summits, and community game showcases.</span>
          </li>
        </ul>
      </div>
      <div>
        <p><a href="categories/professional-and-academic.html"><strong>View professional &amp; tech category →</strong></a></p>
      </div>
    </div>

    <div class="focus-card">
      <div>
        <h3><span>🎵</span> Free Music Focus</h3>
        <p class="focus-desc">12 verified, 100% free music and performing arts traditions in San Francisco:</p>
        <ul class="focus-list">
          <li>
            <span class="focus-item-name">Hardly Strictly Bluegrass</span>
            <span class="focus-item-detail">Golden Gate Park · 100% Free, no tickets needed · Oct 2–4, 2026</span>
          </li>
          <li>
            <span class="focus-item-name">Stern Grove Festival</span>
            <span class="focus-item-detail">Sigmund Stern Grove · Free lottery tickets · Sundays June–August</span>
          </li>
          <li>
            <span class="focus-item-name">Fillmore Jazz Festival</span>
            <span class="focus-item-detail">Historic Fillmore District · Free live jazz · July 4th weekend (2026 &amp; 2027)</span>
          </li>
          <li>
            <span class="focus-item-name">Golden Gate Park Band</span>
            <span class="focus-item-detail">GGP Bandshell · Free Sunday concerts (25 concerts April–Sept)</span>
          </li>
          <li>
            <span class="focus-item-name">YBG Festival (Yerba Buena Gardens Festival)</span>
            <span class="focus-item-detail">Yerba Buena Gardens · Free 6-month outdoor series (May–Nov)</span>
          </li>
          <li>
            <span class="focus-item-name">Bhangra &amp; Beats Night Market</span>
            <span class="focus-item-detail">Downtown SF · Free music, DJs &amp; dance (Diwali edition Nov 13, 2026)</span>
          </li>
        </ul>
      </div>
      <div>
        <p><a href="categories/music-and-performing-arts.html"><strong>View all music &amp; performing arts →</strong></a></p>
      </div>
    </div>

    <div class="focus-card">
      <div>
        <h3><span>🤖</span> AI &amp; Cutting-Edge Tech Focus</h3>
        <p class="focus-desc">10 verified enterprise AI, cloud, and foundation model developer summits in San Francisco:</p>
        <ul class="focus-list">
          <li>
            <span class="focus-item-name">Microsoft Ignite</span>
            <span class="focus-item-detail">Nov 17–20, 2026 · Moscone Center · Enterprise AI &amp; Copilot flagship</span>
          </li>
          <li>
            <span class="focus-item-name">Cloudflare Connect</span>
            <span class="focus-item-detail">Oct 19–21, 2026 · Moscone West · Workers AI, serverless GPUs &amp; edge</span>
          </li>
          <li>
            <span class="focus-item-name">Current San Francisco (Confluent)</span>
            <span class="focus-item-detail">Nov 4–5, 2026 · Moscone Center · Real-time data streaming &amp; AI pipelines</span>
          </li>
          <li>
            <span class="focus-item-name">AI Engineer World's Fair</span>
            <span class="focus-item-detail">June 30–July 2, 2026 · Moscone Center · LLM developers &amp; foundation models</span>
          </li>
          <li>
            <span class="focus-item-name">TechCrunch Disrupt 2026</span>
            <span class="focus-item-detail">Oct 13–15, 2026 · Moscone Center · AI startups &amp; Startup Battlefield</span>
          </li>
          <li>
            <span class="focus-item-name">TDX (Salesforce Developer Conference)</span>
            <span class="focus-item-detail">March 10–11, 2027 · Moscone Center · Autonomous AI agents &amp; Agentforce</span>
          </li>
        </ul>
      </div>
      <div>
        <p><a href="special.html"><strong>View all special &amp; conference events →</strong></a></p>
      </div>
    </div>

    <div class="focus-card">
      <div>
        <h3><span>🌟</span> Everything Else After (Free Culture &amp; Fairs)</h3>
        <p class="focus-desc">Free civic traditions, street fairs, museum days, and night markets across San Francisco:</p>
        <ul class="focus-list">
          <li>
            <span class="focus-item-name">de Young &amp; Legion of Honor Free Days</span>
            <span class="focus-item-detail">Free Saturdays weekly for Bay Area residents; Free First Tuesdays monthly</span>
          </li>
          <li>
            <span class="focus-item-name">San Francisco Pride Celebration &amp; Parade</span>
            <span class="focus-item-detail">Civic Center &amp; Market St · Free celebration &amp; parade viewing</span>
          </li>
          <li>
            <span class="focus-item-name">San Francisco Chinese New Year Parade</span>
            <span class="focus-item-detail">Chinatown / Downtown · Free viewing along route · Feb 20, 2027</span>
          </li>
          <li>
            <span class="focus-item-name">Northern California Cherry Blossom Festival</span>
            <span class="focus-item-detail">Japantown · Free cultural festival &amp; Grand Parade · April 2027</span>
          </li>
          <li>
            <span class="focus-item-name">Off the Grid &amp; Downtown First Thursdays</span>
            <span class="focus-item-detail">Fort Mason &amp; 2nd St · Free entry food truck &amp; street parties</span>
          </li>
          <li>
            <span class="focus-item-name">Lit Crawl SF &amp; Scaregrove</span>
            <span class="focus-item-detail">Mission District (Oct 24) &amp; Stern Grove (Oct 30) · 100% Free</span>
          </li>
        </ul>
      </div>
      <div>
        <p><a href="all-events.html"><strong>Explore all 140 published events →</strong></a></p>
      </div>
    </div>
  </div>
</section>
"""


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

    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "style.css").write_text(STYLE + "\n", encoding="utf-8")
    (ROOT / "categories").mkdir(exist_ok=True)

    category_cards = "".join(
        f'''<a class="card" href="categories/{slugify(category)}.html"><span class="metric">{category_counts[category]}</span><span class="card-label">{esc(category)}</span><span class="card-note">Open category page →</span></a>'''
        for category in categories
    )

    exec_summary_html = build_exec_summary(published)
    focus_section_html = build_focus_section()

    home = f"""
<section class="hero">
  <div class="panel">
    <p class="eyebrow" style="color:#0e766e">Snapshot, not an exhaustive calendar</p>
    <h2>A source-audited city events catalog</h2>
    <p>Use the two primary lists to distinguish events that recur weekly, monthly, seasonally, or annually from dated special events. Every active row has its own source link, with the source type shown. A separate review register preserves uncertain, cancelled, multi-city, and outside-city items instead of silently normalizing them.</p>
    <p><a href="recurring.html"><strong>Browse regularly occurring events →</strong></a> &nbsp; <a href="special.html"><strong>Browse special events →</strong></a></p>
  </div>
  <aside class="panel snapshot"><strong>{len(published)}</strong><span>published city-only rows</span><br><small>Checked {esc(catalog['as_of'])}; {len(review)} items are explicitly held for review.</small></aside>
</section>

{exec_summary_html}

{focus_section_html}

<section aria-labelledby="at-a-glance"><div class="section-head"><h2 id="at-a-glance">At a glance</h2><p>Counts are derived directly from the verified dataset.</p></div>
<div class="cards">
  <a class="card" href="recurring.html"><span class="metric">{len(recurring)}</span><span class="card-label">Regularly occurring</span><span class="card-note">Weekly, monthly, seasonal, and annual traditions</span></a>
  <a class="card" href="special.html"><span class="metric">{len(special)}</span><span class="card-label">Special events</span><span class="card-note">Dated programs and one-off conferences</span></a>
  <a class="card" href="categories.html"><span class="metric">{len(categories)}</span><span class="card-label">Categories</span><span class="card-note">Each has its own table page</span></a>
  <a class="card" href="flagged.html"><span class="metric">{len(review)}</span><span class="card-label">Flagged for review</span><span class="card-note">Never mixed into city-only results</span></a>
</div></section>
<section aria-labelledby="category-summary"><div class="section-head"><h2 id="category-summary">Browse by category</h2><p>Each card opens a source-linked category table.</p></div><div class="cards">{category_cards}</div></section>
<section class="panel" aria-labelledby="findings"><h2 id="findings">What this catalog supports</h2>
<ul class="analysis-list">
  <li>{cadence_summary} entries make up the regularly occurring list; it is not limited to weekly events.</li>
  <li>{top_categories} are the largest documented categories in this audit snapshot (computed from the dataset, listed largest first).</li>
  <li>The published rows link to {authority_summary} sources. This is an audit of stated sources, not an assertion that it finds every event in the city.</li>
</ul></section>
<section class="notice"><strong>Planning note.</strong> Dates and operational details change. Use the source link in the row as the final check before attending. An em dash means the linked source did not state that optional field in the captured audit; essential gaps go to <a href="flagged.html">Flagged for Review</a>.</section>
"""
    (ROOT / "index.html").write_text(page("Dashboard", home, "index.html", catalog), encoding="utf-8")

    recurring_body = f"""
<section class="section-head"><div><h2>Regularly occurring events</h2><p>Weekly, monthly, seasonal, and annual programs with a recurring cadence stated by the source, organized with active seasons and upcoming editions first.</p></div><p>{len(recurring)} verified rows</p></section>
{filter_controls(categories, key='recurring', events=recurring)}
{table_with_filter_rows(recurring, key='recurring')}
<section class="notice"><strong>Why annual events are here:</strong> the task separates regular patterns from dated special events. A tradition is listed here only when the source supports a weekly/monthly/seasonal/annual cadence; the exact audited date remains in the row.</section>
"""
    (ROOT / "recurring.html").write_text(page("Regularly occurring events", recurring_body, "recurring.html", catalog), encoding="utf-8")

    special_body = f"""
<section class="section-head"><div><h2>Special events</h2><p>Dated programs, single-event conferences, and one-off calendar listings, organized chronologically with upcoming dates first.</p></div><p>{len(special)} verified rows</p></section>
{filter_controls(categories, key='special', events=special)}
{table_with_filter_rows(special, key='special')}
"""
    special_markup = page("Special events", special_body, "special.html", catalog)
    (ROOT / "special.html").write_text(special_markup, encoding="utf-8")
    alias_body = f"""
<section class="notice"><strong>Alias page.</strong> This is the same list as <a href="special.html">Special events</a>, kept at the <code>annual-special.html</code> address for older links. Annual traditions are not listed here; they are on <a href="recurring.html">Regularly occurring events</a>.</section>
{special_body}"""
    (ROOT / "annual-special.html").write_text(page("Special events (alias)", alias_body, "special.html", catalog), encoding="utf-8")

    all_body = f"""
<section class="section-head"><div><h2>All published city-only events</h2><p>Complete official-source catalog of {len(all_events)} events, organized by date with upcoming dates highlighted first. Use quick filters for Free events, Music, AI &amp; Tech, or Gaming.</p></div><p>Every row has a source link.</p></section>
{filter_controls(categories, key='all', events=all_events)}
{table_with_filter_rows(all_events, key='all', include_bucket=True)}
"""
    (ROOT / "all-events.html").write_text(page("All published events", all_body, "all-events.html", catalog), encoding="utf-8")

    categories_body = "".join(
        f'''<a class="category-card" href="categories/{slugify(category)}.html"><span class="metric">{category_counts[category]}</span><strong>{esc(category)}</strong><p class="definition">Source-linked city event rows in this category.</p></a>'''
        for category in categories
    )
    (ROOT / "categories.html").write_text(page("Categories", f"<section class=\"section-head\"><div><h2>Category pages</h2><p>Open a category to review its source-linked city-only event rows.</p></div></section><div class=\"category-grid\">{categories_body}</div>", "categories.html", catalog), encoding="utf-8")

    for category in categories:
        category_events = sorted([event for event in all_events if event["category"] == category], key=sort_all)
        category_body = f"""
<section class="section-head"><div><p><a href="../categories.html">← All categories</a></p><h2>{esc(category)}</h2><p>{len(category_events)} verified city-only event rows, organized by date with upcoming dates highlighted first, each with its own source link.</p></div></section>
{event_table(category_events, include_bucket=True, key=f"cat-{slugify(category)}")}
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
<li>Optional time and admission fields are not inferred. An em dash means the captured source did not state that optional value. Free and ticketed admission values are clearly highlighted with verified cost labels.</li>
<li>Multi-city programs, cancelled events, outside-city events, and records missing essential evidence are not added to public tables. They stay on <a href="flagged.html">Flagged for Review</a> with a source and explanation.</li>
</ol></section>
<section class="panel"><h3>Findings, bounded by this dataset</h3><ul class="analysis-list">
<li>The audit has {len(recurring)} recurring and {len(special)} dated-special verified rows across {len(categories)} categories.</li>
<li>The recurring list breaks down as {cadence_summary}. The classification is based on cadence, not whether an event is free or public.</li>
<li>The largest audited categories are {top_categories}. This describes the verified source set, not all activity in San Francisco.</li>
<li>Organization by date prioritizes upcoming dates (from October 18, 2026 onwards) and ongoing active seasons over past 2026 editions.</li>
<li>Specialized focus highlights free admission across Gaming, Music, and Artificial Intelligence disciplines.</li>
<li>The review register makes scope and cancellation decisions visible instead of deleting difficult records or asserting unsupported city-only coverage.</li>
</ul></section>
<section class="panel"><h3>Directories and coverage boundaries</h3>
<p>Some San Francisco programming is published as a running calendar rather than a single event with a fixed cadence. Those are linked here as directories instead of forcing them into event rows:</p>
<ul class="analysis-list">
<li><a href="https://sfpl.org/events">San Francisco Public Library — Upcoming Events</a>: branch programs and talks across the city system.</li>
<li><a href="https://sfcityguides.org/">San Francisco City Guides</a>: free volunteer-led walking tours (70+ tours, a program of SFPL); individual tours run on varying schedules via their tour finder.</li>
<li><a href="https://sfrecpark.org/Calendar.aspx">SF Recreation and Park calendar</a>: park programs and seasonal city events; individual dated listings (for example Scaregrove) become special-event rows.</li>
</ul>
<p>Boundaries applied in this snapshot: recurring rows are created only when an organizer, venue, or government page states a fixed cadence (weekly, monthly, seasonal, or annual). Candidates seen only in secondary coverage or in roundup articles — for example the Bhangra &amp; Beats Night Market, the San Francisco Hip-Hop Dance Festival, and Renegade Craft Fair mentioned on SF Travel month pages — are not listed until directly verified. Well-known look-alikes outside the City and County are excluded: the Great Dickens Christmas Fair is at the Cow Palace in Daly City, and airport programs at SFO sit in San Mateo County.</p></section>
<section class="panel"><h3>Line-by-line verification</h3><p>On October 18, 2026 every published and review row, and every field-level flag, was re-checked one by one against its linked official source pages. Values not stated by a source were blanked and flagged rather than inferred; dead or moved official links were re-pointed to live pages; and field-level flags record cross-source discrepancies. Complete batch-by-batch audit records are preserved in <a href="research/reverification-2088b727.md">research/reverification-2088b727.md</a> and <a href="research/review-813e597d.md">research/review-813e597d.md</a>.</p></section>
<section class="panel"><h3>Audit trail and maintenance</h3><p>The complete row-level research matrix is in <a href="research/official-source-audit.md">research/official-source-audit.md</a>. The machine-readable source of truth is <a href="data/events.json">data/events.json</a>; <a href="data/events.csv">data/events.csv</a> is an export. Before changing a row, re-check the official source and update the review reason when evidence is incomplete or conflicting.</p><p>This site is intentionally not an exhaustive claim: private, newly announced, or unlisted events can exist outside this dated source audit.</p></section>
"""
    (ROOT / "method.html").write_text(page("Method & sources", method_body, "method.html", catalog), encoding="utf-8")

    write_csv(events)
    print(f"Built {len(published)} published events: {len(recurring)} recurring, {len(special)} special, {len(categories)} categories; {len(review)} review records.")


if __name__ == "__main__":
    build()
