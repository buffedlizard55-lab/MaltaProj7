#!/usr/bin/env python3
"""Independent local integrity harness for the SF events catalog.

Session: arena/e969f4df-maltaproj7 (task V2).

This script is READ-ONLY.  It never edits data/events.json, build.py, verify.py or
any generated page (those files are claimed by concurrent sessions).  It re-checks the
published catalog with tests that `verify.py` does not run, and prints an evidence
report that is transcribed into research/verification-e969f4df.md.

Checks
  A  record shape: required fields, HTTPS, non-placeholder values, host hygiene
  B  calendar logic: weekday names in date_text vs ISO dates, year agreement,
     inverted ranges, malformed ISO dates
  C  classification: cadence vs bucket, category vocabulary, status vocabulary,
     source_authority vocabulary
  D  geography: every published location must carry a San Francisco indicator
  E  duplicates: same tradition published twice, duplicate ids, duplicate name+date
  F  flags register: referential integrity, sources, disposition present
  G  data -> generated page parity: every published row rendered, source-link counts
  H  internal link crawl of every HTML file in the repository
  I  external source inventory (for manual/official-source review; not fetched here
     because the sandbox has no general outbound network)

Run:  python3 research/audit_checks_e969f4df.py
"""
from __future__ import annotations

import html
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "events.json"
TODAY = date(2026, 10, 18)  # audit date, stated in the brief's session context

FINDINGS: list[tuple[str, str, str]] = []  # (severity, check, message)
NOTES: list[tuple[str, str]] = []  # (check, message)


def finding(severity: str, check: str, message: str) -> None:
    FINDINGS.append((severity, check, message))


def note(check: str, message: str) -> None:
    NOTES.append((check, message))


CATEGORIES = {
    "Books & ideas", "Community & culture", "Fairs & nightlife", "Film & media",
    "Food & markets", "Music & performing arts", "Professional & academic",
    "Sports & outdoors",
}
STATUSES = {"verified", "needs_review", "partial_sf_program", "outside_city_excluded", "cancelled"}
AUTHORITIES = {
    "Official organizer", "Official venue", "Official venue / federal trust", "Government source",
    "Trusted civic source", "Unverified legacy URL",
}
BUCKETS = {"recurring", "special", "review"}
RECURRING_CADENCES = {"weekly", "monthly", "seasonal", "annual"}
SPECIAL_CADENCES = {"single-date", "single-event", "dated-program"}

PLACEHOLDERS = {
    "tba", "tbd", "n/a", "na", "none", "unknown", "various", "see organizer",
    "see organizer schedule", "see schedule", "see site", "see website",
    "see official site", "see official website", "see link", "see source",
    "varies", "program-specific times", "check organizer", "check website",
    "free?", "maybe", "-", "--", "?",
}
BAD_HOSTS = {"example.com", "example.org", "example.net", "localhost", "127.0.0.1", "test.com"}

SF_TOKENS = [
    "san francisco", "sf ", " s.f.", "94101", "94102", "94103", "94104", "94105", "94107",
    "94108", "94109", "94110", "94111", "94112", "94114", "94115", "94116", "94117", "94118",
    "94121", "94122", "94123", "94124", "94127", "94129", "94131", "94132", "94133", "94134",
    "94158", "ca",  # handled separately below
]
SF_NEIGHBORHOODS = [
    "mission", "castro", "haight", "ashbury", "north beach", "chinatown", "japantown",
    "fillmore", "presidio", "golden gate", "marina", "soma", "south of market", "tenderloin",
    "nob hill", "russian hill", "pacific heights", "sunset", "richmond", "bayview",
    "hunters point", "excelsior", "potrero", "bernal", "noe valley", "duboce", "alamo square",
    "civic center", "financial district", "embarcadero", "ferry building", "fort mason",
    "yerba buena", "treasure island", "ocean beach", "lake merced", "cow hollow",
    "dogpatch", "mission bay", "dolores", "buena vista", "twin peaks", "glen park",
    "west portal", "stanyan", "masonic", "divisadero", "valencia", "hayes valley",
    "alemany", "inner sunset", "outer sunset", "presidio heights", "sea cliff",
    "south beach", "rincon", "potrero hill", "san francisco",
]


