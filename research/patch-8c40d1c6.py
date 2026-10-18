#!/usr/bin/env python3
"""Reproducible data patch for session arena/8c40d1c6-maltaproj7 (2026-10-18).

Every change below was made only after re-fetching the linked official page on
2026-10-18 and reading the value from that page. Nothing is inferred: where an
official page published no price, the admission field stays blank and a
field-level flag records the gap.

Changes
-------
1. Cost fills (and note updates) for four rows whose official pages state a
   ticket requirement or a free-activities statement but no/partial pricing.
2. Six new published rows, each from a live official organizer or government page:
   Sunday Streets Excelsior (Oct 18), SFIAC & Olympic Club Cornhole Tournament
   (Oct 23), and four Foodwise farmers-market cooking demos (Oct 31 - Dec 19).
3. Six new field-level flags recording the residual gaps found in this pass.

Run from the repository root:  python3 research/patch-8c40d1c6.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "events.json"

# --------------------------------------------------------------------------- #
# 1. Field updates on existing published rows
# --------------------------------------------------------------------------- #
FIELD_UPDATES: dict[str, dict[str, str]] = {
    "diplos-run-club-5k-sf-2026": {
        "admission": (
            "Tickets sold (registration required; the official event page listed the "
            "event 95% sold out on 2026-10-18). Registration price is not stated on the "
            "official page."
        ),
        "time_text": (
            "8:30 a.m. race start; festival open 8:30 a.m.; Jax Jones 9:30 a.m.; "
            "Diplo 10:30 a.m."
        ),
        "notes": (
            "Re-verified 2026-10-18 (arena/8c40d1c6) against the organizer's own event page "
            "(diplosrunclub.com/san-francisco) and SFMTA's weekly advisory: round three of "
            "Diplo's Run Club in San Francisco, October 18, 2026, starting and finishing at "
            "Robin Williams Meadow in Golden Gate Park (entrance at John F Kennedy Promenade "
            "and Kezar Dr), 8:30 AM race start, post-race concert with Jax Jones (9:30 AM) and "
            "Diplo (10:30 AM); mandatory packet pick-up was Saturday, October 17, 10 a.m.-4 p.m. "
            "at Sports Basement Presidio. The organizer page shows the event 95% sold out and "
            "routes registration through LetsDoThis; no dollar price is published on the page, "
            "so no price is recorded here - see flag-diplos-price-unstated."
        ),
    },
    "exploratorium-after-dark": {
        "admission": (
            "Tickets required (18+; advance tickets recommended). Price is not stated on the "
            "official After Dark page."
        ),
        "notes": (
            "Ages 18+. The organizer lists After Dark every Thursday, 6:00-10:00 p.m., at Pier 15 "
            "with dated themes (50+ evenings a year). Re-checked 2026-10-18 (arena/8c40d1c6): the "
            "page's dated schedule lists After Dark: Death and Life (Thu Oct 22), Creepatorium "
            "(Thu Oct 29), Digest This (Thu Nov 5), Unplug and Play (Thu Nov 12), Glow Opening "
            "(Thu Nov 19), Rule Breakers (Thu Dec 3), Unplug and Play (Thu Dec 10) and Solstice "
            "(Thu Dec 17), all 6-10 p.m. The page states that tickets are required and that "
            "advance purchase is strongly recommended, but publishes no price - see "
            "flag-exploratorium-price-unstated."
        ),
    },
    "sf-ballet-nutcracker-2026": {
        "admission": "Tickets sold; prices are not listed on the production page.",
        "notes": (
            "Page header 'DEC 4-27'; 'Location: War Memorial Opera House'; first performance "
            "Fri Dec 4 7:00 pm, last Sun Dec 27 4:00 pm; sensory-friendly performance Dec 27 "
            "11am. Re-verified 2026-10-18 (arena/8c40d1c6): the production page publishes the "
            "full dated performance calendar (Dec 4-27, 2026) and a 'Buy Tickets' flow, and it "
            "states 'Programming, casting, and prices subject to change', but it lists no ticket "
            "price. The separately ticketed Nutcracker Nightcap afterparty (Dec 4, 9 p.m., 21+) is "
            "listed by the organizer at $150 and does not include a performance ticket. No "
            "performance price is recorded because none is stated - see "
            "flag-nutcracker-price-unstated."
        ),
    },
    "sunday-streets-2026": {
        "admission": (
            "Free (open-streets program: the organizer states Sunday Streets events feature "
            "\"fun, free activities provided by local nonprofits, community groups and small "
            "businesses\"; no admission charge is stated anywhere on the site)"
        ),
        "notes": (
            "The source confirms four 2026 city-neighborhood events: Tenderloin Jun 14, Mission "
            "Jul 19, Bayview Aug 23, Excelsior Oct 18; times and routes vary by neighborhood. "
            "Re-verified 2026-10-18 (arena/8c40d1c6): the organizer's About page states Sunday "
            "Streets is 'a program of the nonprofit Livable City presented in partnership with the "
            "SFMTA, San Francisco Department of Public Health, and the City and County of San "
            "Francisco' and that events offer 'fun, free activities provided by local nonprofits, "
            "community groups and small businesses'. No admission charge is stated anywhere on the "
            "site; the free label rests on that organizer statement - see "
            "flag-sundaystreets-free-wording. The Excelsior edition is also published as its own "
            "dated row (sunday-streets-excelsior-2026)."
        ),
    },
    "bhangra-beats-night-market-2026": {
        "notes": (
            "Official site confirms November 13, 2026 (Diwali edition) at Yerba Buena Gardens, "
            "4-9 p.m., free admission; July 24, 2026 edition has already occurred by the audit "
            "date. Source does not state an annual cadence explicitly. Location discrepancy "
            "flagged 2026-10-18: SF Travel's July and November 2026 guides still list Clay & "
            "Battery streets; the row follows the organizer's \"Yerba Buena Gardens, Jessie "
            "Square, and Yerba Buena Lane\" - see flag-bhangra-location-conflict. Re-verified "
            "2026-10-18 (arena/8c40d1c6): the organizer homepage states the two 2026 dates "
            "(\"Happening on two Fridays-July 24 and November 13 (Diwali edition)-from 4pm-9pm\"), "
            "prints \"PRICE: FREE\", \"TIME: 4 PM - 9 PM\", \"ALL AGES\", and lists the venue as "
            "Yerba Buena Gardens / Jessie Square / Yerba Buena Lane, confirming this row over the "
            "civic guide."
        ),
    },
    "castro-farmers-market-2026": {
        "notes": (
            "This record is specifically the 2026 season published by PCFMA. Re-verified "
            "2026-10-18 (arena/8c40d1c6): the market page states Wednesdays 3:00 pm - 7:00 pm, "
            "April 1st 2026 - November 18th 2026, at 270 Noe St., San Francisco, in partnership "
            "with the Castro Merchants Association. The page states no admission charge, so the "
            "cost field stays blank."
        ),
    },
    "day-of-the-dead-procession-2026": {
        "notes": (
            "SF Travel describes the Day of the Dead processions and Festival of Altars as annual "
            "community events in the Mission District on November 2, 2026. Route and start time "
            "are announced by the community organizers and are not stated on the linked page. "
            "Source caveat (2026-10-18, per correction request from session arena/e969f4df-maltaproj7): "
            "the organizer dayofthedeadsf.org still displays a 2025 edition and states no 2026 date, "
            "so this row's date rests on the trusted civic source alone - see flag-day-of-the-dead-date. "
            "Re-checked 2026-10-18 (arena/8c40d1c6): SF Travel's November 2026 guide still states "
            "\"November 2, 2026\" and links dayofthedeadsf.org; the condition is unchanged."
        ),
    },
    "current-san-francisco-2026": {
        "notes": (
            "Added 2026-10-18 (arena/5e333a6e) from the Moscone Center's own event page, which "
            "states the dates and Moscone West as the venue. Session times and pass prices are not "
            "stated there and are left blank. Re-verified 2026-10-18 (arena/8c40d1c6): the page "
            "reads \"IN-PERSON | November 4-5, 2026 | Moscone West | San Francisco, CA, USA\" and "
            "offers only a 'Register your interest' form; no price is published."
        ),
    },
    "ai-engineer-code-summit-2026": {
        "notes": (
            "Official page: \"NOV 10-12, 2026 // SF, CA\"; \"AIE CODE returns for its second annual "
            "code-focused summit\"; venue block states \"Hilton Union Square, 333 O'Farrell St, San "
            "Francisco, CA 94102\"; pricing block lists regular $1,299 + fees, final and at-door "
            "$1,499 + fees, workshop add-on $299 + fees, and \"Applying is free and doesn't reserve "
            "a seat.\" No 2027 edition has been announced by the organizer. Re-verified "
            "2026-10-18 (arena/8c40d1c6): the page adds that attendance is by application only "
            "(\"Invitations by application only\"; 800 admitted last year) and that the regular "
            "$1,299 ticket covers \"Talks + expo, Nov 11-12\" while the $299 add-on covers the "
            "Nov 10 workshops."
        ),
    },
    "union-square-park-programs": {
        "notes": (
            "Official schedule page: \"Free Programming in Union Square Plaza\". The published "
            "October 2026 schedule applies through October 20, 2026; programming pauses October "
            "21-November 3, 2026 while the ice rink loads in, free daily amenities resume November "
            "4, 2026, and free winter crafts programming begins November 5, 2026. Funding "
            "statement: \"Free Programming is made possible with support from Bank of America and a "
            "grant from the Office of Mayor Daniel Lurie and the San Francisco Office of Economic "
            "and Workforce Development to Biederman Redevelopment Ventures, in cooperation with San "
            "Francisco Recreation and Parks and the Union Square Alliance.\" Re-verified "
            "2026-10-18 (arena/8c40d1c6): unchanged; the page also notes the Union Square Alliance "
            "is not directly managing these events (contact unionsquare@brvcorp.com)."
        ),
    },
    "sf-hip-hop-dance-festival-2026": {
        "notes": (
            "Official site explicitly calls the 2026 edition the 28th annual festival; dates "
            "November 14-15, 2026 confirmed. Venue evidence chain (checked 2026-10-18): the "
            "organizer's linked official ticketing partner listing "
            "(https://www.cityboxoffice.com/eventperformances.asp?evt=3316) names \"Palace of Fine "
            "Arts Theatre, San Francisco, CA\" for all three performances (Sat 7:00 PM; Sun 12:00 "
            "PM and 5:00 PM; tickets $64.05-$75.45); SF Travel's November 2026 guide also names "
            "Palace of Fine Arts. Time and exact admission price not stated in captured organizer "
            "text and left blank. Re-verified 2026-10-18 (arena/8c40d1c6): the organizer homepage "
            "still reads \"28th Annual San Francisco International Hip Hop DanceFest November 14 & "
            "15, 2026\" with \"Tickets On Sale Now!\" linking to City Box Office; no price is "
            "published on the organizer page itself."
        ),
    },
    "sf-dance-film-festival-2026": {
        "time_text": (
            "Programme times vary by date; opening night is Oct 23 at 7:00 p.m."
        ),
        "notes": (
            "Only the in-person San Francisco component (through November 8) belongs to this "
            "catalog's geographic scope; the organizer also runs an online festival November 9-30. "
            "Venues listed by the organizer: Lucasfilm Premier Theater, Delancey Street Theater, "
            "Catharine Clark Gallery, SHACK15, and Brava Theater. Flagged irregularity "
            "(2026-10-18): SHACK15 is not within the City and County of San Francisco; it is named "
            "separately rather than folded into the \"San Francisco theaters\" list. The November "
            "9-30 online window is stated verbatim on the official festival page. Cost: the "
            "official schedule marks the \"Filmmaking Masterclass: So Close\" program as \"free!\", "
            "and the official tickets page (https://sfdancefilmfest.org/tickets/) sells a Full "
            "Festival Pass, a Streaming Pass and per-program tickets, with student rates at Brava "
            "Theater; individual prices are not published in the page text. See flag-sfdff-cost. "
            "Re-verified 2026-10-18 (arena/8c40d1c6): the festival page states \"Eighteen in-person "
            "screenings take place October 23-November 8 at venues throughout San Francisco\" for "
            "its seventeenth year, and the schedule-at-a-glance confirms the dated programmes "
            "(Oct 23, 28, 29, 30; Nov 4, 5, 6, 7, 8) with the Filmmaking Masterclass listed at "
            "10:30 a.m. on Nov 7 as free."
        ),
    },
    "sf-transgender-film-festival-2026": {
        "notes": (
            "The organizer's 2026 schedule lists in-person programs at the Roxie Theater: Program 1 "
            "Comedy (Nov 12, 7pm), Program 2 Documentary (Nov 12, 9pm), Program 3 Horror (Nov 13, "
            "7pm), Program 4 Grab Bag (Nov 13, 9pm), Program 5 Speculative Fiction (Nov 14, 7pm) "
            "and Program 6 Adult (18+) (Nov 14, 9pm). Each program page links to a ticket purchase "
            "page. A trusted civic listing (SF/Arts) describes a hybrid program with an online "
            "component listed through November 22; only the in-person November 12-14 dates are "
            "published here. Re-verified 2026-10-18 (arena/8c40d1c6): schedule and pricing flow "
            "unchanged; the page adds that all in-person screenings feature ASL interpretation, "
            "all films are closed-captioned, and KN95 masking is required inside the building."
        ),
    },
    "cloudflare-connect-2026": {
        "notes": (
            "Official page: 'Oct 19-21 - Moscone West, SF'. Ticket blocks: Conference Pass $595, "
            "Cloudflare University +$495, group and team passes $495 per pass for groups of 5-9 "
            "with 50% off for 10+, and '$100 off for government, military, nonprofit, and education "
            "(.gov / .mil / .org / .edu)'. Agenda at-a-glance gives day one as 8 a.m.-7 p.m. with "
            "registration 7:30-9 a.m. and a 5-7 p.m. welcome reception; days two and three run 7 "
            "a.m.-5:30 p.m. Re-verified 2026-10-18 (arena/8c40d1c6): unchanged; the University "
            "add-on is listed as 'Sold out' at the time of the check."
        ),
    },
    "microsoft-ignite-2026": {
        "notes": (
            "Organizer (Microsoft) lists November 17-20, 2026, San Francisco. Venue confirmed as "
            "Moscone Center by the venue's own official event listing "
            "(moscone.com/events/microsoft-ignite-2026). Pass prices are not stated on the linked "
            "organizer page and are left blank. The admission field records only the registration "
            "requirement shown by the official site's Register now flow; pass prices remain unstated "
            "and are not inferred. Re-verified 2026-10-18 (arena/8c40d1c6): the organizer homepage "
            "reads \"Nov 17-20, 2026 / San Francisco, Moscone Center\" and offers 'Register now'; no "
            "price is published."
        ),
    },
    "agu-annual-meeting-2026": {
        "notes": (
            "The captured agu.org/annual-meeting page names only \"San Francisco, CA\", so the venue "
            "was initially removed rather than inferred. Restored 2026-10-18 from AGU's official "
            "newsroom release (\"7 - 11 December 2026 George R. Moscone Convention Center 747 Howard "
            "St. San Francisco, CA 94103\") - see field-level flag. Re-verified 2026-10-18 "
            "(arena/8c40d1c6): the official page header reads \"7-11 December 2026 | San Francisco, "
            "CA\", registration is open, and the early registration deadline is 5 November 2026; the "
            "page publishes registration links but no price."
        ),
    },
    "sf-sketchfest-2027": {
        "notes": (
            "Billed by the organizer as 'The San Francisco Comedy Festival.' The homepage announces "
            "SF Sketchfest 2027 (January 14-31) with lineup and venues to follow; a 2026 press page "
            "supports the annual classification. No venues, times, or prices are shown until posted. "
            "Re-verified 2026-10-18 (arena/8c40d1c6): the homepage reads \"Jan 14 - 31, 2027\" with "
            "\"Lineup announcing in November!\"; still no venues or prices."
        ),
    },
    "sf-half-marathon-2027": {
        "notes": (
            "Added 2026-10-18 (arena/5e333a6e). Organizer states the race \"returns on February 7, "
            "2027\" in Golden Gate Park and along the Pacific Ocean (Panhandle, Golden Gate Park, "
            "Sunset Dunes); bib pickup February 4-6. Start times and registration prices are not "
            "stated on the page and are blank. Classed as a dated special event because no cadence "
            "is stated. Re-verified 2026-10-18 (arena/8c40d1c6): the race information page confirms "
            "\"Event Date: FEBRUARY 7, 2027\" and adds that optional bib mailing costs a $20 fee "
            "(plus processing) with a January 5, 2027 deadline; no entry fee is published on the page."
        ),
    },
    "tdx-2027": {
        "notes": (
            "Added 2026-10-18 (arena/5e333a6e) from the Moscone Center's own event page, which "
            "states the dates and Moscone Center as the venue. Session times and pass prices are not "
            "stated there and are left blank. Re-verified 2026-10-18 (arena/8c40d1c6): the page "
            "reads \"IN-PERSON | March 10-11, 2027 | Moscone Center | San Francisco, CA USA\" and "
            "offers a save-the-date signup only; no price is published."
        ),
    },
    "spie-photonics-west-2027": {
        "notes": (
            "Added 2026-10-18 (arena/5e333a6e) from the Moscone Center's own event page, which "
            "states the dates but not the hall; the page also says the event is held annually in San "
            "Francisco, but only the 2027 edition is recorded here. Session times and pass prices "
            "are not stated there and are left blank. Re-verified 2026-10-18 (arena/8c40d1c6): the "
            "page reads \"January 30 - February 4, 2027 | San Francisco, CA, USA\"."
        ),
    },
    "illuminate-sf-2026": {
        "notes": (
            "SF Travel lists 60+ permanent and temporary light-art installations citywide beginning "
            "November 27, 2026; no end date is stated on the linked page and illuminatesf.com "
            "returned an error at the re-check, so the season end and installation list are left "
            "blank. Re-verified 2026-10-18 (arena/8c40d1c6): SF Travel's November 2026 guide still "
            "states \"Begins November 27, 2026\" and describes \"More than 60 permanent and temporary "
            "eco-friendly light art installations\"; the organizer site is still unreachable, so the "
            "end date remains blank."
        ),
    },
    "lit-crawl-sf-2026": {
        "notes": (
            "Organizer calls Lit Crawl the annual Litquake Festival finale. Official page states: "
            "\"all programs from 6:30-7:30 PM\" (2026-10-18 re-check). Pointer-style time text "
            "removed per correction request from session arena/e969f4df-maltaproj7. Re-verified "
            "2026-10-18 (arena/8c40d1c6): the page header reads \"OCTOBER 24, 2026\" and describes "
            "Lit Crawl SF as \"the world's largest free pop-up literary event\" with 250+ authors "
            "across Mission District venues, which is the basis for the Free cost label."
        ),
    },
    "foodwise-sunday-supper-2026": {
        "notes": (
            "Official page: \"Sunday, October 18, 2026, 4:30 pm - 9:30 pm\", Evening Party at Ferry "
            "Plaza, an abundant walkaround reception and a seated four-course dinner in the Ferry "
            "Building Grand Hall with 35 participating restaurants. FAQ states the fair market value "
            "of a single dinner ticket is $200 and a single reception-only ticket is $75, and that "
            "the event is for guests 21 and over. Tickets are sold through Eventbrite. Re-verified "
            "2026-10-18 (arena/8c40d1c6): unchanged; the page adds that new reception-only tickets "
            "admit guests from 4:30 to 6:00 p.m. (seated dinner not included) and that tickets are "
            "non-refundable but transferable."
        ),
    },
    "fall-fruit-celebration-2026": {
        "notes": (
            "Official page: \"Saturday, October 31, 2026, 11:00 am - 1:00 pm\", Seasonal Celebration, "
            "Ferry Plaza. Tasting of fall fruit varieties, a free-samples tent, and a cooking demo at "
            "the Foodwise Classroom. The page states free samples and cooking tips but does not state "
            "an admission charge, so the cost field is left blank rather than inferred. Re-verified "
            "2026-10-18 (arena/8c40d1c6): unchanged; the page lists the fall-fruit farms taking part "
            "and states \"Free samples, recipes, and cooking tips at the Seasonal Spotlight tent "
            "(front plaza)\"."
        ),
    },
    "dia-de-los-muertos-halloween-mission-market-2026": {
        "notes": (
            "Official page: \"Thursday, October 29, 2026, 3:00 pm - 7:00 pm\", Market Happening, "
            "Mission. Family activities, live music with DJ Lamont 5-7 p.m. at the Little Mission "
            "Studio stage, and free samples, recipes and cooking tips at the Seasonal Spotlight tent. "
            "The page does not state an admission charge, so the cost field is left blank rather than "
            "inferred. Re-verified 2026-10-18 (arena/8c40d1c6): unchanged; the page adds the market "
            "footprint (22nd Street between Mission and Valencia)."
        ),
    },
    "mission-community-market-last-day-2026": {
        "notes": (
            "Official page: \"Thursday, November 12, 2026, 3:00 pm - 7:00 pm\", Market Happening, "
            "Mission. \"Mission Community Market's last day of the 2026 season will be Thursday, "
            "November 12. We'll be back on March 18, 2027.\" This row records the final day of the "
            "2026 season; the weekly market itself is catalogued separately as \"Mission Community "
            "Market\". Re-verified 2026-10-18 (arena/8c40d1c6): unchanged; no admission charge is "
            "stated."
        ),
    },
    "fall-holiday-farmers-market-2026": {
        "notes": (
            "Official page: \"Tuesday, November 24, 2026, 10:00 am - 2:00 pm\", Market Happening, "
            "Ferry Plaza. \"You'll find our regular Tuesday farms along with some special guest "
            "vendors.\" The page does not state an admission charge, so the cost field is left blank "
            "rather than inferred. Re-verified 2026-10-18 (arena/8c40d1c6): unchanged."
        ),
    },
    "foodwise-black-holiday-market-2026": {
        "notes": (
            "Foodwise organizer page confirms December 12, 2026, 9 a.m.-2 p.m., south arcade of the "
            "Ferry Building, free entry. Re-verified 2026-10-18 (arena/8c40d1c6) against the "
            "organizer's events index as well: \"Pop-Ups on the Plaza: Black Holiday Market | Market "
            "Happening, Pop-Ups on the Plaza, Ferry Plaza | Saturday, December 12, 2026, 9:00 am - "
            "2:00 pm\"."
        ),
    },
    "sf-open-studios-2026": {
        "notes": (
            "Added 2026-10-18 (arena/5e333a6e). Venue page states ArtSpan's 52nd annual SF Open "
            "Studios, Preview Exhibition September 19-27, 2026 (1-7pm daily) and artist studio events "
            "through October 25, 2026; ArtLaunch was Friday, September 18, 7-10pm, 21+, $25. "
            "Studio-weekend start date and hours are not stated on that page (flagged); admission to "
            "studios is not stated and is blank. Re-verified 2026-10-18 (arena/8c40d1c6): the SOMArts "
            "page still states \"September 19, 2026 thru September 27, 2026\", \"through October 25, "
            "2026\" and \"The gallery is open 1-7 PM daily from September 19-27\"; the ArtLaunch "
            "ticket price of $25 is unchanged."
        ),
    },
    "scaregrove-2026": {
        "notes": (
            "SF Recreation and Parks calendar lists Scaregrove 3-9 p.m. at Sigmund Stern Grove on "
            "October 30, 2026 (corroborated by the department's SF Children & Nature organizer "
            "listing and local press). The separate 'Mobile Rec at Scaregrove' 12-8 p.m. listing is "
            "a different program and does not overwrite the main event hours. See Flagged for "
            "Review. Re-check note 2026-10-18 (arena/8c40d1c6): the department calendar is a "
            "JavaScript-rendered list, so the individual listing could not be re-read directly in "
            "this pass; the row is retained on the earlier verification and is flagged for manual "
            "re-check - see flag-scaregrove-recheck."
        ),
    },
    "lower-polk-live-2026-10-23": {
        "notes": (
            "Added 2026-10-18 (arena/5e333a6e). SFMTA states the date, 4-9pm, and street footprint. "
            "Recurrence is not stated by the source and is not inferred. Re-verified 2026-10-18 "
            "(arena/8c40d1c6): the SFMTA travel update reads \"Lower Polk Live will be held on "
            "Friday, October 23, from 4 to 9 p.m.\" with Polk Street (Bush to Sutter) and Fern "
            "Street (Van Ness to Larkin) closed 2-10:30 p.m.; no admission charge is stated."
        ),
    },
    "from-the-e-night-market-2026-10-23": {
        "notes": (
            "Added 2026-10-18 (arena/5e333a6e). SFMTA states food, crafts, entertainment, and live "
            "music, 4:30-8:30pm. Recurrence is not stated by the source and is not inferred. "
            "Re-verified 2026-10-18 (arena/8c40d1c6): the SFMTA travel update reads \"From the E "
            "Excelsior Night Market is a night of food, fun, unique crafts, entertainment and live "
            "music taking place on Ocean Avenue this Friday, October 23, from 4:30 to 8:30 p.m.\"; "
            "no admission charge is stated."
        ),
    },
    "noe-valley-night-market-2026-10-27": {
        "notes": (
            "Added 2026-10-18 (arena/5e333a6e). SFMTA states the host, date, 4:30-8:30pm, and 24th "
            "Street footprint. Recurrence is not stated by the source and is not inferred. "
            "Re-verified 2026-10-18 (arena/8c40d1c6): the SFMTA travel update reads \"Noe Valley "
            "Merchants will host the Noe Valley Night Market on Tuesday, October 27, from 4:30 to "
            "8:30 p.m.\" with live music, local food, artists and retail vendors; no admission "
            "charge is stated."
        ),
    },
}

# --------------------------------------------------------------------------- #
# 2. New published rows (each verified against the linked official page)
# --------------------------------------------------------------------------- #
FOODWISE_DEMO_LOCATION = (
    "Foodwise Classroom (green tent in front of the Ferry Building), "
    "Ferry Plaza Farmers Market, San Francisco"
)
FOODWISE_DEMO_NOTE_TAIL = (
    " All demos take place in the Foodwise Classroom (green tent in front of the Ferry Building) "
    "and are free to the public, with recipes and samples for all."
)

NEW_EVENTS: list[dict] = [
    {
        "id": "sunday-streets-excelsior-2026",
        "name": "Sunday Streets Excelsior — 2026 season finale",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Community & culture",
        "date_text": "Sunday, October 18, 2026",
        "start_date": "2026-10-18",
        "end_date": "2026-10-18",
        "time_text": "11 a.m.–4 p.m.",
        "location": (
            "Mission Street between Geneva Avenue and Theresa Street, with Ocean Avenue between "
            "Persia Avenue and Mission Street also closed, Excelsior, San Francisco"
        ),
        "organizer": "Livable City / Sunday Streets SF (in partnership with the SFMTA)",
        "admission": (
            "Free (open-streets program: the organizer states Sunday Streets events feature "
            "“fun, free activities provided by local nonprofits, community groups and small "
            "businesses”; no admission charge is stated anywhere on the site)"
        ),
        "source_url": "https://sundaystreetssf.com/sunday-streets-excelsior-2026/",
        "source_label": "Sunday Streets SF — Excelsior 2026 event page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/8c40d1c6). Organizer event page: “Sunday Streets is excited "
            "to host the 2026 season finale in the Excelsior on Sunday, October 18 on Mission "
            "Street between Geneva Avenue and Theresa Street from 11am to 4pm”, with a Lucha "
            "Libre showcase, Salvi Soul Encuentro zone, Kultura Crawl food tasting, Polynesian "
            "dance performances, a family hub and a community clothing swap. SFMTA's weekly "
            "advisory independently confirms the same date and 11 a.m.–4 p.m. window. The free "
            "label rests on the organizer's About page (“fun, free activities provided by local "
            "nonprofits, community groups and small businesses”); the site states no separate "
            "admission charge — see flag-sundaystreets-free-wording. The season row "
            "(sunday-streets-2026) covers the full 2026 programme."
        ),
    },
    {
        "id": "sfiac-olympic-club-cornhole-2026-10-23",
        "name": "SFIAC and Olympic Club Cornhole Tournament",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Sports & outdoors",
        "date_text": "Friday, October 23, 2026",
        "start_date": "2026-10-23",
        "end_date": "2026-10-23",
        "time_text": "11 a.m.–4 p.m.",
        "location": (
            "Stockton Street between Filbert and Union streets, North Beach, San Francisco"
        ),
        "organizer": "San Francisco Italian Athletic Club and The Olympic Club",
        "admission": "",
        "source_url": (
            "https://www.sfmta.com/travel-updates/"
            "sfiac-and-olympic-club-cornhole-tournament-friday-october-23-2026"
        ),
        "source_label": "SFMTA travel update: SFIAC and Olympic Club Cornhole Tournament",
        "source_authority": "Government source",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/8c40d1c6). SFMTA: “The SF Italian Athletic Club and the "
            "Olympic Club are bringing their competition to the cornhole lanes of North Beach for "
            "an afternoon of fundraising, fun, and community building on Friday, October 23, from "
            "11 a.m. to 4 p.m.” Street closure: Stockton Street between Filbert and Union, "
            "8 a.m.–7 p.m. No entry fee, team fee or spectator charge is published on the source "
            "page, so the cost field is left blank rather than inferred — see "
            "flag-cornhole-cost-unstated. Recurrence is not stated by the source and is not "
            "inferred."
        ),
    },
    {
        "id": "foodwise-demo-sofia-jimenez-2026-10-31",
        "name": "Foodwise cooking demo — Sofía Jiménez, Tutuli Mexican Bakery",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Saturday, October 31, 2026",
        "start_date": "2026-10-31",
        "end_date": "2026-10-31",
        "time_text": "11:00–11:45 a.m.",
        "location": FOODWISE_DEMO_LOCATION,
        "organizer": "Foodwise",
        "admission": "Free",
        "source_url": "https://foodwise.org/events/sofia-jimenez-tutuli-mexican-bakery/",
        "source_label": "Foodwise event page: Sofía Jiménez, Tutuli Mexican Bakery",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/8c40d1c6). Official page: “Saturday, October 31, 2026, "
            "11:00 am - 11:45 am”, Foodwise Demo, Ferry Plaza."
            + FOODWISE_DEMO_NOTE_TAIL
        ),
    },
    {
        "id": "foodwise-demo-ann-evans-brennan-2026-11-21",
        "name": "Foodwise cooking demo — Ann M. Evans and Georgeanne Brennan, Market Memories Cookbook",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Saturday, November 21, 2026",
        "start_date": "2026-11-21",
        "end_date": "2026-11-21",
        "time_text": "11:00–11:45 a.m.",
        "location": FOODWISE_DEMO_LOCATION,
        "organizer": "Foodwise",
        "admission": "Free",
        "source_url": (
            "https://foodwise.org/events/ann-m-evans-and-georgeanne-brennan-market-memories-cookbook/"
        ),
        "source_label": "Foodwise event page: Ann M. Evans and Georgeanne Brennan",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/8c40d1c6). Official page: “Saturday, November 21, 2026, "
            "11:00 am - 11:45 am”, Foodwise Demo, Ferry Plaza, followed by a book signing with "
            "book sales courtesy of Book Passage." + FOODWISE_DEMO_NOTE_TAIL
        ),
    },
    {
        "id": "foodwise-demo-anna-voloshyna-2026-12-05",
        "name": "Foodwise cooking demo — Anna Voloshyna, Ukraïne",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Saturday, December 5, 2026",
        "start_date": "2026-12-05",
        "end_date": "2026-12-05",
        "time_text": "11:00–11:45 a.m.",
        "location": FOODWISE_DEMO_LOCATION,
        "organizer": "Foodwise",
        "admission": "Free",
        "source_url": "https://foodwise.org/events/anna-voloshyna-ukraine/",
        "source_label": "Foodwise event page: Anna Voloshyna, Ukraïne",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/8c40d1c6). Official page: “Saturday, December 5, 2026, "
            "11:00 am - 11:45 am”, Foodwise Demo, Ferry Plaza, followed by a book signing with "
            "book sales courtesy of Book Passage." + FOODWISE_DEMO_NOTE_TAIL
        ),
    },
    {
        "id": "foodwise-demo-florencia-ramirez-2026-12-19",
        "name": "Foodwise cooking demo — Florencia Ramirez, The Kitchen Activist",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Food & markets",
        "date_text": "Saturday, December 19, 2026",
        "start_date": "2026-12-19",
        "end_date": "2026-12-19",
        "time_text": "11:00–11:45 a.m.",
        "location": FOODWISE_DEMO_LOCATION,
        "organizer": "Foodwise",
        "admission": "Free",
        "source_url": "https://foodwise.org/events/florencia-ramirez-the-kitchen-activist/",
        "source_label": "Foodwise event page: Florencia Ramirez, The Kitchen Activist",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/8c40d1c6). Official page: “Saturday, December 19, 2026, "
            "11:00 am - 11:45 am”, Foodwise Demo, Ferry Plaza, followed by a book signing with "
            "book sales courtesy of Book Passage." + FOODWISE_DEMO_NOTE_TAIL
        ),
    },
]

# --------------------------------------------------------------------------- #
# 3. New field-level flags
# --------------------------------------------------------------------------- #
NEW_FLAGS: list[dict] = [
    {
        "id": "flag-diplos-price-unstated",
        "event_id": "diplos-run-club-5k-sf-2026",
        "event": "Diplo's Run Club San Francisco 5K (2026)",
        "issue": (
            "Cost gap: the organizer's official event page confirms the date, 8:30 a.m. start, "
            "Golden Gate Park venue and post-race concert, and it routes entrants through a "
            "LetsDoThis registration checkout while displaying “95% SOLD OUT”, but it publishes "
            "no dollar price (it only warns that “Pricing is subject to increase pending ticket "
            "inventory”). The row is therefore classed as ticketed with the price left unstated; "
            "no price was inferred from the ticket vendor."
        ),
        "sources": [
            {
                "label": "Diplo's Run Club — San Francisco official event page",
                "url": "https://diplosrunclub.com/san-francisco",
            },
            {
                "label": "SFMTA weekly transit and traffic advisory (Oct 15-21, 2026)",
                "url": (
                    "https://www.sfmta.com/press-releases/"
                    "sfmta-transit-and-traffic-advisory-week-thursday-october-15-through-"
                    "wednesday-october-21-2026"
                ),
            },
        ],
        "disposition": (
            "Row published as ticketed with “registration price is not stated on the official "
            "page”; re-check the organizer checkout for a price before quoting one."
        ),
    },
    {
        "id": "flag-exploratorium-price-unstated",
        "event_id": "exploratorium-after-dark",
        "event": "Exploratorium After Dark (weekly, Thursdays)",
        "issue": (
            "Cost gap: the official After Dark calendar page confirms the weekly Thursday "
            "6:00-10:00 p.m. programme, the 18+ age rule and the dated 2026 themes, and it states "
            "that tickets are required and that advance purchase is strongly recommended, but it "
            "publishes no admission price on that page."
        ),
        "sources": [
            {
                "label": "Exploratorium — After Dark Thursday Nights",
                "url": "https://www.exploratorium.edu/visit/calendar/after-dark",
            }
        ],
        "disposition": (
            "Row classed as ticketed with the price left unstated; add a price only when the "
            "official ticketing page states one."
        ),
    },
    {
        "id": "flag-nutcracker-price-unstated",
        "event_id": "sf-ballet-nutcracker-2026",
        "event": "San Francisco Ballet — Nutcracker (Dec 4-27, 2026)",
        "issue": (
            "Cost gap: the official production page publishes the full dated performance calendar "
            "at the War Memorial Opera House and a ticket-purchase flow, but lists no ticket "
            "prices (it only says “Programming, casting, and prices subject to change”). The "
            "separately ticketed Nutcracker Nightcap afterparty is listed at $150 and explicitly "
            "excludes a performance ticket, so that figure is not the performance price."
        ),
        "sources": [
            {
                "label": "San Francisco Ballet — Nutcracker production page",
                "url": "https://www.sfballet.org/productions/nutcracker/",
            }
        ],
        "disposition": (
            "Row classed as ticketed with “prices are not listed on the production page”; no "
            "price inferred from the ticketing partner."
        ),
    },
    {
        "id": "flag-sundaystreets-free-wording",
        "event_id": "sunday-streets-2026",
        "event": "Sunday Streets SF (2026 season) and the Excelsior edition",
        "issue": (
            "Wording nuance: no Sunday Streets page uses the phrase “free admission”. The free "
            "label rests on the organizer's About-page statement that the events feature “fun, "
            "free activities provided by local nonprofits, community groups and small businesses”, "
            "combined with the absence of any stated admission charge and the programme's "
            "description as an open-streets programme run with the SFMTA. Exhibitor fees "
            "($35, free for organisations on the route) and sponsorships are how the programme is "
            "funded, which is a separate matter from attendee admission."
        ),
        "sources": [
            {"label": "Sunday Streets SF — About", "url": "https://sundaystreetssf.com/about"},
            {
                "label": "Sunday Streets SF — Excelsior 2026 event page",
                "url": "https://sundaystreetssf.com/sunday-streets-excelsior-2026/",
            },
            {
                "label": "SFMTA weekly transit and traffic advisory (Oct 15-21, 2026)",
                "url": (
                    "https://www.sfmta.com/press-releases/"
                    "sfmta-transit-and-traffic-advisory-week-thursday-october-15-through-"
                    "wednesday-october-21-2026"
                ),
            },
        ],
        "disposition": (
            "Both rows are labelled Free with the supporting quote copied into the notes; human "
            "reviewer can downgrade to “not stated” if a stricter reading is preferred."
        ),
    },
    {
        "id": "flag-cornhole-cost-unstated",
        "event_id": "sfiac-olympic-club-cornhole-2026-10-23",
        "event": "SFIAC and Olympic Club Cornhole Tournament (Oct 23, 2026)",
        "issue": (
            "Cost gap: the only official source for this street-closure event is the SFMTA travel "
            "update, which describes “an afternoon of fundraising” on Stockton Street between "
            "Filbert and Union but publishes no entry fee, team fee or spectator charge. The "
            "organisers' own pages were not used as the source because the row's date, time and "
            "footprint come from the city advisory."
        ),
        "sources": [
            {
                "label": "SFMTA travel update — SFIAC and Olympic Club Cornhole Tournament",
                "url": (
                    "https://www.sfmta.com/travel-updates/"
                    "sfiac-and-olympic-club-cornhole-tournament-friday-october-23-2026"
                ),
            }
        ],
        "disposition": (
            "Row published with a blank cost (the row appears under “Cost not stated” on Flagged "
            "for Review); add a fee only when an official organiser page states one."
        ),
    },
    {
        "id": "flag-ledger-missing-cornhole-row",
        "event_id": "sfiac-olympic-club-cornhole-2026-10-23",
        "event": "Cross-session ledger mismatch — SFIAC & Olympic Club Cornhole Tournament",
        "issue": (
            "Process irregularity for manual review: the COORDINATION ledger entry for session "
            "arena/e79e0de2-maltaproj7 and the audit comment in verify.py both state that an "
            "\"SFIAC & Olympic Club Cornhole Tournament\" row was added in PR #25. No such record "
            "exists in data/events.json — a search of every record id, event name and source URL "
            "on 2026-10-18 returns nothing, and the pre-patch catalog held 148 rows with no "
            "cornhole entry. The row was therefore added in this session from the SFMTA travel "
            "update instead. No other row claimed by that ledger entry is missing."
        ),
        "sources": [
            {
                "label": "COORDINATION.md work ledger (prior session claims)",
                "url": "https://github.com/buffedlizard55-lab/MaltaProj7/blob/main/COORDINATION.md",
            },
            {
                "label": "SFMTA travel update used to add the row in this session",
                "url": (
                    "https://www.sfmta.com/travel-updates/"
                    "sfiac-and-olympic-club-cornhole-tournament-friday-october-23-2026"
                ),
            },
        ],
        "disposition": (
            "Row added in this session and published; the historical ledger entry is left intact "
            "and corrected here and in COORDINATION.md so the discrepancy is visible."
        ),
    },
    {
        "id": "flag-scaregrove-recheck",
        "event_id": "scaregrove-2026",
        "event": "Scaregrove (Oct 30, 2026, Sigmund Stern Grove)",
        "issue": (
            "Re-check limitation: the linked source (SF Recreation and Park Department calendar) "
            "is a JavaScript-rendered list, so the individual Scaregrove listing could not be "
            "re-read directly in the 2026-10-18 pass; the page returns its loading state to a "
            "text-only fetch. The row is retained on the earlier verification (date, 3-9 p.m. "
            "hours, Sigmund Stern Grove, free admission) and needs a manual confirmation against "
            "the rendered calendar or the department's programme listing before the event date."
        ),
        "sources": [
            {
                "label": "SF Recreation and Park Department calendar (JS-rendered)",
                "url": "https://sfrecpark.org/Calendar.aspx",
            }
        ],
        "disposition": (
            "Row retained as verified from the prior pass and flagged for manual re-check; no "
            "value changed in this session."
        ),
    },
]


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    events = data["events"]
    flags = data["flags"]
    by_id = {event["id"]: event for event in events}

    applied = []
    for event_id, fields in FIELD_UPDATES.items():
        event = by_id.get(event_id)
        if event is None:
            raise SystemExit(f"unknown event id in FIELD_UPDATES: {event_id}")
        for key, value in fields.items():
            if event.get(key) != value:
                event[key] = value
                applied.append(f"{event_id}.{key}")

    # Additions are idempotent: re-running the patch only re-applies field
    # updates, so a partially applied run can be completed safely.
    existing_ids = set(by_id)
    for event in NEW_EVENTS:
        if event["id"] in existing_ids:
            for key, value in event.items():
                target = by_id[event["id"]]
                if target.get(key) != value:
                    target[key] = value
                    applied.append(f"{event['id']}.{key} (re-applied)")
            continue
        events.append(event)
        existing_ids.add(event["id"])
        applied.append(f"+{event['id']}")

    existing_flag_ids = {flag["id"] for flag in flags}
    for flag in NEW_FLAGS:
        if flag["id"] in existing_flag_ids:
            continue
        flags.append(flag)
        existing_flag_ids.add(flag["id"])
        applied.append(f"+{flag['id']}")

    DATA_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"patched {len(applied)} changes:")
    for change in applied:
        print("  -", change)
    print(
        f"totals: {len(events)} records "
        f"({sum(1 for e in events if e['status'] == 'verified')} published), {len(flags)} flags"
    )


if __name__ == "__main__":
    main()
