#!/usr/bin/env python3
"""Reproducible data patch for session arena/56415e75-maltaproj7 (2026-10-18).

Applies only changes that were confirmed against a live official publisher page on
2026-10-18 by this session.  Nothing is inferred: every value carries the source
URL that stated it, either in the row's own source fields or in `notes`, and each
source is re-listed in research/verification-56415e75.md.

The patch is **idempotent and merge-aware**, because other sessions edit the same
file concurrently:

* field edits set a value only when it differs, and `note_append` text is appended
  only when it is not already present — a peer session's notes are never replaced;
* new rows are skipped when the id exists or when an equivalent row (same event,
  same start date) was already published by another session;
* new flags are skipped when the id exists or when a peer flag covering the same
  point is listed in `superseded_by`.

Run from the repository root:

    python3 research/patch-56415e75.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "events.json"

# --------------------------------------------------------------------------- #
# 1. Field corrections / fills on existing published rows
#    `set`   -> value is written when different
#    `append`-> sentence is appended to `notes` when not already present
# --------------------------------------------------------------------------- #
FIELD_EDITS: dict[str, dict] = {
    # Live re-check 2026-10-18 of https://www.litquake.org/litcrawl and the
    # organizer's own schedule instance https://litcrawlsf2026.sched.com/
    "lit-crawl-sf-2026": {
        "set": {
            "time_text": "5:00\u20139:00 p.m.; individual Lit Crawl programs 6:30\u20137:30 p.m.",
            "admission": "Free; no RSVP required",
        },
        "append": (
            " Re-checked 2026-10-18 (arena/56415e75) against the organizer's own schedule instance "
            "(litcrawlsf2026.sched.com, linked from litquake.org/litcrawl): \u201cLit Crawl San Francisco "
            "is a massive, one-night literary pub crawl through San Francisco\u2019s Mission District on "
            "Saturday, October 24th from 5:00-9:00pm\u201d and \u201cNo RSVPs are necessary, just show up! "
            "Seating + space are first come, first serve.\u201d The crawl window is therefore published "
            "alongside the 6:30\u20137:30 p.m. per-program slot; see flag-litcrawl-suggested-donation."
        ),
    },
    # Live re-check 2026-10-18 of https://gdconf.com/passes-pricing/
    "gdc-festival-of-gaming-2027": {
        "set": {
            "admission": (
                "Early Rate through Fri Dec 11, 2026: Festival pass $549; Game Changer $1,249; "
                "Indie / Start-Up / Academic $299; Festival Hall only $175; Business Hall only $125; "
                "1-Day Career $125. Super Early Rate (Festival $499) closed Oct 9, 2026; regular, "
                "final and onsite rates are higher."
            ),
        },
        "append": (
            " Re-checked 2026-10-18 (arena/56415e75): the page now asks visitors to \u201cRegister by "
            "December 11 at 11:59pm PT to lock in our Early Rate\u201d, and its rate table reads Super Early "
            "(Fri Oct 9, 2026) $1,149 / $499 / $299 / $149 / $99 / $99, Early (Fri Dec 11, 2026) $1,249 / "
            "$549 / $299 / $175 / $125 / $125, Regular (Fri Feb 5, 2027) $1,449 / $649 / $349 / $199 / "
            "$149 / $149, Final (Fri Feb 26, 2027) $1,649 / $749 / $399 / $249 / $199 / $199, Onsite "
            "(Mar 5, 2027) $1,849 / $849 / $399 / $299 / $249 / $249 across Game Changer / Festival / "
            "Indie-Start-Up-Academic / Festival Hall only / Business Hall only / 1-Day Career."
        ),
    },
    # Official event page / In-Person Events index state "8 Mar 2026 \u2022 3pm to 8pm".
    "day-of-the-devs-sf-2026": {
        "set": {"time_text": "3:00\u20138:00 p.m."},
        "append": (
            " Time filled 2026-10-18 (arena/56415e75) from the organizer's In-Person Events index, which "
            "lists \u201c8 Mar 2026 \u2022 3pm to 8pm \u2022 San Francisco, CA\u201d and states \u201cAdmission is always free, "
            "for developers and players alike, and open to all ages.\u201d"
        ),
    },
    # Organizer's own 2026 press release corroborates the free season and its dates.
    "ybg-festival-2026": {
        "set": {},
        "append": (
            " Corroborated 2026-10-18 (arena/56415e75) directly against the organizer: the festival's own "
            "2026 season press release "
            "(https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf) is readable and states "
            "\u201cOver 100+ Free Performances from May to November in Downtown San Francisco\u201d, a season "
            "opener on \u201cSaturday, May 9, 2:00pm\u201d, and the October programmes (Oct 10 Follow the Music, "
            "Oct 11 Dance Day, Oct 12 Indigenous Peoples Day, Oct 17 Joe Bataan, Oct 24 Afro-Filipino Jazz "
            "Project, Oct 31 26th Annual Halloween Hoopla). The November 13 end date remains sourced from "
            "the SF Travel release rather than from the organizer, whose release says only \u201cfrom May to "
            "November\u201d with \u201cNOVEMBER programs to be announced\u201d."
        ),
    },
    # Cost fill from the organizer's own site; SFMTA stays the date/hours source.
    "from-the-e-night-market-2026-10-23": {
        "set": {
            "admission": "Free",
            "admission_source_url": "https://www.fromtheesf.com/",
            "organizer": "From the E Excelsior Night Market",
        },
        "append": (
            " Cost and organizer filled 2026-10-18 (arena/56415e75) from the organizer's own site "
            "(fromtheesf.com), which describes the programme as \u201cfree community fun\u201d and lists \u201cFrom "
            "the E: Fall Festival Night Market \u2014 Fri, Oct 23 \u2014 Ocean Ave & Mission St \u2014 \u2728\ufe0f FREE "
            "COMMUNITY FUN! \u2728\ufe0f\u201d. SFMTA remains the source for the date, hours and street footprint."
        ),
    },
}

# --------------------------------------------------------------------------- #
# 2. New verified rows (all free, all city-only, all from an official publisher)
#    `dedupe_names` lists titles another session may have used for the same event.
# --------------------------------------------------------------------------- #
NEW_EVENTS: list[dict] = [
    {
        "id": "ybgf-afro-filipino-jazz-project-2026",
        "dedupe_names": ["afro-filipino jazz project"],
        "event": {
            "id": "ybgf-afro-filipino-jazz-project-2026",
            "name": "Afro-Filipino Jazz Project (Yerba Buena Gardens Festival)",
            "bucket": "special",
            "cadence": "single-date",
            "category": "Music & performing arts",
            "date_text": "Saturday, October 24, 2026",
            "start_date": "2026-10-24",
            "end_date": "2026-10-24",
            "time_text": "2:00 p.m.",
            "location": "Yerba Buena Gardens, San Francisco",
            "organizer": "Yerba Buena Gardens Festival",
            "admission": "Free",
            "source_url": "https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf",
            "source_label": "Yerba Buena Gardens Festival 2026 season press release (official)",
            "source_authority": "Official organizer",
            "status": "verified",
            "review_reason": "",
            "notes": (
                "The organizer's 2026 season press release (read 2026-10-18) lists \u201cAfro-Filipino Jazz "
                "Project, Saturday, October 24, 2:00pm\u201d among the free outdoor programmes of the 26th "
                "season, which the same release describes as \u201cOver 100+ Free Performances from May to "
                "November in Downtown San Francisco\u201d. The 2026 season itself is catalogued separately as "
                "\u201cYBG Festival (Yerba Buena Gardens Festival)\u201d."
            ),
        },
    },
    {
        "id": "ybgf-halloween-hoopla-2026",
        "dedupe_names": ["halloween hoopla"],
        "event": {
            "id": "ybgf-halloween-hoopla-2026",
            "name": "Halloween Hoopla (Yerba Buena Gardens Festival, 26th annual)",
            "bucket": "recurring",
            "cadence": "annual",
            "category": "Community & culture",
            "date_text": "Saturday, October 31, 2026 (26th annual)",
            "start_date": "2026-10-31",
            "end_date": "2026-10-31",
            "time_text": "Noon",
            "location": "Yerba Buena Gardens, San Francisco",
            "organizer": "Yerba Buena Gardens Festival",
            "admission": "Free",
            "source_url": "https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf",
            "source_label": "Yerba Buena Gardens Festival 2026 season press release (official)",
            "source_authority": "Official organizer",
            "status": "verified",
            "review_reason": "",
            "notes": (
                "The organizer's 2026 season press release (read 2026-10-18) lists \u201c26th Annual Halloween "
                "Hoopla, Saturday, October 31, Noon\u201d as part of the free 26th season; the edition number "
                "stated by the organizer is the basis for the annual cadence. No end time is stated, so "
                "only the noon start is published."
            ),
        },
    },
    {
        "id": "sf-tech-week-2026",
        "dedupe_names": ["sf tech week"],
        "event": {
            "id": "sf-tech-week-2026",
            "name": "SF Tech Week \u2014 San Francisco Public Library programs (2026)",
            "bucket": "recurring",
            "cadence": "annual",
            "category": "Technology, AI & gaming",
            "date_text": "May 9\u201316, 2026",
            "start_date": "2026-05-09",
            "end_date": "2026-05-16",
            "time_text": "",
            "location": "San Francisco Public Library, Main Library, 100 Larkin Street, San Francisco",
            "organizer": "San Francisco Public Library",
            "admission": "Free",
            "source_url": "https://sfpl.org/locations/main-library/bridge-main-5th-floor/sf-tech-week",
            "source_label": "San Francisco Public Library \u2014 SF Tech Week program page",
            "source_authority": "Government source",
            "status": "verified",
            "review_reason": "",
            "notes": (
                "SFPL's Tech Week program page (read 2026-10-18) states \u201cMay 9-16, 2026 \u2026 Take your next "
                "step with technology during Tech Week \u2026 All programs are free\u201d and notes that \u201cTech Week "
                "is produced by a coalition of Bay Area organizations\u201d. The library's own release "
                "(sfpl.org/releases/2026-04-24/level-tech-week-san-francisco-public-library) describes it "
                "as annual: \u201cFrom May 9\u201316, San Francisco Public Library (SFPL) is offering over 30 free "
                "workshops for its annual Tech Week.\u201d SFPL's events pages state that \u201call programs and "
                "events are free and open to the public\u201d. Individual workshop times are not published here."
            ),
        },
    },
    {
        "id": "from-the-e-harvest-night-market-2026-11-20",
        "dedupe_names": ["harvest night market"],
        "event": {
            "id": "from-the-e-harvest-night-market-2026-11-20",
            "name": "From the E: Harvest Night Market (Excelsior)",
            "bucket": "recurring",
            "cadence": "monthly",
            "category": "Food & markets",
            "date_text": "Friday, November 20, 2026",
            "start_date": "2026-11-20",
            "end_date": "2026-11-20",
            "time_text": "",
            "location": "Ocean Avenue & Mission Street, Excelsior, San Francisco",
            "organizer": "From the E Excelsior Night Market",
            "admission": "Free",
            "source_url": "https://www.fromtheesf.com/",
            "source_label": "From the E Excelsior Night Market official site",
            "source_authority": "Official organizer",
            "status": "verified",
            "review_reason": "",
            "notes": (
                "The organizer's site (read 2026-10-18) lists \u201cFrom the E: Harvest Night Market \u2014 Fri, "
                "Nov 20 \u2014 Ocean Ave & Mission St \u2014 \u2728\ufe0f FREE COMMUNITY FUN! \u2728\ufe0f\u201d and describes the "
                "programme as \u201cfree community fun\u201d. Hours are not published for this edition, so the time "
                "field is left blank rather than borrowed from the organizer's general monthly wording "
                "(\u201cthe second Saturday of the month from 5pm-10pm\u201d), which does not match a Friday date. "
                "The October 23, 2026 edition is catalogued separately from the SFMTA travel update."
            ),
        },
    },
]

# --------------------------------------------------------------------------- #
# 3. New field-level flags (irregularities found during this session's pass)
#    `superseded_by` names peer flags that already cover the same point.
# --------------------------------------------------------------------------- #
NEW_FLAGS: list[dict] = [
    {
        "id": "flag-litcrawl-suggested-donation",
        "event_id": "lit-crawl-sf-2026",
        "event": "Lit Crawl SF",
        "superseded_by": [],
        "issue": (
            "The organizer's festival-schedule listing for Lit Crawl "
            "(litquake2026.sched.com/event/2WFLw/lit-crawl-sf) is labelled \u201cFREE, $10-15 suggested "
            "donation\u201d, while the Lit Crawl programme page and the Lit Crawl schedule instance both "
            "present the night as free with no RSVP. The row publishes the cost label \u201cFree\u201d and records "
            "the suggested-donation wording here rather than treating the night as ticketed."
        ),
        "sources": [
            {"label": "Lit Crawl SF official page", "url": "https://www.litquake.org/litcrawl"},
            {"label": "Lit Crawl SF 2026 official schedule", "url": "https://litcrawlsf2026.sched.com/"},
            {
                "label": "Litquake 2026 festival schedule \u2014 Lit Crawl listing",
                "url": "https://litquake2026.sched.com/event/2WFLw/lit-crawl-sf",
            },
        ],
        "disposition": "Cost label stays Free with the donation wording documented. Nonblocking.",
    },
    {
        "id": "flag-sunday-streets-route-conflict",
        "event_id": "sunday-streets-excelsior-2026",
        "event": "Sunday Streets Excelsior \u2014 2026 season finale",
        "superseded_by": [],
        "issue": (
            "The organizer states the October 18, 2026 route as \u201cMission Street between Geneva Avenue and "
            "Theresa Street\u201d, while the SF Recreation and Park Department calendar entry for the same "
            "date describes \u201cMobile Rec at Sunday Streets on Mission Street between Avalon Avenue and "
            "Geneva Avenue\u201d. The row follows the organizer's route; the city listing describes the Rec & "
            "Park activity location on the same closed corridor and is not treated as a second, different "
            "event."
        ),
        "sources": [
            {
                "label": "Sunday Streets Excelsior 2026 official event page",
                "url": "https://sundaystreetssf.com/sunday-streets-excelsior-2026/",
            },
            {
                "label": "SF Recreation and Park Department calendar",
                "url": "https://sfrecpark.org/Calendar.aspx",
            },
        ],
        "disposition": "Organizer route published; discrepancy documented. Nonblocking.",
    },
    {
        "id": "flag-sunday-streets-free-wording",
        "event_id": "sunday-streets-2026",
        "event": "Sunday Streets SF \u2014 2026 season",
        # arena/8c40d1c6-maltaproj7 filed the same point as flag-sundaystreets-free-wording.
        "superseded_by": ["flag-sundaystreets-free-wording"],
        "issue": (
            "The organizer's About page does not use the phrase \u201cfree admission\u201d; it states that the "
            "open-streets events offer \u201cfun, free activities provided by local nonprofits, community "
            "groups and small businesses\u201d on \u201ccar-free spaces for all to enjoy\u201d. The Free cost label "
            "rests on that wording rather than on an explicit no-admission statement."
        ),
        "sources": [
            {"label": "Sunday Streets SF \u2014 About", "url": "https://sundaystreetssf.com/about/"},
            {"label": "Sunday Streets SF \u2014 2026 season", "url": "https://sundaystreetssf.com/"},
        ],
        "disposition": "Free label retained with its exact source wording recorded. Nonblocking.",
    },
    {
        "id": "flag-from-the-e-general-hours-mismatch",
        "event_id": "from-the-e-harvest-night-market-2026-11-20",
        "event": "From the E: Harvest Night Market (Excelsior)",
        "superseded_by": [],
        "issue": (
            "The organizer's site describes the Excelsior Night Market as running \u201cthe second Saturday of "
            "the month from 5pm -10pm\u201d, but the 2026 editions it lists (August 21, September 18, October "
            "23, November 20) are Fridays and SFMTA publishes 4:30\u20138:30 p.m. for the October edition. The "
            "row therefore publishes no hours for the November 20 edition instead of reusing either "
            "wording."
        ),
        "sources": [
            {"label": "From the E Excelsior Night Market official site", "url": "https://www.fromtheesf.com/"},
            {
                "label": "SFMTA travel update \u2014 From the E Night Market, October 23, 2026",
                "url": "https://www.sfmta.com/travel-updates/e-night-market-friday-october-23-2026",
            },
        ],
        "disposition": "Time left blank and the conflict documented. Nonblocking.",
    },
]


def main() -> None:
    document = json.loads(DATA.read_text(encoding="utf-8"))
    events = document["events"]
    by_id = {event["id"]: event for event in events}
    names = {str(event.get("name", "")).lower() for event in events}

    changed: list[str] = []

    for event_id, edit in FIELD_EDITS.items():
        event = by_id.get(event_id)
        if event is None:
            print(f"skip (row absent): {event_id}")
            continue
        for field, value in edit.get("set", {}).items():
            if event.get(field) != value:
                event[field] = value
                changed.append(f"{event_id}.{field}")
        note = edit.get("append")
        if note:
            marker = note.strip().split(". ")[0][:60]
            if marker not in (event.get("notes") or ""):
                event["notes"] = ((event.get("notes") or "").rstrip() + note).strip()
                changed.append(f"{event_id}.notes")

    for entry in NEW_EVENTS:
        event = entry["event"]
        if event["id"] in by_id:
            print(f"skip (id exists): {event['id']}")
            continue
        if any(alias in " ".join(names) for alias in entry.get("dedupe_names", [])):
            print(f"skip (equivalent row published by another session): {event['id']}")
            continue
        events.append(dict(event))
        by_id[event["id"]] = events[-1]
        changed.append(f"+{event['id']}")

    existing_flags = {flag["id"] for flag in document["flags"]}
    for flag in NEW_FLAGS:
        if flag["id"] in existing_flags:
            print(f"skip (flag exists): {flag['id']}")
            continue
        superseded = [peer for peer in flag.get("superseded_by", []) if peer in existing_flags]
        if superseded:
            print(f"skip (superseded by {', '.join(superseded)}): {flag['id']}")
            continue
        if flag["event_id"] not in by_id:
            print(f"skip (event absent): {flag['id']} -> {flag['event_id']}")
            continue
        record = {k: v for k, v in flag.items() if k != "superseded_by"}
        record["event"] = by_id[flag["event_id"]].get("name", flag["event"])
        document["flags"].append(record)
        existing_flags.add(flag["id"])
        changed.append(f"+{flag['id']}")

    catalog = document["catalog"]
    attribution = "arena/56415e75-maltaproj7 official-source re-check and free-event coverage pass (2026-10-18)"
    if attribution not in (catalog.get("updated_by") or ""):
        catalog["updated_by"] = (catalog.get("updated_by") or "") + "; " + attribution
        changed.append("catalog.updated_by")
    catalog["as_of"] = "2026-10-18"

    # Preserve whatever indentation the file already uses (a peer session may have
    # re-serialised it) so this patch never produces a whole-file reformat diff.
    raw = DATA.read_text(encoding="utf-8")
    indent = 1
    for line in raw.splitlines()[1:4]:
        stripped = line.lstrip(" ")
        if stripped and stripped[0] in '"':
            indent = len(line) - len(stripped)
            break
    DATA.write_text(json.dumps(document, indent=indent, ensure_ascii=False) + "\n", encoding="utf-8")

    published = [e for e in events if e["status"] == "verified"]
    recurring = [e for e in published if e["bucket"] == "recurring"]
    special = [e for e in published if e["bucket"] == "special"]
    review = [e for e in events if e["status"] != "verified"]
    print("changed:", ", ".join(changed) if changed else "nothing (already applied)")
    print(
        f"published={len(published)} recurring={len(recurring)} special={len(special)} "
        f"review={len(review)} flags={len(document['flags'])}"
    )


if __name__ == "__main__":
    main()
