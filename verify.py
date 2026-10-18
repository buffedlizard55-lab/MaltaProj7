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
    if not isinstance(catalog, dict) or not isinstance(events, list):
        error("data/events.json must be a catalog object with an events list")
        events = []

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
    if len(published) != 70:
        error(f"expected 70 published rows, found {len(published)}")
    if len(recurring) != 62 or len(special) != 8:
        error(f"expected 62 recurring / 8 special, found {len(recurring)} / {len(special)}")
    if len(review) != 5:
        error(f"expected 5 review records, found {len(review)}")
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
    expected_counts = {
        ROOT / "recurring.html": len(recurring),
        ROOT / "special.html": len(special),
        ROOT / "annual-special.html": len(special),
        ROOT / "all-events.html": len(published),
        ROOT / "flagged.html": len(review),
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

    if not (ROOT / "research" / "official-source-audit.md").exists():
        error("missing research/official-source-audit.md")
    if not (ROOT / "data" / "events.csv").exists():
        error("missing data/events.csv export")

    print(
        f"published={len(published)} recurring={len(recurring)} special={len(special)} "
        f"review={len(review)} categories={len(categories)} "
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