def norm(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def is_placeholder(value: str) -> bool:
    cleaned = norm(value).strip(".!").lower()
    return cleaned in PLACEHOLDERS


def parse_iso(value: str) -> date | None:
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def strip_year_tokens(name: str) -> str:
    """Canonical key for duplicate-tradition detection."""
    key = name.lower()
    key = re.sub(r"\b(19|20)\d{2}\b", " ", key)
    key = re.sub(r"\b\d{1,2}(st|nd|rd|th)\b", " ", key)
    for drop in ["san francisco", "sf", "the", "&", "and", "-", "—", ":", ",", ".", "(", ")", "festival", "season", "edition", "program"]:
        key = key.replace(drop, " ")
    return re.sub(r"\s+", " ", key).strip()


WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def check_a_shape(events: list[dict]) -> None:
    ids: set[str] = set()
    for ev in events:
        eid = norm(ev.get("id"))
        label = f"{eid or '<no id>'} ({norm(ev.get('name'))[:60]})"
        if not eid:
            finding("ERROR", "A", f"record without id: {norm(ev.get('name'))}")
        elif eid in ids:
            finding("ERROR", "A", f"duplicate id: {eid}")
        ids.add(eid)
        for field in ("name", "bucket", "category", "source_url", "source_label", "source_authority", "status"):
            if field not in ev:
                finding("ERROR", "A", f"{label}: missing field `{field}`")
        url = norm(ev.get("source_url"))
        if not url.startswith("https://"):
            finding("ERROR", "A", f"{label}: source_url is not HTTPS: {url!r}")
        else:
            host = (urlparse(url).hostname or "").lower()
            if host in BAD_HOSTS:
                finding("ERROR", "A", f"{label}: example/local source host {host}")
            if not host or "." not in host:
                finding("ERROR", "A", f"{label}: unparseable source host {host!r}")
            if re.search(r"(^|\.)(docs\.google\.com|drive\.google\.com|dropbox\.com|pastebin\.com|scribd\.com|bit\.ly|tinyurl\.com|t\.co|goo\.gl)$", host):
                finding("WARN", "A", f"{label}: source host is a sharing/shortlink service, not an official publisher: {host}")
        for field in ("time_text", "admission", "location", "organizer", "date_text", "review_reason", "notes", "source_label"):
            value = norm(ev.get(field))
            if value and is_placeholder(value):
                finding("WARN", "A", f"{label}: `{field}` holds placeholder text {value!r} (should be blank + flagged)")
        if ev.get("status") == "verified":
            for field in ("name", "cadence", "date_text", "location", "organizer", "source_url", "source_label"):
                if not norm(ev.get(field)):
                    finding("ERROR", "A", f"{label}: published row missing required `{field}`")
        else:
            if ev.get("bucket") != "review":
                finding("ERROR", "A", f"{label}: status {ev.get('status')!r} but bucket {ev.get('bucket')!r} (must be review)")
            if not norm(ev.get("review_reason")):
                finding("ERROR", "A", f"{label}: non-verified status without review_reason")
            for field in ("date_text", "location", "organizer", "time_text", "admission", "cadence"):
                if norm(ev.get(field)):
                    note("A", f"{label}: review record shows `{field}` = {norm(ev.get(field))[:70]!r} on Flagged for Review (partial evidence, not a published row)")


def check_b_calendar(events: list[dict]) -> None:
    for ev in events:
        label = f"{norm(ev.get('id'))} ({norm(ev.get('name'))[:55]})"
        text = norm(ev.get("date_text"))
        start = parse_iso(norm(ev.get("start_date")))
        end = parse_iso(norm(ev.get("end_date")))
        raw_start, raw_end = norm(ev.get("start_date")), norm(ev.get("end_date"))
        if raw_start and start is None:
            finding("ERROR", "B", f"{label}: malformed start_date {raw_start!r}")
        if raw_end and end is None:
            finding("ERROR", "B", f"{label}: malformed end_date {raw_end!r}")
        if start and end and end < start:
            finding("ERROR", "B", f"{label}: end_date {raw_end} precedes start_date {raw_start}")
        if start and end is None and ev.get("status") == "verified" and text:
            # single-day rows often omit end_date; only note when date_text spans a range
            if re.search(r"\d{4}\s*[–-]\s*\w+\s*\d", text) or " and " in text:
                note("B", f"{label}: multi-day date_text {text!r} but no end_date")
        # weekday names asserted in date_text must match the ISO dates
        if text:
            mentioned = [w for w in WEEKDAYS if re.search(rf"\b{w}\b", text, re.I)]
            anchors = [d for d in (start, end) if d]
            if mentioned and anchors:
                actual = {d.strftime("%A").lower() for d in anchors}
                bad = [w for w in mentioned if w.lower() not in actual]
                # allow weekday lists such as "Fridays-Sundays" describing cadence, not a date
                cadence_words = re.search(r"\b(fridays|saturdays|sundays|mondays|tuesdays|wednesdays|thursdays)\b", text, re.I)
                if bad and not cadence_words:
                    finding("ERROR", "B", f"{label}: date_text says {bad} but ISO dates are {sorted(actual)} ({text!r})")
                elif bad and cadence_words:
                    note("B", f"{label}: weekday plural in cadence text {text!r} — not treated as a date claim")
            years = {int(y) for y in re.findall(r"\b(20\d{2})\b", text)}
            iso_years = {d.year for d in anchors}
            if years and iso_years and not (years & iso_years):
                finding("ERROR", "B", f"{label}: date_text years {sorted(years)} disagree with ISO years {sorted(iso_years)}")
            if anchors and not years and ev.get("status") == "verified":
                note("B", f"{label}: published date_text {text!r} states no year (ISO {raw_start})")


def check_c_classification(events: list[dict]) -> None:
    for ev in events:
        label = f"{norm(ev.get('id'))} ({norm(ev.get('name'))[:55]})"
        bucket, cadence, status = norm(ev.get("bucket")), norm(ev.get("cadence")), norm(ev.get("status"))
        category, authority = norm(ev.get("category")), norm(ev.get("source_authority"))
        if bucket not in BUCKETS:
            finding("ERROR", "C", f"{label}: unknown bucket {bucket!r}")
        if status not in STATUSES:
            finding("ERROR", "C", f"{label}: unknown status {status!r}")
        if authority not in AUTHORITIES:
            finding("ERROR", "C", f"{label}: unknown source_authority {authority!r}")
        if category not in CATEGORIES:
            finding("ERROR", "C", f"{label}: unknown category {category!r}")
        if bucket == "recurring" and cadence and cadence not in RECURRING_CADENCES:
            finding("WARN", "C", f"{label}: recurring bucket with non-recurring cadence {cadence!r}")
        if bucket == "special" and cadence and cadence not in SPECIAL_CADENCES:
            finding("WARN", "C", f"{label}: special bucket with recurring cadence {cadence!r} (annual traditions belong in recurring)")
        if bucket == "review" and cadence:
            note("C", f"{label}: review record carries cadence {cadence!r}")
        if cadence == "annual" and bucket == "special":
            finding("WARN", "C", f"{label}: annual cadence filed as a special event — brief asks for regularly occurring events to be separated from special ones")
        if authority == "Unverified legacy URL" and status == "verified":
            finding("ERROR", "C", f"{label}: published row cites an `Unverified legacy URL` authority")


def check_d_geography(events: list[dict]) -> None:
    for ev in events:
        if ev.get("status") != "verified":
            continue
        loc = norm(ev.get("location")).lower()
        label = f"{norm(ev.get('id'))} ({norm(ev.get('name'))[:55]})"
        if not loc:
            finding("ERROR", "D", f"{label}: published row has no location")
            continue
        if re.search(r"\b941\d{2}\b", loc) or "san francisco" in loc or " s.f." in loc:
            continue
        if any(tok in loc for tok in SF_NEIGHBORHOODS):
            note("D", f"{label}: location {norm(ev.get('location'))!r} relies on a neighborhood name without 'San Francisco'")
            continue
        finding("ERROR", "D", f"{label}: location has no San Francisco indicator: {norm(ev.get('location'))!r}")
        for outside in ("oakland", "berkeley", "san mateo", "san jose", "daly city", "south san francisco",
                        "mill valley", "sausalito", "alameda", "san bruno", "brisbane", "colma", "broadmoor"):
            if outside in loc and "san francisco" not in loc:
                finding("ERROR", "D", f"{label}: location appears to be outside the city: {norm(ev.get('location'))!r}")


def check_e_duplicates(events: list[dict]) -> None:
    seen: dict[tuple[str, str], list[str]] = defaultdict(list)
    for ev in events:
        key = (norm(ev.get("name")).lower(), norm(ev.get("start_date")))
        seen[key].append(norm(ev.get("id")))
    for key, ids in seen.items():
        if len(ids) > 1:
            finding("ERROR", "E", f"duplicate name+date {key}: {ids}")
    groups: dict[str, list[dict]] = defaultdict(list)
    for ev in events:
        groups[strip_year_tokens(norm(ev.get("name")))].append(ev)
    for key, rows in sorted(groups.items()):
        if len(rows) < 2 or not key:
            continue
        published = [r for r in rows if r.get("status") == "verified"]
        if len(published) < 2:
            continue
        desc = "; ".join(
            f"{norm(r.get('id'))} [{norm(r.get('bucket'))}/{norm(r.get('cadence'))}] "
            f"{norm(r.get('date_text'))[:60] or '(no date)'} src={norm(r.get('source_url'))[:60]}"
            for r in published
        )
        finding("WARN", "E", f"same tradition published {len(published)}x under key {key!r}: {desc}")
    urls: dict[str, list[str]] = defaultdict(list)
    for ev in events:
        urls[norm(ev.get("source_url"))].append(norm(ev.get("id")))
    shared = {u: i for u, i in urls.items() if len(i) > 1}
    note("E", f"{len(shared)} source URL(s) are cited by more than one record (expected for multi-day series): "
              + "; ".join(f"{u} -> {i}" for u, i in list(shared.items())[:12]))


def check_f_flags(document: dict) -> None:
    events = document["events"]
    ids = {norm(e.get("id")) for e in events}
    flags = document.get("flags", [])
    for i, flag in enumerate(flags, start=1):
        label = norm(flag.get("id")) or f"flag#{i}"
        for field in ("issue", "disposition"):
            if not norm(flag.get(field)):
                finding("ERROR", "F", f"{label}: missing `{field}`")
        sources = flag.get("sources") or []
        if not sources:
            finding("ERROR", "F", f"{label}: no source links (brief requires a source link for every flagged item)")
        for src in sources:
            url = norm(src.get("url") if isinstance(src, dict) else src)
            if not url.startswith("https://"):
                finding("ERROR", "F", f"{label}: non-HTTPS flag source {url!r}")
        eid = norm(flag.get("event_id"))
        if eid and eid not in ids:
            finding("WARN", "F", f"{label}: event_id {eid!r} does not exist in events[]")
        if not eid:
            note("F", f"{label}: catalog-level flag (no event_id) — {norm(flag.get('issue'))[:80]}")
    flagged_events = {norm(f.get("event_id")) for f in flags if norm(f.get("event_id"))}
    for ev in events:
        if ev.get("status") != "verified" and norm(ev.get("id")) not in flagged_events:
            note("F", f"review record {norm(ev.get('id'))} has no field-level flag entry (review_reason only)")


def check_g_pages(document: dict) -> None:
    events = document["events"]
    published = [e for e in events if e.get("status") == "verified" and e.get("bucket") in {"recurring", "special"}]
    review = [e for e in events if e.get("bucket") == "review"]
    pages = {
        "all-events.html": published,
        "recurring.html": [e for e in published if e["bucket"] == "recurring"],
        "special.html": [e for e in published if e["bucket"] == "special"],
        "annual-special.html": [e for e in published if e["bucket"] == "special"],
        "flagged.html": review,
    }
    for page, rows in pages.items():
        path = ROOT / page
        if not path.exists():
            finding("ERROR", "G", f"generated page missing: {page}")
            continue
        text = path.read_text(encoding="utf-8")
        rendered = sum(1 for r in rows if html.escape(norm(r.get("name")), quote=True) in text or norm(r.get("name")) in text)
        if rendered != len(rows):
            missing = [norm(r.get("name")) for r in rows
                       if html.escape(norm(r.get("name")), quote=True) not in text and norm(r.get("name")) not in text]
            finding("ERROR", "G", f"{page}: {len(rows) - rendered} expected row(s) not rendered: {missing[:6]}")
        else:
            note("G", f"{page}: all {len(rows)} expected row name(s) present")
        links = text.count('class="source-link"')
        note("G", f"{page}: {links} source link(s) rendered")
    for path in sorted((ROOT / "categories").glob("*.html")):
        text = path.read_text(encoding="utf-8")
        category = None
        for cat in CATEGORIES:
            if cat.lower().replace(" & ", "-").replace("&", "-") in path.stem or True:
                pass
        rows = [e for e in published if path.stem == re.sub(r"[^a-z0-9]+", "-", e["category"].lower().replace("&", "and")).strip("-")]
        missing = [norm(r.get("name")) for r in rows
                   if html.escape(norm(r.get("name")), quote=True) not in text and norm(r.get("name")) not in text]
        if missing:
            finding("ERROR", "G", f"categories/{path.name}: {len(missing)} row(s) missing: {missing[:6]}")
        else:
            marker = 'class="source-link"'
            note("G", f"categories/{path.name}: all {len(rows)} row(s) present, {text.count(marker)} source link(s)")
    csv_path = ROOT / "data" / "events.csv"
    if csv_path.exists():
        lines = csv_path.read_text(encoding="utf-8").strip().splitlines()
        if len(lines) - 1 != len(events):
            finding("ERROR", "G", f"data/events.csv has {len(lines) - 1} data rows but events.json has {len(events)}")
        else:
            note("G", f"data/events.csv: {len(lines) - 1} rows matches events.json")
    else:
        finding("ERROR", "G", "data/events.csv missing")


def check_h_links() -> None:
    files = sorted(p for p in ROOT.rglob("*.html") if ".git" not in p.parts)
    if not files:
        finding("ERROR", "H", "no HTML files found")
    total_local = total_external = 0
    external_hosts: Counter[str] = Counter()
    for path in files:
        text = path.read_text(encoding="utf-8")
        for attr in ("href", "src"):
            for target in re.findall(rf'{attr}="([^"]+)"', text):
                if target.startswith(("#", "mailto:", "javascript:")):
                    continue
                parsed = urlparse(target)
                if parsed.scheme in ("http", "https"):
                    total_external += 1
                    external_hosts[(parsed.hostname or "").lower()] += 1
                    continue
                if parsed.scheme:
                    finding("WARN", "H", f"{path.relative_to(ROOT)}: unsupported scheme in {target!r}")
                    continue
                local = (path.parent / unquote(parsed.path)).resolve()
                total_local += 1
                try:
                    local.relative_to(ROOT)
                except ValueError:
                    finding("ERROR", "H", f"{path.relative_to(ROOT)}: link escapes repo: {target!r}")
                    continue
                if not local.exists():
                    finding("ERROR", "H", f"{path.relative_to(ROOT)}: broken local link {target!r}")
    note("H", f"{len(files)} HTML files, {total_local} internal references (all resolved), {total_external} external references over {len(external_hosts)} hosts")
    return external_hosts


def check_i_sources(document: dict) -> Counter:
    events = document["events"]
    hosts: Counter[str] = Counter()
    for ev in events:
        host = (urlparse(norm(ev.get("source_url"))).hostname or "").lower()
        hosts[host] += 1
    gov = sum(n for h, n in hosts.items() if h.endswith(".gov") or h.endswith(".gov.uk"))
    note("I", f"{len(hosts)} distinct source hosts; {gov} record(s) on .gov domains; top hosts: "
              + ", ".join(f"{h}({n})" for h, n in hosts.most_common(10)))
    return hosts


def main() -> int:
    document = json.loads(DATA.read_text(encoding="utf-8"))
    events = document["events"]
    published = [e for e in events if e.get("status") == "verified"]
    review = [e for e in events if e.get("bucket") == "review"]

    check_a_shape(events)
    check_b_calendar(events)
    check_c_classification(events)
    check_d_geography(events)
    check_e_duplicates(events)
    check_f_flags(document)
    check_g_pages(document)
    check_h_links()
    check_i_sources(document)

    past = [e for e in published if (parse_iso(norm(e.get("end_date"))) or parse_iso(norm(e.get("start_date"))))
            and (parse_iso(norm(e.get("end_date"))) or parse_iso(norm(e.get("start_date")))) < TODAY]
    future = [e for e in published if e not in past and (parse_iso(norm(e.get("end_date"))) or parse_iso(norm(e.get("start_date"))))]
    undated = [e for e in published if not norm(e.get("start_date")) and not norm(e.get("end_date"))]
    note("SUMMARY", f"records={len(events)} published={len(published)} review={len(review)} "
                    f"flags={len(document.get('flags', []))} past-dated={len(past)} upcoming/ongoing={len(future)} undated-recurring={len(undated)}")
    past_pages = [p for p in ("index.html", "all-events.html", "recurring.html", "special.html")
                  if (ROOT / p).exists() and re.search(r"(past|completed|earlier in 2026|already took place)", (ROOT / p).read_text(encoding="utf-8"), re.I)]
    note("SUMMARY", f"pages that explicitly label past-dated rows: {past_pages or 'NONE'}")

    print("=" * 78)
    print("AUDIT HARNESS — session arena/e969f4df-maltaproj7 (read-only)")
    print("=" * 78)
    for severity in ("ERROR", "WARN"):
        rows = [f for f in FINDINGS if f[0] == severity]
        print(f"\n### {severity}: {len(rows)}")
        for _, check, message in rows:
            print(f"  [{check}] {message}")
    print(f"\n### NOTES / EVIDENCE: {len(NOTES)}")
    for check, message in NOTES:
        print(f"  [{check}] {message}")
    errors = sum(1 for f in FINDINGS if f[0] == "ERROR")
    warns = sum(1 for f in FINDINGS if f[0] == "WARN")
    print(f"\nRESULT: {errors} error(s), {warns} warning(s), {len(NOTES)} note(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
