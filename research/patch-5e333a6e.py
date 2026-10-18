#!/usr/bin/env python3
"""Coverage-gap patch (S2), session arena/5e333a6e-maltaproj7, 2026-10-18.

Adds rows that were directly verified on 2026-10-18 against official
organizer, official venue (Moscone Center event pages), or government
(SFMTA) pages.  Values not stated by the linked source are left blank;
conflicting values are blanked and flagged.  Nothing is inferred: rows whose
source does not state a recurrence are classed as dated special events.

Idempotent: rows/flags whose id already exists are skipped.
Run from the repository root:  python3 research/patch-5e333a6e.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "events.json"

PRO = "Professional & academic"
COM = "Community & culture"
FAIR = "Fairs & nightlife"
FOOD = "Food & markets"
SPORT = "Sports & outdoors"
BOOKS = "Books & ideas"

VENUE = "Official venue"
ORG = "Official organizer"
GOV = "Government source"

MOSCONE_LABEL = "Moscone Center official event listing"
MOSCONE_NOTE = (
    "Added 2026-10-18 (arena/5e333a6e) from the Moscone Center's own event page, which states "
    "the dates{extra}. Session times and pass prices are not stated there and are left blank."
)
LISTED_AT_MOSCONE = "Listed on the Moscone Center events calendar, San Francisco (hall not stated)"
SFMTA_ADVISORY_OCT15 = (
    "https://www.sfmta.com/press-releases/"
    "sfmta-transit-and-traffic-advisory-week-thursday-october-15-through-wednesday-october-21-2026"
)
SFMTA_ADVISORY_LABEL = "SFMTA Transit and Traffic Advisory, Oct 15–21, 2026 (press release)"


def row(**kw) -> dict:
    base = {
        "id": "", "name": "", "bucket": "special", "cadence": "single-event", "category": PRO,
        "date_text": "", "start_date": "", "end_date": "", "time_text": "", "location": "",
        "organizer": "", "admission": "", "source_url": "", "source_label": "",
        "source_authority": VENUE, "status": "verified", "review_reason": "", "notes": "",
    }
    base.update(kw)
    return base


def moscone(id_, name, slug, date_text, start, end, location, organizer, extra=""):
    return row(
        id=id_, name=name, date_text=date_text, start_date=start, end_date=end,
        cadence="single-date" if start == end else "single-event",
        location=location, organizer=organizer,
        source_url=f"https://www.moscone.com/events/{slug}", source_label=MOSCONE_LABEL,
        source_authority=VENUE, notes=MOSCONE_NOTE.format(extra=extra),
    )


NEW_ROWS: list[dict] = [
    # ---------------- Professional & academic (Moscone + organizers) ----------------
    moscone("ai-engineer-worlds-fair-2026", "AI Engineer World's Fair", "ai-engineer-worlds-fair-2026",
            "June 30–July 2, 2026", "2026-06-30", "2026-07-02", "Moscone Center, San Francisco",
            "AI Engineer", " and Moscone Center as the venue"),
    moscone("amd-advancing-ai-2026", "AMD Advancing AI", "amd-advancing-ai",
            "July 22–23, 2026", "2026-07-22", "2026-07-23", "Moscone Center, San Francisco", "AMD",
            " (\"July 22-23\" under the heading \"Advancing AI 2026\") and Moscone Center as the venue"),
    moscone("nph-affordable-housing-conference-2026",
            "Non-Profit Housing Association of Northern California — 47th Annual Affordable Housing Conference",
            "non-profit-housing-association-northern-california-47th-annual-affordable-housing-conference",
            "September 24, 2026", "2026-09-24", "2026-09-24", "Moscone Center, San Francisco",
            "Non-Profit Housing Association of Northern California (NPH)", " and Moscone Center as the venue"),
    moscone("coreweave-fully-connected-2026", "CoreWeave Fully Connected", "coreweave-fully-connected-2026",
            "September 29–October 1, 2026", "2026-09-29", "2026-10-01", "Moscone Center, San Francisco",
            "CoreWeave", " and Moscone Center as the venue"),
    moscone("semicon-west-2026", "SEMICON West", "semicon-west-2026",
            "October 13–15, 2026", "2026-10-13", "2026-10-15", "Moscone Center, San Francisco",
            "SEMICON West", " and Moscone Center as the venue"),
    moscone("techcrunch-disrupt-2026", "TechCrunch Disrupt", "techcrunch-disrupt-2026",
            "October 13–15, 2026", "2026-10-13", "2026-10-15", LISTED_AT_MOSCONE, "TechCrunch",
            " (\"October 13–15\" for TechCrunch Disrupt 2026) but not the hall"),
    moscone("current-san-francisco-2026", "Current San Francisco (Confluent)", "current-san-francisco-2026",
            "November 4–5, 2026", "2026-11-04", "2026-11-05", "Moscone West, San Francisco", "Confluent",
            " and Moscone West as the venue"),
    moscone("winter-fancyfaire-2027", "Specialty Food Association Winter FancyFaire",
            "specialty-food-association-winter-fancyfaire-2027",
            "January 17–19, 2027", "2027-01-17", "2027-01-19", LISTED_AT_MOSCONE,
            "Specialty Food Association", " but not the hall"),
    moscone("asco-gi-cancers-symposium-2027", "ASCO Gastrointestinal Cancers Symposium",
            "american-society-clinical-oncology-gi-cancers-symposium-2027",
            "January 21–23, 2027", "2027-01-21", "2027-01-23", "Moscone West, San Francisco",
            "American Society of Clinical Oncology (ASCO)", " and Moscone West as the venue"),
    moscone("spie-photonics-west-2027", "SPIE Photonics West", "spie-photonics-west-2027",
            "January 30–February 4, 2027", "2027-01-30", "2027-02-04", LISTED_AT_MOSCONE, "SPIE",
            " but not the hall; the page also says the event is held annually in San Francisco, but only the 2027 "
            "edition is recorded here"),
    moscone("asco-gu-cancers-symposium-2027", "ASCO Genitourinary Cancers Symposium",
            "american-society-clinical-oncology-gu-cancers-symposium-2027",
            "February 11–13, 2027", "2027-02-11", "2027-02-13", "Moscone West, San Francisco",
            "American Society of Clinical Oncology (ASCO)", " and Moscone West as the venue"),
    moscone("ors-annual-meeting-2027", "Orthopaedic Research Society Annual Meeting",
            "orthopaedic-research-society-2027-annual-meeting",
            "February 19–23, 2027", "2027-02-19", "2027-02-23", LISTED_AT_MOSCONE,
            "Orthopaedic Research Society (ORS)", " but not the hall"),
    row(id="gdc-festival-of-gaming-2027", name="GDC Festival of Gaming",
        date_text="March 1–5, 2027", start_date="2027-03-01", end_date="2027-03-05",
        location="Moscone Center, San Francisco", organizer="Game Developers Conference (GDC)",
        source_url="https://gdconf.com/", source_label="GDC official site", source_authority=ORG,
        notes="Added 2026-10-18 (arena/5e333a6e). Organizer site states the GDC Festival of Gaming, March 1–5, 2027, "
              "at Moscone Center; the Moscone event page (moscone.com/events/gdc-festival-gaming-2027) states the "
              "same dates and venue. Pass prices and hours were not captured and are left blank."),
    moscone("tdx-2027", "TDX (Salesforce developer conference)", "tdx-2027",
            "March 10–11, 2027", "2027-03-10", "2027-03-11", "Moscone Center, San Francisco", "Salesforce",
            " and Moscone Center as the venue"),
    moscone("aad-annual-meeting-2027", "American Academy of Dermatology Annual Meeting",
            "american-academy-dermatology-annual-meeting-2027",
            "March 19–23, 2027", "2027-03-19", "2027-03-23", LISTED_AT_MOSCONE,
            "American Academy of Dermatology (AAD)", " but not the hall"),
    row(id="rsac-conference-2027", name="RSAC Conference",
        date_text="April 5–8, 2027", start_date="2027-04-05", end_date="2027-04-08",
        location="Moscone Center and Yerba Buena Center for the Arts, San Francisco", organizer="RSAC",
        admission="Core pass from $1,695 early bird (through Dec 18, 2026); $2,495 regular",
        source_url="https://www.rsaconference.com/about/faq", source_label="RSAC Conference official FAQ",
        source_authority=ORG,
        notes="Added 2026-10-18 (arena/5e333a6e). The organizer FAQ states April 5–8, 2027 at Moscone Center and YBCA; "
              "the Moscone event page (moscone.com/events/rsac-2027-conference) states the same dates. Pass prices are "
              "from the organizer's registration page (rsaconference.com/usa)."),
    moscone("amcp-annual-meeting-2027", "Academy of Managed Care Pharmacy Annual Meeting (AMCP 2027)",
            "academy-managed-care-pharmacy-annual-meeting-2027",
            "April 13–16, 2027", "2027-04-13", "2027-04-16", LISTED_AT_MOSCONE,
            "Academy of Managed Care Pharmacy (AMCP)", " but not the hall"),
    moscone("atlassian-team-2027", "Atlassian Team ’27", "atlassian-team-27",
            "April 20–22, 2027", "2027-04-20", "2027-04-22", "Moscone Center, San Francisco", "Atlassian",
            " and Moscone Center as the venue"),
    moscone("asrs-annual-meeting-2027", "American Society of Retina Specialists Annual Meeting",
            "american-society-retina-specialists-annual-meeting-2027",
            "July 28–31, 2027", "2027-07-28", "2027-07-31", LISTED_AT_MOSCONE,
            "American Society of Retina Specialists (ASRS)", " but not the hall"),
    row(id="dreamforce-2027", name="Dreamforce",
        date_text="September 21–23, 2027", start_date="2027-09-21", end_date="2027-09-23",
        location="San Francisco (venue not stated by organizer) and Salesforce+", organizer="Salesforce",
        source_url="https://www.salesforce.com/dreamforce/df27-save-the-date/",
        source_label="Salesforce Dreamforce 2027 save-the-date page", source_authority=ORG,
        notes="Added 2026-10-18 (arena/5e333a6e). Organizer page states \"September 21-23, 2027 | San Francisco and "
              "Salesforce+\" without a venue, so the venue is blank and flagged. The 2026 edition (September 15–17) is "
              "past; it is documented on moscone.com/events/salesforce-dreamforce-2026."),
    row(id="jpm-healthcare-conference-2027", name="J.P. Morgan Healthcare Conference (45th annual)",
        date_text="January 11–14, 2027", start_date="2027-01-11", end_date="2027-01-14",
        location="San Francisco (venue not stated by organizer)", organizer="J.P. Morgan",
        admission="Invitation only",
        source_url="https://www.jpmorgan.com/about-us/events-conferences/health-care-conference",
        source_label="J.P. Morgan Healthcare Conference official page", source_authority=ORG,
        notes="Added 2026-10-18 (arena/5e333a6e). Organizer states the 45th annual conference, January 11–14, 2027, "
              "San Francisco, invitation only. The venue appears only on third-party sites and is left blank and flagged."),

    # ---------------- Museums / recurring programs ----------------
    row(id="famsf-free-saturdays", name="de Young & Legion of Honor — Free Saturdays for Bay Area residents",
        bucket="recurring", cadence="weekly", category=COM,
        date_text="Every Saturday", location="de Young Museum and Legion of Honor, San Francisco",
        organizer="Fine Arts Museums of San Francisco (FAMSF)",
        admission="Free general admission (permanent collection) for residents of the nine Bay Area counties",
        source_url="https://www.famsf.org/visit/free-reduced-admission",
        source_label="FAMSF free and reduced admission page", source_authority=VENUE,
        notes="Added 2026-10-18 (arena/5e333a6e). The museum page states free general admission every Saturday for "
              "residents of the nine Bay Area counties; special exhibitions are not included. Hours are not stated on "
              "that page and are left blank."),
    row(id="famsf-free-first-tuesdays", name="de Young & Legion of Honor — Free First Tuesdays",
        bucket="recurring", cadence="monthly", category=COM,
        date_text="First Tuesday of every month", location="de Young Museum and Legion of Honor, San Francisco",
        organizer="Fine Arts Museums of San Francisco (FAMSF)", admission="Free general admission",
        source_url="https://www.famsf.org/visit/free-reduced-admission",
        source_label="FAMSF free and reduced admission page", source_authority=VENUE,
        notes="Added 2026-10-18 (arena/5e333a6e). The museum page states general admission is free the first Tuesday "
              "of every month. Hours are not stated on that page and are left blank."),
    row(id="fort-mason-night-market-2026", name="Fort Mason Night Market",
        bucket="recurring", cadence="monthly", category=FOOD,
        date_text="September 18, October 16, and monthly on select Fridays in 2026",
        start_date="2026-09-18", time_text="5:00–10:00pm",
        location="Fort Mason Center for Arts & Culture, 2 Marina Blvd, San Francisco",
        organizer="Fort Mason Center for Arts & Culture", admission="Free",
        source_url="https://fortmason.org/series/fort-mason-night-market-2026/",
        source_label="Fort Mason Center Night Market 2026 series page", source_authority=VENUE,
        notes="Added 2026-10-18 (arena/5e333a6e). Venue page states September 18, October 16, and monthly on select "
              "Fridays in 2026, 5–10pm, free. Remaining dates are not listed; flagged because an Off the Grid listing "
              "says the season has wrapped."),
    row(id="sf-open-studios-2026", name="SF Open Studios (ArtSpan, 52nd annual)",
        bucket="recurring", cadence="annual", category=COM,
        date_text="Preview Exhibition September 19–27, 2026; artist studio events through October 25, 2026",
        start_date="2026-09-19", end_date="2026-10-25", time_text="Preview Exhibition 1:00–7:00pm daily",
        location="SOMArts Cultural Center, 934 Brannan St (preview) and artist studios citywide, San Francisco",
        organizer="ArtSpan",
        source_url="https://somarts.org/exhibition/sfopenstudios2026/",
        source_label="SOMArts SF Open Studios 2026 exhibition page", source_authority=VENUE,
        notes="Added 2026-10-18 (arena/5e333a6e). Venue page states ArtSpan's 52nd annual SF Open Studios, Preview "
              "Exhibition September 19–27, 2026 (1–7pm daily) and artist studio events through October 25, 2026; "
              "ArtLaunch was Friday, September 18, 7–10pm, 21+, $25. Studio-weekend start date and hours are not "
              "stated on that page (flagged); admission to studios is not stated and is blank."),

    # ---------------- Neighborhood festivals and fairs ----------------
    row(id="autumn-moon-festival-2026", name="Chinatown Autumn Moon Festival",
        bucket="recurring", cadence="annual", category=COM,
        date_text="September 19–20, 2026", start_date="2026-09-19", end_date="2026-09-20",
        location="Grant Avenue between California Street and Broadway, Chinatown, San Francisco",
        organizer="Chinatown Merchants Association", admission="Free",
        source_url="https://www.moonfestival.org/", source_label="Autumn Moon Festival official site",
        source_authority=ORG,
        notes="Added 2026-10-18 (arena/5e333a6e). Organizer site states September 19–20, Grant Ave between California "
              "and Broadway, free; SFMTA calls it the annual Autumn Moon Festival hosted by the Chinatown Merchants "
              "Association. Hours conflict (organizer 11am–5pm vs SFMTA 11am–6pm) and are blank pending review."),
    row(id="sf-lowriders-king-of-the-streets-2026", name="SF Lowriders King of the Streets cruise and car show",
        bucket="special", cadence="single-date", category=COM,
        date_text="Saturday, September 19, 2026", start_date="2026-09-19", end_date="2026-09-19",
        location="Mission Street between 18th and 26th streets, Mission District, San Francisco",
        organizer="San Francisco Lowrider Council",
        source_url="https://www.sfmta.com/travel-updates/sf-lowriders-king-streets-saturday-september-19-2026",
        source_label="SFMTA travel update: SF Lowriders King of the Streets", source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA states the date, host, and Mission Street route; it gives "
              "street-closure hours (6am–7pm) but not event hours, so time is blank. Recurrence is not stated."),
    row(id="cole-valley-street-fair-2026", name="Cole Valley Street Fair",
        bucket="recurring", cadence="annual", category=FAIR,
        date_text="Sunday, September 27, 2026", start_date="2026-09-27", end_date="2026-09-27",
        time_text="10:00am–5:00pm",
        location="Cole Street (Frederick–Grattan) and Parnassus Avenue (Belvedere–Shrader), Cole Valley, San Francisco",
        organizer="Organizer not named in source",
        source_url="https://www.sfmta.com/travel-updates/cole-valley-street-fair-sunday-september-27-2026",
        source_label="SFMTA travel update: Cole Valley Street Fair", source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA calls it the annual Cole Valley Street Fair, 10am–5pm, with "
              "crafts, food, live music, vintage automobiles, and children's events. The organizer is not named on the "
              "page and admission is not stated."),
    row(id="bearrison-street-fair-2026", name="Bearrison Street Fair (third annual)",
        bucket="recurring", cadence="annual", category=FAIR,
        date_text="Saturday, October 17, 2026", start_date="2026-10-17", end_date="2026-10-17",
        time_text="12:00–6:00pm",
        location="Harrison Street between 10th and 13th streets, SoMa, San Francisco",
        organizer="Sisters of Perpetual Indulgence and the Bears of San Francisco",
        source_url=SFMTA_ADVISORY_OCT15, source_label=SFMTA_ADVISORY_LABEL, source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA's weekly advisory states the third annual Bearrison Street "
              "Fair, noon–6pm, primarily on Harrison between 10th and 13th, expected attendance 2,500 (event site "
              "bearrison.org). Admission is not stated."),
    row(id="potrero-hill-festival-2026", name="Potrero Hill Festival",
        bucket="recurring", cadence="annual", category=FAIR,
        date_text="Saturday, October 17, 2026", start_date="2026-10-17", end_date="2026-10-17",
        location="20th Street between Wisconsin and Missouri streets, Potrero Hill, San Francisco",
        organizer="Potrero Hill Neighborhood House (beneficiary; organizer not separately named)",
        source_url=SFMTA_ADVISORY_OCT15, source_label=SFMTA_ADVISORY_LABEL, source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA's weekly advisory calls it the annual Potrero Hill Festival "
              "on 20th Street (event site potrerofestival.com); the SFMTA travel-update page describes it as a "
              "fundraiser for the Potrero Hill Neighborhood House. Hours conflict between the two SFMTA pages "
              "(10am–4:30pm vs 11am–4pm) and are blank pending review."),
    row(id="clement-street-art-fair-2026", name="Clement Street Art Fair",
        bucket="special", cadence="single-date", category=FAIR,
        date_text="Saturday, October 17, 2026", start_date="2026-10-17", end_date="2026-10-17",
        time_text="12:00–5:00pm",
        location="Clement Street between 6th and 8th avenues, Inner Richmond, San Francisco",
        organizer="Organizer not named in source",
        source_url=SFMTA_ADVISORY_OCT15, source_label=SFMTA_ADVISORY_LABEL, source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA's weekly advisory states the fair (music and local makers), "
              "noon–5pm on Clement between 6th and 8th avenues. Recurrence, organizer, and admission are not stated."),
    row(id="brava-block-party-2026", name="Brava Block Party",
        bucket="special", cadence="single-date", category=COM,
        date_text="Saturday, October 17, 2026", start_date="2026-10-17", end_date="2026-10-17",
        time_text="12:00–5:00pm",
        location="24th Street between Bryant and Hampshire streets, Mission District, San Francisco",
        organizer="Brava! For Women in the Arts",
        source_url=SFMTA_ADVISORY_OCT15, source_label=SFMTA_ADVISORY_LABEL, source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA's weekly advisory states the block party celebrating "
              "milestones for Brava! For Women in the Arts, noon–5pm, with 24th Street closed between Bryant and "
              "Hampshire. Recurrence and admission are not stated."),
    row(id="diplos-run-club-5k-sf-2026", name="Diplo's Run Club San Francisco 5K",
        bucket="special", cadence="single-date", category=SPORT,
        date_text="Sunday, October 18, 2026", start_date="2026-10-18", end_date="2026-10-18",
        time_text="Start 8:30am",
        location="Robin Williams Meadow, Golden Gate Park, San Francisco",
        organizer="Diplo's Run Club",
        source_url=SFMTA_ADVISORY_OCT15, source_label=SFMTA_ADVISORY_LABEL, source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA's weekly advisory states an 8:30am start and finish at Robin "
              "Williams Meadow with a post-race concert (event site diplosrunclub.com/san-francisco). Registration "
              "price is not stated."),
    row(id="lower-polk-live-2026-10-23", name="Lower Polk Live",
        bucket="special", cadence="single-date", category=FAIR,
        date_text="Friday, October 23, 2026", start_date="2026-10-23", end_date="2026-10-23",
        time_text="4:00–9:00pm",
        location="Polk Street between Bush and Sutter, and Fern Street between Van Ness and Larkin, San Francisco",
        organizer="Organizer not named in source",
        source_url="https://www.sfmta.com/travel-updates/lower-polk-live-friday-october-23-2026",
        source_label="SFMTA travel update: Lower Polk Live", source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA states the date, 4–9pm, and street footprint. Recurrence is "
              "not stated by the source and is not inferred."),
    row(id="from-the-e-night-market-2026-10-23", name="From the E Excelsior Night Market",
        bucket="special", cadence="single-date", category=FOOD,
        date_text="Friday, October 23, 2026", start_date="2026-10-23", end_date="2026-10-23",
        time_text="4:30–8:30pm",
        location="Ocean Avenue between Mission Street and Persia Avenue, Excelsior, San Francisco",
        organizer="Organizer not named in source",
        source_url="https://www.sfmta.com/travel-updates/e-night-market-friday-october-23-2026",
        source_label="SFMTA travel update: From the E Night Market", source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA states food, crafts, entertainment, and live music, 4:30–8:30pm. "
              "Recurrence is not stated by the source and is not inferred."),
    row(id="noe-valley-night-market-2026-10-27", name="Noe Valley Night Market",
        bucket="special", cadence="single-date", category=FOOD,
        date_text="Tuesday, October 27, 2026", start_date="2026-10-27", end_date="2026-10-27",
        time_text="4:30–8:30pm",
        location="24th Street between Sanchez and Vicksburg streets, Noe Valley, San Francisco",
        organizer="Noe Valley Merchants",
        source_url="https://www.sfmta.com/travel-updates/noe-valley-night-market-tuesday-october-27-2026",
        source_label="SFMTA travel update: Noe Valley Night Market", source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA states the host, date, 4:30–8:30pm, and 24th Street footprint. "
              "Recurrence is not stated by the source and is not inferred."),

    # ---------------- Sports ----------------
    row(id="sf-half-marathon-2027", name="The San Francisco Half Marathon & 5K",
        bucket="special", cadence="single-date", category=SPORT,
        date_text="February 7, 2027", start_date="2027-02-07", end_date="2027-02-07",
        location="Golden Gate Park, the Panhandle, and Sunset Dunes along the Pacific Ocean, San Francisco",
        organizer="The San Francisco Half Marathon",
        source_url="https://sanfranciscohalfmarathon.org/race-information/",
        source_label="San Francisco Half Marathon race information", source_authority=ORG,
        notes="Added 2026-10-18 (arena/5e333a6e). Organizer states the race \"returns on February 7, 2027\" in Golden "
              "Gate Park and along the Pacific Ocean (Panhandle, Golden Gate Park, Sunset Dunes); bib pickup "
              "February 4–6. Start times and registration prices are not stated on the page and are blank. Classed "
              "as a dated special event because no cadence is stated."),

    # ---------------- Pride-week community marches (2026, past) ----------------
    row(id="pink-triangle-2026", name="The Pink Triangle (installation and ceremony)",
        bucket="special", cadence="single-date", category=COM,
        date_text="Sunday, June 7, 2026", start_date="2026-06-07", end_date="2026-06-07",
        location="Twin Peaks, San Francisco", organizer="The Pink Triangle (SF Pride fiscally sponsored event)",
        source_url="https://sfpride.org/events/", source_label="SF Pride 2026 events page", source_authority=ORG,
        notes="Added 2026-10-18 (arena/5e333a6e). SF Pride's official events page lists The Pink Triangle on Sunday, "
              "June 7, 2026 at Twin Peaks as a fiscally sponsored event. Time and recurrence are not stated there."),
    row(id="trans-march-2026", name="Trans March",
        bucket="recurring", cadence="annual", category=COM,
        date_text="Friday, June 26, 2026", start_date="2026-06-26", end_date="2026-06-26",
        location="Dolores Park, Mission District, San Francisco", organizer="Trans March",
        source_url="https://sfpride.org/events/", source_label="SF Pride 2026 events page (Community Marches)",
        source_authority=ORG,
        notes="Added 2026-10-18 (arena/5e333a6e). SF Pride's official events page describes the Trans March as an "
              "annual gathering and march starting at Dolores Park, Friday, June 26, 2026. Time is not stated there; "
              "transmarch.org was not fetched."),
    row(id="dyke-march-2026", name="SF Dyke March",
        bucket="recurring", cadence="annual", category=COM,
        date_text="Saturday, June 27, 2026", start_date="2026-06-27", end_date="2026-06-27",
        time_text="Rally at Dolores Park; march begins 5:00pm",
        location="Dolores Park, then 18th, Valencia, 16th, Market, and Castro streets, San Francisco",
        organizer="SF Dyke March",
        source_url="https://www.sfmta.com/project-updates/dyke-march",
        source_label="SFMTA project update: SF Pride Dyke March, June 27, 2026", source_authority=GOV,
        notes="Added 2026-10-18 (arena/5e333a6e). SFMTA calls it the annual Dyke March and states the march begins at "
              "5pm after a rally at Dolores Park. SF Pride's events page lists the same date."),

    # ---------------- Review register ----------------
    row(id="litquake-2026", name="Litquake 2026 (mixed-geography program)",
        bucket="review", cadence="annual", category=BOOKS,
        location="San Francisco and Berkeley", organizer="Litquake",
        source_url="https://litquake2026.sched.com/", source_label="Litquake 2026 official schedule (Sched)",
        source_authority=ORG, status="partial_sf_program",
        review_reason="Litquake's official 2026 schedule includes at least one Berkeley venue (Gilman Brewing), so the "
                      "festival is not city-only. Official pages also disagree on the opening date, so dates are left "
                      "blank until a San Francisco-only program and confirmed dates can be separated.",
        notes="Not shown in the recurring or special catalog tables. Lit Crawl SF is catalogued separately."),
]

NEW_FLAGS: list[dict] = [
    {
        "id": "flag-dreamforce-2027-venue", "event_id": "dreamforce-2027", "event": "Dreamforce (2027)",
        "issue": "The organizer page gives only \"San Francisco and Salesforce+\" for September 21–23, 2027 and names no venue.",
        "sources": [{"label": "Salesforce Dreamforce 2027 save-the-date", "url": "https://www.salesforce.com/dreamforce/df27-save-the-date/"}],
        "disposition": "Published with the venue blank; confirm the venue when the organizer announces it.",
    },
    {
        "id": "flag-jpm-2027-venue", "event_id": "jpm-healthcare-conference-2027",
        "event": "J.P. Morgan Healthcare Conference (2027)",
        "issue": "The organizer page states January 11–14, 2027, San Francisco, invitation only, but no venue. The venue appears only on third-party sites.",
        "sources": [{"label": "J.P. Morgan Healthcare Conference page", "url": "https://www.jpmorgan.com/about-us/events-conferences/health-care-conference"}],
        "disposition": "Published with the venue blank; third-party venue claims were not used.",
    },
    {
        "id": "flag-fort-mason-night-market-season", "event_id": "fort-mason-night-market-2026",
        "event": "Fort Mason Night Market (2026)",
        "issue": "The venue's series page lists September 18, October 16, and \"monthly on select Fridays\" without listing the remaining dates. An Off the Grid listing (a vendor partner, not used as a source) says the season has wrapped.",
        "sources": [{"label": "Fort Mason Night Market 2026 series page", "url": "https://fortmason.org/series/fort-mason-night-market-2026/"}],
        "disposition": "Published as monthly per the venue page; confirm whether any dates after October 16 remain.",
    },
    {
        "id": "flag-litquake-2026-dates", "event_id": "litquake-2026", "event": "Litquake (2026)",
        "issue": "The official Sched schedule shows sessions from October 11 onward and includes a Berkeley venue. Official pages give conflicting opening dates (October 4 vs October 8).",
        "sources": [{"label": "Litquake 2026 official schedule (Sched)", "url": "https://litquake2026.sched.com/"}],
        "disposition": "Held in the review register as a mixed-geography program; dates blank.",
    },
    {
        "id": "flag-sf-open-studios-start", "event_id": "sf-open-studios-2026", "event": "SF Open Studios (2026)",
        "issue": "The SOMArts page confirms the Preview Exhibition (September 19–27) and that studio events run through October 25, 2026, but not when studio weekends start or their hours. ArtSpan's own visit page returned an empty shell.",
        "sources": [{"label": "SOMArts SF Open Studios 2026 page", "url": "https://somarts.org/exhibition/sfopenstudios2026/"}],
        "disposition": "Published with the preview dates; studio-weekend start date and hours were not inferred.",
    },
    {
        "id": "flag-autumn-moon-hours", "event_id": "autumn-moon-festival-2026",
        "event": "Chinatown Autumn Moon Festival (2026)",
        "issue": "Hours conflict: the organizer site says 11am–5pm while SFMTA says 11am–6pm each day.",
        "sources": [
            {"label": "Autumn Moon Festival official site", "url": "https://www.moonfestival.org/"},
            {"label": "SFMTA travel update: Autumn Moon Festival", "url": "https://www.sfmta.com/travel-updates/chinatown-autumn-moon-festival-september-19-20-2026"},
        ],
        "disposition": "Time left blank; dates, location, and free admission published.",
    },
    {
        "id": "flag-potrero-hill-festival-hours", "event_id": "potrero-hill-festival-2026",
        "event": "Potrero Hill Festival (2026)",
        "issue": "Hours conflict between two SFMTA pages: the weekly advisory says 10am–4:30pm and the travel-update page says 11am–4pm. The organizer site potrerofestival.com was not fetched.",
        "sources": [
            {"label": SFMTA_ADVISORY_LABEL, "url": SFMTA_ADVISORY_OCT15},
            {"label": "SFMTA travel update: Potrero Hill Festival", "url": "https://www.sfmta.com/travel-updates/potrero-hill-festival-saturday-october-17-2026"},
        ],
        "disposition": "Time left blank; date and location published.",
    },
]


def main() -> None:
    doc = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    ids = {e["id"] for e in doc["events"]}
    added = 0
    for r in NEW_ROWS:
        if r["id"] not in ids:
            doc["events"].append(r)
            ids.add(r["id"])
            added += 1
    flag_ids = {f["id"] for f in doc["flags"]}
    flags_added = 0
    for f in NEW_FLAGS:
        if f["id"] not in flag_ids:
            doc["flags"].append(f)
            flags_added += 1
    cat = doc["catalog"]
    marker = "arena/5e333a6e-maltaproj7 coverage-gap pass"
    if marker not in cat.get("updated_by", ""):
        cat["updated_by"] = cat.get("updated_by", "") + f"; {marker} (Moscone, SFMTA, FAMSF, organizer sources)"
    DATA_PATH.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"added {added} events, {flags_added} flags")


if __name__ == "__main__":
    main()
