#!/usr/bin/env python3
"""Coverage-gap patch applied by session arena/646f6727-maltaproj7 on 2026-10-18.

Every value below was read directly from the linked official page via the
sandbox fetch tool on 2026-10-18 (quoted evidence is logged in
research/coverage-gap-646f6727.md).  Fields the source did not state are left
blank.  Re-runnable: records are inserted by id only if absent.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "events.json"

NEW_EVENTS = [
    # ---------------- verified, published rows ----------------
    {
        "id": "gdc-festival-of-gaming-2027",
        "name": "GDC Festival of Gaming (Game Developers Conference)",
        "bucket": "recurring", "cadence": "annual", "category": "Professional & academic",
        "date_text": "March 1–5, 2027", "start_date": "2027-03-01", "end_date": "2027-03-05",
        "time_text": "", "location": "Moscone Center, San Francisco, CA",
        "organizer": "GDC Festival of Gaming (Informa Festivals)", "admission": "",
        "source_url": "https://gdconf.com/", "source_label": "GDC official site",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Homepage header states 'March 1-5, 2027 — Moscone Center, San Francisco, CA'. Pass prices are on a separate page and are not recorded here.",
    },
    {
        "id": "rsa-conference-2027",
        "name": "RSA Conference (RSAC) 2027",
        "bucket": "recurring", "cadence": "annual", "category": "Professional & academic",
        "date_text": "April 5–8, 2027", "start_date": "2027-04-05", "end_date": "2027-04-08",
        "time_text": "", "location": "Moscone Center, San Francisco, CA",
        "organizer": "RSA Conference LLC", "admission": "",
        "source_url": "https://www.rsaconference.com/library/press-release/2026-closing-release",
        "source_label": "RSAC official 2026 closing press release (announces 2027 dates)",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Release text: 'RSAC 2027 Conference will take place April 5-8, 2027, in San Francisco at the Moscone Center.' The 2026 edition drew 43,500+ attendees. Pass pricing (shown on rsaconference.com/usa) is not recorded here.",
    },
    {
        "id": "dreamforce-2027",
        "name": "Dreamforce 2027",
        "bucket": "recurring", "cadence": "annual", "category": "Professional & academic",
        "date_text": "September 21–23, 2027", "start_date": "2027-09-21", "end_date": "2027-09-23",
        "time_text": "", "location": "San Francisco (venue not stated on save-the-date page)",
        "organizer": "Salesforce", "admission": "",
        "source_url": "https://www.salesforce.com/dreamforce/df27-save-the-date/",
        "source_label": "Salesforce Dreamforce 2027 save-the-date page",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Page states 'September 21-23, 2027 | San Francisco and Salesforce+'. No venue named; see field flag.",
    },
    {
        "id": "jpm-healthcare-conference-2027",
        "name": "J.P. Morgan Healthcare Conference (45th annual)",
        "bucket": "recurring", "cadence": "annual", "category": "Professional & academic",
        "date_text": "January 11–14, 2027", "start_date": "2027-01-11", "end_date": "2027-01-14",
        "time_text": "", "location": "San Francisco, California (venue not stated on official page)",
        "organizer": "J.P. Morgan", "admission": "By invitation only (invitations not transferable)",
        "source_url": "https://www.jpmorgan.com/about-us/events-conferences/health-care-conference",
        "source_label": "J.P. Morgan official conference page",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Official page: 'The 45th Annual Healthcare Conference will take place on January 11-14, 2027 in San Francisco, California' and 'This event is by invitation only'.",
    },
    {
        "id": "techcrunch-disrupt-2026",
        "name": "TechCrunch Disrupt 2026",
        "bucket": "recurring", "cadence": "annual", "category": "Professional & academic",
        "date_text": "October 13–15, 2026", "start_date": "2026-10-13", "end_date": "2026-10-15",
        "time_text": "", "location": "San Francisco, CA (venue not stated on events index)",
        "organizer": "TechCrunch", "admission": "",
        "source_url": "https://techcrunch.com/events/", "source_label": "TechCrunch events index (official organizer)",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Events index lists 'Oct 13 – 15, 2026, San Francisco, CA — TechCrunch Disrupt 2026' (10,000 founders, VCs, operators). The dedicated event page sits behind a Cloudflare challenge and could not be read.",
    },
    {
        "id": "chinatown-autumn-moon-festival-2026",
        "name": "San Francisco Chinatown Autumn Moon Festival",
        "bucket": "recurring", "cadence": "annual", "category": "Community & culture",
        "date_text": "September 19–20, 2026", "start_date": "2026-09-19", "end_date": "2026-09-20",
        "time_text": "11am–5pm (Saturday and Sunday)",
        "location": "Grant Avenue between California Street and Broadway, Chinatown, San Francisco",
        "organizer": "Chinatown Merchants Association", "admission": "Free",
        "source_url": "https://www.moonfestival.org/", "source_label": "Autumn Moon Festival official site",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Official page: 'September 19 - 20 • 11am - 5pm', 'Location GRANT Avenue Between California & Broadway', 'Cost FREE!'. Main stage at Washington & Grant.",
    },
    {
        "id": "chinese-new-year-flower-market-fair-2027",
        "name": "Chinese New Year Flower Market Fair",
        "bucket": "recurring", "cadence": "annual", "category": "Community & culture",
        "date_text": "Saturday–Sunday, January 30–31, 2027", "start_date": "2027-01-30", "end_date": "2027-01-31",
        "time_text": "", "location": "Grant Avenue between Clay Street and Broadway, Chinatown, San Francisco",
        "organizer": "San Francisco Chinese New Year Festival & Parade (chineseparade.com)", "admission": "",
        "source_url": "https://chineseparade.com/flowermarketfair/",
        "source_label": "Chinese New Year Festival & Parade — Flower Market Fair page",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Page: 'The 2027 Flower Market Fair is scheduled for Sat. & Sun. Jan. 30 & 31 @Grant between Clay and Broadway.' Held the weekend before Chinese New Year Day; 120+ booths. Hours not stated.",
    },
    {
        "id": "trans-march-2026",
        "name": "San Francisco Trans March",
        "bucket": "recurring", "cadence": "annual", "category": "Community & culture",
        "date_text": "Friday, June 26, 2026 (Friday of Pride weekend every year)",
        "start_date": "2026-06-26", "end_date": "2026-06-26",
        "time_text": "Dolores Park gathering 3–6pm; march at 6pm",
        "location": "Dolores Park, San Francisco", "organizer": "Trans March", "admission": "",
        "source_url": "https://transmarch.org/", "source_label": "Trans March official site",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Site: 'Trans March kicks off Pride weekend on Friday every year. Dolores Park: 3 - 6pm, March @ 6pm.' and 'Trans March 2026: June 26 @ Dolores Park'. 2027 date not yet posted.",
    },
    {
        "id": "golden-gate-park-band-2026-season",
        "name": "Golden Gate Park Band — 2026 Sunday concert season",
        "bucket": "recurring", "cadence": "seasonal", "category": "Music & performing arts",
        "date_text": "April–September 2026, every Sunday plus July 4 and Labor Day (25 concerts)",
        "start_date": "", "end_date": "", "time_text": "",
        "location": "Spreckels Temple of Music, Music Concourse, Golden Gate Park, San Francisco",
        "organizer": "Golden Gate Park Band (sponsored in part by SF Recreation and Parks)", "admission": "Free",
        "source_url": "https://goldengateparkband.org/", "source_label": "Golden Gate Park Band official site",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Site: 'Our season runs from April through September, with shows every Sunday plus July 4 and Labor Day at the Spreckels Temple of Music'; '2026 season … 25 high-quality concerts'; 'keep this treasured cultural tradition free for all'. Concert start time is on the calendar page and not recorded here. Band founded 1882.",
    },
    {
        "id": "sf-ballet-nutcracker-2026",
        "name": "San Francisco Ballet — Nutcracker",
        "bucket": "recurring", "cadence": "annual", "category": "Music & performing arts",
        "date_text": "December 4–27, 2026", "start_date": "2026-12-04", "end_date": "2026-12-27",
        "time_text": "Matinee and evening performances (11am, 2pm, 4pm, 6pm or 7pm depending on date); opens Fri Dec 4 at 7:00pm",
        "location": "War Memorial Opera House, San Francisco", "organizer": "San Francisco Ballet", "admission": "",
        "source_url": "https://www.sfballet.org/productions/nutcracker/", "source_label": "San Francisco Ballet production page",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Page header 'DEC 4–27'; 'Location: War Memorial Opera House'; first performance Fri Dec 4 7:00 pm, last Sun Dec 27 4:00 pm; sensory-friendly performance Dec 27 11am. Ticketed; prices not stated on page.",
    },
    {
        "id": "off-the-grid-fort-mason-night-market-2026",
        "name": "Off the Grid — Fort Mason Center Night Market (2026 season)",
        "bucket": "recurring", "cadence": "seasonal", "category": "Food & markets",
        "date_text": "Select Fridays, May–December 2026 (May 22, Jun 19, Jul 24, Aug 21, Sep 18, Nov 6; remaining Oct–Dec dates to be announced)",
        "start_date": "2026-05-22", "end_date": "", "time_text": "5:00pm–10:00pm",
        "location": "Fort Mason Center for Arts & Culture, 2 Marina Blvd, San Francisco",
        "organizer": "Off the Grid", "admission": "Free admission; all ages",
        "source_url": "https://offthegrid.com/event/fort-mason-center/", "source_label": "Off the Grid market page",
        "source_authority": "Official organizer", "status": "verified", "review_reason": "",
        "notes": "Page: 'Free admission. All ages welcome. May through December.' with 2026 dates listed and 'Upcoming Schedule: Fri 11/6 5PM - 10PM'. Season 2 of the night market; 25+ food creators, music curated by Stern Grove Festival.",
    },
    # ---------------- review-only records (never in normal tables) ----------------
    {
        "id": "how-weird-street-faire",
        "name": "How Weird Street Faire — discontinued",
        "bucket": "review", "cadence": "", "category": "Fairs & nightlife",
        "date_text": "", "start_date": "", "end_date": "", "time_text": "",
        "location": "Howard & 2nd Street, SoMa, San Francisco", "organizer": "How Weird Street Faire", "admission": "",
        "source_url": "https://howweird.org/", "source_label": "How Weird Street Faire official site",
        "source_authority": "Official organizer", "status": "cancelled",
        "review_reason": "Organizer site states '2000 — 2024 … Twenty-five years of costumes, sound systems and dancing in the middle of Howard Street. The Faire is done.' Recorded so it is not re-added as an active annual event.",
        "notes": "Audit exception only.",
    },
    {
        "id": "union-street-festival",
        "name": "Union Street Festival — no live official source",
        "bucket": "review", "cadence": "", "category": "Fairs & nightlife",
        "date_text": "", "start_date": "", "end_date": "", "time_text": "",
        "location": "", "organizer": "", "admission": "",
        "source_url": "https://www.unionstreetfestival.com/",
        "source_label": "Legacy domain — NOT official (now serves unrelated Turkish casino spam)",
        "source_authority": "Unverified legacy URL", "status": "needs_review",
        "review_reason": "Both historical organizer domains are compromised: unionstreetfestival.com serves Turkish gambling spam and sresproductions.com redirects to an unrelated sports-streaming site. No official page confirming a 2026/2027 edition could be located, so nothing is published.",
        "notes": "Needs a human to identify the current organizer page before any row is created.",
    },
    {
        "id": "sf-dyke-march-2027",
        "name": "San Francisco Dyke March 2027",
        "bucket": "review", "cadence": "annual", "category": "Community & culture",
        "date_text": "Saturday, June 26, 2027", "start_date": "2027-06-26", "end_date": "2027-06-26",
        "time_text": "", "location": "", "organizer": "SF Dyke March", "admission": "",
        "source_url": "https://www.thedykemarch.org/", "source_label": "SF Dyke March official site",
        "source_authority": "Official organizer", "status": "needs_review",
        "review_reason": "Official homepage states only the date ('Saturday, June 26, 2027'); it does not state the gathering location, route, or time, and the FAQ URL returns a not-found page. Location left blank rather than inferred, so the row cannot be published.",
        "notes": "",
    },
    {
        "id": "litquake-2026",
        "name": "Litquake 2026 — mixed-geography literary festival",
        "bucket": "review", "cadence": "annual", "category": "Books & ideas",
        "date_text": "Begins Sunday, October 11, 2026 (end date not stated on the schedule index)",
        "start_date": "2026-10-11", "end_date": "", "time_text": "",
        "location": "Venues in San Francisco plus Oakland, Berkeley, Sausalito and Marin",
        "organizer": "Litquake Foundation", "admission": "",
        "source_url": "https://litquake2026.sched.com/", "source_label": "Litquake 2026 official schedule (Sched)",
        "source_authority": "Official organizer", "status": "partial_sf_program",
        "review_reason": "The official schedule lists venues in San Francisco and also Oakland, Berkeley, Sausalito and a 'Marin' city filter, and the festival site gives no single date range, so the festival as a whole is not city-only. The San Francisco-only component Lit Crawl SF (October 24, 2026) is already a published row.",
        "notes": "",
    },
]

NEW_FLAGS = [
    {
        "id": "flag-union-street-festival-domains",
        "event_id": "union-street-festival",
        "event": "Union Street Festival",
        "issue": "Both domains historically used for the festival are compromised at audit time: unionstreetfestival.com serves Turkish online-casino spam and sresproductions.com (the producer's domain) redirects to an unrelated Vietnamese sports-streaming site. No official source for a current edition was found.",
        "sources": [
            {"label": "unionstreetfestival.com (hijacked)", "url": "https://www.unionstreetfestival.com/"},
            {"label": "sresproductions.com event page (redirects off-domain)", "url": "https://www.sresproductions.com/events/union-street-festival/"},
        ],
        "disposition": "Held on Flagged for Review with blank fields; nothing published.",
    },
    {
        "id": "flag-dreamforce-2027-venue",
        "event_id": "dreamforce-2027",
        "event": "Dreamforce 2027",
        "issue": "The official save-the-date page states only 'September 21-23, 2027 | San Francisco and Salesforce+'. No venue is named, so the location field carries the city only.",
        "sources": [
            {"label": "Salesforce Dreamforce 2027 save-the-date", "url": "https://www.salesforce.com/dreamforce/df27-save-the-date/"},
        ],
        "disposition": "Published with city-level location; venue left blank until Salesforce names it.",
    },
    {
        "id": "flag-bay-to-breakers-page-copy",
        "event_id": "bay-to-breakers-2027",
        "event": "Bay to Breakers (2027)",
        "issue": "The organizer homepage headline and title read 'May 16, 2027', but residual sidebar copy says 'happenings to get you in the spirit before May 18' and lists pre-race events dated May 15 and May 16. The published date follows the headline; the inconsistency is on the source page itself.",
        "sources": [
            {"label": "Bay to Breakers official site", "url": "https://www.baytobreakers.com/"},
        ],
        "disposition": "Published date unchanged (May 16, 2027); discrepancy recorded for manual review.",
    },
    {
        "id": "flag-techcrunch-disrupt-event-page",
        "event_id": "techcrunch-disrupt-2026",
        "event": "TechCrunch Disrupt 2026",
        "issue": "The dedicated Disrupt event page is behind a Cloudflare browser challenge and the /events/techcrunch-disrupt-2026/ URL returns 404; dates and city were taken from the organizer's events index table only. Venue not stated there.",
        "sources": [
            {"label": "TechCrunch events index", "url": "https://techcrunch.com/events/"},
        ],
        "disposition": "Published with city-level location from the organizer index; venue blank.",
    },
]


def main() -> None:
    doc = json.loads(DATA.read_text(encoding="utf-8"))
    ids = {e["id"] for e in doc["events"]}
    added = 0
    for ev in NEW_EVENTS:
        if ev["id"] not in ids:
            doc["events"].append(ev)
            added += 1
    flag_ids = {f["id"] for f in doc.get("flags", [])}
    fadded = 0
    for fl in NEW_FLAGS:
        if fl["id"] not in flag_ids:
            doc.setdefault("flags", []).append(fl)
            fadded += 1
    # Ensure the Bay to Breakers flag points at the real row id.
    b2b = [e["id"] for e in doc["events"] if e["name"].startswith("Bay to Breakers")]
    for fl in doc["flags"]:
        if fl["id"] == "flag-bay-to-breakers-page-copy" and b2b:
            fl["event_id"] = b2b[0]
    doc["catalog"]["updated_by"] = (
        doc["catalog"].get("updated_by", "") +
        " + arena/646f6727-maltaproj7 coverage-gap additions (2026-10-18)"
    )
    DATA.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"added {added} events, {fadded} flags; total events {len(doc['events'])}, flags {len(doc['flags'])}")


if __name__ == "__main__":
    main()
