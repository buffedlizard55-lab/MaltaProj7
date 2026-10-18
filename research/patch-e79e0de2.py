#!/usr/bin/env python3
"""Reproducible data patch — session arena/e79e0de2-maltaproj7 (2026-10-18).

Scope
-----
1. 14 new published rows, each added only after a direct fetch of the named
   official organizer / official venue / government page (evidence quoted in
   research/verification-e79e0de2.md).
2. Cost ("admission") and time fills on existing rows, only where the linked
   official page states the value. Nothing is inferred.
3. A new "Technology, AI & gaming" category; clearly tech/AI/gaming rows move
   out of "Professional & academic" so the brief's gaming/AI emphasis is
   visible on the site. The `category` field is descriptive metadata only.
4. New field-level flags for cross-source discrepancies, published on the
   site's Flagged for Review page.

Run:  python3 research/patch-e79e0de2.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "events.json"

NEW_CATEGORY = "Technology, AI & gaming"

# --- rows moved into the new category (from "Professional & academic") -------
MOVE_TO_TECH = [
    "gdc-festival-of-gaming-2027",
    "rsa-conference-2027",
    "dreamforce-2027",
    "cloudflare-connect-2026",
    "microsoft-ignite-2026",
    "techcrunch-disrupt-2026",
    "ai-engineer-worlds-fair-2026",
    "amd-advancing-ai-2026",
    "coreweave-fully-connected-2026",
    "current-san-francisco-2026",
    "semicon-west-2026",
    "spie-photonics-west-2027",
    "tdx-2027",
    "atlassian-team-2027",
]

SFMTA_ADVISORY = (
    "https://www.sfmta.com/press-releases/sfmta-transit-and-traffic-advisory-week-"
    "thursday-october-15-through-wednesday-october-21-2026"
)
SFMTA_LABEL = "SFMTA weekly transit and traffic advisory (Oct 15–21, 2026)"

NEW_ROWS = [
    {
        "id": "ai-engineer-code-summit-2026",
        "name": "AI Engineer Code Summit 2026",
        "bucket": "recurring",
        "cadence": "annual",
        "category": NEW_CATEGORY,
        "date_text": "November 10–12, 2026",
        "start_date": "2026-11-10",
        "end_date": "2026-11-12",
        "time_text": "Workshops Nov 10; talks and expo Nov 11–12",
        "location": "Hilton San Francisco Union Square, 333 O'Farrell St., San Francisco",
        "organizer": "AI Engineer",
        "admission": (
            "Tickets sold: regular $1,299 + fees (talks and expo, Nov 11–12); "
            "final and at-door $1,499 + fees; workshop add-on $299 + fees (Nov 10). "
            "Attendance by application only."
        ),
        "source_url": "https://ai.engineer/code/2026",
        "source_label": "AI Engineer Code Summit 2026 official page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Official page: \"NOV 10-12, 2026 // SF, CA\"; \"AIE CODE returns for its second annual "
            "code-focused summit\"; venue block states \"Hilton Union Square, 333 O'Farrell St, "
            "San Francisco, CA 94102\"; pricing block lists regular $1,299 + fees, final and at-door "
            "$1,499 + fees, workshop add-on $299 + fees, and \"Applying is free and doesn't reserve a seat.\" "
            "No 2027 edition has been announced by the organizer."
        ),
    },
    {
        "id": "day-of-the-devs-sf-2026",
        "name": "Day of the Devs — San Francisco Edition (2026)",
        "bucket": "recurring",
        "cadence": "annual",
        "category": NEW_CATEGORY,
        "date_text": "March 8, 2026 (67 games shown)",
        "start_date": "2026-03-08",
        "end_date": "2026-03-08",
        "time_text": "",
        "location": "The Midway, 900 Marin Street, San Francisco",
        "organizer": "Day of the Devs",
        "admission": "Free",
        "source_url": "https://www.dayofthedevs.org/events/day-of-the-devs-san-francisco-edition-2026",
        "source_label": "Day of the Devs — San Francisco Edition (2026) official event page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Official event page: \"Day of the Devs returns to the Midway in San Francisco for the 2026 "
            "In-Person Celebration: San Francisco Edition!\" and \"Our last physical event brought together "
            "more than 60 inspiring indie games and developers ... all free with no costs either to developers "
            "or attendees.\" Location block: \"The Midway, 900 Marin Street, San Francisco, 94124, CA\". "
            "The organizer's In-Person Events index lists \"8 Mar 2026 • 67 Games shown\" and describes the "
            "San Francisco edition as the flagship annual event. No 2027 edition is announced yet."
        ),
    },
    {
        "id": "union-square-park-programs",
        "name": "Union Square Plaza — Free Park Programs",
        "bucket": "recurring",
        "cadence": "weekly",
        "category": "Community & culture",
        "date_text": "Daily free amenities plus a weekly Mon–Sun program rotation",
        "start_date": "",
        "end_date": "",
        "time_text": (
            "Free daily amenities 9:00am–6:00pm; Monday Imagination Mondays 10:00am; "
            "Tuesday Blues 4:00–6:00pm; Wednesday Cardio Dance 5:30–6:30pm; "
            "Thursday Crafternoons 4:30–6:30pm; Friday Union Square Dances 5:00–8:00pm; "
            "Saturday Juggling Lessons 11:30am–1:30pm and Second Saturdays 'Round the World 11:00am–2:00pm; "
            "Sunday Mahjong & Mixer 3:00–6:00pm"
        ),
        "location": "Union Square Plaza, San Francisco",
        "organizer": "Union Square Alliance",
        "admission": "Free",
        "source_url": "https://visitunionsquaresf.com/park-programs",
        "source_label": "Union Square Alliance — park programs schedule",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Official schedule page: \"Free Programming in Union Square Plaza\". The published October 2026 "
            "schedule applies through October 20, 2026; programming pauses October 21–November 3, 2026 while "
            "the ice rink loads, free daily amenities resume November 4, 2026, and free winter crafts "
            "programming begins November 5, 2026. Funding statement: \"Free Programming is made possible with "
            "support from Bank of America and a grant from the Office of Mayor Daniel Lurie and the San "
            "Francisco Office of Economic and Workforce Development to Biederman Redevelopment Ventures, in "
            "cooperation with San Francisco Recreation and Parks and the Union Square Alliance.\""
        ),
    },
    {
        "id": "foodwise-sunday-supper-2026",
        "name": "Foodwise Sunday Supper — A Farm to City Feast",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Sunday, October 18, 2026",
        "start_date": "2026-10-18",
        "end_date": "2026-10-18",
        "time_text": "4:30–9:30 p.m. (reception-only 4:30–6:00 p.m.)",
        "location": "Ferry Building, San Francisco",
        "organizer": "Foodwise",
        "admission": (
            "Tickets sold (21+ only). Fair market value of a dinner ticket $200; "
            "reception-only ticket $75; anything paid above that value is tax-deductible."
        ),
        "source_url": "https://foodwise.org/events/foodwise-sunday-supper/",
        "source_label": "Foodwise Sunday Supper official event page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Official page: \"Sunday, October 18, 2026, 4:30 pm - 9:30 pm\", Evening Party at Ferry Plaza, "
            "an abundant walkaround reception and a seated four-course dinner in the Ferry Building Grand Hall "
            "with 35 participating restaurants. FAQ states the fair market value of a single dinner ticket is "
            "$200 and a single reception-only ticket is $75, and that the event is for guests 21 and over. "
            "Tickets are sold through Eventbrite."
        ),
    },
    {
        "id": "dia-de-los-muertos-halloween-mission-market-2026",
        "name": "Día de los Muertos and Halloween at Mission Community Market",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Thursday, October 29, 2026",
        "start_date": "2026-10-29",
        "end_date": "2026-10-29",
        "time_text": "3:00–7:00 p.m. (DJ Lamont 5–7 p.m.)",
        "location": "Mission Community Market, 22nd Street between Mission and Valencia, San Francisco",
        "organizer": "Foodwise",
        "admission": "",
        "source_url": (
            "https://foodwise.org/events/dia-de-los-muertos-and-halloween-at-mission-community-market/"
        ),
        "source_label": "Foodwise — Día de los Muertos and Halloween at Mission Community Market",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Official page: \"Thursday, October 29, 2026, 3:00 pm - 7:00 pm\", Market Happening, Mission. "
            "Family activities, live music with DJ Lamont 5–7 p.m. at the Little Mission Studio stage, and free "
            "samples, recipes and cooking tips at the Seasonal Spotlight tent. The page does not state an "
            "admission charge, so the cost field is left blank rather than inferred."
        ),
    },
    {
        "id": "fall-fruit-celebration-2026",
        "name": "Foodwise Fall Fruit Celebration — Seasonal Spotlight",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Saturday, October 31, 2026",
        "start_date": "2026-10-31",
        "end_date": "2026-10-31",
        "time_text": "11:00 a.m. – 1:00 p.m.",
        "location": "Ferry Plaza Farmers Market, Seasonal Spotlight tent in front of the Ferry Building, "
                   "San Francisco",
        "organizer": "Foodwise",
        "admission": "",
        "source_url": "https://foodwise.org/events/fall-fruit-celebration/",
        "source_label": "Foodwise — Fall Fruit Celebration official event page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Official page: \"Saturday, October 31, 2026, 11:00 am - 1:00 pm\", Seasonal Celebration, Ferry "
            "Plaza. Tasting of fall fruit varieties, a free-samples tent, and a cooking demo at the Foodwise "
            "Classroom. The page states free samples and cooking tips but does not state an admission charge, "
            "so the cost field is left blank rather than inferred."
        ),
    },
    {
        "id": "mission-community-market-last-day-2026",
        "name": "Mission Community Market — Last Day of the 2026 Season",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Thursday, November 12, 2026",
        "start_date": "2026-11-12",
        "end_date": "2026-11-12",
        "time_text": "3:00–7:00 p.m.",
        "location": "Mission Community Market, 22nd Street between Mission and Valencia, San Francisco",
        "organizer": "Foodwise",
        "admission": "",
        "source_url": "https://foodwise.org/events/mission-community-market-last-day-of-the-season/",
        "source_label": "Foodwise — Mission Community Market last day of the season",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Official page: \"Thursday, November 12, 2026, 3:00 pm - 7:00 pm\", Market Happening, Mission. "
            "\"Mission Community Market's last day of the 2026 season will be Thursday, November 12. We'll be "
            "back on March 18, 2027.\" This row records the final day of the 2026 season; the weekly market "
            "itself is catalogued separately as “Mission Community Market”."
        ),
    },
    {
        "id": "fall-holiday-farmers-market-2026",
        "name": "Foodwise Fall Holiday Farmers Market",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Tuesday, November 24, 2026",
        "start_date": "2026-11-24",
        "end_date": "2026-11-24",
        "time_text": "10:00 a.m. – 2:00 p.m.",
        "location": "Ferry Plaza Farmers Market, San Francisco",
        "organizer": "Foodwise",
        "admission": "",
        "source_url": "https://foodwise.org/events/fall-holiday-farmers-market/",
        "source_label": "Foodwise — Fall Holiday Farmers Market official event page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Official page: \"Tuesday, November 24, 2026, 10:00 am - 2:00 pm\", Market Happening, Ferry Plaza. "
            "\"You'll find our regular Tuesday farms along with some special guest vendors.\" The page does not "
            "state an admission charge, so the cost field is left blank rather than inferred."
        ),
    },
]

# --- value fills on existing rows (value present on the linked official page)
UPDATES = {
    "bearrison-street-fair-2026": {
        "source_url": "https://www.bearrison.org/",
        "source_label": "Bearrison Street Fair official site",
        "source_authority": "Official organizer",
        "time_text": "12:00–6:00pm",
        "location": "11th & Harrison, San Francisco",
        "notes": (
            "Re-sourced 2026-10-18 (arena/e79e0de2) from the event's own official site, which states "
            "\"Bearrison is Back! 12-6 PM, 11th & Harrison, SF, Saturday, October 17, 2026\". The SFMTA weekly "
            "advisory for Oct 15-21, 2026 independently records the third annual Bearrison Street Fair, noon-6pm, "
            "primarily on Harrison Street between 10th and 13th streets, expected attendance 2,500, and names "
            "the event site bearrison.org. Admission is not stated by the organizer and is left blank."
        ),
    },
    "potrero-hill-festival-2026": {
        "source_url": "https://potrerofestival.com/",
        "source_label": "Potrero Hill Festival official site",
        "source_authority": "Official organizer",
        "time_text": "10 a.m. – 5 p.m.",
        "organizer": "Potrero Hill Festival",
        "notes": (
            "Re-sourced 2026-10-18 (arena/e79e0de2) from the festival's own official site, which states "
            "\"Saturday October 17, 2026 - 10 a.m. - 5 p.m.\" and \"We are excited to celebrate our 51st year "
            "as the premier neighborhood festival on Potrero Hill!\" Two stages of live R&B on 20th Street; a "
            "benefit for Potrero Hill public schools. The SFMTA weekly advisory for Oct 15-21, 2026 gives the "
            "same date and street span but an end time of 4:30 p.m., and a second SFMTA travel-update page gives "
            "11 a.m.-4 p.m. - see flag-potrero-hill-festival-hours. Admission is not stated by the organizer and "
            "is left blank."
        ),
    },
    "gdc-festival-of-gaming-2027": {
        "admission": (
            "Festival pass $549 early rate (super early $499 through Oct 9, 2026); Game Changer $1,249; "
            "Indie/Start-up/Academic $299; Festival Hall only $175; Business Hall only $125; "
            "1-Day Career $125"
        ),
        "source_url": "https://gdconf.com/passes-pricing/",
        "source_label": "GDC official Passes & Pricing page",
        "notes": (
            "Header states 'March 1-5, 2027 — Moscone Center, San Francisco, CA'. Passes & Pricing page "
            "lists early-rate prices (Festival $549, Game Changer $1,249, Indie/Start-up/Academic $299, "
            "Festival Hall only $175, Business Hall only $125, 1-Day Career $125) and a super-early deadline of "
            "Fri Oct 9, 2026, an early deadline of Fri Dec 11, 2026, and higher regular/final/onsite rates "
            "after that. See flag-gdc-2027-pass-deadlines."
        ),
    },
    "cloudflare-connect-2026": {
        "admission": (
            "Conference pass $595; group/team pass $495 per pass for 5–9 (50% off for 10+); "
            "Cloudflare University add-on $495; $100 off for government, military, nonprofit and education"
        ),
        "time_text": "Registration 7:30 a.m.–9 a.m. on day one; day-one programme 8 a.m.–7 p.m.",
        "notes": (
            "Official page: 'Oct 19-21 · Moscone West, SF'. Ticket blocks: Conference Pass $595, Cloudflare "
            "University +$495, group and team passes $495 per pass for groups of 5–9 with 50% off for 10+, and "
            "'$100 off for government, military, nonprofit, and education (.gov / .mil / .org / .edu)'. "
            "Agenda at-a-glance gives day one as 8 a.m.–7 p.m. with registration 7:30–9 a.m. and a 5–7 p.m. "
            "welcome reception; days two and three run 7 a.m.–5:30 p.m."
        ),
    },
    "sf-dance-film-festival-2026": {
        "admission": "Tickets sold (festival pass and individual programs); filmmaking masterclass free",
        "notes": (
            "Only the in-person San Francisco component (through November 8) belongs to this catalog's "
            "geographic scope; the organizer also runs an online festival November 9-30. Venues listed by the "
            "organizer: Lucasfilm Premier Theater, Delancey Street Theater, Catharine Clark Gallery, SHACK15, "
            "and Brava Theater. Flagged irregularity (2026-10-18): SHACK15 is not within the City and County "
            "of San Francisco; it is named separately rather than folded into the “San Francisco theaters” list. "
            "The November 9–30 online window is stated verbatim on the official festival page. Cost: the "
            "official schedule marks the “Filmmaking Masterclass: So Close” program as “free!”, and the "
            "official tickets page (https://sfdancefilmfest.org/tickets/) sells a Full Festival Pass, a "
            "Streaming Pass and per-program tickets, with student rates at Brava Theater; individual prices "
            "are not published in the page text. See flag-sfdff-cost."
        ),
    },
    "sf-transgender-film-festival-2026": {
        "time_text": (
            "Nov 12: 7pm Comedy, 9pm Documentary; Nov 13: 7pm Horror, 9pm Grab Bag; "
            "Nov 14: 7pm Speculative Fiction, 9pm Adult (18+)"
        ),
        "admission": "Tickets sold (per-program tickets)",
        "notes": (
            "The organizer's 2026 schedule lists in-person programs at the Roxie Theater: Program 1 Comedy "
            "(Nov 12, 7pm), Program 2 Documentary (Nov 12, 9pm), Program 3 Horror (Nov 13, 7pm), Program 4 "
            "Grab Bag (Nov 13, 9pm), Program 5 Speculative Fiction (Nov 14, 7pm) and Program 6 Adult (18+) "
            "(Nov 14, 9pm). Each program page links to a ticket purchase page. A trusted civic listing "
            "(SF/Arts) describes a hybrid program with an online component listed through November 22; only the "
            "in-person November 12-14 dates are published here."
        ),
    },
    "sf-open-studios-2026": {
        "time_text": "Preview Exhibition 1:00–7:00pm daily, September 19–27",
    },
    "lower-polk-live-2026-10-23": {
        "time_text": "4:00–9:00 p.m.",
    },
    "from-the-e-night-market-2026-10-23": {
        "time_text": "4:30–8:30 p.m.",
    },
    "noe-valley-night-market-2026-10-27": {
        "time_text": "4:30–8:30 p.m.",
    },
    "diplos-run-club-5k-sf-2026": {
        "time_text": "8:30 a.m. start; post-race concert featuring Diplo and friends",
    },
}

# --- new field-level flags (published on Flagged for Review) -----------------
NEW_FLAGS = [
    {
        "id": "flag-hayes-valley-shared-spaces",
        "event_id": "hayes-valley-shared-spaces-2026",
        "event": "Hayes Valley Farmers Market & Shared Spaces (2026 extended hours)",
        "issue": (
            "Two official sources describe overlapping but different hours on the same block. The SFMTA travel "
            "update records a street closure on Hayes between Gough and Octavia every Friday 4–10 p.m. and "
            "Saturday 7 a.m.–10 p.m. for the “Hayes Valley Farmers Market & Shared Spaces” through the "
            "remainder of 2026, while the PCFMA market page lists the market itself as Saturday 10 a.m.–2 p.m. "
            "at 450 Hayes. The market row and the shared-spaces row are kept separate; a human should confirm "
            "whether the extended Friday/Saturday hours are a 2026-only expansion."
        ),
        "sources": [
            {
                "label": "SFMTA travel update — Hayes Valley Farmers Market & Shared Spaces",
                "url": (
                    "https://www.sfmta.com/travel-updates/hayes-valley-farmers-market-shared-spaces-"
                    "fridays-saturdays-october-2026"
                ),
            },
            {"label": "PCFMA — Hayes Valley Farmers' Market", "url": "https://www.pcfma.org/market/hayes-valley-farmers-market"},
        ],
        "disposition": "Both official sources published; rows kept separate. Flagged for review, nonblocking.",
    },
    {
        "id": "flag-day-of-devs-next-edition",
        "event_id": "day-of-the-devs-sf-2026",
        "event": "Day of the Devs — San Francisco Edition (2026)",
        "issue": (
            "The organizer calls the San Francisco edition its flagship annual event and lists 2024, 2025 and "
            "2026 editions, but no 2027 San Francisco date is published on the organizer's In-Person Events "
            "index as of 2026-10-18. The 2026 edition (March 8, 2026) is published because it is a completed, "
            "documented, free edition; a 2027 date is not inferred."
        ),
        "sources": [
            {
                "label": "Day of the Devs — In-Person Events index",
                "url": "https://www.dayofthedevs.org/events",
            },
            {
                "label": "Day of the Devs — San Francisco Edition (2026)",
                "url": "https://www.dayofthedevs.org/events/day-of-the-devs-san-francisco-edition-2026",
            },
        ],
        "disposition": "2026 edition published; 2027 date left blank until the organizer announces it. Nonblocking.",
    },
    {
        "id": "flag-ai-engineer-code-next-edition",
        "event_id": "ai-engineer-code-summit-2026",
        "event": "AI Engineer Code Summit 2026",
        "issue": (
            "The organizer states this is the second annual code-focused summit and publishes the 2026 dates "
            "(Nov 10–12, 2026) and venue, but no 2027 edition is announced. The row records the 2026 edition; "
            "a 2027 date is not inferred from the “second annual” wording."
        ),
        "sources": [
            {"label": "AI Engineer Code Summit 2026 official page", "url": "https://ai.engineer/code/2026"},
        ],
        "disposition": "2026 edition published; 2027 date left blank. Nonblocking.",
    },
    {
        "id": "flag-gdc-2027-pass-deadlines",
        "event_id": "gdc-festival-of-gaming-2027",
        "event": "GDC Festival of Gaming (Game Developers Conference)",
        "issue": (
            "Published prices are early-rate prices and are time-limited: super early deadline Fri Oct 9, "
            "2026, early deadline Fri Dec 11, 2026, then higher regular (Fri Feb 5, 2027), final (Fri Feb 26, "
            "2027) and onsite (Mar 5, 2027) rates. The row states the early rates and the deadline dates so "
            "the number is not read as a fixed price."
        ),
        "sources": [
            {"label": "GDC official Passes & Pricing page", "url": "https://gdconf.com/passes-pricing/"},
        ],
        "disposition": "Early-rate prices published with their deadlines. Flagged for awareness, nonblocking.",
    },
    {
        "id": "flag-sfdff-cost",
        "event_id": "sf-dance-film-festival-2026",
        "event": "San Francisco Dance Film Festival",
        "issue": (
            "The official schedule marks only the “Filmmaking Masterclass: So Close” program as “free!”; "
            "the official tickets page sells a Full Festival Pass, a Streaming Pass and per-program tickets "
            "(student rates at Brava Theater) but does not publish individual prices in the page text. The row "
            "states the cost structure that the sources do state and does not invent a dollar amount for a "
            "general screening."
        ),
        "sources": [
            {"label": "SFDFF Fall Festival 2026 schedule", "url": "https://sfdancefilmfest.org/fall-festival-2026/"},
            {"label": "SFDFF tickets and passes", "url": "https://sfdancefilmfest.org/tickets/"},
        ],
        "disposition": "Cost structure published; individual prices left blank. Flagged for review, nonblocking.",
    },
]


# --- updates to flags raised by earlier sessions ---------------------------
FLAG_UPDATES = {
    "flag-potrero-hill-festival-hours": {
        "issue": (
            "Hours conflict between official sources. The festival's own official site states "
            "\"Saturday October 17, 2026 - 10 a.m. - 5 p.m.\"; the SFMTA weekly transit and traffic advisory "
            "for Oct 15-21, 2026 states \"from 10 a.m. to 4:30 p.m.\"; a second SFMTA travel-update page states "
            "11 a.m.-4 p.m. The organizer's own hours are now published in the row (the row was previously "
            "sourced only to SFMTA and had a blank time) and the two SFMTA variants are recorded here for a "
            "human to confirm with the organizer."
        ),
        "sources": [
            {"label": "Potrero Hill Festival official site", "url": "https://potrerofestival.com/"},
            {
                "label": "SFMTA weekly transit and traffic advisory (Oct 15–21, 2026)",
                "url": SFMTA_ADVISORY,
            },
            {
                "label": "SFMTA travel update — Potrero Hill Festival",
                "url": "https://www.sfmta.com/travel-updates/potrero-hill-festival-saturday-october-17-2026",
            },
        ],
        "disposition": (
            "Row re-sourced to the organizer and its hours published; SFMTA variants recorded for review. "
            "Nonblocking."
        ),
    },
}


def main() -> None:
    document = json.loads(DATA.read_text(encoding="utf-8"))
    events = document["events"]
    flags = document.get("flags", [])
    by_id = {event["id"]: event for event in events}

    # 1. new rows
    for row in NEW_ROWS:
        if row["id"] in by_id:
            raise SystemExit(f"row already exists: {row['id']}")
        events.append(row)

    # 2. value fills
    for event_id, changes in UPDATES.items():
        event = by_id.get(event_id)
        if event is None:
            raise SystemExit(f"cannot update missing row: {event_id}")
        event.update(changes)

    # 3. category split
    for event_id in MOVE_TO_TECH:
        event = by_id.get(event_id)
        if event is None:
            raise SystemExit(f"cannot recategorise missing row: {event_id}")
        if event["category"] != "Professional & academic":
            raise SystemExit(f"unexpected source category for {event_id}: {event['category']}")
        event["category"] = NEW_CATEGORY

    # 4. flags
    known_flag_ids = {flag["id"] for flag in flags}
    for flag in NEW_FLAGS:
        if flag["id"] in known_flag_ids:
            continue
        flags.append(flag)

    # 5. update flags raised by earlier sessions where a new official source changes them
    flag_by_id = {flag["id"]: flag for flag in flags}
    for flag_id, changes in FLAG_UPDATES.items():
        flag = flag_by_id.get(flag_id)
        if flag is None:
            raise SystemExit(f"cannot update missing flag: {flag_id}")
        flag.update(changes)

    DATA.write_text(json.dumps(document, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    published = [event for event in events if event["status"] == "verified"]
    print(
        f"patched: {len(events)} records "
        f"({len(published)} published, {len(events) - len(published)} review), {len(flags)} flags"
    )


if __name__ == "__main__":
    main()
