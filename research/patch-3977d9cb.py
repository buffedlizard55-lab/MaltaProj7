#!/usr/bin/env python3
"""Reproducible data patch for session arena/3977d9cb-maltaproj7 (2026-10-18).

Every value below was read from an official source page fetched on 2026-10-18 and is
quoted in `notes`, in `research/reverification-3977d9cb.md`, or in the flag text.
Nothing is inferred: where the official page published no price, `admission` stays
blank and a flag records the gap.

Re-based 2026-10-18 on the merged main (commit 2f21f34) after three parallel
sessions landed PRs #27—#33: the four records and six flags below are still absent from
main, while two flags this session had drafted were DROPPED as duplicates of peer work
already on main (flag-registration-only-cost-class — main's classifier already returns
"not-stated" for registration-only wording and main carries flag-diplos-price-unstated,
flag-nutcracker-price-unstated and flag-cornhole-cost-unstated; flag-dual-edition-cost-evidence
— main carries flag-italian-heritage-2027). Both observations remain recorded as R3 and R11
in research/review-3977d9cb.md. Integration also added a fifth published row (From the E:
Holiday Night Market, Fri Dec 11 2026) read from the organizer's own event page, plus
flag-from-the-e-cadence-inconsistency.

Counts move from the merged baseline: published 158 — 162 (recurring 101 — 102,
special 57 — 60), review 16 — 17, flags 44 — 51.

Run:  python3 research/patch-3977d9cb.py     (idempotent)
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "events.json"

NEW_PUBLISHED = [
    {
        "id": "hunters-point-shipyard-fall-open-studios-2026",
        "name": "Hunters Point Shipyard Fall Open Studios",
        "bucket": "recurring",
        "cadence": "seasonal",
        "category": "Community & culture",
        "date_text": "October 17–18, 2026",
        "start_date": "2026-10-17",
        "end_date": "2026-10-18",
        "time_text": "11:00 a.m.–6:00 p.m.",
        "location": "Hunters Point Shipyard, 451 Galvez Ave, and Islais Creek Studios, 1 Rankin St, San Francisco",
        "organizer": "Shipyard Trust for the Arts",
        "admission": "Free admission & parking (optional supporter ticket)",
        "admission_source_url": "https://www.thepointart.com/hunters-point-shipyard",
    "admission_source_url": "https://www.thepointart.com/hunters-point-shipyard",
        "source_url": "https://www.eventbrite.com/e/shipyard-open-studios-fall-2026-registration-1992234233221",
        "source_label": "Shipyard Trust for the Arts — official Shipyard Open Studios Fall 2026 listing",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/3977d9cb-maltaproj7). Official organizer listing states "
            "\"October 17–18, 2026 · 11 AM–6 PM\", \"Hunters Point Shipyard & Islais Creek Studios\", "
            "\"Free admission & parking — reserve your free ticket below\", and \"Twice a year, one of "
            "San Francisco's most fascinating hidden landmarks throws open its doors\" — the twice-yearly "
            "cadence is the source's own wording; no further recurrence is inferred. Addresses from the same "
            "page: main shipyard site 451 Galvez Ave, San Francisco, CA 94124; satellite studios 1 Rankin St, "
            "San Francisco. An optional paid \"Supporter Ticket\" is offered at registration and every dollar "
            "\"goes directly to keeping this weekend free and open to all\"; admission itself is free. "
            "Corroborated by The Point's official Hunters Point Shipyard page (\"Fall Open Studio 2026 • "
            "Saturday & Sunday, October 17 & 18, 2026 ... Free admission and free parking\") because "
            "shipyardartists.com served an interstitial page at verification time — "
            "see flag-shipyard-open-studios-source."
        ),
    },
    {
        "id": "open-weight-debate-night-2026",
        "name": "Open Source AI Week — Open Weight Debate Night",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Technology, AI & gaming",
        "date_text": "Monday, October 19, 2026",
        "start_date": "2026-10-19",
        "end_date": "2026-10-19",
        "time_text": "5:00–9:00 p.m.",
        "location": "GitHub Office, 88 Colin P. Kelly Jr. Street, San Francisco",
        "organizer": "Open Source AI Week (Open Intelligence Foundation) with GitHub and Microsoft Azure",
        "admission": "",
        "source_url": "https://opensourceaiweek.com/the-debates/",
        "source_label": "Open Source AI Week — The Debates official event page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/3977d9cb-maltaproj7). Official event page states \"Date: Monday, "
            "October 19, 2026\", \"Time: 5:00 PM – 9:00 PM\", \"Where: GitHub Office — 88 Colin P. Kelly Jr. "
            "Street, San Francisco, CA 94107\", \"Capacity: Limited to 250 — reserve early\", hosted by "
            "GitHub, Microsoft Azure and the Open Intelligence Foundation, with confirmed debaters including "
            "Ion Stoica (UC Berkeley, Databricks, Anyscale) and Percy Liang (Stanford, Marin, Together AI). "
            "Neither this page nor the official registration listing (https://luma.com/592fcwx2, which shows "
            "\"Approval Required\") publishes a price, so admission is left blank rather than inferred — "
            "see flag-open-source-ai-cost. First edition observed; the source states no recurrence, so none "
            "is inferred."
        ),
    },
    {
        "id": "open-source-ai-awards-night-2026",
        "name": "Open Source AI Awards Night",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Technology, AI & gaming",
        "date_text": "Friday, October 23, 2026",
        "start_date": "2026-10-23",
        "end_date": "2026-10-23",
        "time_text": "5:00–9:00 p.m.",
        "location": "Founder's Inc, 2 Marina Blvd B300, San Francisco",
        "organizer": "Open Source AI Week (Founders Inc, OSS4AI, Open Intelligence Foundation)",
        "admission": "",
        "source_url": "https://opensourceaiweek.com/open-source-ai-awards/",
        "source_label": "Open Source AI Week — Open Source AI Awards official event page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/3977d9cb-maltaproj7). Official event page states \"Date: Friday, "
            "October 23, 2026 — awards night\", \"Time: 5:00 PM – 9:00 PM\", \"Where: Founder's Inc — "
            "2 Marina Blvd B300, San Francisco, CA 94123\". The official registration listing "
            "(https://luma.com/7ebvz0oq) carries the same date but \"5:00 PM - 10:00 PM PDT\" and \"Approval "
            "Required\"; the row keeps the official event page's 5:00–9:00 p.m. and the conflict is recorded "
            "in flag-open-source-ai-awards-time. No price is published on either page, so admission is left "
            "blank rather than inferred — see flag-open-source-ai-cost."
        ),
    },
    {
        "id": "from-the-e-holiday-night-market-2026-12-11",
        "name": "From the E: Holiday Night Market (Excelsior)",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Friday, December 11, 2026",
        "start_date": "2026-12-11",
        "end_date": "2026-12-11",
        "time_text": "4:30—8:30 p.m.",
        "location": "Ocean Avenue & Mission Street, Excelsior, San Francisco",
        "organizer": "From the E Excelsior Night Market",
        "admission": "Free",
        "source_url": "https://www.fromtheesf.com/events/from-the-e-holiday-night-market",
        "source_label": "From the E — Holiday Night Market official event page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/3977d9cb-maltaproj7) during final integration. The organizer's event "
            "page reads \"From the E: Holiday Night Market — Fri, Dec 11 — Ocean Ave & Mission St — "
            "✨️ FREE COMMUNITY FUN! ✨️\" and gives \"Time & Location: Dec 11, 2026, 4:30 PM — 8:30 PM; "
            "Ocean Ave & Mission St, San Francisco, CA 94112, USA\", with an RSVP link and \"Registration "
            "closes Dec 11, 2026, 7:00 PM\" (an RSVP is not an admission charge). The organizer's homepage "
            "lists three dated 2026 editions (Fall Festival Oct 23, Harvest Nov 20, Holiday Dec 11) but the "
            "event page states no recurrence rule, so cadence is recorded as single-date rather than inferred "
            "— see flag-from-the-e-cadence-inconsistency. The Oct 23 and Nov 20 editions were catalogued by "
            "arena/5e333a6e-maltaproj7 and arena/56415e75-maltaproj7."
        ),
    },
]

NEW_REVIEW = [
    {
        "id": "open-source-ai-week-2026",
        "name": "Open Source AI Week 2026",
        "bucket": "review",
        "cadence": "",
        "category": "Technology, AI & gaming",
        "date_text": "October 16–25, 2026",
        "start_date": "2026-10-16",
        "end_date": "2026-10-25",
        "time_text": "",
        "location": "San Francisco Bay Area — flagship events in San Francisco, other events outside the city",
        "organizer": "Open Intelligence Foundation",
        "admission": "",
        "source_url": "https://opensourceaiweek.com/",
        "source_label": "Open Source AI Week official site",
        "source_authority": "Official organizer",
        "status": "partial_sf_program",
        "review_reason": (
            "Bay Area–wide decentralized program rather than a single city-only event: the official site "
            "describes \"Ten days · October 16-25, 2026 · San Francisco Bay Area\" with 66 events across the "
            "Bay Area and 200+ participating organizations, and its calendar includes events outside the city "
            "(for example the MITAI Conference at the Computer History Museum in Mountain View). Held out of "
            "the city-only tables; its San Francisco flagship programs are catalogued individually as the Open "
            "Weight Debate Night (October 19, 2026) and the Open Source AI Awards Night (October 23, 2026). "
            "No price is published for the week itself, so no cost is asserted."
        ),
        "notes": (
            "Added 2026-10-18 (arena/3977d9cb-maltaproj7) so this week's AI programming is visible without "
            "asserting city-only scope. Official flagship pages: "
            "https://opensourceaiweek.com/the-debates/ and "
            "https://opensourceaiweek.com/open-source-ai-awards/."
        ),
    },
]

NEW_FLAGS = [
    {
        "id": "flag-open-source-ai-cost",
        "event_id": "open-weight-debate-night-2026",
        "event": "Open Source AI Week — Open Weight Debate Night; Open Source AI Awards Night",
        "issue": (
            "The official Open Source AI Week event pages publish date, time, venue and capacity for both San "
            "Francisco flagship programs but state no price, and the official registration listings show "
            "\"Approval Required\" / \"Request to Join\" with no ticket price. Attendance may well be free, but "
            "no official page says so, so the cost cell reads \"Not stated\" on both rows instead of being "
            "filled in with an assumption."
        ),
        "sources": [
            {"label": "Official event page — The Debates (GitHub Office, SF)", "url": "https://opensourceaiweek.com/the-debates/"},
            {"label": "Official event page — Open Source AI Awards (Founder's Inc, SF)", "url": "https://opensourceaiweek.com/open-source-ai-awards/"},
            {"label": "Official registration listing — Debate Night (Luma, approval required)", "url": "https://luma.com/592fcwx2"},
            {"label": "Official registration listing — Awards Night (Luma, approval required)", "url": "https://luma.com/7ebvz0oq"},
        ],
        "disposition": (
            "Both rows published with the cost left blank (\"Not stated\") and listed on the cost-not-stated "
            "register; they are kept out of the free-events main section until an official page states a cost. "
            "Nonblocking."
        ),
    },
    {
        "id": "flag-open-source-ai-awards-time",
        "event_id": "open-source-ai-awards-night-2026",
        "event": "Open Source AI Awards Night",
        "issue": (
            "Conflicting official times for the same event: the organizer's event page states \"Time: 5:00 PM – "
            "9:00 PM\" while the organizer's own registration listing states \"5:00 PM - 10:00 PM PDT\" for "
            "Friday, October 23, 2026."
        ),
        "sources": [
            {"label": "Official event page (5:00–9:00 PM)", "url": "https://opensourceaiweek.com/open-source-ai-awards/"},
            {"label": "Official registration listing (5:00–10:00 PM PDT)", "url": "https://luma.com/7ebvz0oq"},
        ],
        "disposition": (
            "Row keeps the event-page value (5:00–9:00 p.m.); the one-hour conflict is recorded here for manual "
            "review rather than averaged or guessed. Nonblocking."
        ),
    },
    {
        "id": "flag-shipyard-open-studios-source",
        "event_id": "hunters-point-shipyard-fall-open-studios-2026",
        "event": "Hunters Point Shipyard Fall Open Studios",
        "issue": (
            "The lead organizer's own domain (shipyardartists.com) returned an interstitial \"Please wait …\" "
            "page when fetched on 2026-10-18, so it could not be used as the row's source link. The dates, "
            "hours, venues and \"Free admission & parking\" wording were instead read from the organizer's "
            "official Eventbrite listing and corroborated by The Point's official Hunters Point Shipyard page "
            "(\"Fall Open Studio 2026 • Saturday & Sunday, October 17 & 18, 2026 ... Free admission and free "
            "parking\"), a collaborating studio organization."
        ),
        "sources": [
            {"label": "Official organizer listing (Shipyard Trust for the Arts, Eventbrite)", "url": "https://www.eventbrite.com/e/shipyard-open-studios-fall-2026-registration-1992234233221"},
            {"label": "The Point — Hunters Point Shipyard (corroborating official page)", "url": "https://www.thepointart.com/hunters-point-shipyard"},
            {"label": "shipyardartists.com — served an interstitial page at check time", "url": "https://www.shipyardartists.com/shipyard-open-studios/"},
        ],
        "disposition": (
            "Row published from the organizer's official listing with a corroborating official page; re-point "
            "the source link to shipyardartists.com when that domain serves content again. Nonblocking."
        ),
    },
    {
        "id": "flag-hsb-2027-dates-unconfirmed",
        "event_id": "hardly-strictly-bluegrass-2026",
        "event": "Hardly Strictly Bluegrass",
        "issue": (
            "Secondary aggregators already publish 2027 dates for this free festival (Music Festival Wizard and "
            "JamBase both list October 8–10, 2027 in Golden Gate Park), but the official festival site fetched "
            "on 2026-10-18 — both the home page and the row's own 2026 info/FAQ page — still presents the 2026 "
            "edition (October 2–4, 2026) and publishes no 2027 dates or lineup. The 2027 dates therefore rest on non-official sources only."
        ),
        "sources": [
            {"label": "Official festival site home page (2026 edition; no 2027 dates published)", "url": "https://hardlystrictlybluegrass.com/"},
            {"label": "Official 2026 info & FAQ page (row source)", "url": "https://hardlystrictlybluegrass.com/info-faq-2026/"},
            {"label": "Music Festival Wizard listing claiming Oct 8–10, 2027 (not official)", "url": "https://www.musicfestivalwizard.com/festivals/hardly-strictly-bluegrass-2027/"},
            {"label": "JamBase listing claiming Oct 8–10, 2027 (not official)", "url": "https://www.jambase.com/festival/hardly-strictly-bluegrass-2027"},
        ],
        "disposition": (
            "No 2027 row added and the existing 2026 row's dates are unchanged; re-check the official site when "
            "the 2027 edition is announced. Nonblocking."
        ),
    },
    {
        "id": "flag-free-gaming-coverage-gap",
        "event_id": "day-of-the-devs-sf-2026",
        "event": "Free gaming events — coverage gap as of 2026-10-18",
        "issue": (
            "The brief asks for free gaming events first, but no upcoming in-person free gaming event inside the "
            "city could be verified from an official source on 2026-10-18. The catalog's free gaming row (Day of "
            "the Devs — San Francisco Edition, March 8, 2026, The Midway) is a completed edition. Day of the "
            "Devs' official site states \"Our programs are provided entirely for free\" and \"We want Day of the "
            "Devs to always remain FREE to everyone\", but the next program it announces is an online digital "
            "showcase tied to The Game Awards, which is not a San Francisco in-person event; no new SF edition "
            "is announced. GDC Festival of Gaming (March 1–5, 2027, Moscone Center) is a gaming event in the "
            "city, but its official pricing page sells passes, so it belongs in the paid section, not the free "
            "gaming spotlight. The nearest free-admission gaming event found this pass is also outside city "
            "limits: GobbleCon's official site states \"There is no longer an admission fee!\" for "
            "\"Nov. 26 - 29, 2026 Burlingame Hyatt Regency SFO\", so it is excluded from the city-only catalog."
        ),
        "sources": [
            {"label": "Day of the Devs official site (\"programs are provided entirely for free\")", "url": "https://www.dayofthedevs.org/"},
            {"label": "Day of the Devs — San Francisco Edition 2026 (completed edition)", "url": "https://www.dayofthedevs.org/events/day-of-the-devs-san-francisco-edition-2026"},
            {"label": "GDC official pass pricing page (paid passes)", "url": "https://gdconf.com/passes-pricing/"},
            {"label": "GobbleCon official site (free admission, but Burlingame — outside the city)", "url": "https://gobblecon.com/"},
        ],
        "disposition": (
            "Published as a coverage-gap finding: the gaming focus area on the dashboard shows the verified free "
            "gaming row with its completed-edition badge and links here, rather than implying an upcoming free "
            "gaming event exists. Nonblocking."
        ),
    },
    {
        "id": "flag-free-ai-coverage-gap",
        "event_id": "open-weight-debate-night-2026",
        "event": "Free AI events — coverage gap as of 2026-10-18",
        "issue": (
            "The brief asks for free AI events first, but not one of the 16 verified rows in the "
            "Technology, AI & gaming category carries a source-stated free admission. Thirteen are priced, "
            "ticketed or registration/invitation-gated (for example GDC Festival of Gaming, whose official "
            "pricing page sells passes from $125 to $1,249, Cloudflare Connect at $595, AI Engineer Code Summit "
            "from $1,299, Microsoft Ignite and Bay to Breakers on registration wording alone), and the remainder "
            "publish no price at all. The two closest candidates found this pass — the Open Source AI Week Open "
            "Weight Debate Night (October 19, 2026, GitHub Office, SF) and the Open Source AI Awards Night "
            "(October 23, 2026, Founder's Inc, SF) — publish date, time, venue and capacity on their official "
            "pages but no price, and their official registration listings show \"Approval Required\" with no "
            "ticket price, so they are published with the cost left blank instead of being counted as free."
        ),
        "sources": [
            {"label": "Open Source AI Week — The Debates official page (no price published)", "url": "https://opensourceaiweek.com/the-debates/"},
            {"label": "Open Source AI Week — Awards official page (no price published)", "url": "https://opensourceaiweek.com/open-source-ai-awards/"},
            {"label": "Official registration listing — Debate Night (approval required, no price)", "url": "https://luma.com/592fcwx2"},
            {"label": "Official registration listing — Awards Night (approval required, no price)", "url": "https://luma.com/7ebvz0oq"},
            {"label": "GDC official pass pricing page (paid passes)", "url": "https://gdconf.com/passes-pricing/"},
        ],
        "disposition": (
            "Published as a coverage-gap finding: the AI focus card on the dashboard reports 0 verified free rows "
            "and links here rather than implying that a free AI event was confirmed. The two October 2026 "
            "Open Source AI Week programs stay in the separate non-free section until an official page states a "
            "cost. Nonblocking."
        ),
    },
    {
        "id": "flag-from-the-e-cadence-inconsistency",
        "event_id": "from-the-e-holiday-night-market-2026-12-11",
        "event": "From the E Excelsior Night Market (2026 editions)",
        "issue": (
            "The three From the E 2026 editions carry different cadence labels: Oct 23 is "
            "special/single-date (SFMTA source, recurrence not stated), Nov 20 is recurring/monthly "
            "(organizer homepage), Dec 11 is special/single-date (organizer event page). The organizer "
            "publishes three dated editions but no recurrence rule, and its own general wording (\"the "
            "second Saturday of the month from 5pm-10pm\") does not match Friday dates — see "
            "flag-from-the-e-general-hours-mismatch. A human owner may want one cadence convention for "
            "the series."
        ),
        "disposition": (
            "Catalogued as single-date. A human owner can pick one convention: date each edition as "
            "single-date, or publish one recurring/monthly "
            "series row listing all three 2026 dates."
        ),
        "sources": [
            {
                "label": "From the E — Holiday Night Market official event page",
                "url": "https://www.fromtheesf.com/events/from-the-e-holiday-night-market",
            },
            {
                "label": "From the E Excelsior Night Market official site",
                "url": "https://www.fromtheesf.com/",
            },
            {
                "label": "SFMTA travel update: From the E Night Market (Oct 23, 2026)",
                "url": "https://www.sfmta.com/travel-updates/e-night-market-friday-october-23-2026",
            },
        ],
    },
]


def insert_alphabetical(events: list[dict], row: dict) -> None:
    """Insert a published row keeping the file's alphabetical-by-name convention."""
    name = row["name"].lower()
    for index, existing in enumerate(events):
        if existing["status"] != "verified":
            continue
        if existing["name"].lower() > name:
            events.insert(index, row)
            return
    events.append(row)


