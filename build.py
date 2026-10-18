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

# The brief keeps free events as the main section and paid events in a separate one,
# so the navigation is ordered free-first and the paid section is its own page.
NAV_ITEMS = [
    ("index.html", "Dashboard"),
    ("free.html", "Free events (main)"),
    ("paid.html", "Paid & ticketed"),
    ("upcoming.html", "Upcoming by date"),
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
FREE_HINTS = ("free", "no-cost", "no cost", "no fundraising minimum", "suggested")
PAID_HINTS = ("$", "tickets sold", "pass", "price", "ticket")
# A free statement that also names a ticketed/paid option is "mixed", not "free".
TICKETED_HINTS = ("ticketed", "tickets sold", "reserved", "seating tickets", "hospitality packages")
# A gate with no published price.  Calling these "paid" would be an inference: the
# source states that registration or an invitation is required, not what it costs.
RESTRICTED_HINTS = (
    "registration required", "invitation only", "by invitation",
    "application only", "apply to attend",
)

# Free-first split used by every page: the main section carries free/mixed rows only,
# and everything else lives in the separate paid section.
FREE_CLASSES = ("free", "mixed")
NONFREE_CLASSES = ("paid", "restricted", "not-stated")


def cost_class(admission: str) -> str:
    """Classify a sourced admission string.  Never guesses: blank means not stated."""
    text = (admission or "").strip().lower()
    if not text:
        return "not-stated"
    has_free = any(hint in text for hint in FREE_HINTS)
    if has_free:
        if "$" in text or any(hint in text for hint in TICKETED_HINTS):
            return "mixed"
        return "free"
    if any(hint in text for hint in PAID_HINTS):
        return "paid"
    if any(hint in text for hint in RESTRICTED_HINTS):
        return "restricted"
    return "not-stated"


def is_free(event: dict) -> bool:
    return cost_class(event.get("admission", "")) in FREE_CLASSES


COST_LABELS = {
    "free": "Free",
    "paid": "Paid / ticketed",
    "mixed": "Free or partly ticketed",
    "restricted": "Registration / invitation — no price published",
    "not-stated": "Not stated",
}

COST_SHORT_LABELS = {
    "free": "Free",
    "mixed": "Free or partly free",
    "paid": "Paid / ticketed",
    "restricted": "Registration only",
    "not-stated": "Cost not stated",
}


def cost_cell(event: dict) -> str:
    admission = (event.get("admission") or "").strip()
    kind = cost_class(admission)
    if kind == "not-stated":
        return (
            '<span class="cost cost-unknown" title="The linked source did not state a cost for this event">'
            "Not stated</span>"
            '<span class="cost-detail">The linked official page published no price — never assumed free</span>'
        )
    label = COST_LABELS[kind]
    text = f'<span class="cost cost-{kind}">{esc(label)}</span>'
    # Skip the detail line when the sourced wording adds nothing to the label itself.
    redundant = {"free", "free admission", "no cost", "no-cost", "free.", "free admission."}
    if admission and admission.strip().lower() not in redundant:
        text += f'<span class="cost-detail">{esc(admission)}</span>'
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
    # These rows are weekly / monthly / seasonal programs whose source states a schedule
    # rather than one date. The label points at the sourced schedule text in the row.
    "undated": "Repeating — no single date",
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


# --------------------------------------------------------------------------- #
# focus areas — the brief asks for free gaming, music and AI events first and
# everything else after.  The assignment below is derived only from the verified
# category and the event's own name, never from prose written by hand.
# --------------------------------------------------------------------------- #
TECH_CATEGORY = "Technology, AI & gaming"
MUSIC_CATEGORY = "Music & performing arts"
GAMING_WORDS = re.compile(
    r"\b(game|games|gaming|gdc|devs|arcade|esports|play|player|video)\b", re.IGNORECASE
)

FOCUS_AREAS = (
    ("gaming", "Gaming"),
    ("music", "Music & performing arts"),
    ("ai", "AI & technology"),
    ("other", "Everything else"),
)
FOCUS_LABELS = dict(FOCUS_AREAS)
FOCUS_RANK = {key: index for index, (key, _) in enumerate(FOCUS_AREAS)}


def focus_area(event: dict) -> str:
    """Return the focus key for a row: gaming, music, ai, or other."""
    category = event.get("category", "")
    haystack = f"{event.get('name', '')} {event.get('organizer', '')}"
    if category == TECH_CATEGORY:
        return "gaming" if GAMING_WORDS.search(haystack) else "ai"
    if category == MUSIC_CATEGORY:
        return "music"
    return "other"


def sort_focus(event: dict, as_of: date) -> tuple:
    """Focus area first (gaming, music, AI, everything else), then date-first."""
    return (FOCUS_RANK[focus_area(event)],) + sort_key(event, as_of)


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
        "“Not stated” in the Cost column means the source did not publish a price (it does not mean free).</caption>",
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
            f'<tr id="{esc(flag.get("id", ""))}">'
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
        "<caption>Published rows whose linked official page did not state a cost. The cost cell on these rows "
        "reads “Not stated”. Blank never means free — check the source link before assuming entry is free.</caption>",
        '<thead><tr><th scope="col">Event</th><th scope="col">Date</th><th scope="col">Source</th></tr></thead>',
        "<tbody>",
    ]
    for event in rows:
        output.append(
            "<tr>"
            f'<td data-label="Event"><strong>{esc(event["name"])}</strong>'
            f'<span class="organizer">{esc(event["organizer"])}</span></td>'
            f'<td data-label="Date">{esc(event.get("date_text", ""))}</td>'
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
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--mist);line-height:1.5}a{color:#075f99}a:hover{color:#064b78}.site-header{color:#fff;background:linear-gradient(120deg,#0d314a,#155d83 55%,#168178);padding:2.4rem 1.25rem 2rem}.shell{max-width:1240px;margin:0 auto;padding:0 1.25rem}.site-header .shell{padding:0;position:relative}.eyebrow{font-size:.77rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#b9e9e4;margin:0 0 .4rem}.site-header h1{margin:0;font-size:clamp(2rem,5vw,3.5rem);letter-spacing:-.045em}.lede{max-width:850px;margin:.7rem 0 0;font-size:1.06rem;color:#e7f4f5}.main{padding-top:1.2rem;padding-bottom:2rem}.nav{display:flex;gap:.55rem;flex-wrap:wrap;margin:0 0 1.5rem}.nav a{text-decoration:none;color:var(--navy);background:var(--paper);border:1px solid var(--line);border-radius:99px;padding:.48rem .77rem;font-weight:700;font-size:.9rem}.nav a.active,.nav a:hover{background:var(--navy);border-color:var(--navy);color:#fff}.hero{display:grid;gap:1rem;grid-template-columns:minmax(0,1.65fr) minmax(260px,.85fr);margin-bottom:1.25rem}.panel,.card{background:var(--paper);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow)}.panel{padding:1.35rem}.panel h2,.panel h3{margin-top:0}.panel p:last-child{margin-bottom:0}.snapshot{background:#eaf5f4;border-color:#bde0dc}.snapshot strong{display:block;font-size:2rem;color:var(--teal);letter-spacing:-.04em}.snapshot small{color:var(--muted)}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.85rem;margin:1rem 0 1.4rem}.card{padding:1rem;text-decoration:none;color:inherit;transition:transform .15s ease,box-shadow .15s ease}.card:hover{transform:translateY(-2px);box-shadow:0 12px 28px rgba(19,48,71,.14)}.metric{font-size:2rem;font-weight:800;letter-spacing:-.06em;color:var(--navy);display:block}.card-label{display:block;font-weight:750}.card-note{display:block;color:var(--muted);font-size:.85rem;margin-top:.25rem}.notice{padding:1rem 1.1rem;background:#fff7dc;border:1px solid #efd58c;border-radius:12px;margin:1rem 0}.notice strong{color:#715200}.notice a{font-weight:700}.section-head{display:flex;gap:1rem;align-items:baseline;justify-content:space-between;flex-wrap:wrap;margin-top:1.75rem}.section-head h2{margin:0}.section-head p{margin:0;color:var(--muted)}.filterbar{display:flex;gap:.65rem;align-items:center;flex-wrap:wrap;background:var(--paper);border:1px solid var(--line);padding:.8rem;border-radius:12px;margin:.85rem 0}.filterbar label{font-weight:700;font-size:.9rem}.filterbar input,.filterbar select{font:inherit;padding:.55rem .65rem;border:1px solid #aebdc9;border-radius:8px;background:#fff;min-height:2.6rem}.filterbar input{min-width:min(100%,320px);flex:1}.filterbar select{max-width:100%}.table-wrap{overflow:auto;border:1px solid var(--line);border-radius:14px;background:#fff}.table-wrap table{width:100%;min-width:940px;border-collapse:collapse;font-size:.88rem}.table-wrap caption{padding:.8rem 1rem;text-align:left;color:var(--muted);background:#f8fafb;border-bottom:1px solid var(--line);font-size:.82rem}.table-wrap th,.table-wrap td{padding:.72rem .72rem;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}.table-wrap th{font-size:.75rem;letter-spacing:.04em;text-transform:uppercase;color:#405262;background:#edf3f7;position:sticky;top:0;z-index:1}.table-wrap tr:last-child td{border-bottom:0}.table-wrap tbody tr:hover{background:#f7fbfd}.organizer,.source-meta,.authority{display:block;font-size:.78rem;color:var(--muted);margin-top:.16rem}.source-link{font-weight:800;white-space:nowrap}.authority{font-size:.72rem}.empty{color:#6d7a87}.rel{display:block;font-size:.76rem;font-weight:700;color:var(--teal);margin-top:.2rem}.badge{display:inline-block;border-radius:999px;padding:.22rem .5rem;font-size:.74rem;font-weight:800;line-height:1.2;margin-top:.3rem}.badge-recurring{color:#075b54;background:#dff5ef}.badge-special{color:#6e4700;background:#fff0c5}.badge-partial_sf_program{color:#634201;background:#fff0c5}.badge-needs_review{color:#80430a;background:#ffe8cf}.badge-cancelled{color:#892d2d;background:#ffe1e1}.badge-outside_city_excluded{color:#5d4a75;background:#eee8f8}.status-upcoming{color:#075b54;background:#dff5ef}.status-completed{color:#5c6672;background:#eceff2}.status-undated{color:#5d4a75;background:#eee8f8}.cost{display:inline-block;border-radius:6px;padding:.16rem .45rem;font-size:.8rem;font-weight:800}.cost-free{color:#075b54;background:#dff5ef}.cost-paid{color:#6e4700;background:#fff0c5}.cost-mixed{color:#2b4c7e;background:#e2ecfa}.cost-unknown{color:#5c6672;background:#eceff2}.cost-detail{display:block;font-size:.78rem;color:var(--muted);margin-top:.22rem}.review-table td:nth-child(5){min-width:280px}.category-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.85rem}.category-card{padding:1.05rem;background:#fff;border:1px solid var(--line);border-radius:14px;text-decoration:none;color:inherit}.category-card:hover{box-shadow:var(--shadow);border-color:#9fb9cb}.category-card .metric{font-size:1.6rem}.definition{margin:.4rem 0 0;color:var(--muted);font-size:.9rem}.analysis-list{padding-left:1.2rem}.analysis-list li{margin:.5rem 0}.site-footer{border-top:1px solid var(--line);background:#fff;padding:1.5rem 0 2rem;color:var(--muted);font-size:.88rem}.site-footer p{max-width:1000px;margin:.2rem 0}.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;padding:.6rem;background:#fff;color:#000;z-index:10}
.nextup{list-style:none;margin:0;padding:0}.nextup li{display:flex;gap:.85rem;align-items:flex-start;padding:.7rem 0;border-bottom:1px solid var(--line)}.nextup li:last-child{border-bottom:0}.nextup .when{flex:0 0 8.6rem;font-weight:800;color:var(--navy);font-size:.88rem}.nextup .when small{display:block;font-weight:700;color:var(--teal);font-size:.78rem}.nextup .what{flex:1}.nextup .what a{font-weight:750;text-decoration:none}.nextup .meta{display:block;font-size:.78rem;color:var(--muted);margin-top:.15rem}.today-strip{display:flex;gap:.6rem;flex-wrap:wrap;margin:.6rem 0 1rem}.today-pill{background:#eaf5f4;border:1px solid #bde0dc;border-radius:999px;padding:.4rem .8rem;font-size:.85rem;font-weight:700;color:var(--teal)}.legend{display:flex;gap:.6rem;flex-wrap:wrap;font-size:.82rem;color:var(--muted);margin:.4rem 0 0}.legend .cost{margin-right:.2rem}
.button{display:inline-block;background:var(--teal);color:#fff;text-decoration:none;font-weight:800;border-radius:999px;padding:.62rem 1rem;font-size:.92rem;border:1px solid var(--teal)}.button:hover{background:#0b5f59;color:#fff}.button-ghost{background:#fff;color:var(--navy);border-color:var(--line)}.button-ghost:hover{background:var(--navy);color:#fff;border-color:var(--navy)}.cta-row{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:.9rem}
.cost-restricted{color:#5d4a75;background:#eee8f8}
.panel-muted{background:#fbfbfd;border-color:#e2e6ec}
.today-pill.pill-strong{background:#0e766e;border-color:#0e766e;color:#fff}.today-pill.pill-muted{background:#f1f3f6;border-color:#d9e2ea;color:#526171}
.focus-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:.85rem;margin:.9rem 0 1.4rem}
.focus-card{padding:1.05rem;display:flex;flex-direction:column;gap:.45rem}
.focus-title{font-size:1.05rem;color:#0f172a;font-weight:800}
.focus-blurb{margin:0;font-size:.85rem;color:var(--muted)}
.focus-list{margin:.2rem 0 .1rem;border-top:1px solid var(--line)}
.focus-list li{padding:.6rem 0}
.focus-card .card-note{font-size:.83rem;line-height:1.45}
.split-head{margin:1.5rem 0 .4rem;padding:.85rem 1rem;background:#eaf5f4;border:1px solid #bde0dc;border-left:6px solid var(--teal);border-radius:12px}
.split-head h3{margin:0;font-size:1.05rem;color:#0b4f4a}
.split-head p{margin:.25rem 0 0;color:#2f5f5a;font-size:.9rem}
.split-head.split-paid{background:#fff7e6;border-color:#efd58c;border-left-color:#c98a00}
.split-head.split-paid h3{color:#715200}.split-head.split-paid p{color:#7a5c07}
.split-count{display:inline-block;margin-left:.4rem;font-size:.78rem;font-weight:800;background:#fff;border:1px solid var(--line);border-radius:999px;padding:.1rem .5rem;color:var(--muted);vertical-align:middle}
.empty-note{padding:.8rem 1rem;color:var(--muted);background:#fff;border:1px dashed var(--line);border-radius:12px}
@media(max-width:760px){.hero{grid-template-columns:1fr}.site-header{padding:1.5rem 1rem 1.4rem}.shell{padding:0 1rem}.main{padding-top:.9rem}.nav{gap:.4rem;margin-bottom:1rem}.nav a{font-size:.8rem;padding:.42rem .6rem}.section-head{margin-top:1.3rem}.panel{padding:1rem}.cards{grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.6rem}.metric{font-size:1.6rem}.nextup li{flex-direction:column;gap:.2rem}.nextup .when{flex:none}.filterbar{padding:.7rem}.filterbar input,.filterbar select{min-width:0;width:100%;flex:1 1 100%}.table-wrap{border-radius:12px}.table-wrap table{min-width:0;display:block}.table-wrap caption{font-size:.8rem}.table-wrap thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}.table-wrap tbody,.table-wrap tr,.table-wrap td{display:block;width:100%}.table-wrap tr{border-bottom:1px solid var(--line);padding:.55rem .8rem}.table-wrap tr:last-child{border-bottom:0}.table-wrap td{border:0;padding:.22rem 0;display:flex;gap:.6rem;align-items:flex-start}.table-wrap td::before{content:attr(data-label);font-weight:800;font-size:.7rem;letter-spacing:.05em;text-transform:uppercase;color:#5b6b7a;flex:0 0 6.6em}.table-wrap td[data-label="Event"]{display:block}.table-wrap td[data-label="Event"]::before{display:none}.table-wrap td[data-label="Source"]::before{flex-basis:4.6em}.site-footer{font-size:.85rem}.nav{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;margin:0 -.35rem 1rem;padding:.1rem .35rem .35rem}
.nav::-webkit-scrollbar{display:none;height:0}
.nav a{flex:0 0 auto;white-space:nowrap;padding:.5rem .7rem;min-height:2.4rem;display:inline-flex;align-items:center}
.focus-grid{grid-template-columns:1fr;gap:.7rem}
.focus-card{padding:.9rem}
.button{flex:1 1 45%;text-align:center;padding:.7rem .8rem}
.split-head{padding:.75rem .85rem;margin-top:1.15rem}
.split-head h3{font-size:1rem}
.table-wrap td::before{flex:0 0 6.2em}
.today-strip{gap:.4rem}.today-pill{font-size:.8rem;padding:.35rem .65rem}
.legend{font-size:.8rem}}
""".strip()


# --------------------------------------------------------------------------- #
# page shell
# --------------------------------------------------------------------------- #
def nav(active: str, prefix: str = "") -> str:
    return '<nav class="nav" aria-label="Primary">' + "".join(
        f'<a class="{"active" if href == active else ""}" href="{prefix}{href}">{label}</a>'
        for href, label in NAV_ITEMS
    ) + "</nav>"


SCRIPT = """
const DATA = (() => { try { return JSON.parse(document.getElementById('sf-events-data').textContent); } catch (e) { return []; } })();
const TODAY = new Date(); TODAY.setHours(0, 0, 0, 0);
const FREE = new Set(['free', 'mixed']);
const dayDiff = (iso) => { if (!iso) return null; const d = new Date(iso + 'T00:00:00'); return Math.round((d - TODAY) / 86400000); };
const fmtDay = (iso) => { if (!iso) return ''; const d = new Date(iso + 'T00:00:00');
  return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' }); };
const A = (url, text) => '<a href=' + JSON.stringify(url) + ' target=_blank rel=noopener noreferrer>' + text + '</a>';
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
// 1. Live relative labels everywhere (table rows and dashboard lists).
for (const rel of document.querySelectorAll('.rel[data-start], .rel[data-end]')) {
  const label = relative(rel.dataset.start, rel.dataset.end);
  if (label === 'past') { rel.textContent = 'Completed edition'; } else if (label) { rel.textContent = label; }
}
for (const row of document.querySelectorAll('tbody tr')) {
  const rel = row.querySelector('.rel');
  const badge = row.querySelector('.badge.status-upcoming, .badge.status-completed, .badge.status-undated');
  if (!badge || !rel) continue;
  const live = relative(rel.dataset.start, rel.dataset.end);
  const isPast = live === 'past';
  const isOngoing = live.indexOf('ongoing') === 0;
  badge.textContent = isPast ? 'Completed' : (isOngoing ? 'Ongoing now' : (live === '' ? badge.textContent : 'Upcoming'));
  badge.className = 'badge ' + (isPast ? 'status-completed' : (live === '' ? 'status-undated' : 'status-upcoming'));
}
// 2. Executive summary — free and upcoming first, paid kept in its own panel.
const costBadge = (r) => r.cost_class === 'free' ? '<span class="cost cost-free">Free</span>'
  : (r.cost_class === 'mixed' ? '<span class="cost cost-mixed">Free or partly free</span>'
  : (r.cost_class === 'paid' ? '<span class="cost cost-paid">Paid / ticketed</span>'
  : (r.cost_class === 'restricted' ? '<span class="cost cost-restricted">Registration only — no price published</span>'
  : '<span class="cost cost-unknown">Cost not stated</span>')));
const rowHtml = (r) => {
  const when = r.start ? fmtDay(r.start) : (r.end ? fmtDay(r.end) : '');
  const rel = relative(r.start, r.end);
  return '<li><span class="when">' + when + (rel ? '<small>' + rel + '</small>' : '') + '</span>'
    + '<span class="what">' + A(r.source_url, r.name)
    + '<span class="meta">' + r.category + ' · ' + r.bucket_label + ' · ' + r.location + '</span>'
    + '<span class="meta">' + costBadge(r) + '</span></span></li>';
};
const nextUp = document.getElementById('next-up');
if (nextUp && DATA.length) {
  const endOf = (r) => r.end || r.start;
  const upcoming = DATA.filter((r) => { const e = endOf(r); return e && dayDiff(e) >= 0; });
  const startsSoon = upcoming.filter((r) => { const s = dayDiff(r.start); return s === null || s >= 0; })
    .sort((a, b) => (a.start || '9999').localeCompare(b.start || '9999'));
  const ongoing = upcoming.filter((r) => { const s = dayDiff(r.start); return s !== null && s < 0; })
    .sort((a, b) => (a.end || '').localeCompare(b.end || ''));
  const freeSoon = startsSoon.filter((r) => FREE.has(r.cost_class));
  const freeOngoing = ongoing.filter((r) => FREE.has(r.cost_class));
  const paidSoon = startsSoon.filter((r) => !FREE.has(r.cost_class));
  const paidOngoing = ongoing.filter((r) => !FREE.has(r.cost_class));
  const horizons = [7, 30, 90].map((h) => freeSoon.filter((r) => {
    const s = dayDiff(r.start); return s !== null && s >= 0 && s <= h;
  }).length);
  const strip = document.getElementById('today-strip');
  if (strip) {
    strip.innerHTML = '<span class="today-pill pill-strong">Today: ' + TODAY.toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }) + '</span>'
      + '<span class="today-pill">Free starting in 7 days: ' + horizons[0] + '</span>'
      + '<span class="today-pill">Free starting in 30 days: ' + horizons[1] + '</span>'
      + '<span class="today-pill">Free starting in 90 days: ' + horizons[2] + '</span>'
      + '<span class="today-pill">Free running now: ' + freeOngoing.length + '</span>'
      + '<span class="today-pill pill-muted">Upcoming paid or no price published: ' + paidSoon.length + '</span>';
  }
  const freeNext = freeSoon.slice(0, 10).concat(freeOngoing.slice(0, 3));
  nextUp.innerHTML = freeNext.length ? freeNext.map(rowHtml).join('')
    : '<li><span class="what">No free events are currently listed as upcoming on this snapshot. '
      + 'Rows whose source published no price are never counted as free.</span></li>';
  const freeList = document.getElementById('free-upcoming');
  if (freeList) {
    const freeWindow = freeSoon.filter((r) => { const s = dayDiff(r.start); return s !== null && s <= 120; }).slice(0, 12);
    freeList.innerHTML = freeWindow.length ? freeWindow.map(rowHtml).join('')
      : '<li><span class="what">No free events start in the next 120 days on this snapshot.</span></li>';
  }
  const paidList = document.getElementById('paid-next-up');
  if (paidList) {
    const paidNext = paidSoon.slice(0, 6).concat(paidOngoing.slice(0, 2));
    paidList.innerHTML = paidNext.length ? paidNext.map(rowHtml).join('')
      : '<li><span class="what">No paid or unpriced events are currently listed as upcoming.</span></li>';
  }
}
// 3. Search / focus / category / cost / when filters and sorting.
for (const table of document.querySelectorAll('[data-filter-table]')) {
  const input = document.querySelector('#' + table.dataset.searchControl);
  const select = document.querySelector('#' + table.dataset.categoryControl);
  const cost = document.querySelector('#' + (table.dataset.costControl || 'missing-cost-control'));
  const when = document.querySelector('#' + (table.dataset.whenControl || 'missing-when-control'));
  const focus = document.querySelector('#' + (table.dataset.focusControl || 'missing-focus-control'));
  const sorter = document.querySelector('#' + (table.dataset.sortControl || 'missing-sort-control'));
  const apply = () => {
    const term = (input?.value || '').toLowerCase();
    const category = select?.value || '';
    const costFilter = cost?.value || '';
    const whenFilter = when?.value || '';
    const focusFilter = focus?.value || '';
    for (const row of table.tBodies[0].rows) {
      const matchText = !term || row.textContent.toLowerCase().includes(term);
      const matchCategory = !category || row.dataset.category === category;
      const matchCost = !costFilter || row.dataset.cost === costFilter;
      const matchWhen = !whenFilter || row.dataset.status === whenFilter;
      const matchFocus = !focusFilter || row.dataset.focus === focusFilter;
      row.hidden = !(matchText && matchCategory && matchCost && matchWhen && matchFocus);
    }
  };
  input?.addEventListener('input', apply); select?.addEventListener('change', apply);
  cost?.addEventListener('change', apply); when?.addEventListener('change', apply);
  focus?.addEventListener('change', apply);
  if (sorter) {
    const tbody = table.tBodies[0];
    const key = (row) => {
      const mode = sorter.value;
      if (mode === 'name') return row.dataset.name || '';
      if (mode === 'category') return row.dataset.category || '';
      if (mode === 'cost') return row.dataset.costrank + '|' + (row.dataset.daterank || '') + '|' + (row.dataset.name || '');
      if (mode === 'focus') return row.dataset.focusrank + '|' + (row.dataset.daterank || '') + '|' + (row.dataset.name || '');
      return row.dataset.daterank + '|' + (row.dataset.name || '');
    };
    sorter.addEventListener('change', () => {
      const rows = Array.from(tbody.rows);
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
  <p class="lede">City and County of San Francisco only. Lists are ordered by date with upcoming events first, every row shows what it costs to attend, and every row links to the official source used for verification.</p>
</div></header>
<main id="content" class="shell main">
{nav(active, prefix)}
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
                    with_when: bool = True, with_sort: bool = True,
                    with_focus: bool = False, default_sort: str = "date") -> str:
    options = "".join(f'<option value="{esc(category)}">{esc(category)}</option>' for category in categories)
    cost_options = "".join(
        f'<option value="{value}">{label}</option>'
        for value, label in (
            ("free", "Free"),
            ("mixed", "Free or partly free"),
            ("paid", "Paid / ticketed"),
            ("restricted", "Registration only — no price published"),
            ("not-stated", "Cost not stated"),
        )
    )
    when_options = "".join(
        f'<option value="{value}">{label}</option>'
        for value, label in (
            ("upcoming", "Upcoming only"),
            ("completed", "Completed only"),
            ("undated", "Repeating programs (no single date)"),
        )
    )
    focus_options = "".join(
        f'<option value="{value}">{label}</option>' for value, label in FOCUS_AREAS
    )
    sort_options = "".join(
        f'<option value="{value}"{" selected" if value == default_sort else ""}>{label}</option>'
        for value, label in (
            ("date", "Date — upcoming first"),
            ("focus", "Focus — gaming, music, AI first"),
            ("name", "Name A–Z"),
            ("category", "Category"),
            ("cost", "Cost — free first"),
        )
    )
    parts = [
        '<div class="filterbar" aria-label="Filter events">',
        f'<label for="search-{key}">Search</label>',
        f'<input id="search-{key}" type="search" placeholder="Event, organizer, place, or category">',
    ]
    if with_focus:
        parts.append(f'<label for="focus-{key}">Focus</label>')
        parts.append(f'<select id="focus-{key}"><option value="">All focus areas</option>{focus_options}</select>')
    parts.extend([
        f'<label for="category-{key}">Category</label>',
        f'<select id="category-{key}"><option value="">All categories</option>{options}</select>',
    ])
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
                      with_when: bool = True, with_sort: bool = True,
                      with_focus: bool = False) -> str:
    attributes = f'<table data-filter-table data-search-control="search-{key}" data-category-control="category-{key}"'
    if with_cost:
        attributes += f' data-cost-control="cost-{key}"'
    if with_when:
        attributes += f' data-when-control="when-{key}"'
    if with_focus:
        attributes += f' data-focus-control="focus-{key}"'
    if with_sort:
        attributes += f' data-sort-control="sort-{key}"'
    attributes += ">"
    return markup.replace("<table>", attributes, 1)


COST_RANK = {"free": "0", "mixed": "1", "paid": "2", "restricted": "3", "not-stated": "4"}


def table_with_filter_rows(events: list[dict], *, key: str, as_of: date,
                           include_bucket: bool = False, with_cost: bool = True,
                           with_when: bool = True, with_sort: bool = True,
                           with_focus: bool = False, default_sort: str = "date") -> str:
    markup = event_table(events, as_of=as_of, include_bucket=include_bucket)
    for event in events:
        kind = cost_class(event.get("admission", ""))
        needle = f'<tr><td data-label="Event"><strong>{esc(event["name"])}</strong>'
        replacement = (
            f'<tr data-category="{esc(event["category"])}"'
            f' data-name="{esc(event["name"].lower())}"'
            f' data-cost="{kind}"'
            f' data-costrank="{COST_RANK[kind]}"'
            f' data-focus="{focus_area(event)}"'
            f' data-focusrank="{FOCUS_RANK[focus_area(event)]}"'
            f' data-status="{event_status(event, as_of)}"'
            f' data-daterank="{sort_key(event, as_of)[0]}-{event.get("start_date") or event.get("end_date") or "9999-99-99"}">'
            f'<td data-label="Event"><strong>{esc(event["name"])}</strong>'
        )
        markup = markup.replace(needle, replacement, 1)
    return mark_filter_table(
        markup, key=key, with_cost=with_cost, with_when=with_when, with_sort=with_sort,
        with_focus=with_focus,
    )


def split_by_cost(events: list[dict], *, key: str, as_of: date,
                  include_bucket: bool = False, with_focus: bool = False,
                  default_sort: str = "date", free_caption: str = "",
                  nonfree_caption: str = "") -> str:
    """Render the free-first split the brief asks for: the free rows lead, and the
    paid / registration-only / no-price-published rows follow in their own table."""
    free_events = [event for event in events if is_free(event)]
    nonfree_events = [event for event in events if not is_free(event)]
    blocks = [
        f'<div class="split-head"><h3>Free to attend <span class="split-count">{len(free_events)} rows</span></h3>'
        f'<p>{free_caption or "The official source states these events are free, or free for part of the programme."}</p></div>',
    ]
    if free_events:
        blocks.append(filter_controls(
            sorted({event["category"] for event in free_events}), key=f"{key}-free",
            with_focus=with_focus, default_sort=default_sort,
        ))
        blocks.append(table_with_filter_rows(
            free_events, key=f"{key}-free", as_of=as_of, include_bucket=include_bucket,
            with_focus=with_focus, default_sort=default_sort,
        ))
    else:
        blocks.append('<p class="empty-note">No rows in this view have a source-stated free admission.</p>')
    blocks.append(
        f'<div class="split-head split-paid"><h3>Paid, registration-only, or cost not published '
        f'<span class="split-count">{len(nonfree_events)} rows</span></h3>'
        f'<p>{nonfree_caption or "Kept separate from the free list. A blank cost is never treated as free; every one of these rows is also listed on the Flagged for Review page."}</p></div>'
    )
    if nonfree_events:
        blocks.append(filter_controls(
            sorted({event["category"] for event in nonfree_events}), key=f"{key}-paid",
            with_focus=with_focus, default_sort=default_sort,
        ))
        blocks.append(table_with_filter_rows(
            nonfree_events, key=f"{key}-paid", as_of=as_of, include_bucket=include_bucket,
            with_focus=with_focus, default_sort=default_sort,
        ))
    else:
        blocks.append('<p class="empty-note">No paid or unpriced rows in this view.</p>')
    return "\n".join(blocks)


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
            "focus": focus_area(event),
            "focus_label": FOCUS_LABELS[focus_area(event)],
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
        "time_text", "location", "organizer", "admission", "cost_class", "source_label", "source_url",
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
def focus_card(key: str, label: str, free_events: list[dict], nonfree_events: list[dict],
               *, as_of: date, gap_flag: str = "", blurb: str = "") -> str:
    """Build one focus card from verified rows only — no hand-written event claims."""
    free_sorted = sorted(free_events, key=lambda event: sort_key(event, as_of))
    free_upcoming = [event for event in free_sorted if event_status(event, as_of) == "upcoming"]
    shown = (free_upcoming or free_sorted)[:4]
    if shown:
        items = "".join(
            f'<li><span class="when">{esc(event.get("date_text", "") or "Date not published")}'
            f'<span class="rel" data-start="{esc(event.get("start_date", ""))}" '
            f'data-end="{esc(event.get("end_date", ""))}"></span></span>'
            f'<span class="what"><a href="{esc(event["source_url"])}" target="_blank" rel="noopener noreferrer">'
            f'{esc(event["name"])}</a>'
            f'<span class="meta">{esc(event.get("category", ""))} · {esc(event.get("location", ""))}</span>'
            f'<span class="meta">{cost_cell(event)}</span></span></li>'
            for event in shown
        )
    else:
        # Show the nearest non-free rows so the card is still useful, labelled honestly.
        items = "".join(
            f'<li class="not-free"><span class="when">{esc(event.get("date_text", "") or "Date not published")}'
            f'<span class="rel" data-start="{esc(event.get("start_date", ""))}" '
            f'data-end="{esc(event.get("end_date", ""))}"></span></span>'
            f'<span class="what"><a href="{esc(event["source_url"])}" target="_blank" rel="noopener noreferrer">'
            f'{esc(event["name"])}</a>'
            f'<span class="meta">Not free — {esc(event.get("category", ""))} · {esc(event.get("location", ""))}</span>'
            f'<span class="meta">{cost_cell(event)}</span></span></li>'
            for event in sorted(nonfree_events, key=lambda event: sort_key(event, as_of))[:3]
        ) or '<li><span class="what">No verified rows in this focus area at all.</span></li>'
    anchor = f'flagged.html#{gap_flag}' if gap_flag else "flagged.html"
    if free_upcoming:
        status_line = (
            f'<span class="card-note"><strong>{len(free_upcoming)}</strong> free and upcoming · '
            f'<strong>{len(free_events)}</strong> free rows in total</span>'
        )
    elif free_events:
        status_line = (
            f'<span class="card-note"><strong>0</strong> upcoming free rows verified as of {esc(str(as_of))} — '
            f'the {len(free_events)} free row(s) below are completed editions. The gap is recorded on '
            f'<a href="{anchor}">Flagged for Review</a>.</span>'
        )
    else:
        status_line = (
            f'<span class="card-note"><strong>0</strong> free rows verified in this focus area as of '
            f'{esc(str(as_of))} — every verified row here is paid, registration-only, or publishes no price, so '
            f'none of them may be counted as free. The gap is recorded on '
            f'<a href="{anchor}">Flagged for Review</a>.</span>'
        )
    paid_line = (
        f'<span class="card-note">{len(nonfree_events)} rows in this focus area are paid, registration-only, '
        f'or have no published price — they are kept in the separate '
        f'<a href="paid.html">Paid &amp; ticketed</a> section.</span>'
        if nonfree_events else
        '<span class="card-note">Every verified row in this focus area is free.</span>'
    )
    blurb_html = f'<p class="focus-blurb">{blurb}</p>' if blurb else ""
    return f"""
<article class="card focus-card" id="focus-{esc(key)}" aria-labelledby="focus-{esc(key)}-title">
  <span class="card-label focus-title" id="focus-{esc(key)}-title">{esc(label)}</span>
  {blurb_html}
  {status_line}
  <ul class="nextup focus-list">{items}</ul>
  {paid_line}
  <span class="card-note"><a href="free.html">Open the free list →</a></span>
</article>"""


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

    # --- the free-first split the brief asks for ------------------------------ #
    free_rows = [event for event in published if is_free(event)]
    nonfree_rows = [event for event in published if not is_free(event)]
    free_upcoming = [event for event in free_rows if event_status(event, as_of) == "upcoming"]
    nonfree_upcoming = [event for event in nonfree_rows if event_status(event, as_of) == "upcoming"]
    priced_rows = [event for event in nonfree_rows if cost_class(event.get("admission", "")) in {"paid", "restricted"}]
    unstated_rows = [event for event in nonfree_rows if cost_class(event.get("admission", "")) == "not-stated"]
    free_rows_focus = sorted(free_rows, key=lambda event: sort_focus(event, as_of))
    fallback_free_next_up = sorted(
        free_upcoming, key=lambda event: (event.get("start_date") or "9999-99-99", event.get("name", "").lower()),
    )[:10] + sorted(
        [event for event in free_upcoming if event.get("start_date") and event["start_date"] < catalog["as_of"]],
        key=lambda event: (event.get("end_date") or "9999-99-99", event.get("name", "").lower()),
    )[:3]
    fallback_paid_next_up = sorted(
        nonfree_upcoming, key=lambda event: (event.get("start_date") or "9999-99-99", event.get("name", "").lower()),
    )[:6]

    def focus_split(key: str) -> tuple[list[dict], list[dict]]:
        area = [event for event in published if focus_area(event) == key]
        return [event for event in area if is_free(event)], [event for event in area if not is_free(event)]

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
        f"<strong>{cost_counts[kind]} {COST_SHORT_LABELS[kind].lower()}</strong>"
        for kind in ("free", "mixed", "paid", "restricted", "not-stated") if cost_counts.get(kind)
    )

    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "style.css").write_text(STYLE + "\n", encoding="utf-8")
    (ROOT / "categories").mkdir(exist_ok=True)

    data_block = embed_data(published)

    def nextup_fallback(rows: list[dict]) -> str:
        return "".join(
            f'<li><span class="when">{esc(event.get("date_text", "") or "Date not published")}</span><span class="what">'
            f'<a href="{esc(event["source_url"])}" target="_blank" rel="noopener noreferrer">{esc(event["name"])}</a>'
            f'<span class="meta">{esc(event["category"])} · {esc(event.get("location", ""))}</span>'
            f'<span class="meta">{cost_cell(event)}</span></span></li>'
            for event in rows
        )

    category_cards = "".join(
        f'<a class="card" href="categories/{slugify(category)}.html">'
        f'<span class="metric">{category_counts[category]}</span>'
        f'<span class="card-label">{esc(category)}</span>'
        f'<span class="card-note">Free first, then paid →</span></a>'
        for category in categories
    )

    gaming_free, gaming_nonfree = focus_split("gaming")
    music_free, music_nonfree = focus_split("music")
    ai_free, ai_nonfree = focus_split("ai")
    other_free, other_nonfree = focus_split("other")

    focus_cards = "".join((
        focus_card(
            "gaming", "🎮 Gaming — free first", gaming_free, gaming_nonfree, as_of=as_of,
            gap_flag="flag-free-gaming-coverage-gap",
            blurb="Rows in the Technology, AI &amp; gaming category whose own name identifies a game, gaming, "
                  "arcade or developer event.",
        ),
        focus_card(
            "music", "🎵 Music & performing arts — free first", music_free, music_nonfree, as_of=as_of,
            blurb="Every row in the verified Music &amp; performing arts category, free rows first.",
        ),
        focus_card(
            "ai", "🤖 AI & technology — free first", ai_free, ai_nonfree, as_of=as_of,
            gap_flag="flag-free-ai-coverage-gap",
            blurb="Remaining rows in the Technology, AI &amp; gaming category: AI, developer and industry events. "
                  "The nearest ones are shown labelled with their real cost because no AI row in this audit has a "
                  "source-stated free admission.",
        ),
        focus_card(
            "other", "🌟 Everything else — after the focus areas", other_free, other_nonfree, as_of=as_of,
            blurb="Community celebrations, markets, fairs, film, sport and civic programs, free rows first.",
        ),
    ))

    home = f"""
<section class="hero">
  <div class="panel">
    <p class="eyebrow">Free events first · official sources only · {esc(catalog['as_of'])} snapshot</p>
    <h2>San Francisco free events, by date</h2>
    <p>The main list holds <strong>only free upcoming events</strong> inside the City and County of San Francisco,
    ordered by date with the nearest first and the requested focus areas — <strong>gaming, music, AI</strong> —
    ahead of everything else. Paid, ticketed and unpriced events are collected and organised too, but they live in a
    clearly separate <a href="paid.html">Paid &amp; ticketed</a> section. Regularly occurring events are kept apart
    from dated special events, every row shows what it costs, and every row links to the official source used to
    verify it.</p>
    <p class="cta-row"><a class="button" href="free.html">Free events — main list</a>
       <a class="button button-ghost" href="paid.html">Paid &amp; ticketed</a>
       <a class="button button-ghost" href="upcoming.html">Everything by date</a></p>
  </div>
  <aside class="panel snapshot"><strong>{len(free_upcoming)}</strong><span>free events still upcoming</span><br>
  <small>{len(free_rows)} free rows of {len(published)} published; {len(nonfree_upcoming)} upcoming rows are paid,
  registration-only or have no published price; {len(review)} items held for review.</small></aside>
</section>

<section aria-labelledby="next-up">
  <div class="section-head"><h2 id="next-up">Executive summary — free and upcoming</h2>
  <p>The free events closest to today's date, recalculated in your browser from the same source-verified data.
  Paid and unpriced events are summarised separately below.</p></div>
  <div class="today-strip" id="today-strip"><span class="today-pill">Loading today’s dates…</span></div>
  <div class="panel"><ul class="nextup" id="next-up"><li><span class="what">Loading…</span></li></ul></div>
  <noscript><div class="panel"><p><strong>Free and upcoming as of the {esc(catalog['as_of'])} audit date:</strong></p>
    <ul class="nextup">{nextup_fallback(fallback_free_next_up)}</ul></div></noscript>
</section>

<section aria-labelledby="free-upcoming">
  <div class="section-head"><h2 id="free-upcoming">Free — starting soon</h2>
  <p>Free events that begin in the next 120 days, nearest first. Full list:
  <a href="free.html">Free events (main)</a>.</p></div>
  <div class="panel"><ul class="nextup" id="free-upcoming"><li><span class="what">Loading…</span></li></ul></div>
  <noscript><div class="panel"><ul class="nextup">{nextup_fallback(
      sorted([event for event in free_upcoming if event.get("start_date") and event["start_date"] >= catalog["as_of"]],
             key=lambda event: (event["start_date"], event.get("name", "").lower()))[:12]
  )}</ul></div></noscript>
</section>

<section aria-labelledby="paid-next-up">
  <div class="section-head"><h2 id="paid-next-up">Separate section — paid, registration-only, or no price published</h2>
  <p>Collected and organised, kept out of the free list. Full list:
  <a href="paid.html">Paid &amp; ticketed</a>.</p></div>
  <div class="panel panel-muted"><ul class="nextup" id="paid-next-up"><li><span class="what">Loading…</span></li></ul></div>
  <noscript><div class="panel panel-muted"><ul class="nextup">{nextup_fallback(fallback_paid_next_up)}</ul></div></noscript>
</section>

<section aria-labelledby="focus-disciplines">
  <div class="section-head"><h2 id="focus-disciplines">Focus: free gaming, music and AI first, everything else after</h2>
  <p>Generated from the verified dataset — each card lists free rows first, with the official source link and the
  sourced cost on every line.</p></div>
  <div class="focus-grid">{focus_cards}</div>
</section>

<section aria-labelledby="at-a-glance">
  <div class="section-head"><h2 id="at-a-glance">At a glance</h2><p>Counts are derived directly from the verified dataset.</p></div>
  <div class="cards">
    <a class="card" href="free.html"><span class="metric">{len(free_rows)}</span><span class="card-label">Free to attend</span><span class="card-note">Main list — source states free or partly free</span></a>
    <a class="card" href="free.html"><span class="metric">{len(free_upcoming)}</span><span class="card-label">Free and upcoming</span><span class="card-note">Nearest dates first</span></a>
    <a class="card" href="paid.html"><span class="metric">{len(nonfree_rows)}</span><span class="card-label">Paid, registration-only or unpriced</span><span class="card-note">Separate section</span></a>
    <a class="card" href="all-events.html"><span class="metric">{len(published)}</span><span class="card-label">Published rows</span><span class="card-note">City-only, source-linked</span></a>
    <a class="card" href="recurring.html"><span class="metric">{len(recurring)}</span><span class="card-label">Regularly occurring</span><span class="card-note">Weekly, monthly, seasonal, annual</span></a>
    <a class="card" href="special.html"><span class="metric">{len(special)}</span><span class="card-label">Special events</span><span class="card-note">Dated programs and one-offs</span></a>
    <a class="card" href="categories.html"><span class="metric">{len(categories)}</span><span class="card-label">Categories</span><span class="card-note">Each has its own page</span></a>
    <a class="card" href="flagged.html"><span class="metric">{len(review)}</span><span class="card-label">Flagged for review</span><span class="card-note">Never mixed into city-only results</span></a>
  </div>
</section>

<section aria-labelledby="category-summary">
  <div class="section-head"><h2 id="category-summary">Browse by category</h2><p>Each card opens a source-linked category table, free rows first.</p></div>
  <div class="cards">{category_cards}</div>
</section>

<section class="panel" aria-labelledby="findings">
  <h2 id="findings">What this catalog supports</h2>
  <ul class="analysis-list">
    <li><strong>{len(free_rows)}</strong> of the <strong>{len(published)}</strong> published rows have a
        source-stated free or partly free admission; <strong>{len(free_upcoming)}</strong> of those are still
        upcoming as of {esc(catalog['as_of'])}. The remaining <strong>{len(nonfree_rows)}</strong> rows are paid,
        registration-only, or have no published price, and they are kept in the separate
        <a href="paid.html">Paid &amp; ticketed</a> section.</li>
    <li>Cost labelling: {cost_summary}. “Not stated” means the linked official page published no price —
        it never means free. Every such row is listed with its source link on
        <a href="flagged.html">Flagged for Review</a>.</li>
    <li><strong>{len(upcoming)}</strong> of the {len(published)} published rows are still upcoming as of
        {esc(catalog['as_of'])}; completed editions are kept because the brief asks for the full list, and they are
        pushed to the bottom of every list and badged <em>Completed</em>.</li>
    <li>{cadence_summary} entries make up the regularly occurring list; it is not limited to weekly events.</li>
    <li>{top_categories} are the largest documented categories in this audit snapshot (computed from the dataset, listed largest first).</li>
    <li>The published rows link to {authority_summary} sources. This is an audit of stated sources, not an assertion
        that it finds every event in the city.</li>
  </ul>
</section>

<section class="panel" aria-labelledby="cost-legend">
  <h2 id="cost-legend">How cost is labelled</h2>
  <div class="legend">
    <span class="cost cost-free">Free</span> the source states no charge
    <span class="cost cost-mixed">Free or partly free</span> some programmes free, others ticketed
    <span class="cost cost-paid">Paid / ticketed</span> the source states a price, pass or ticket
    <span class="cost cost-restricted">Registration only</span> the source names registration or an invitation but publishes no price
    <span class="cost cost-unknown">Not stated</span> the source published no price — <strong>never</strong> treated as free
  </div>
</section>

<section class="notice"><strong>Planning note.</strong> Dates and operational details change. Use the source link in the row as
the final check before attending. An em dash means the linked source did not state that optional field in the captured audit;
essential gaps go to <a href="flagged.html">Flagged for Review</a>.</section>
"""
    (ROOT / "index.html").write_text(
        page("Dashboard", home, "index.html", catalog, data_block=data_block), encoding="utf-8"
    )

    # --- free.html: the main section ----------------------------------------- #
    free_body = f"""
<section class="section-head"><div><h2>Free events — the main list</h2>
<p>Only rows whose linked official source states the event is free, or free for part of the programme. Ordered with
the requested focus areas first — gaming, then music, then AI and technology, then everything else — and within each
focus area the nearest upcoming date leads and completed editions sit at the bottom. Rows whose source published no
price are <strong>not</strong> listed here: a blank cost is never treated as free, and those rows are published on
<a href="flagged.html">Flagged for Review</a>. Paid and ticketed events are collected in the separate
<a href="paid.html">Paid &amp; ticketed</a> section.</p></div>
<p>{len(free_rows)} free rows · {len(free_upcoming)} upcoming</p></section>
{filter_controls(categories, key='free', with_focus=True, default_sort='focus')}
{table_with_filter_rows(free_rows_focus, key='free', as_of=as_of, include_bucket=True,
                        with_focus=True, default_sort='focus')}
<section class="notice"><strong>Focus ordering.</strong> The Focus control filters this list by gaming, music,
AI &amp; technology, or everything else; the Sort control can switch back to plain date order, name, category or
cost. Focus areas are derived from each row's verified category and name, not from hand-written prose.</section>
"""
    (ROOT / "free.html").write_text(
        page("Free events (main list)", free_body, "free.html", catalog, data_block=data_block), encoding="utf-8"
    )

    # --- paid.html: the separate section ------------------------------------- #
    paid_body = f"""
<section class="section-head"><div><h2>Paid &amp; ticketed — separate section</h2>
<p>These San Francisco rows are collected and organised, but the brief keeps them out of the free-events main list.
Two groups appear below, both ordered with upcoming dates first: rows whose official source states a price, pass or
ticket (including rows that name registration or an invitation without publishing a price), and rows whose official
page published no cost at all. Nothing here is inferred — where the source is silent, the cost reads
“Not stated” and the row is also listed on <a href="flagged.html">Flagged for Review</a>.</p></div>
<p>{len(nonfree_rows)} rows · {len(nonfree_upcoming)} upcoming</p></section>

<div class="split-head split-paid"><h3>Priced, ticketed, or registration-only
<span class="split-count">{len(priced_rows)} rows</span></h3>
<p>The linked official source states a price, a pass, a ticket, or that registration or an invitation is required.</p></div>
{filter_controls(categories, key='priced')}
{table_with_filter_rows(sorted(priced_rows, key=lambda event: sort_key(event, as_of)), key='priced',
                        as_of=as_of, include_bucket=True)}

<div class="split-head split-paid"><h3>Cost not stated in the linked source
<span class="split-count">{len(unstated_rows)} rows</span></h3>
<p>The official page published no price. These rows are never treated as free and never promoted into the main
list; each one is listed with its source link so the cost can be checked by hand.</p></div>
{filter_controls(categories, key='unstated', with_cost=False)}
{table_with_filter_rows(sorted(unstated_rows, key=lambda event: sort_key(event, as_of)), key='unstated',
                        as_of=as_of, include_bucket=True, with_cost=False)}
<section class="notice"><strong>Looking for free events?</strong> The main list is
<a href="free.html">Free events</a>; the whole catalog ordered by date is
<a href="upcoming.html">Upcoming by date</a>.</section>
"""
    (ROOT / "paid.html").write_text(
        page("Paid & ticketed (separate section)", paid_body, "paid.html", catalog, data_block=data_block),
        encoding="utf-8",
    )

    # --- upcoming: everything, ordered by date with upcoming first ------------ #
    upcoming_body = f"""
<section class="section-head"><div><h2>All events by date</h2>
<p>Every published city-only row in one date-ordered list, with upcoming dates first and the nearest date at the top.
Rows that are already past are pushed to the bottom and labelled <em>Completed</em>. The Cost column shows what each
row costs; use the Cost control to isolate free rows, or open the dedicated
<a href="free.html">free events</a> and <a href="paid.html">paid &amp; ticketed</a> sections.</p></div>
<p>{len(all_events)} verified rows · {len(upcoming)} upcoming</p></section>
{filter_controls(categories, key='upcoming', with_focus=True)}
{table_with_filter_rows(all_events, key='upcoming', as_of=as_of, include_bucket=True, with_focus=True)}
"""
    (ROOT / "upcoming.html").write_text(
        page("Upcoming by date", upcoming_body, "upcoming.html", catalog, data_block=data_block),
        encoding="utf-8",
    )

    # --- recurring / special: regularly occurring vs dated special events ----- #
    recurring_body = f"""
<section class="section-head"><div><h2>Regularly occurring events</h2>
<p>Weekly, monthly, seasonal, and annual programs with a recurring cadence stated by the source. Free rows lead, and
paid, registration-only and unpriced rows follow in their own table, each ordered with upcoming dates first.</p></div>
<p>{len(recurring)} verified rows · {sum(1 for event in recurring if is_free(event))} free</p></section>
{split_by_cost(recurring, key='recurring', as_of=as_of)}
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
<p>Dated programs, single-event conferences, and one-off calendar listings. No recurrence is inferred. Free rows lead,
and paid, registration-only and unpriced rows follow in their own table, each ordered with upcoming dates first.</p></div>
<p>{len(special)} verified rows · {sum(1 for event in special if is_free(event))} free</p></section>
{split_by_cost(special, key='special', as_of=as_of)}
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
<p>Search across the {len(all_events)} records, narrow by focus area, category, cost or date status, and sort by date,
focus, name, category or cost. Every row has a source link. The free-only main list is
<a href="free.html">Free events</a>; the separate paid section is <a href="paid.html">Paid &amp; ticketed</a>.</p></div>
<p>{len(all_events)} verified rows</p></section>
{filter_controls(categories, key='all', with_focus=True)}
{table_with_filter_rows(all_events, key='all', as_of=as_of, include_bucket=True, with_focus=True)}
"""
    (ROOT / "all-events.html").write_text(
        page("All published events", all_body, "all-events.html", catalog, data_block=data_block),
        encoding="utf-8",
    )

    categories_body = "".join(
        f'<a class="category-card" href="categories/{slugify(category)}.html">'
        f'<span class="metric">{category_counts[category]}</span><strong>{esc(category)}</strong>'
        f'<p class="definition">{sum(1 for event in published if event["category"] == category and is_free(event))} '
        f'free rows · {sum(1 for event in published if event["category"] == category and not is_free(event))} '
        f'paid, registration-only or unpriced · free first, upcoming first.</p></a>'
        for category in categories
    )
    (ROOT / "categories.html").write_text(
        page(
            "Categories",
            f'<section class="section-head"><div><h2>Category pages</h2>'
            f'<p>Open a category to review its source-linked city-only event rows: free rows first, then the paid, '
            f'registration-only and unpriced rows, each ordered with upcoming dates first.</p>'
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
        free_in_category = sum(1 for event in category_events if is_free(event))
        category_body = f"""
<section class="section-head"><div><p><a href="../categories.html">← All categories</a></p><h2>{esc(category)}</h2>
<p>{len(category_events)} verified city-only event rows, each with its own source link: {free_in_category} free,
{len(category_events) - free_in_category} paid, registration-only or unpriced.</p></div></section>
{split_by_cost(category_events, key='cat-' + slugify(category), as_of=as_of, include_bucket=True)}
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
<p>Corrections applied to published rows, source-availability problems, coverage gaps, and residual discrepancies
that merit manual review. Each finding links the sources used and can be linked to directly by its id.</p></div><p>{len(flags)} findings</p></section>
{flags_table(flags)}
<section class="section-head"><div><h2>Cost not stated in the linked source</h2>
<p>The brief asks that every row state what it costs to attend. Where the official page published no price, the cost
cell reads “Not stated” rather than being filled with an assumption. Every such row is listed here with its source
link so it can be checked by hand. Blank never means free. These rows also appear in the separate
<a href="paid.html">Paid &amp; ticketed</a> section, never in the free main list.</p></div>
<p>{len(unstated_rows)} rows</p></section>
{cost_not_stated_table(published)}
"""
    (ROOT / "flagged.html").write_text(
        page("Flagged for Review", flagged_body, "flagged.html", catalog), encoding="utf-8"
    )

    method_body = f"""
<section class="section-head"><div><h2>Method, sources, and findings</h2>
<p>A reproducible snapshot of publicly advertised San Francisco city events, organised free-first.</p></div></section>
<section class="panel"><h3>How the site is organised</h3><ol>
<li><strong>Free events are the main section.</strong> <a href="free.html">Free events (main)</a> contains only rows
whose linked official source states the event is free or free for part of the programme.</li>
<li><strong>Paid events are a separate section.</strong> <a href="paid.html">Paid &amp; ticketed</a> collects and
organises the priced, ticketed, registration-only and unpriced rows so they never mix into the free list.</li>
<li><strong>Focus areas come first.</strong> Inside the free list the order is gaming, then music and performing arts,
then AI and technology, then everything else — the ordering the brief asks for. Focus areas are derived from each
row's verified category and its own name, never from hand-written prose, and the Focus control filters any list by
them.</li>
<li><strong>Regular patterns are separated from dated specials.</strong> <a href="recurring.html">Regularly
occurring</a> holds weekly, monthly, seasonal and annual programs; <a href="special.html">Special events</a> holds
dated one-offs. Each of those pages, and every category page, shows its free rows first and its non-free rows in a
second table.</li>
<li><strong>Everything is also available in one date-ordered list</strong> on
<a href="upcoming.html">Upcoming by date</a> and <a href="all-events.html">All events</a>.</li>
</ol></section>
<section class="panel"><h3>Publish rule</h3><ol>
<li>Each active row needs a title, source-stated date/cadence, San Francisco city location, organizer, and HTTPS source link.</li>
<li>Accepted sources are official organizers, official venues, government sources, and clearly labeled trusted civic sources. The source type is visible in every row.</li>
<li>Optional time and admission fields are not inferred. An em dash means the captured source did not state that optional value; “Not stated” in the Cost column means no price was published.</li>
<li>Multi-city programs, cancelled events, outside-city events, and records missing essential evidence are not added to public tables. They stay on <a href="flagged.html">Flagged for Review</a> with a source and explanation.</li>
</ol></section>
<section class="panel"><h3>How date ordering and the executive summary work</h3><ul class="analysis-list">
<li>Every list is generated with upcoming rows first, ordered by start date, with completed editions pushed to the bottom and labelled <em>Completed</em>.</li>
<li>A small script re-computes each row's status against the visitor's actual current date, so the "Upcoming" / "Completed" / "Ongoing now" badge and the "in N days" label stay correct after the static build date. The same script refreshes every relative label on the dashboard's lists.</li>
<li>The dashboard's executive summary is <strong>free-first</strong>: it shows the free events closest to today, how many free events start in the next 7, 30 and 90 days, how many free programs are running now, and then — in its own clearly labelled panel — the nearest paid, registration-only or unpriced events. A build-time list is included for readers without JavaScript.</li>
</ul></section>
<section class="panel"><h3>How cost is labelled</h3><p>Cost classes are derived only from the admission text that the
linked official page stated. Nothing is inferred from an event's type.</p>
<div class="legend">
<span class="cost cost-free">Free</span> the source states no charge
<span class="cost cost-mixed">Free or partly free</span> some programmes free, others ticketed
<span class="cost cost-paid">Paid / ticketed</span> the source states a price, pass or ticket
<span class="cost cost-restricted">Registration only</span> the source names registration or an invitation but publishes no price
<span class="cost cost-unknown">Not stated</span> the source published no price — <strong>never</strong> treated as free
</div>
<p>Current split: {cost_summary}. Only the free and partly-free classes appear in the main list. The rows with an
unstated cost are listed, with their source links, on the <a href="flagged.html">Flagged for Review</a> page and in
the separate <a href="paid.html">Paid &amp; ticketed</a> section.</p>
<p><strong>Registration wording is not a price.</strong> Where a source says only “Registration required” or “By
invitation only”, the row is labelled <em>Registration only — no price published</em> rather than “Paid”, because
asserting a price would be an inference. Four rows are affected and they are recorded in
<a href="flagged.html#flag-registration-only-cost-class">flag-registration-only-cost-class</a>.</p></section>
<section class="panel"><h3>Findings, bounded by this dataset</h3><ul class="analysis-list">
<li>The audit has {len(recurring)} recurring and {len(special)} dated-special verified rows across {len(categories)} categories; {len(upcoming)} of the {len(published)} published rows are still upcoming as of {esc(catalog['as_of'])}.</li>
<li>Free coverage: {len(free_rows)} rows are free or partly free, and {len(free_upcoming)} of those are still upcoming. {len(unstated_rows)} rows have no published price, so they cannot be counted as free even where attendance may in fact cost nothing.</li>
<li>The recurring list breaks down as {cadence_summary}. The classification is based on cadence, not whether an event is free or public.</li>
<li>The largest audited categories are {top_categories}. This describes the verified source set, not all activity in San Francisco.</li>
<li>Most 2026 editions in this snapshot had already taken place by the October 18, 2026 check date, while several rows document confirmed 2027 editions. Rows record the audited edition, not a promise that the same dates repeat.</li>
<li>Focus-area gaps are published rather than papered over. As of October 18, 2026: no <em>upcoming</em> in-person free gaming event inside the city could be verified from an official source (<a href="flagged.html#flag-free-gaming-coverage-gap">flag-free-gaming-coverage-gap</a>); none of the 16 AI &amp; technology rows carries a source-stated free admission (<a href="flagged.html#flag-free-ai-coverage-gap">flag-free-ai-coverage-gap</a>); and 2027 dates for Hardly Strictly Bluegrass are published only by secondary aggregators (<a href="flagged.html#flag-hsb-2027-dates-unconfirmed">flag-hsb-2027-dates-unconfirmed</a>).</li>
<li>The review register makes scope and cancellation decisions visible instead of deleting difficult records or asserting unsupported city-only coverage.</li>
</ul></section>
<section class="panel"><h3>Directories and coverage boundaries</h3>
<p>Some San Francisco programming is published as a running calendar rather than a single event with a fixed cadence. Those are linked here as directories instead of forcing them into event rows:</p>
<ul class="analysis-list">
<li><a href="https://sfpl.org/events">San Francisco Public Library — Upcoming Events</a>: branch programs and talks across the city system.</li>
<li><a href="https://sfcityguides.org/">San Francisco City Guides</a>: free volunteer-led walking tours (70+ tours, a program of SFPL); individual tours run on varying schedules via their tour finder.</li>
<li><a href="https://sfrecpark.org/Calendar.aspx">SF Recreation and Park calendar</a>: park programs and seasonal city events; individual dated listings (for example Scaregrove) become special-event rows.</li>
<li><a href="https://sf.gov/events/upcoming">SF.gov citywide meetings and events</a>: the city's own calendar, including free civic programs; dated listings become rows when a city page states the date and location.</li>
</ul>
<p>Boundaries applied in this snapshot: recurring rows are created only when an organizer, venue, or government page states a fixed cadence (weekly, monthly, seasonal, or annual). Candidates seen only in secondary coverage or in roundup articles are not listed until directly verified. Well-known look-alikes outside the City and County are excluded: the Great Dickens Christmas Fair is at the Cow Palace in Daly City, and airport programs at SFO sit in San Mateo County.</p></section>
<section class="panel"><h3>Line-by-line verification</h3><p>Every published and review row is checked against its
linked official source page, and each session's pass is logged row by row with quoted source text:
<a href="research/reverification-3977d9cb.md">research/reverification-3977d9cb.md</a> (this pass),
<a href="research/review-3977d9cb.md">research/review-3977d9cb.md</a> (repository review and irregularities),
<a href="research/verification-e79e0de2.md">research/verification-e79e0de2.md</a>,
<a href="research/reverification-2088b727.md">research/reverification-2088b727.md</a>,
<a href="research/verification-e969f4df.md">research/verification-e969f4df.md</a> and
<a href="research/reverification-55c58947.md">research/reverification-55c58947.md</a>. Values not stated by a source
were blanked and flagged rather than inferred; dead or moved official links were re-pointed to live pages.</p></section>
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
        f"{len(free_rows)} free or partly free ({len(free_upcoming)} upcoming); "
        f"{len(priced_rows)} priced/registration-only; {len(unstated_rows)} cost not stated."
    )


if __name__ == "__main__":
    build()
