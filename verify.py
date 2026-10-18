#!/usr/bin/env python3
"""Validate the static SF Events site without fetching external sites.

External organizers remain the authoritative source, but sandbox network policy does
not permit a dependable live crawl of every linked source. This verifier therefore
checks the local, reproducible guarantees: data shape, row-level HTTPS links,
separation of review-only records, generated source-link counts, and local links.
"""
from __future__ import annotations

import html
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).parent.resolve()
DATA_PATH = ROOT / "data" / "events.json"
ERRORS: list[str] = []

sys.path.insert(0, str(ROOT))
try:  # the cost classifier lives with the generator so both agree on the policy
    from build import cost_class
except Exception:  # pragma: no cover - standalone fallback
    def cost_class(admission: str) -> str:
        text = (admission or "").strip().lower()
        if not text:
            return "not-stated"
        has_free = any(h in text for h in ("free", "no-cost", "no cost",
                                           "no fundraising minimum", "suggested"))
        if has_free:
            if "$" in text or any(h in text for h in ("ticketed", "tickets sold",
                                                       "reserved", "seating tickets",
                                                       "hospitality packages")):
                return "mixed"
            return "free"
        return "paid"


def error(message: str) -> None:
    ERRORS.append(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        error(f"missing generated file: {path.relative_to(ROOT)}")
        return ""


def source_link_count(path: Path) -> int:
    return read(path).count('class="source-link"')


def check_internal_links(path: Path, text: str) -> None:
    # Duplicate ids break the browser-side scripts (getElementById silently
    # targets the first match) and duplicate aria-labelledby references, so both
    # are treated as build errors rather than cosmetic nits.
    ids = re.findall(r'\sid="([^"]+)"', text)
    for identifier, count in Counter(ids).items():
        if count > 1:
            error(f"{path.relative_to(ROOT)}: duplicate id {identifier!r} ({count} times)")
    for reference in re.findall(r'aria-labelledby="([^"]+)"', text):
        for identifier in reference.split():
            if identifier not in ids:
                error(
                    f"{path.relative_to(ROOT)}: aria-labelledby={identifier!r} "
                    "points at a missing id"
                )
    for href in re.findall(r'href="([^"]+)"', text):
        parsed = urlparse(href)
        if parsed.scheme or href.startswith("#") or href.startswith("//"):
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            error(f"{path.relative_to(ROOT)}: local link escapes repository: {href}")
            continue
        if not target.exists():
            error(f"{path.relative_to(ROOT)}: broken local link {href}")


def main() -> int:
    document = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    catalog = document.get("catalog")
    events = document.get("events")
    flags = document.get("flags", [])
    if not isinstance(catalog, dict) or not isinstance(events, list):
        error("data/events.json must be a catalog object with an events list")
        events = []
    if not isinstance(flags, list):
        error("data/events.json flags must be an array")
        flags = []

    ids: set[str] = set()
    published: list[dict] = []
    review: list[dict] = []
    required_published = {
        "id", "name", "bucket", "cadence", "category", "date_text", "location",
        "organizer", "source_url", "source_label", "source_authority", "status",
    }
    for index, event in enumerate(events):
        event_id = event.get("id", f"row-{index}")
        if event_id in ids:
            error(f"duplicate id: {event_id}")
        ids.add(event_id)
        if not str(event.get("source_url", "")).startswith("https://"):
            error(f"{event_id}: source_url must be HTTPS")
        if event.get("status") == "verified":
            missing = sorted(field for field in required_published if not event.get(field))
            if missing:
                error(f"{event_id}: published row missing {', '.join(missing)}")
            if event.get("bucket") not in {"recurring", "special"}:
                error(f"{event_id}: verified row is not in a public bucket")
            published.append(event)
        else:
            if event.get("bucket") != "review":
                error(f"{event_id}: non-verified row must use review bucket")
            if not event.get("review_reason"):
                error(f"{event_id}: review row needs review_reason")
            review.append(event)

    recurring = [event for event in published if event["bucket"] == "recurring"]
    special = [event for event in published if event["bucket"] == "special"]
    categories = sorted({event["category"] for event in published})

    # Stable audit counts are a guard against accidental loss of catalog/review rows.
    # Update these constants only with a corresponding audit entry in
    # research/official-source-audit.md (2026-10-18 three-way integration
    # reconciliation incl. arena/55c58947-maltaproj7: 93 = 74 + 19, 12 review,
    # 16 field-level flags; sf-aloha-run restored to verified via live .org source,
    # IOFF-2027 and Italian-Heritage-2027 rows added).
    # Stable audit counts updated 2026-10-18 by session arena/d07e4ede-maltaproj7:
    # +3 verified events added from official sources (Bhangra & Beats Night
    # Market — recurring/seasonal; SF International Hip Hop DanceFest —
    # recurring/annual; Renegade Craft Fair — special/single-event). Final
    # total: 96 published (76 recurring + 20 special), 12 review, 16 flags.
    # 2026-10-18 arena/5e333a6e-maltaproj7 coverage-gap pass (audit entry
    # "Coverage-gap pass — arena/5e333a6e"): +32 published (+7 recurring,
    # +25 special), review unchanged -> 139 = 94 + 45, 16 review, 25 flags.
    # Audit counts updated 2026-10-18 by session arena/2088b727-maltaproj7 during
    # three-way integration with PRs #18-#22: +1 verified recurring row
    # (San Francisco Pride Celebration & Parade 2026) and 3 new field-level flags
    # (fillmore-jazz-2027-span, bhangra-location-conflict, haight-cross-source).
    # 2026-10-18 arena/e79e0de2-maltaproj7: date-first/freeness rebuild pass.
    # +8 verified rows added from official organizer/government sources
    # (AI Engineer Code Summit 2026, Day of the Devs SF Edition 2026, Union Square
    # Plaza Free Park Programs, SFIAC & Olympic Club Cornhole Tournament, Hayes
    # Valley Farmers Market & Shared Spaces, Foodwise Sunday Supper, Dia de los
    # Muertos/Halloween at Mission Community Market, Fall Fruit Celebration,
    # Mission Community Market last day of the season, Fall Holiday Farmers
    # Market) plus 2 rows re-sourced to the organiser's own site (Bearrison
    # Street Fair, Potrero Hill Festival). New "Technology, AI & gaming"
    # category created by moving 14 clearly tech/AI/gaming rows out of
    # "Professional & academic". Total: 148 published (98 recurring + 50
    # special), 16 review records, 34 field-level flags, 9 categories.
    # 2026-10-18 arena/8c40d1c6-maltaproj7 verification pass (log:
    # research/verification-8c40d1c6.md, patch: research/patch-8c40d1c6.py):
    # +6 published special rows added from official organizer/government pages
    # (Sunday Streets Excelsior 2026, SFIAC and Olympic Club Cornhole Tournament,
    # and four Foodwise farmers-market cooking demos), cost and note fills on 4
    # rows, and 6 new field-level flags. Total: 154 published (98 recurring + 56
    # special), 16 review records, 41 field-level flags, 9 categories.
    # Irregularity noted by this pass: the ledger entry for arena/e79e0de2 above
    # lists an "SFIAC & Olympic Club Cornhole Tournament" row that is absent from
    # data/events.json (verified by searching every record id, name and source
    # URL on 2026-10-18); the row was added in this pass from the SFMTA source
    # instead, and the discrepancy is logged in COORDINATION.md and on the
    # Flagged for Review page.
    if len(published) != 154:
        error(f"expected 154 published rows, found {len(published)}")
    if len(recurring) != 98 or len(special) != 56:
        error(f"expected 98 recurring / 56 special, found {len(recurring)} / {len(special)}")
    if len(review) != 16:
        error(f"expected 16 review records, found {len(review)}")
    if len(flags) != 41:
        error(f"expected 41 field-level flags, found {len(flags)}")

    # --- hardened semantic checks (added after mutation testing showed the shape
    # checks alone accepted example.com sources, out-of-city venues, fabricated
    # cadences, duplicates under new ids, and end < start) ---
    allowed_statuses = {"verified", "partial_sf_program", "needs_review", "cancelled", "outside_city_excluded"}
    allowed_cadences = {
        "recurring": {"weekly", "monthly", "seasonal", "annual"},
        "special": {"single-date", "single-event", "dated-program"},
    }
    allowed_authorities = {
        "Official organizer", "Official venue", "Official venue / federal trust",
        "Government source", "Trusted civic source",
    }
    banned_hosts = {"example.com", "example.org", "example.net", "localhost", "127.0.0.1"}
    placeholder_fragments = (
        "see organizer", "see schedule", "program-specific", "see race", "see neighborhood",
        "see performance", "see sfmta", "see city", "see presidio", "not stated in captured",
        "see official", "see event page", "varies; see", "tba", "tbd",
    )
    sf_markers = (
        "san francisco", "golden gate park", "presidio", "fort mason", "moscone",
        "japantown", "civic center", "mission district", "ferry building", "pier 80",
        "mclaren park", "yerba buena gardens", "stern grove", "golden gate bridge",
        "alcatraz island", "city hall", "marina green", "roxie theater",
    )
    seen_name_start: set[tuple[str, str]] = set()
    try:
        as_of = date.fromisoformat(str(catalog.get("as_of", "")))
    except ValueError:
        error("catalog as_of is not an ISO date")
        as_of = None
    for event in events:
        event_id = event.get("id", "<missing id>")
        if event.get("status") not in allowed_statuses:
            error(f"{event_id}: unknown status {event.get('status')!r}")
        host = urlparse(str(event.get("source_url", ""))).netloc.lower().removeprefix("www.")
        if host in banned_hosts:
            error(f"{event_id}: source_url uses a banned example/local host")
        dup_key = (str(event.get("name", "")).strip().lower(), str(event.get("start_date", "")))
        if dup_key[0] and dup_key in seen_name_start:
            error(f"{event_id}: duplicate name+start_date {dup_key}")
        seen_name_start.add(dup_key)
        start = end = None
        for field in ("start_date", "end_date"):
            value = str(event.get(field, "") or "")
            if value:
                try:
                    parsed = date.fromisoformat(value)
                except ValueError:
                    error(f"{event_id}: {field} is not an ISO date: {value!r}")
                    continue
                if field == "start_date":
                    start = parsed
                else:
                    end = parsed
                if as_of and not (as_of.year - 1 <= parsed.year <= as_of.year + 1):
                    error(f"{event_id}: {field} year {parsed.year} implausible for as_of {as_of}")
        if start and end and end < start:
            error(f"{event_id}: end_date {end} is before start_date {start}")
        if start:
            years = {int(y) for y in re.findall(r"\b(20\d{2})\b", str(event.get("date_text", "")))}
            allowed_years = {start.year} | ({end.year} if end else set())
            stray = years - allowed_years
            if stray:
                error(f"{event_id}: date_text year(s) {sorted(stray)} disagree with ISO dates")
        for field in ("time_text", "admission"):
            value = str(event.get(field, "") or "").lower()
            hit = next((frag for frag in placeholder_fragments if frag in value), None)
            if hit:
                error(f"{event_id}: {field} contains placeholder fragment {hit!r}; blank it instead")
        if event.get("status") == "verified":
            bucket = event.get("bucket")
            if event.get("cadence") not in allowed_cadences.get(bucket, set()):
                error(f"{event_id}: cadence {event.get('cadence')!r} not allowed for bucket {bucket!r}")
            if event.get("source_authority") not in allowed_authorities:
                error(f"{event_id}: unknown published source_authority {event.get('source_authority')!r}")
            location = str(event.get("location", "")).lower()
            if not any(marker in location for marker in sf_markers):
                error(f"{event_id}: published location has no San Francisco indicator: {event.get('location')!r}")
        elif event.get("source_authority") not in allowed_authorities | {"Unverified legacy URL"}:
            error(f"{event_id}: unknown review source_authority {event.get('source_authority')!r}")
    if catalog.get("geography") != "City and County of San Francisco only":
        error("catalog geography statement does not enforce city-only scope")

    root_pages = [
        ROOT / "index.html", ROOT / "upcoming.html", ROOT / "free.html", ROOT / "paid.html",
        ROOT / "recurring.html", ROOT / "special.html",
        ROOT / "annual-special.html", ROOT / "categories.html", ROOT / "all-events.html",
        ROOT / "flagged.html", ROOT / "method.html",
    ]
    category_pages = [ROOT / "categories" / f"{category.lower().replace('&', 'and').replace(' ', '-').replace('/', '-')}.html" for category in categories]
    # build.py's slug normalization also collapses punctuation. Validate actual category page names by discovery.
    category_pages = sorted((ROOT / "categories").glob("*.html"))
    if len(category_pages) != len(categories):
        error(f"expected {len(categories)} category pages, found {len(category_pages)}")

    for path in [*root_pages, *category_pages]:
        text = read(path)
        if not text:
            continue
        if "<<<<<<<" in text or "=======" in text or ">>>>>>>" in text:
            error(f"{path.relative_to(ROOT)} contains a merge marker")
        check_internal_links(path, text)

    # Each generated public/review table has exactly one source link for each row.
    # flagged.html also carries one link per field-level flag source.
    flag_source_links = sum(len(flag.get("sources", [])) for flag in flags)
    cost_not_stated = [event for event in published if not str(event.get("admission") or "").strip()]
    free_rows = [
        event for event in published
        if cost_class(str(event.get("admission") or "")) in {"free", "mixed"}
    ]
    expected_counts = {
        ROOT / "upcoming.html": len(published),
        ROOT / "free.html": len(free_rows),
        ROOT / "paid.html": len(
            [e for e in published if cost_class(str(e.get("admission") or "")) == "paid"]
        ),
        ROOT / "recurring.html": len(recurring),
        ROOT / "special.html": len(special),
        ROOT / "annual-special.html": len(special),
        ROOT / "all-events.html": len(published),
        ROOT / "flagged.html": len(review) + flag_source_links + len(cost_not_stated),
    }
    for path, expected in expected_counts.items():
        actual = source_link_count(path)
        if actual != expected:
            error(f"{path.relative_to(ROOT)}: expected {expected} official-source links, found {actual}")

    all_html = read(ROOT / "all-events.html")
    flagged_html = read(ROOT / "flagged.html")
    for event in published:
        if html.escape(event["source_url"], quote=True) not in all_html:
            error(f"all-events.html missing source URL for {event['id']}")
        if html.escape(event["name"], quote=True) not in all_html:
            error(f"all-events.html missing row name for {event['id']}")
    for event in review:
        if html.escape(event["source_url"], quote=True) not in flagged_html:
            error(f"flagged.html missing source URL for {event['id']}")
        if html.escape(event["review_reason"], quote=True) not in flagged_html:
            error(f"flagged.html missing review reason for {event['id']}")

    for category in categories:
        matching = [event for event in published if event["category"] == category]
        heading = f"<h2>{html.escape(category)}</h2>"
        files = [path for path in category_pages if heading in read(path)]
        if len(files) != 1:
            error(f"could not identify one category page for {category}")
        elif source_link_count(files[0]) != len(matching):
            error(f"{files[0].relative_to(ROOT)}: expected {len(matching)} source links")

    index_html = read(ROOT / "index.html")
    for expected in (f">{len(published)}<", f">{len(recurring)}<", f">{len(special)}<", f">{len(review)}<"):
        if expected not in index_html:
            error(f"dashboard missing expected metric {expected}")
    # Dashboard prose summaries must cover every cadence and authority present
    # (guards against hardcoded summary sentences silently dropping a group).
    from collections import Counter as _Counter
    for cadence, count in _Counter(event["cadence"] for event in recurring).items():
        if f"<strong>{count} {cadence}</strong>" not in index_html:
            error(f"dashboard cadence summary missing {count} {cadence}")
    for authority, count in _Counter(event["source_authority"] for event in published).items():
        if f"<strong>{count} {html.escape(authority.lower())}</strong>" not in index_html:
            error(f"dashboard authority summary missing {count} {authority}")
    if "Official source ↗" in index_html or "Official source ↗" in all_html:
        error("generated pages still use the inaccurate 'Official source' link text")

    # --- date-first ordering and cost disclosure checks (2026-10-18) ---
    upcoming_html = read(ROOT / "upcoming.html")
    free_html = read(ROOT / "free.html")
    method_html = read(ROOT / "method.html")
    for event in published:
        for label, page_html in (("upcoming.html", upcoming_html), ("all-events.html", all_html)):
            if html.escape(event["name"], quote=True) not in page_html:
                error(f"{label} missing row name for {event['id']}")
            if html.escape(event["source_url"], quote=True) not in page_html:
                error(f"{label} missing source URL for {event['id']}")
    # The upcoming list must lead with upcoming rows and keep them in date order.
    # Upcoming page is split into free / paid / cost-not-stated tables by the
    # brief's sectioning rule, so the date-first ordering guarantee is checked
    # inside each table (and the free table must lead the page).
    table_blocks = re.findall(r'<table data-filter-table(.*?)</table>', upcoming_html, re.S)
    if len(table_blocks) < 3:
        error(
            "upcoming.html expected 3 cost-split tables (free, paid, not stated), "
            f"found {len(table_blocks)}"
        )
    for index, block in enumerate(table_blocks, start=1):
        statuses = re.findall(r'data-status="([a-z\-]+)"', block)
        if not statuses:
            error(f"upcoming.html table {index} has no filterable rows")
            continue
        order = {"upcoming": 0, "undated": 1, "completed": 2}
        ranks = [order.get(status, 9) for status in statuses]
        if ranks != sorted(ranks):
            error(f"upcoming.html table {index} is not ordered with upcoming rows first")
        dateranks = re.findall(r'data-daterank="([0-9]-\d{4}-\d{2}-\d{2})"', block)
        upcoming_dates = [
            rank for rank, status in zip(dateranks, statuses) if status == "upcoming"
        ]
        if upcoming_dates != sorted(upcoming_dates):
            error(f"upcoming.html table {index} upcoming rows are not in ascending date order")
    first_block = table_blocks[0] if table_blocks else ""
    first_statuses = re.findall(r'data-status="([a-z\-]+)"', first_block)
    if first_statuses and first_statuses[0] != "upcoming":
        error("upcoming.html does not start with an upcoming row")
    first_costs = re.findall(r'data-cost="([a-z\-]+)"', first_block)
    if first_costs and any(cost not in {"free", "mixed"} for cost in first_costs):
        error("upcoming.html main table must contain only free / partly-free rows")
    if first_block and 'data-default-when="upcoming"' not in first_block:
        error("upcoming.html main table does not default to upcoming rows only")
    # paid.html mirrors the ticketed rows and must stay separate from the free list.
    paid_html = read(ROOT / "paid.html")
    paid_costs = re.findall(r'data-cost="([a-z\-]+)"', paid_html)
    paid_rows = [e for e in published if cost_class(e.get("admission", "")) == "paid"]
    if len(paid_costs) != len(paid_rows):
        error(f"paid.html: expected {len(paid_rows)} rows, found {len(paid_costs)}")
    for cost in paid_costs:
        if cost != "paid":
            error(f"paid.html contains a {cost!r} row; only ticketed rows belong there")
    for event in paid_rows:
        if html.escape(event["name"], quote=True) not in paid_html:
            error(f"paid.html missing paid row {event['id']}")
        if html.escape(event["source_url"], quote=True) not in paid_html:
            error(f"paid.html missing source URL for {event['id']}")
    # free.html must contain only rows the source describes as free or partly free.
    free_costs = re.findall(r'data-cost="([a-z\-]+)"', free_html)
    if len(free_costs) != len(free_rows):
        error(f"free.html: expected {len(free_rows)} rows, found {len(free_costs)}")
    for cost in free_costs:
        if cost not in {"free", "mixed"}:
            error(f"free.html contains a {cost!r} row; only source-stated free rows belong there")
    for event in free_rows:
        if html.escape(event["name"], quote=True) not in free_html:
            error(f"free.html missing free row {event['id']}")
    # Rows whose source published no price are disclosed on the Flagged page.
    for event in cost_not_stated:
        if html.escape(event["name"], quote=True) not in flagged_html:
            error(f"flagged.html missing cost-not-stated row {event['id']}")
    if "Not stated" not in flagged_html:
        error("flagged.html does not disclose rows whose cost was not stated")
    # Dashboard must expose the executive summary and the free-focus view.
    for needle in ("next-up", "free-upcoming", "Executive summary", "Free to attend"):
        if needle not in index_html:
            error(f"dashboard missing {needle!r} section")
    if "Not stated" not in index_html:
        error("dashboard does not explain the 'Not stated' cost label")
    if "cost_class" not in index_html or "sf-events-data" not in index_html:
        error("dashboard is missing the embedded dataset used for the live next-up summary")
    if "Not stated" not in method_html or "cost" not in method_html.lower():
        error("method.html does not document the cost policy")
    # The embedded dataset must cover every published row.
    blob = re.search(r'id="sf-events-data">(.*?)</script>', index_html, re.S)
    if not blob:
        error("dashboard is missing the embedded event dataset")
    else:
        payload = json.loads(blob.group(1).replace("<\\/", "</"))
        embedded = {item["id"] for item in payload}
        missing = {event["id"] for event in published} - embedded
        if missing:
            error(f"dashboard dataset missing {len(missing)} published rows")
    if "Technology, AI & gaming" not in categories:
        error("expected the new Technology, AI & gaming category")
    if not (ROOT / "categories" / "technology-ai-and-gaming.html").exists():
        error("missing categories/technology-ai-and-gaming.html")

    if not (ROOT / "research" / "official-source-audit.md").exists():
        error("missing research/official-source-audit.md")
    if not (ROOT / "data" / "events.csv").exists():
        error("missing data/events.csv export")

    print(
        f"published={len(published)} recurring={len(recurring)} special={len(special)} "
        f"review={len(review)} flags={len(flags)} categories={len(categories)} "
        f"authorities={dict(sorted(Counter(e['source_authority'] for e in published).items()))}"
    )
    if ERRORS:
        print("CHECKS FAILED:")
        print("\n".join(f"- {message}" for message in ERRORS))
        return 1
    print("ALL LOCAL CATALOG, SOURCE-LINK, AND NAVIGATION CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