def main() -> None:
    document = json.loads(DATA.read_text(encoding="utf-8"))
    events: list[dict] = document["events"]
    flags: list[dict] = document["flags"]
    known_events = {event["id"] for event in events}
    known_flags = {flag["id"] for flag in flags}

    added = []
    for row in NEW_PUBLISHED:
        if row["id"] in known_events:
            continue
        insert_alphabetical(events, row)
        known_events.add(row["id"])
        added.append(row["id"])

    for row in NEW_REVIEW:
        if row["id"] in known_events:
            continue
        # keep review records together: insert after the last existing review record
        last_review = max(
            (index for index, event in enumerate(events) if event["status"] != "verified"),
            default=len(events) - 1,
        )
        events.insert(last_review + 1, row)
        known_events.add(row["id"])
        added.append(row["id"])

    added_flags = []
    for flag in NEW_FLAGS:
        if flag["id"] in known_flags:
            # declarative upsert: keep the position, refresh the wording
            index = next(i for i, existing in enumerate(flags) if existing["id"] == flag["id"])
            if flags[index] != flag:
                flags[index] = flag
                added_flags.append(flag["id"] + " (updated)")
            continue
        flags.append(flag)
        known_flags.add(flag["id"])
        added_flags.append(flag["id"])

    catalog = document["catalog"]
    session_note = "arena/3977d9cb-maltaproj7 free-first restructure + verification pass (2026-10-18)"
    if session_note not in catalog.get("updated_by", ""):
        catalog["updated_by"] = catalog.get("updated_by", "").rstrip("; ") + "; " + session_note
    reverification = (
        "2026-10-18 — arena/3977d9cb-maltaproj7 re-fetched the official pages behind the near-term upcoming "
        "rows (SFMTA travel updates for Lower Polk Live and the From the E Excelsior Night Market, Foodwise "
        "event pages, Sunday Streets SF season and Excelsior pages, Hardly Strictly Bluegrass, Day of the Devs) "
        "and added three rows plus one review record from official organizer pages (Shipyard Trust for the Arts "
        "Fall Open Studios, Open Source AI Week Debate Night and Awards Night). Log: "
        "research/reverification-3977d9cb.md. "
    )
    if "reverification-3977d9cb.md" not in catalog.get("last_reverification", ""):
        catalog["last_reverification"] = reverification + catalog.get("last_reverification", "")

    DATA.write_text(json.dumps(document, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    published = [event for event in events if event["status"] == "verified"]
    recurring = [event for event in published if event["bucket"] == "recurring"]
    special = [event for event in published if event["bucket"] == "special"]
    review = [event for event in events if event["status"] != "verified"]
    print(f"added events: {added or 'none (already applied)'}")
    print(f"added flags: {added_flags or 'none (already applied)'}")
    print(
        f"now: published={len(published)} recurring={len(recurring)} special={len(special)} "
        f"review={len(review)} flags={len(flags)}"
    )


if __name__ == "__main__":
    main()
