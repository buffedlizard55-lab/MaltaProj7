#!/usr/bin/env python3
"""Reproducible data patch for session arena/56415e75-maltaproj7 (2026-10-18).

Applies only the changes that were confirmed against a live official publisher
page on 2026-10-18 by this session.  Nothing here is inferred: every value has
the source URL that stated it recorded either in `notes` or in the new row's
own source fields, and each source is re-listed in
research/verification-56415e75.md.

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
# --------------------------------------------------------------------------- #
FIELD_EDITS: dict[str, dict[str, str]] = {
    # Live re-check 2026-10-18 of https://www.litquake.org/litcrawl and the
    # organizer's own schedule instance https://litcrawlsf2026.sched.com/
    "lit-crawl-sf-2026": {
        "time_text": "5:00\u20139:00 p.m.; individual Lit Crawl programs 6:30\u20137:30 p.m.",
        "admission": "Free; no RSVP required",
        "notes": (
            "Organizer calls Lit Crawl the annual Litquake Festival finale. "
            "litquake.org/litcrawl (re-fetched 2026-10-18) states \u201cOCTOBER 24, 2026\u201d, "
            "\u201cthe world\u2019s largest free pop-up literary event\u201d and \u201call programs from "
            "6:30\u20147:30 PM\u201d. The organizer's own schedule instance "
            "(litcrawlsf2026.sched.com, linked from that page and fetched 2026-10-18) "
            "states \u201cSaturday, October 24th from 5:00-9:00pm\u201d and \u201cNo RSVPs are "
            "necessary, just show up! Seating + space are first come, first serve.\u201d "
            "Pointer-style time text removed per correction request from session "
            "arena/e969f4df-maltaproj7. See flag-litcrawl-suggested-donation."
        ),
    },
    # Live re-check 2026-10-18 of https://gdconf.com/passes-pricing/
    "gdc-festival-of-gaming-2027": {
        "admission": (
            "Early Rate through Fri Dec 11, 2026: Festival pass $549; Game Changer $1,249; "
            "Indie / Start-Up / Academic $299; Festival Hall only $175; Business Hall only $125; "
            "1-Day Career $125. Super Early Rate (Festival $499) closed Oct 9, 2026; regular, "
            "final and onsite rates are higher."
        ),
        "notes": (
            "Header states 'March 1-5, 2027 \u2014 Moscone Center, San Francisco, CA'. "
            "Passes & Pricing page re-fetched 2026-10-18: the page now asks visitors to "
            "\u201cRegister by December 11 at 11:59pm PT to lock in our Early Rate\u201d and its rate "
            "table lists Super Early (deadline Fri Oct 9, 2026) $1,149 / $499 / $299 / $149 / $99 / "
            "$99, Early (deadline Fri Dec 11, 2026) $1,249 / $549 / $299 / $175 / $125 / $125, "
            "Regular (Fri Feb 5, 2027) $1,449 / $649 / $349 / $199 / $149 / $149, Final "
            "(Fri Feb 26, 2027) $1,649 / $749 / $399 / $249 / $199 / $199 and Onsite "
            "(Mar 5, 2027) $1,849 / $849 / $399 / $299 / $249 / $249 for Game Changer / Festival / "
            "Indie-Start-Up-Academic / Festival Hall only / Business Hall only / 1-Day Career. "
            "See flag-gdc-2027-pass-deadlines."
        ),
    },
    # Official event page states "8 Mar 2026 \u2022 3pm to 8pm" (organizer's In-Person
    # Events index and event page, re-checked 2026-10-18).
    "day-of-the-devs-sf-2026": {
        "time_text": "3:00\u20138:00 p.m.",
        "notes": (
            "Official event page: \u201cDay of the Devs returns to the Midway in San Francisco for the "
            "2026 In-Person Celebration: San Francisco Edition!\u201d The organizer's In-Person Events "
            "index lists \u201c8 Mar 2026 \u2022 3pm to 8pm \u2022 San Francisco, CA\u201d and \u201c67 Games shown\u201d, and "
            "states \u201cAdmission is always free, for developers and players alike, and open to all "
            "ages.\u201d Location block: \u201cThe Midway, 900 Marin Street, San Francisco, 94124, CA\u201d. "
            "Time filled 2026-10-18 from that organizer listing. No 2027 edition is announced yet."
        ),
    },
    # Organizer's own 2026 press release corroborates the free season.
    "ybg-festival-2026": {
        "notes": (
            "The festival's own homepage was behind a reCAPTCHA at the 2026-10-18 re-check; "
            "SF Travel, the City and County's official destination marketing organization, lists "
            "the free 2026 season at Yerba Buena Gardens and is the source of the November 13 "
            "season end date; see flag-ybg-2026-source-availability. The organizer's own 2026 season "
            "press release (https://ybgfestival.org/wp-content/uploads/2026/04/YBGF-2026-PR.pdf) "
            "independently confirms the 26th season of \u201cfree outdoor music, theater, circus, dance, "
            "poetry and children\u2019s programs\u201d opening Saturday, May 9 at 2:00pm with \u201cOver 100+ Free "
            "Performances from May to November\u201d. Individual program times are on the festival site."
        ),
    },
    # Official city calendar corroborates the Excelsior finale date and hours.
    "sunday-streets-2026": {
        "admission": "Free",
        "admission_source_url": "https://sundaystreetssf.com/about/",
        "notes": (
            "The source confirms four 2026 city-neighborhood events; times and routes vary by "
            "neighborhood. The organizer's About page states the programme runs on \u201ccar-free spaces "
            "for all to enjoy\u201d with \u201cfun, free activities provided by local nonprofits, community "
            "groups and small businesses\u201d (basis for the Free cost label \u2014 see "
            "flag-sunday-streets-free-wording). The October 18 Excelsior finale, 11 a.m.\u20134 p.m., is "
            "also listed by the San Francisco Recreation and Park Department calendar "
            "(sfrecpark.org/Calendar.aspx, fetched 2026-10-18) as \u201cMobile Rec at Sunday Streets \u2026 on "
            "Mission Street between Avalon Avenue and Geneva Avenue\u201d \u2014 see flag-sunday-streets-route-conflict."
        ),
    },
}

# --------------------------------------------------------------------------- #
# 2. New verified rows (all free, all city-only, all from an official publisher)
# --------------------------------------------------------------------------- #
NEW_EVENTS: list[dict] = [
    {
        "id": "sunday-streets-excelsior-2026-10-18",
        "name": "Sunday Streets \u2014 Excelsior Community Block Party (2026 season finale)",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Community & culture",
        "date_text": "Sunday, October 18, 2026",
        "start_date": "2026-10-18",
        "end_date": "2026-10-18",
        "time_text": "11:00 a.m.\u20134:00 p.m.",
        "location": "Mission Street between Geneva Avenue and Theresa Street, Excelsior, San Francisco",
        "organizer": "Sunday Streets SF (Livable City) with SFMTA and the City and County of San Francisco",
        "admission": "Free",
        "admission_source_url": "https://sundaystreetssf.com/about/",
        "source_url": "https://sundaystreetssf.com/sunday-streets-excelsior-2026/",
        "source_label": "Sunday Streets Excelsior 2026 official event page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Organizer's event page (fetched 2026-10-18): \u201cExcelsior Community Block Party \u2014 Mission "
            "Street between Geneva Avenue and Theresa Street \u2014 Sunday, October 18, 2026 \u2027 11 AM \u2013 4 PM\u201d "
            "and \u201cSunday Streets is excited to host the 2026 season finale in the Excelsior on Sunday, "
            "October 18 \u2026 nearly a mile of car-free streets\u201d. Cost basis: the organizer's About page "
            "describes \u201cfun, free activities provided by local nonprofits, community groups and small "
            "businesses\u201d (see flag-sunday-streets-free-wording). Date and hours independently listed by "
            "the SF Recreation and Park Department calendar (sfrecpark.org/Calendar.aspx). The 2026 "
            "season itself is catalogued separately as \u201cSunday Streets SF \u2014 2026 season\u201d."
        ),
    },
    {
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
            "The organizer's 2026 season press release lists \u201cAfro-Filipino Jazz Project, Saturday, "
            "October 24, 2:00pm\u201d among the free outdoor programmes of the 26th season, which the same "
            "release describes as \u201cOver 100+ Free Performances from May to November in Downtown San "
            "Francisco\u201d. The 2026 season is catalogued separately as \u201cYBG Festival (Yerba Buena Gardens "
            "Festival)\u201d."
        ),
    },
    {
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
            "The organizer's 2026 season press release lists \u201c26th Annual Halloween Hoopla, Saturday, "
            "October 31, Noon\u201d as part of the free 26th season; the edition number stated by the "
            "organizer is the basis for the annual cadence. An end time is not stated in the release, so "
            "only the noon start is published."
        ),
    },
    {
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
            "SFPL's Tech Week program page states \u201cMay 9-16, 2026 \u2026 Take your next step with technology "
            "during Tech Week \u2026 All programs are free\u201d and notes that \u201cTech Week is produced by a "
            "coalition of Bay Area organizations\u201d. The library's own release "
            "(sfpl.org/releases/2026-04-24/level-tech-week-san-francisco-public-library) describes the "
            "annual programme: \u201cFrom May 9\u201316, San Francisco Public Library (SFPL) is offering over 30 "
            "free workshops for its annual Tech Week.\u201d SFPL's events pages state that \u201call programs and "
            "events are free and open to the public\u201d. Individual workshop times are not published here."
        ),
    },
]

# --------------------------------------------------------------------------- #
# 3. New field-level flags (irregularities found during this session's pass)
# --------------------------------------------------------------------------- #
NEW_FLAGS: list[dict] = [
    {
        "id": "flag-litcrawl-suggested-donation",
        "event_id": "lit-crawl-sf-2026",
        "event": "Lit Crawl SF",
        "issue": (
            "The organizer's festival-schedule listing for Lit Crawl "
            "(litquake2026.sched.com/event/2WFLw/lit-crawl-sf) is labelled \u201cFREE, $10-15 suggested "
            "donation\u201d, while the Lit Crawl programme page and the Lit Crawl schedule instance both "
            "present the night as free with no RSVP. The row publishes the cost label \u201cFree\u201d and "
            "records the suggested-donation wording here rather than treating the night as ticketed."
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
        "event_id": "sunday-streets-excelsior-2026-10-18",
        "event": "Sunday Streets \u2014 Excelsior Community Block Party (2026 season finale)",
        "issue": (
            "The organizer states the October 18, 2026 route as \u201cMission Street between Geneva Avenue "
            "and Theresa Street\u201d, while the SF Recreation and Park Department calendar entry for the "
            "same date describes \u201cMobile Rec at Sunday Streets on Mission Street between Avalon Avenue "
            "and Geneva Avenue\u201d. The row follows the organizer's route; the city listing describes the "
            "Rec & Park activity location on the same closed corridor and is not treated as a second, "
            "different event."
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
]


def main() -> None:
    document = json.loads(DATA.read_text(encoding="utf-8"))
    events = document["events"]
    by_id = {event["id"]: event for event in events}

    for event_id, edits in FIELD_EDITS.items():
        if event_id not in by_id:
            raise SystemExit(f"missing event for edit: {event_id}")
        by_id[event_id].update(edits)

    for event in NEW_EVENTS:
        if event["id"] in by_id:
            raise SystemExit(f"duplicate event id: {event['id']}")
        events.append(event)

    existing_flags = {flag["id"] for flag in document["flags"]}
    for flag in NEW_FLAGS:
        if flag["id"] in existing_flags:
            raise SystemExit(f"duplicate flag id: {flag['id']}")
        document["flags"].append(flag)

    catalog = document["catalog"]
    catalog["as_of"] = "2026-10-18"
    catalog["updated_by"] = catalog.get("updated_by", "") + (
        "; arena/56415e75-maltaproj7 official-source re-check and free-event coverage pass (2026-10-18)"
    )

    DATA.write_text(json.dumps(document, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    published = [e for e in events if e["status"] == "verified"]
    recurring = [e for e in published if e["bucket"] == "recurring"]
    special = [e for e in published if e["bucket"] == "special"]
    review = [e for e in events if e["status"] != "verified"]
    print(
        f"published={len(published)} recurring={len(recurring)} special={len(special)} "
        f"review={len(review)} flags={len(document['flags'])}"
    )


if __name__ == "__main__":
    main()
