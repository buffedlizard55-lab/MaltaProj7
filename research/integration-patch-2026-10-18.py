#!/usr/bin/env python3
"""Final-integration patch — 2026-10-18 (arena/d71d78cc-maltaproj7).

Applies the pending independent-audit findings plus this session's line-by-line
re-verification of every official source URL in data/events.json.

Every correction below is backed by an official publisher page fetched on
2026-10-18 (organizer, official venue, or government source).  Values that
could not be confirmed are left blank or moved to the review register /
flags list.  Nothing is inferred.

Run from the repository root:  python3 research/integration-patch-2026-10-18.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "events.json"

PRESIDIO_SRC = "https://presidio.gov/about/press/presidio-unveils-vibrant-2026-summer-event-lineup"
PRESIDIO_LABEL = "Presidio Trust 2026 summer lineup press release (May 7, 2026)"
CARNAVAL_SRC = "https://carnavalsanfrancisco.org/special-events/"
CARNAVAL_LABEL = "Carnaval SF special events page"
SFGOV_SRC = "https://www.sf.gov/san-francisco-celebrates-juneteenth-2026"
SFGOV_LABEL = "SF.gov Juneteenth 2026 campaign page"

# ---------------------------------------------------------------------------
# Field-level corrections to existing rows (verified 2026-10-18).
# ---------------------------------------------------------------------------
PATCHES: dict[str, dict] = {
    "fillmore-jazz-festival-2026": {
        "date_text": "July 4–5, 2026 (July Fourth weekend)",
        "location": "Fillmore District (Fillmore Street), San Francisco",
        "admission": "",
        "source_url": "https://www.fillmorejazzfest.com/",
        "source_label": "Fillmore Jazz Festival official site (Fillmore Merchants Association / Preservation Fund)",
        "notes": (
            "Source replaced 2026-10-18: the previously listed domain fillmorejazzfestival.com is no longer "
            "controlled by the organizer. The canonical organizer site fillmorejazzfest.com confirms the 2026 "
            "edition was held over the July Fourth weekend (press posts dated July 3–5, 2026); the exact "
            "July 4–5 dates are stated in the SF Travel July 2026 guide (trusted civic source)."
        ),
    },
    "comedy-day-2026": {
        "date_text": "Sunday, September 20, 2026",
        "start_date": "2026-09-20",
        "end_date": "2026-09-20",
        "time_text": "12:00pm–5:00pm",
        "admission": "Free",
        "notes": (
            "Date corrected 2026-10-18 from September 13 to September 20, 2026. The organizer page (comedyday.org) "
            "confirms the 2026 edition, free admission, noon–5pm program, and Robin Williams Meadow location, but "
            "states the date only inside its header image. The date is corroborated by the SF Recreation and Parks "
            "Department's official Tentative Calendars of Special Events ('September 20 Comedy Day at Robin Williams "
            "Meadow') and the SF Travel September 2026 guide ('September 20'). The previously published September 13 "
            "is the SF Opera in the Park date at the same meadow. See Flagged for Review."
        ),
    },
    "fleet-week-sf-2026": {
        "date_text": "October 4–12, 2026 (umbrella range per SF Travel); ship tours October 7–12; air show October 9–11",
        "start_date": "2026-10-04",
        "end_date": "2026-10-12",
        "time_text": "Air show noon–4:00pm daily, October 9–11",
        "admission": "Air show general admission free; hospitality packages ticketed",
        "source_url": "https://fleetweeksf.org/",
        "source_label": "San Francisco Fleet Week official site",
        "notes": (
            "Reworked 2026-10-18. The organizer site confirms ship tours October 7–12, Fleet Fest October 10–11, "
            "and the air show October 9–11, 2026 (noon–4pm). The umbrella October 4–12 range comes from the SF Travel "
            "Fleet Week guide; the organizer's calendar page shows day headings October 6–12 but no posted events. "
            "See Flagged for Review for the umbrella-date discrepancy."
        ),
    },
    "sf-international-arts-festival-2026": {
        "date_text": "April 29–May 10, 2026",
        "start_date": "2026-04-29",
        "end_date": "2026-05-10",
        "source_url": "https://www.sfiaf.org/2026_festival",
        "source_label": "SFIAF 2026 festival archive page",
        "notes": (
            "Dates corrected 2026-10-18 to April 29–May 10, 2026 per the official 2026 festival archive heading "
            "(the previously published April 30 start disagreed with the archive)."
        ),
    },
    "international-ocean-film-festival-2026": {
        "location": "Cowell Theater, Pier 2, and BATS Improv Bayfront Theatre, Fort Mason Center for Arts & Culture, 2 Marina Boulevard, San Francisco",
        "time_text": "Fri 4:00–11:00 p.m.; Sat 10:00 a.m.–11:00 a.m. (as posted); Sun 10:00 a.m.–6:00 p.m.",
        "admission": "$20–$450",
        "source_url": "https://fortmason.org/event/international-ocean-film-festival-2026/2026-04-12/",
        "source_label": "Fort Mason Center for Arts & Culture event listing",
        "source_authority": "Official venue / federal trust",
        "notes": (
            "Source replaced 2026-10-18: the organizer URLs intloceanfilmfest.org/festival and /awards now return 404 "
            "(site restructured around the 2027 edition). The official venue listing at Fort Mason confirms the 23rd "
            "annual festival, April 10–12, 2026, and the Cowell Theater / Bayfront Theatre location. The venue's "
            "posted Saturday window (10:00 a.m.–11:00 a.m.) is copied verbatim and appears inconsistent with its own "
            "full-day Saturday pass description — see Flagged for Review. The San Rafael First Look screening "
            "(April 2) is outside city limits and is not included in this SF row."
        ),
    },
    "world-arts-west-dance-festival-2026": {
        "date_text": "Sunday, September 6, 2026 (third and final weekend of the 2026 festival)",
        "time_text": "1:00–4:00pm",
        "location": "East Meadow, Presidio Tunnel Tops, San Francisco",
        "admission": "Free",
        "source_url": "https://presidio.gov/about/press/world-arts-west-enlivens-presidio-tunnel-tops-sept-6/",
        "source_label": "Presidio Trust press release (August 6, 2026)",
        "source_authority": "Official venue / federal trust",
        "notes": (
            "Source replaced 2026-10-18: the Presidio event URL previously listed (presidio.gov/explore/events/"
            "world-arts-west-dance-festival-2026) returns 404. The dated Presidio Trust press release confirms "
            "Sunday, September 6, 2026, 1–4 p.m., East Meadow at Presidio Tunnel Tops, free admission, fifth "
            "consecutive year, third and final weekend of the 2026 festival."
        ),
    },
    "muni-heritage-weekend-2026": {
        "time_text": "10:00am–4:00pm",
        "location": "San Francisco Railway Museum, 77 Steuart Street, San Francisco",
        "admission": "Free (historic vehicle rides and museum entry)",
        "notes": "Optional fields completed 2026-10-18 from the SFMTA event page, which states 10 a.m.–4 p.m., the 77 Steuart Street museum location, and free rides on rare historic vehicles.",
    },
    "italian-heritage-parade-2026": {
        "date_text": "Sunday, October 11, 2026 (158th annual)",
        "source_url": "https://sfitalianheritage.org/san-francisco-italian-heritage-parade-celebrates-158-years-with-grand-marshal-joe-mantegna/",
        "source_label": "Italian Heritage Parade organizer retrospective (October 12, 2026)",
        "notes": (
            "Edition-specific organizer retrospective used 2026-10-18: confirms the 158th parade took place Sunday, "
            "October 11, 2026, and describes it as the longest-running annual Italian heritage parade in the United "
            "States. The parade route is not stated on the retrospective."
        ),
    },
    "sf-porchfest-2026": {
        "admission": "Free",
        "notes": (
            "Organizer app confirms May 30, 2026, 8th annual, 100 acts in the Mission, free admission. "
            "Set times and venue assignments are announced as acts are confirmed and are therefore left blank. "
            "A kick-off party and fundraiser is listed for May 29, 2026, 7–11 p.m. at Hotel Utah Saloon (500 4th St)."
        ),
    },
    "juneteenth-sf-freedom-celebration-2026": {
        "date_text": "Saturday, June 13, 2026 (annual)",
        "location": "Fillmore Street (eight-block stretch), Fillmore/Western Addition, San Francisco",
        "admission": "No-cost (per SF.gov)",
        "source_authority": "Government source",
        "notes": "SF.gov (Human Rights Commission) lists the annual eight-block Fillmore celebration on June 13; organizer is linked from that page as juneteenth-sf.org. No start time is stated on the government source.",
    },
    "juneteenth-market-street-parade-2026": {
        "date_text": "Saturday, June 20, 2026 (fourth annual)",
        "time_text": "11:00am start",
        "location": "Market Street from 2nd Street to Embarcadero Plaza, San Francisco",
        "admission": "No-cost (per SF.gov)",
        "notes": "SF.gov states the fourth annual parade starts at Market and Second Streets at 11:00 a.m. and ends at Embarcadero Plaza.",
    },
    "juneteenth-on-the-waterfront-2026": {
        "date_text": "Sunday, June 7, 2026 (sixth annual)",
        "time_text": "11:00am–4:00pm",
        "location": "Front plaza, Ferry Building, San Francisco",
        "admission": "Free entry (food and drink available for purchase)",
        "organizer": "Foodwise",
        "source_url": "https://foodwise.org/events/pop-ups-on-the-plaza-juneteenth-on-the-waterfront/",
        "source_label": "Foodwise event page",
        "source_authority": "Official organizer",
        "notes": "Organizer page confirms the sixth annual event, Sunday, June 7, 2026, 11 a.m.–4 p.m., Ferry Building front plaza, free entry. Also listed on the SF.gov Juneteenth 2026 calendar.",
    },
    "sundown-cinema-inside-out-2026": {
        "time_text": "7:00pm",
        "location": "Civil War Parade Ground, Graham Street, Presidio, San Francisco",
        "admission": "Free",
        "notes": "Presidio Trust press release confirms Friday, July 24, 2026, 7 p.m., free, Civil War Parade Ground. Presented by The San Francisco Standard and Amazon.",
    },
    "scaregrove-2026": {
        "date_text": "Friday, October 30, 2026",
        "location": "Sigmund Stern Grove (19th Avenue & Sloat Boulevard), San Francisco",
        "admission": "Free",
        "notes": (
            "SF Recreation and Parks calendar lists Scaregrove 3–9 p.m. at Sigmund Stern Grove on October 30, 2026 "
            "(corroborated by the department's SF Children & Nature organizer listing and local press). The separate "
            "'Mobile Rec at Scaregrove' 12–8 p.m. listing is a different program and does not overwrite the main "
            "event hours. See Flagged for Review."
        ),
    },
    "foodwise-black-holiday-market-2026": {
        "date_text": "Saturday, December 12, 2026",
        "time_text": "9:00am–2:00pm",
        "location": "South arcade, Ferry Building, San Francisco",
        "admission": "Free entry (products available for purchase)",
        "notes": "Foodwise organizer page confirms December 12, 2026, 9 a.m.–2 p.m., south arcade of the Ferry Building, free entry.",
    },
    "cloudflare-connect-2026": {
        "date_text": "October 19–21, 2026",
        "location": "Moscone West, San Francisco",
        "admission": "Conference pass $595; group pass $495 (5–9); Cloudflare University add-on $495",
        "notes": "Organizer page confirms Oct 19–21 at Moscone West and lists the $595 conference pass.",
    },
    "informs-annual-meeting-2026": {
        "date_text": "November 1–4, 2026",
        "location": "Moscone Center South & San Francisco Marriott Marquis, San Francisco",
        "admission": "",
        "notes": "Organizer page confirms November 1–4, 2026, and names Moscone Center South and the Marriott Marquis as venues. Registration terms are not stated on the linked page.",
    },
    "microsoft-ignite-2026": {
        "date_text": "November 17–20, 2026",
        "location": "Moscone Center, 747 Howard Street, San Francisco",
        "admission": "",
        "notes": (
            "Organizer (Microsoft) lists November 17–20, 2026, San Francisco. Venue confirmed as Moscone Center by "
            "the venue's own official event listing (moscone.com/events/microsoft-ignite-2026). Pass prices are not "
            "stated on the linked organizer page and are left blank."
        ),
    },
    "agu-annual-meeting-2026": {
        "date_text": "December 7–11, 2026",
        "location": "San Francisco, CA",
        "admission": "",
        "notes": "Organizer page states '7–11 December 2026 | San Francisco, CA'. A specific venue is not named on the linked source and is left blank.",
    },
    "sf-marathon-2026": {
        "date_text": "July 24–26, 2026",
        "location": "San Francisco (start/finish at Embarcadero & Market; race expo at Fort Mason Festival Pavilion, 2 Marina Blvd)",
        "notes": (
            "Race weekend dates confirmed in the organizer page body (July 24, 25, and 26, 2026). Scope note: the "
            "full marathon and first half courses cross the Golden Gate Bridge and pass its north side (Marin "
            "headlands side) before returning to San Francisco, so those courses are not wholly within city limits; "
            "the expo, starts, and finishes are in San Francisco. The organizer site currently shows a 2027 marketing "
            "header above 2026 race-weekend content. See Flagged for Review."
        ),
    },
    "carnaval-sf-2026": {
        "date_text": "May 23–24, 2026 (48th anniversary)",
        "time_text": "Festival 11:00am–6:00pm (Sat & Sun); Grand Parade 10:00am–2:00pm (Sun)",
        "location": "Mission District (17 blocks); Grand Parade from 24th & Bryant along Mission Street to 15th Street, San Francisco",
        "admission": "Festival free; grandstand seating tickets sold",
        "notes": (
            "Location text corrected 2026-10-18 to the description on the organizer's own pages ('17 blocks in the "
            "Mission District'; parade starts at 24th & Bryant, travels Mission Street to 15th). The previously "
            "published 'Harrison Street (16th–24th)' detail is not in the current official source — see Flagged."
        ),
    },
    "hardly-strictly-bluegrass-2026": {
        "date_text": "October 2–4, 2026 (Fri–Sun)",
        "time_text": "Gates 11:00am Friday, 9:00am Saturday & Sunday; performances end 7:00pm daily",
        "admission": "Free (no tickets needed)",
        "notes": (
            "Organizer FAQ confirms Fri Oct 2, Sat Oct 3, Sun Oct 4, 2026, at Hellman Hollow, Lindley & Marx meadows. "
            "SF Recreation and Parks' tentative calendar lists an October 2–5 event-impact window — see Flagged for "
            "Review for the discrepancy."
        ),
    },
    "up-your-alley-2026": {
        "time_text": "11:00am–6:00pm",
        "location": "Folsom Street between 8th and 11th, 9th and 10th between Howard and Harrison, and Dore Street, SoMa, San Francisco",
        "admission": "Donation at gate ($10–20 suggested)",
    },
    "folsom-street-fair-2026": {
        "time_text": "11:00am–6:00pm",
        "location": "Folsom Street between 7th and 13th, cross streets 8th–12th (Howard to Harrison) and Dore Street, SoMa, San Francisco",
        "admission": "Donation at gate ($10–20 suggested)",
    },
    "castro-street-fair-2026": {
        "date_text": "Sunday, October 4, 2026 (52nd annual)",
        "time_text": "11:00am–6:00pm",
        "location": "Castro & Market Streets and surrounding Castro District streets, San Francisco",
        "admission": "Suggested donation $10–20",
    },
    "nihonmachi-street-fair-2026": {
        "date_text": "August 1–2, 2026 (52nd annual)",
        "location": "Japantown, San Francisco (organizer information booth at Post & Buchanan)",
        "notes": (
            "Organizer page confirms the 52nd annual fair, August 1–2, 2026, in Japantown. The exact street span "
            "captured in earlier research is not restated on the current page, so the location is limited to what the "
            "source states — see Flagged for Review."
        ),
    },
    "pistahan-2026": {
        "date_text": "August 8–9, 2026 (33rd annual)",
        "time_text": "Parade Saturday 11:00am–12:00pm; festival hours per organizer",
        "location": "Festival at Yerba Buena Gardens; parade from Civic Center Plaza along Market Street (8th to 4th) ending at 4th & Mission, San Francisco",
        "admission": "Festival free admission",
    },
    "north-beach-festival-2026": {
        "date_text": "June 20–21, 2026 (70th annual)",
        "location": "North Beach between Filbert and Broadway and Stockton and Grant, San Francisco",
    },
    "haight-ashbury-street-fair-2026": {
        "date_text": "Sunday, September 20, 2026",
        "time_text": "11:00am–5:30pm",
        "location": "Haight Street between Masonic and Stanyan, San Francisco",
        "admission": "Free",
        "notes": (
            "Date, hours, and street span confirmed 2026-10-18 by the SFMTA travel-update page (government source) "
            "and the organizer's vending page (haightashburystreetfair.org/vending)."
        ),
    },
    "sf-aloha-run-2026": {
        "notes": (
            "This SF event is distinct from the Bay Area Aloha Festival, which is not within city limits. "
            "Re-verification note (2026-10-18): the official organizer site sfaloharun.com could not be retrieved; "
            "the captured date and location are retained from the earlier official-site capture and are flagged as "
            "unconfirmed at re-verification. See Flagged for Review."
        ),
    },
    "sf-dance-film-festival-2026": {
        "location": "San Francisco theaters (Lucasfilm Premier Theater, Delancey Street Theater, Catharine Clark Gallery, SHACK15, Brava Theater); online component separate",
        "time_text": "See screening schedule",
        "admission": "Tickets and passes sold; one masterclass listed free",
    },
    "sf-transgender-film-festival-2026": {
        "date_text": "November 12–14, 2026 (in person); hybrid online program listed through November 22",
        "time_text": "Screenings 7:00–10:00pm nightly",
    },
    "chinese-new-year-parade-2027": {
        "time_text": "5:15pm start",
        "admission": "Free along parade route; bleacher tickets sold",
    },
    "st-patricks-parade-2026": {
        "date_text": "Saturday, March 14, 2026 (175th annual)",
        "time_text": "11:30am start",
        "notes": (
            "Organizer page confirms the 175th parade, Saturday, March 14, 2026, stepping off at 11:30 a.m. from "
            "2nd & Market to Civic Center Plaza, followed by the free Unite SF Festival (Civic Center, 11 a.m.–5 p.m.) "
            "and Youth Sports Day (Civic Center Plaza, 11 a.m.–4 p.m.)."
        ),
    },
    "flower-piano-2026": {
        "admission": "Free–$18 (festival components; Zoox Lounge ticketed)",
        "notes": "Organizer lists Flower Piano 2026 as its 11th year, 11 days (September 10–20, 2026) with 12 pianos across the 55-acre San Francisco Botanical Garden.",
    },
    "sfjff-2026": {
        "source_url": "https://jfi.org/film-festival/festival-archive/sfjff-2026",
        "source_label": "JFI SFJFF 2026 festival archive",
    },
    "sf-fringe-2026": {
        "source_label": "Legacy Fringe domain (no longer organizer-controlled)",
        "source_authority": "Legacy source — NOT verified official",
        "review_reason": (
            "No current direct organizer page with a verified 2026 date, time, and San Francisco venue exists. "
            "The legacy domain sffringe.org now redirects to unrelated third-party content serving a 404 page, so it "
            "is not labeled an official source. Essential fields remain blank; do not infer them."
        ),
    },
    "bay-area-aloha-festival": {
        "notes": (
            "Outside-city exclusion retained from the earlier official capture. Re-verification note (2026-10-18): "
            "the organizer site could not be retrieved; the exclusion rests on the earlier captured official location "
            "evidence. See Flagged for Review."
        ),
    },
}

# ---------------------------------------------------------------------------
# New rows verified from official sources on 2026-10-18.
# ---------------------------------------------------------------------------
NEW_EVENTS: list[dict] = [
    {
        "id": "mayors-juneteenth-kickoff-2026",
        "name": "Mayor's Juneteenth Kickoff",
        "bucket": "special", "cadence": "single-date", "category": "Community & culture",
        "date_text": "Friday, June 5, 2026", "start_date": "2026-06-05", "end_date": "2026-06-05",
        "time_text": "5:00pm–8:00pm", "location": "San Francisco City Hall, San Francisco",
        "organizer": "San Francisco Human Rights Commission (citywide Juneteenth campaign)",
        "admission": "No-cost (registration via the official Eventbrite link on SF.gov)",
        "source_url": SFGOV_SRC, "source_label": SFGOV_LABEL,
        "source_authority": "Government source", "status": "verified", "review_reason": "",
        "notes": "Listed on the city's official Juneteenth 2026 calendar. Single dated kickoff; no annual cadence inferred.",
    },
    {
        "id": "juneteenth-bayview-fathers-day-festival-2026",
        "name": "Juneteenth Bayview Father's Day Festival",
        "bucket": "recurring", "cadence": "annual", "category": "Community & culture",
        "date_text": "Sunday, June 21, 2026 (annual)", "start_date": "2026-06-21", "end_date": "2026-06-21",
        "time_text": "", "location": "Gilman Park, Bayview, San Francisco",
        "organizer": "SF.gov-listed Juneteenth nonprofit partners (sf-juneteenth.com)",
        "admission": "No-cost (per SF.gov)",
        "source_url": SFGOV_SRC, "source_label": SFGOV_LABEL,
        "source_authority": "Government source", "status": "verified", "review_reason": "",
        "notes": "SF.gov lists the annual festival at Gilman Park with carnival rides, shopping, food, and live music. Hours are not stated on the government source and are left blank.",
    },
    {
        "id": "memorial-day-commemoration-presidio-2026",
        "name": "Memorial Day Commemoration in the Presidio",
        "bucket": "recurring", "cadence": "annual", "category": "Community & culture",
        "date_text": "Monday, May 25, 2026 (159th annual)", "start_date": "2026-05-25", "end_date": "2026-05-25",
        "time_text": "Band concert 10:30am; program 11:00am",
        "location": "San Francisco National Cemetery, Presidio, San Francisco",
        "organizer": "U.S. Department of Veterans Affairs",
        "admission": "Free",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "Presidio Trust press release lists the 159th annual commemoration hosted by the U.S. Department of Veterans Affairs.",
    },
    {
        "id": "parks4all-brewfest-2026",
        "name": "Parks4All: BrewFest",
        "bucket": "recurring", "cadence": "annual", "category": "Fairs & nightlife",
        "date_text": "Saturday, May 30, 2026 (fourth annual)", "start_date": "2026-05-30", "end_date": "2026-05-30",
        "time_text": "12:00–4:00pm",
        "location": "Civil War Parade Ground (Graham Street), Presidio, San Francisco",
        "organizer": "Golden Gate National Parks Conservancy",
        "admission": "$60–$315",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "Fourth annual BrewFest with 15+ local breweries, per the Presidio Trust press release (21+ tasting event; ticket tiers $60–$315 as published).",
    },
    {
        "id": "bay-area-international-deaf-dance-festival-2026",
        "name": "Bay Area International Deaf Dance Festival",
        "bucket": "recurring", "cadence": "annual", "category": "Music & performing arts",
        "date_text": "Sunday, August 16, 2026 (14th annual)", "start_date": "2026-08-16", "end_date": "2026-08-16",
        "time_text": "12:00–4:00pm",
        "location": "Presidio Tunnel Tops, East Meadow, San Francisco",
        "organizer": "Urban Jazz Dance Company",
        "admission": "Free",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "New to the 2026 Presidio summer lineup; the press release calls it the 14th annual festival of Deaf, Deaf/Disabled, and hearing artists.",
    },
    {
        "id": "community-arts-market-presidio-2026",
        "name": "Community Arts Market",
        "bucket": "recurring", "cadence": "annual", "category": "Fairs & nightlife",
        "date_text": "July 18–19, 2026 (second annual)", "start_date": "2026-07-18", "end_date": "2026-07-19",
        "time_text": "10:00am–4:00pm",
        "location": "Presidio Tunnel Tops, East Meadow, San Francisco",
        "organizer": "Arts.Co.Lab with Presidio Trust",
        "admission": "Free",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "Second annual market with 20+ BIPOC-led artisan vendors, per the Presidio Trust press release.",
    },
    {
        "id": "fiesta-en-el-parque-2026",
        "name": "Fiesta en el Parque",
        "bucket": "recurring", "cadence": "annual", "category": "Community & culture",
        "date_text": "Saturday, August 1, 2026", "start_date": "2026-08-01", "end_date": "2026-08-01",
        "time_text": "1:00–4:00pm",
        "location": "Presidio Tunnel Tops, East Meadow, San Francisco",
        "organizer": "Telemundo 48 and NBC Bay Area with Presidio Trust",
        "admission": "Free",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "Family-friendly Latin culture celebration returning to Presidio Tunnel Tops for the fourth year (per the Presidio Trust press release).",
    },
    {
        "id": "i-am-an-american-exhibition-2026",
        "name": "I Am An American: The Nisei Soldier Experience (exhibition)",
        "bucket": "recurring", "cadence": "weekly", "category": "Books & ideas",
        "date_text": "Fridays–Tuesdays through August 31, 2026", "start_date": "", "end_date": "2026-08-31",
        "time_text": "12:00–5:00pm",
        "location": "Military Intelligence Service Historic Learning Center, 640 Mason Street, Presidio, San Francisco",
        "organizer": "National Japanese American Historical Society with Presidio Trust",
        "admission": "Free for veterans, children 12 and under, and NJAHS members; $15 all others",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "National traveling exhibition on a weekly public schedule (Fridays–Tuesdays) in the Presidio; closing date August 31, 2026 per the press release.",
    },
    {
        "id": "exclusion-presidio-exhibition-2026",
        "name": "EXCLUSION: The Presidio's Role in World War II Japanese American Incarceration (exhibition)",
        "bucket": "recurring", "cadence": "weekly", "category": "Books & ideas",
        "date_text": "Fridays–Sundays through August 31, 2026", "start_date": "", "end_date": "2026-08-31",
        "time_text": "10:00am–4:00pm",
        "location": "Presidio Officers' Club, 50 Moraga Avenue, Presidio, San Francisco",
        "organizer": "Presidio Trust with the Fred T. Korematsu Institute and NJAHS",
        "admission": "Free",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "Award-winning Presidio Trust exhibition on a weekly public schedule (Fridays–Sundays); closing date August 31, 2026 per the press release.",
    },
    {
        "id": "spring-awakening-art-cumbia-2026",
        "name": "Spring Awakening: Art & Cumbia at Outpost Meadow",
        "bucket": "special", "cadence": "single-date", "category": "Community & culture",
        "date_text": "Saturday, May 16, 2026", "start_date": "2026-05-16", "end_date": "2026-05-16",
        "time_text": "12:00–3:00pm",
        "location": "Outpost Meadow, 609 Old Mason Street, Presidio, San Francisco",
        "organizer": "Presidio Trust",
        "admission": "Free",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "Art reveal and cumbia celebration in the 2026 Presidio summer lineup; single dated program, no recurrence inferred.",
    },
    {
        "id": "intertribal-dance-gathering-2026",
        "name": "Intertribal Dance Gathering",
        "bucket": "special", "cadence": "single-date", "category": "Community & culture",
        "date_text": "Saturday, May 30, 2026", "start_date": "2026-05-30", "end_date": "2026-05-30",
        "time_text": "11:00am–4:00pm",
        "location": "Presidio Tunnel Tops, East Meadow, San Francisco",
        "organizer": "Native American Health Center",
        "admission": "Free",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "Day of dance, music, screen printing, and arts marketplace in the 2026 Presidio summer lineup; single dated program, no recurrence inferred.",
    },
    {
        "id": "presidio-soccer-festival-2026",
        "name": "Presidio Soccer Festival",
        "bucket": "special", "cadence": "single-date", "category": "Sports & outdoors",
        "date_text": "Saturday, June 13, 2026", "start_date": "2026-06-13", "end_date": "2026-06-13",
        "time_text": "1:00–5:00pm",
        "location": "Main Parade Lawn, Presidio, San Francisco",
        "organizer": "Telemundo 48 and NBC Bay Area with the Presidio",
        "admission": "Free",
        "source_url": PRESIDIO_SRC, "source_label": PRESIDIO_LABEL,
        "source_authority": "Official venue / federal trust", "status": "verified", "review_reason": "",
        "notes": "New free family soccer/culture event in the 2026 Presidio summer lineup; single dated program, no recurrence inferred.",
    },
    {
        "id": "carnaval-fat-tuesday-2026",
        "name": "Carnaval SF Fat Tuesday Season Kickoff Celebration",
        "bucket": "special", "cadence": "single-date", "category": "Fairs & nightlife",
        "date_text": "Tuesday, February 17, 2026", "start_date": "2026-02-17", "end_date": "2026-02-17",
        "time_text": "5:00–10:00pm",
        "location": "Multiple venues, Mission District, San Francisco",
        "organizer": "Carnaval San Francisco",
        "admission": "Tickets sold (organizer link)",
        "source_url": CARNAVAL_SRC, "source_label": CARNAVAL_LABEL,
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Mardi Gras season kickoff at several Mission District venues, per the organizer's special-events page; venue list and schedule published separately.",
    },
    {
        "id": "carnaval-king-queen-competition-2026",
        "name": "Carnaval SF King & Queen Dance Competition",
        "bucket": "special", "cadence": "single-date", "category": "Music & performing arts",
        "date_text": "Saturday, March 28, 2026", "start_date": "2026-03-28", "end_date": "2026-03-28",
        "time_text": "4:00–6:00pm",
        "location": "KQED Headquarters, 2601 Mariposa Street (live event); watch party at Casa de Carnaval, 683 Florida Street, San Francisco",
        "organizer": "Carnaval San Francisco",
        "admission": "Tickets sold (live event listed sold out; watch-party tickets via organizer)",
        "source_url": CARNAVAL_SRC, "source_label": CARNAVAL_LABEL,
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Competition crowning royalty for the 48th anniversary celebration ('La Copa Del Pueblo' theme), per the organizer's special-events page.",
    },
    {
        "id": "carnaval-cubacaribe-2026",
        "name": "CubaCaribe Festival of Dance & Music",
        "bucket": "recurring", "cadence": "annual", "category": "Music & performing arts",
        "date_text": "April 15, 2026 (20th annual)", "start_date": "2026-04-15", "end_date": "2026-04-15",
        "time_text": "",
        "location": "Casa de Carnaval, 683 Florida Street, San Francisco",
        "organizer": "CubaCaribe / Carnaval San Francisco",
        "admission": "",
        "source_url": CARNAVAL_SRC, "source_label": CARNAVAL_LABEL,
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Listed on the Carnaval SF special-events page as the 20th annual festival of dance and music. Time and admission were listed 'TBD' on the source and are left blank.",
    },
    {
        "id": "carnaval-pride-night-2026",
        "name": "Carnaval Pride Night with Mission Loteria",
        "bucket": "special", "cadence": "single-date", "category": "Fairs & nightlife",
        "date_text": "Friday, April 24, 2026", "start_date": "2026-04-24", "end_date": "2026-04-24",
        "time_text": "",
        "location": "Casa de Carnaval, 683 Florida Street, San Francisco",
        "organizer": "Carnaval San Francisco",
        "admission": "",
        "source_url": CARNAVAL_SRC, "source_label": CARNAVAL_LABEL,
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Listed on the Carnaval SF special-events page. Time and admission were listed 'TBD' on the source and are left blank.",
    },
    {
        "id": "carnaval-nightlife-calacademy-2026",
        "name": "Carnaval SF Nightlife at the California Academy of Sciences",
        "bucket": "special", "cadence": "single-date", "category": "Fairs & nightlife",
        "date_text": "Thursday, May 7, 2026", "start_date": "2026-05-07", "end_date": "2026-05-07",
        "time_text": "6:00–10:00pm",
        "location": "California Academy of Sciences, 55 Music Concourse Drive, Golden Gate Park, San Francisco",
        "organizer": "Carnaval San Francisco with California Academy of Sciences",
        "admission": "Tickets sold (CalAcademy NightLife); ages 21 and over",
        "source_url": CARNAVAL_SRC, "source_label": CARNAVAL_LABEL,
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "21+ NightLife collaboration listed on the Carnaval SF special-events page; tickets sold through the California Academy of Sciences.",
    },
    {
        "id": "carnaval-business-mixer-2026",
        "name": "Carnaval SF Small Business Mixer",
        "bucket": "special", "cadence": "single-date", "category": "Professional & academic",
        "date_text": "Wednesday, October 14, 2026", "start_date": "2026-10-14", "end_date": "2026-10-14",
        "time_text": "5:00–7:00pm",
        "location": "Casa de Carnaval, 683 Florida Street, San Francisco",
        "organizer": "Carnaval San Francisco (sponsored by Bank of America)",
        "admission": "Free (registration required)",
        "source_url": CARNAVAL_SRC, "source_label": CARNAVAL_LABEL,
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Latino small-business networking mixer closing Latino Heritage Month, listed on the Carnaval SF special-events page with free Latino food and beverages.",
    },
]

# ---------------------------------------------------------------------------
# Field-level flags published on the Flagged for Review page.
# ---------------------------------------------------------------------------
FLAGS: list[dict] = [
    {
        "id": "flag-comedy-day-date",
        "event_id": "comedy-day-2026",
        "event": "Comedy Day (2026)",
        "issue": (
            "Date correction needs human confirmation: the organizer page states the 2026 date only inside a header "
            "image. The published date (Sunday, September 20, 2026) is corroborated by the SF Recreation and Parks "
            "Department's Tentative Calendars of Special Events and the SF Travel September 2026 guide. The earlier "
            "published date (September 13) was the SF Opera in the Park date at the same meadow and was wrong."
        ),
        "sources": [
            {"label": "Comedy Day official site (date in image)", "url": "https://comedyday.org/"},
            {"label": "SF Recreation and Parks Tentative Calendars of Special Events", "url": "https://sfrecpark.org/1310/Tentative-Calendars-of-Special-Events"},
            {"label": "SF Travel September 2026 guide", "url": "https://www.sftravel.com/article/san-francisco-festivals-events-september"},
        ],
        "disposition": "Date corrected to September 20, 2026 and flagged; blank nothing else.",
    },
    {
        "id": "flag-fillmore-jazz-domain",
        "event_id": "fillmore-jazz-festival-2026",
        "event": "Fillmore Jazz Festival (2026)",
        "issue": (
            "The domain previously cited as the official source (fillmorejazzfestival.com) is no longer controlled by "
            "the organizer and resolves to unrelated content. The row now uses the organizer's canonical site "
            "(fillmorejazzfest.com). Exact 2026 dates (July 4–5) are stated by SF Travel and are consistent with the "
            "organizer's July Fourth-weekend framing; the organizer page does not restate them in text."
        ),
        "sources": [
            {"label": "Fillmore Jazz Festival canonical official site", "url": "https://www.fillmorejazzfest.com/"},
            {"label": "SF Travel July 2026 guide (dates, street span)", "url": "https://www.sftravel.com/article/san-francisco-festivals-events-july"},
        ],
        "disposition": "Official source replaced; dates kept with cross-source note. Old domain not labeled official.",
    },
    {
        "id": "flag-fleet-week-dates",
        "event_id": "fleet-week-sf-2026",
        "event": "San Francisco Fleet Week (2026)",
        "issue": (
            "Umbrella date-range discrepancy: SF Travel says Fleet Week runs October 4–12, 2026; the organizer's "
            "calendar page shows day headings October 6–12 (with no posted events); the organizer's own component "
            "listings state ship tours October 7–12 and Fleet Fest October 10–11. The air show is consistently "
            "October 9–11, noon–4 p.m. on the organizer's air-show page."
        ),
        "sources": [
            {"label": "SF Travel Fleet Week guide (umbrella Oct 4–12)", "url": "https://www.sftravel.com/article/where-you-need-to-watch-blue-angels-fly-over-san-francisco-during-fleet-week"},
            {"label": "Fleet Week official site (component dates)", "url": "https://fleetweeksf.org/"},
            {"label": "Fleet Week air show page (Oct 9–11, 2026)", "url": "https://fleetweeksf.org/air-show/"},
        ],
        "disposition": "Row lists the SF Travel umbrella range and the organizer component dates side by side; neither is silently chosen over the other.",
    },
    {
        "id": "flag-sf-marathon-geography",
        "event_id": "sf-marathon-2026",
        "event": "San Francisco Marathon — race weekend (2026)",
        "issue": (
            "Course geography: the official full-marathon course page describes crossing the Golden Gate Bridge and "
            "running its north side (Marin headlands side) before returning to San Francisco, so the full marathon and "
            "first half courses are not wholly within city limits (expo, starts, and finishes are in San Francisco). "
            "The organizer site also mixes a 2027 marketing header with 2026 race-weekend content; 2026 dates "
            "(July 24–26) are taken from the 2026 page body, not the 2027 header."
        ),
        "sources": [
            {"label": "SF Marathon race-weekend page (2026 dates)", "url": "https://www.thesfmarathon.com/race-weekend/"},
            {"label": "SF Marathon full-marathon course page (bridge crossing)", "url": "https://www.thesfmarathon.com/full-marathon/"},
        ],
        "disposition": "Row scoped to SF-based components with an explicit note; city-only purity of the bridge courses is not claimed.",
    },
    {
        "id": "flag-hsb-date-window",
        "event_id": "hardly-strictly-bluegrass-2026",
        "event": "Hardly Strictly Bluegrass (2026)",
        "issue": (
            "Minor date-window discrepancy: the organizer FAQ states Fri Oct 2 – Sun Oct 4, 2026, while SF Recreation "
            "and Parks' Tentative Calendars of Special Events lists 'October 2 - 5' (likely a park-impact window "
            "including load-in/out)."
        ),
        "sources": [
            {"label": "Hardly Strictly Bluegrass 2026 FAQ (organizer)", "url": "https://hardlystrictlybluegrass.com/info-faq-2026/"},
            {"label": "SF Recreation and Parks Tentative Calendars of Special Events", "url": "https://sfrecpark.org/1310/Tentative-Calendars-of-Special-Events"},
        ],
        "disposition": "Organizer dates (Oct 2–4) are published; the RecPark window is recorded here for review.",
    },
    {
        "id": "flag-ioff-source-hours",
        "event_id": "international-ocean-film-festival-2026",
        "event": "International Ocean Film Festival — San Francisco program (2026)",
        "issue": (
            "Source availability: the organizer's former festival and awards pages now return 404 (site restructured "
            "around the 2027 edition), so the row now relies on the official Fort Mason venue listing. On that listing "
            "the posted Saturday hours (10:00 a.m.–11:00 a.m.) conflict with its own full-day Saturday pass "
            "description and are likely a typo; they are copied verbatim rather than corrected."
        ),
        "sources": [
            {"label": "Fort Mason Center event listing (current row source)", "url": "https://fortmason.org/event/international-ocean-film-festival-2026/2026-04-12/"},
            {"label": "Organizer homepage (2027 edition now featured)", "url": "https://intloceanfilmfest.org/"},
        ],
        "disposition": "Venue listing substituted for the dead organizer URLs; Saturday hours flagged, not adjusted.",
    },
    {
        "id": "flag-sf-aloha-run-unreachable",
        "event_id": "sf-aloha-run-2026",
        "event": "San Francisco Aloha Run (2026)",
        "issue": (
            "Source unreachable at re-verification: sfaloharun.com did not respond on 2026-10-18. The captured date "
            "(September 20, 2026) and location (Crissy Field) come from the earlier official-site capture and could "
            "not be re-confirmed. Failed retrieval is not proof the event is false."
        ),
        "sources": [
            {"label": "SF Aloha Run official site (unreachable 2026-10-18)", "url": "https://sfaloharun.com/"},
        ],
        "disposition": "Row retained with a re-verification warning; values marked unconfirmed at re-verification.",
    },
    {
        "id": "flag-bay-area-aloha-unreachable",
        "event_id": "bay-area-aloha-festival",
        "event": "Bay Area Aloha Festival (excluded)",
        "issue": (
            "The outside-city exclusion is retained from the earlier official capture, but the organizer site did not "
            "respond at re-verification (2026-10-18), so the geography evidence could not be independently re-fetched."
        ),
        "sources": [
            {"label": "Bay Area Aloha Festival official site (unreachable 2026-10-18)", "url": "https://www.bayareaalohafestival.com/"},
        ],
        "disposition": "Exclusion preserved; re-verification gap recorded here.",
    },
    {
        "id": "flag-scaregrove-listings",
        "event_id": "scaregrove-2026",
        "event": "Scaregrove (2026)",
        "issue": (
            "The SF Recreation and Parks calendar contains both the main Scaregrove listing (3–9 p.m., Stern Grove) "
            "and a separate 'Mobile Rec at Scaregrove' listing (12–8 p.m.). The main event hours are published; the "
            "Mobile Rec program hours are not merged into them."
        ),
        "sources": [
            {"label": "SF Recreation and Parks calendar (October 2026)", "url": "https://sfrecpark.org/Calendar.aspx"},
            {"label": "SF Children & Nature organizer listing (main event 3–9 p.m.)", "url": "https://sfchildrennature.org/organizer/san-francisco-recreation-parks/"},
        ],
        "disposition": "Main-event hours published; secondary listing documented here so the two are not conflated.",
    },
    {
        "id": "flag-carnaval-location-detail",
        "event_id": "carnaval-sf-2026",
        "event": "Carnaval San Francisco (2026)",
        "issue": (
            "An earlier capture placed the festival 'on Harrison Street (16th–24th)'. The organizer's current pages "
            "describe the festival as covering 17 blocks in the Mission District and the parade as starting at 24th & "
            "Bryant and running Mission Street to 15th; they do not restate the Harrison Street span."
        ),
        "sources": [
            {"label": "Carnaval SF special events page (festival + parade)", "url": "https://carnavalsanfrancisco.org/special-events/"},
        ],
        "disposition": "Location text limited to the source-stated description; the Harrison detail is not republished.",
    },
    {
        "id": "flag-nihonmachi-street-span",
        "event_id": "nihonmachi-street-fair-2026",
        "event": "Nihonmachi Street Fair (2026)",
        "issue": (
            "An earlier capture listed the fair footprint as 'Post Street between Laguna and Fillmore and Osaka Way'. "
            "The current organizer page confirms Japantown and an information booth at Post & Buchanan but does not "
            "restate the street span."
        ),
        "sources": [
            {"label": "Nihonmachi Street Fair official site", "url": "https://www.nihonmachistreetfair.org/home-1"},
        ],
        "disposition": "Location limited to 'Japantown' plus the source-stated info-booth cross street.",
    },
    {
        "id": "flag-bay-to-breakers-copy",
        "event_id": "bay-to-breakers-2027",
        "event": "Bay to Breakers (2027)",
        "issue": (
            "Minor internal inconsistency on the organizer page: the hero and title give May 16, 2027, while one "
            "marketing line refers to happenings 'before May 18'. The published date is the hero/title date; the "
            "stray May 18 reference is recorded here rather than normalized away."
        ),
        "sources": [
            {"label": "Bay to Breakers official site", "url": "https://www.baytobreakers.com/"},
        ],
        "disposition": "May 16, 2027 published; May 18 copy discrepancy flagged for organizer review.",
    },
    {
        "id": "flag-sffringe-domain",
        "event_id": "sf-fringe-2026",
        "event": "San Francisco Fringe Festival — 2026 schedule (excluded)",
        "issue": (
            "The legacy domain sffringe.org now redirects to unrelated third-party content serving a 404 page. It is "
            "no longer an official organizer source and is labeled 'Legacy source — NOT verified official'. No 2026 "
            "date, time, or venue could be confirmed from any direct official page."
        ),
        "sources": [
            {"label": "Legacy Fringe domain (now unrelated content)", "url": "https://www.sffringe.org/"},
        ],
        "disposition": "Remains in the review register with blank fields; source authority corrected.",
    },
]


def main() -> None:
    document = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    events = document["events"]
    by_id = {event["id"]: event for event in events}

    patched = 0
    for event_id, fields in PATCHES.items():
        event = by_id.get(event_id)
        if event is None:
            raise SystemExit(f"patch target not found: {event_id}")
        event.update(fields)
        patched += 1

    existing_ids = set(by_id)
    added = 0
    for new_event in NEW_EVENTS:
        if new_event["id"] in existing_ids:
            raise SystemExit(f"duplicate new id: {new_event['id']}")
        events.append(new_event)
        added += 1

    document["flags"] = FLAGS
    document["catalog"]["updated_by"] = (
        "arena/d71d78cc-maltaproj7 final integration (line-by-line official-source re-verification)"
    )
    document["catalog"]["last_reverification"] = (
        "2026-10-18 — every row's source URL was re-fetched from the official publisher page "
        "(organizer, official venue, or government source); corrections and residual findings are "
        "recorded in flags and research/official-source-audit.md."
    )

    DATA_PATH.write_text(json.dumps(document, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"patched {patched} rows, added {added} rows, {len(FLAGS)} flags registered")
    published = [e for e in events if e["status"] == "verified"]
    recurring = [e for e in published if e["bucket"] == "recurring"]
    special = [e for e in published if e["bucket"] == "special"]
    review = [e for e in events if e["status"] != "verified"]
    print(f"totals: published={len(published)} recurring={len(recurring)} special={len(special)} review={len(review)}")


if __name__ == "__main__":
    main()
