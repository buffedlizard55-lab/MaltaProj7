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
    if len(published) != 140:
        error(f"expected 140 published rows, found {len(published)}")
    if len(recurring) != 95 or len(special) != 45:
        error(f"expected 95 recurring / 45 special, found {len(recurring)} / {len(special)}")
    if len(review) != 16:
        error(f"expected 16 review records, found {len(review)}")

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
        ROOT / "index.html", ROOT / "recurring.html", ROOT / "special.html",
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
    expected_counts = {
        ROOT / "recurring.html": len(recurring),
        ROOT / "special.html": len(special),
        ROOT / "annual-special.html": len(special),
        ROOT / "all-events.html": len(published),
        ROOT / "flagged.html": len(review) + flag_source_links,
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
        files = [path for path in category_pages if f">{category.replace('&', '&amp;')}<" in read(path)]
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
