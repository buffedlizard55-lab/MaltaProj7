#!/usr/bin/env python3
"""Reproducible data patch for session arena/2e5715f9-maltaproj7 (2026-10-18).

Coverage-gap closure: NEW free San Francisco events/programs discovered and verified
from official sources on 2026-10-18. Every value is quoted from the linked official
page in `research/verification-2e5715f9.md`; nothing is inferred. Where an official
page states no cost, `admission` stays blank and a flag records the gap. The review
record (Small Change Arcade grand opening) carries press-only evidence and is NOT
published as verified.

Additive only: inserts new ids and updates only the two coverage-gap flags'
`disposition` fields (claimed as W3). No peer-sourced field values are rewritten.

Counts move: published 162 -> 170 (recurring 102 -> 109, special 60 -> 61),
review 17 -> 18, flags 51 -> 58.

Run:  python3 research/patch-2e5715f9.py     (idempotent)
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "events.json"

NEW_PUBLISHED = [
    {
        "id": "mapp-2026-12-05",
        "name": "MAPP (Mission Arts Performance Project) — December 5, 2026 edition",
        "bucket": "recurring",
        "cadence": "bimonthly",
        "category": "Music & performing arts",
        "date_text": "Saturday, December 5, 2026 (next listed edition)",
        "start_date": "2026-12-05",
        "end_date": "2026-12-05",
        "time_text": "12:00 PM",
        "location": "Mission District of San Francisco (several venues and public spaces)",
        "organizer": "Mission Arts Performance Project (MAPP)",
        "admission": "Free",
        "admission_source_url": "https://mappsf.com/events",
        "source_url": "https://mappsf.com/events",
        "source_label": "MAPP official events page",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7). Official listing states "
            "\"Saturday, December 5 @ 12:00PM\", \"Mission District of San Francisco , San "
            "Francisco\", \"MAPP is a familia, a community and a series of arts, music and "
            "activist events that has been taking place in the Mission for over 20 years. MAPP "
            "is always the first Saturday of the month every two months. MAPP is always free.\" "
            "and lists \"free live music, Spoken word, Performance art, Film screenings\". End "
            "time is not stated on the listing. The series is 20+ years old and bimonthly per "
            "the source's own wording; no further dates are invented."
        ),
    },
    {
        "id": "noontime-concerts",
        "name": "Noontime Concerts — weekly Tuesday classical series",
        "bucket": "recurring",
        "cadence": "weekly",
        "category": "Music & performing arts",
        "date_text": "Tuesdays, 12:30 p.m. (45 minutes); also one Sunday each month, April–November, at the San Francisco Mint",
        "start_date": "",
        "end_date": "",
        "time_text": "12:30 p.m. (45-minute concert)",
        "location": "Old St. Mary's Cathedral, 660 California Street, San Francisco",
        "organizer": "Noontime Concerts",
        "admission": "Free concerts; suggested donations solicited",
        "admission_source_url": "https://noontimeconcerts.org/about/",
        "source_url": "https://noontimeconcerts.org/",
        "source_label": "Noontime Concerts official site",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7). Official site states \"Free Live "
            "Concert Every Tuesday\", \"Live Stream Starts at 12:30PM or attend in person at Old "
            "St. Mary's Cathedral 660 California Street\", and \"Always on Tuesdays and always "
            "free.\" The About page adds: \"Noontime Concerts are not ticketed but suggested "
            "donations are solicited to ensure all can enjoy performances regardless of ability "
            "to pay\" and \"weekly on Tuesdays at 12:30 in historic Old Saint Mary's Cathedral "
            "and on one Sunday each month from April through November at the historic San "
            "Francisco Mint\". No season window is published, so no series dates are invented; "
            "the next listed individual concert is catalogued separately "
            "(noontime-concerts-2026-11-10)."
        ),
    },
    {
        "id": "noontime-concerts-2026-11-10",
        "name": "Noontime Concerts — Angela Lee, cello & Marc Teicholz, guitar",
        "bucket": "special",
        "cadence": "single-date",
        "category": "Music & performing arts",
        "date_text": "Tuesday, November 10, 2026",
        "start_date": "2026-11-10",
        "end_date": "2026-11-10",
        "time_text": "12:30 p.m.",
        "location": "Old St. Mary's Cathedral, 660 California Street, San Francisco",
        "organizer": "Noontime Concerts",
        "admission": "Free concerts; suggested donations solicited",
        "admission_source_url": "https://noontimeconcerts.org/about/",
        "source_url": "https://noontimeconcerts.org/",
        "source_label": "Noontime Concerts official site — Upcoming Concerts",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7). The official homepage's \"Upcoming "
            "Concerts\" block lists \"11/10/2026 — Angela Lee, Cello and Marc Teicholz, Guitar\". "
            "Edition of the free weekly Tuesday series (see noontime-concerts); admission "
            "wording from the organizer's About page (\"not ticketed but suggested donations are "
            "solicited\")."
        ),
    },
    {
        "id": "detour-free-play-tuesday",
        "name": "The Detour — Free Play Tuesday (first Tuesdays)",
        "bucket": "recurring",
        "cadence": "monthly",
        "category": "Technology, AI & gaming",
        "date_text": "1st Tuesday of every month (specific future dates not published on the official page)",
        "start_date": "",
        "end_date": "",
        "time_text": "All day",
        "location": "The Detour, San Francisco",
        "organizer": "The Detour",
        "admission": "Free arcade game play with a food or beverage purchase (21+ event)",
        "admission_source_url": "https://www.detoursf.com/event/free-play-tuesday/",
        "source_url": "https://www.detoursf.com/event/free-play-tuesday/",
        "source_label": "The Detour official event page — Free Play Tuesday",
        "source_authority": "Official venue",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7). Official page states \"1st Tuesday of "
            "the Month Free Play All Day 21+\" and \"On the 1st Tuesday of every month enjoy all "
            "of our arcade games for free with a food or beverage purchase ... 21+ event.\" "
            "Play is free with a purchase — see flag-detour-free-play-condition for the "
            "conditional-free nuance. Specific future dates are not published on the official "
            "page, so none are invented. The official pages fetched name only the venue and "
            "city; the street address (2200A Market St) appears in third-party listings and is "
            "not republished as a source-confirmed field."
        ),
    },
    {
        "id": "detour-board-game-night",
        "name": "The Detour — Tuesday Board Game Night",
        "bucket": "recurring",
        "cadence": "weekly",
        "category": "Technology, AI & gaming",
        "date_text": "Tuesdays, 7:30–10:00 p.m. (weekly; specific future dates not published)",
        "start_date": "",
        "end_date": "",
        "time_text": "7:30–10:00 p.m.",
        "location": "The Detour, San Francisco",
        "organizer": "The Detour",
        "admission": "",
        "source_url": "https://www.detoursf.com/happenings/",
        "source_label": "The Detour official Happenings page",
        "source_authority": "Official venue",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7). Official Happenings page lists "
            "\"Tuesdays Board Game Night 7:30-10:00\" under \"WEEKLY & MONTHLY EVENTS\". The page "
            "states no admission cost for any listed program, so cost is left blank per policy "
            "(flag-detour-weekly-cost-unstated). The same page lists Super Trashed Bros and "
            "Killer Queen League Night (Mondays), --4Play-- Connect 4 Tournament (3rd Tuesday), "
            "Flip'n'Fierce pinball tournament (1st Wednesday), Trivia Night (Thursdays) and "
            "Detour Disco (Fridays); those programs also carry no stated cost and are documented "
            "here rather than given invented rows or prices."
        ),
    },
    {
        "id": "sfpl-gaming-at-the-mix",
        "name": "Gaming at The Mix (San Francisco Public Library)",
        "bucket": "recurring",
        "cadence": "drop-in",
        "category": "Technology, AI & gaming",
        "date_text": "Drop-in during The Mix open hours (standing program)",
        "start_date": "",
        "end_date": "",
        "time_text": "",
        "location": "The Mix, Main Library, 100 Larkin Street, San Francisco",
        "organizer": "San Francisco Public Library",
        "admission": "No-cost (per SFPL: “All programs and events are free and open to the public”)",
        "admission_source_url": "https://sfpl.org/es/teens/events",
        "source_url": "https://sfpl.org/teens/the-mix/gaming",
        "source_label": "SFPL — Gaming at The Mix",
        "source_authority": "Government source",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7). Official SFPL page states \"Come in "
            "and play video games or tabletop gaming with friends!\", \"Teens can check out "
            "controllers with their library card, and our staff will set them up with a console\", "
            "\"we offer sessions of D&D led by teen interns or professional DMs\" and \"The Mix "
            "also hosts monthly gaming tournaments\". SFPL's The Mix page places it at \"100 "
            "Larkin, 2nd Floor San Francisco, CA 94102\" for \"youth ages 12-18\". Cost wording "
            "comes from SFPL's events statement (\"All programs and events are free and open to "
            "the public\", https://sfpl.org/es/teens/events) captured via the live search index "
            "on 2026-10-18 — see flag-sfpl-free-statement-capture for the provenance note and "
            "re-check request."
        ),
    },
    {
        "id": "ai-engineering-sf",
        "name": "AI Engineering SF (Latent.Space)",
        "bucket": "recurring",
        "cadence": "irregular",
        "category": "Technology, AI & gaming",
        "date_text": "Irregular; next edition not posted as of 2026-10-18 (most recent listed edition: Friday, January 23, 2026)",
        "start_date": "",
        "end_date": "",
        "time_text": "",
        "location": "San Francisco (January 2026 edition: AWS Builder Loft, 525 Market Street)",
        "organizer": "Latent.Space",
        "admission": "Free",
        "admission_source_url": "https://luma.com/aieng",
        "source_url": "https://luma.com/aieng",
        "source_label": "AI Engineering SF — official organizer calendar (Latent.Space)",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7). Official organizer page states \"we "
            "are now THE definitive AI Engineering meetup in SF\" and \"This is a free event, "
            "thanks to AWS for the lovely venue!\" The most recent edition listed on the page is "
            "\"Friday, January 23 ... 5:00 PM - 8:00 PM PST ... AWS Builder Loft 525 Market St, "
            "San Francisco, CA 94105, USA\", marked \"Past Event (This event ended 268 days "
            "ago)\". No future edition is posted as of 2026-10-18, so no dates are invented; the "
            "series' free admission is the organizer's own wording for its editions."
        ),
    },
    {
        "id": "ai-tinkerers-san-francisco",
        "name": "AI Tinkerers San Francisco",
        "bucket": "recurring",
        "cadence": "frequent",
        "category": "Technology, AI & gaming",
        "date_text": "Frequent (no future edition posted on the chapter page as of 2026-10-18)",
        "start_date": "",
        "end_date": "",
        "time_text": "",
        "location": "San Francisco (venues vary)",
        "organizer": "AI Tinkerers San Francisco",
        "admission": "",
        "source_url": "https://sf.aitinkerers.org/",
        "source_label": "AI Tinkerers San Francisco — official chapter site",
        "source_authority": "Official organizer",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7). Official chapter site states \"AI "
            "Tinkerers San Francisco is a hands-on AI builder meetup with live demos, technical "
            "discussion, and no-pitch networking\", \"Local cadence: 25 events in the last 12 "
            "months\", \"Format: Live demos, technical Q&A, no sales pitches\", \"Audience: "
            "Screened AI builders, founders, researchers, and engineers\". Cost is left blank per "
            "policy: some past editions' registration listings expose $0 general admission while "
            "others are screened or invitation-only, and no series-level cost statement exists — "
            "see flag-ai-tinkerers-cost-unstated. Newest posts on the fetched page are past "
            "editions; no future date is invented."
        ),
    },
    {
        "id": "nye-fireworks-sf",
        "name": "New Year's Eve Fireworks on the San Francisco waterfront",
        "bucket": "recurring",
        "cadence": "annual",
        "category": "Community & culture",
        "date_text": "New Year's Eve annually — 2026–27 edition not yet posted on the official Port page as of 2026-10-18",
        "start_date": "",
        "end_date": "",
        "time_text": "Midnight (approximately 15 minutes)",
        "location": "San Francisco waterfront / Embarcadero (fireworks over the Bay; viewing around the Ferry Building and the Promenade)",
        "organizer": "Port of San Francisco",
        "admission": "Free",
        "admission_source_url": "https://downtownsf.org/do/san-francisco-new-years-eve-fireworks-at-midnight",
        "source_url": "https://www.sfport.com/blog/nye",
        "source_label": "Port of San Francisco — Celebrate New Year's Eve on the Waterfront",
        "source_authority": "Government source",
        "status": "verified",
        "review_reason": "",
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7). Official Port of San Francisco page "
            "states \"The fireworks show begins at midnight and lasts approximately 15 minutes "
            "over the Bay\" and \"The best places to watch the show are the areas around the "
            "Ferry Building and the open area along the Promenade\". The Port page currently "
            "describes the December 31, 2025 edition; no 2026–27 edition is posted as of "
            "2026-10-18, so no dates are invented (flag-nye-fireworks-edition-unannounced). The "
            "cost wording (\"annual FREE fireworks show over the Bay\") comes from the Downtown "
            "SF Partnership listing (downtownsf.org), labeled a trusted civic source for the cost "
            "statement only; the Port page itself states no cost."
        ),
    },
]

NEW_REVIEW = [
    {
        "id": "small-change-arcade-grand-opening-2026",
        "name": "Small Change Arcade grand opening (Excelsior)",
        "bucket": "review",
        "cadence": "single-date",
        "category": "Technology, AI & gaming",
        "date_text": "October 16, 2026 (press-reported; not on the organizer site)",
        "start_date": "",
        "end_date": "",
        "time_text": "12:00–3:00 p.m. (press-reported)",
        "location": "4740 Mission Street, San Francisco (press-reported storefront)",
        "organizer": "Small Change Arcade",
        "admission": "",
        "source_url": "https://missionlocal.org/2026/09/excelsior-buzz-the-comic-book-store-is-finally-open-coming-soon-an-arcade/",
        "source_label": "Mission Local (community press) — not an official organizer page",
        "source_authority": "Unverified press report",
        "status": "needs_review",
        "review_reason": (
            "Grand opening of the new Excelsior arcade is reported only by community press: "
            "Mission Local (2026-09-25) quotes the organizer's flyer — \"will be having its "
            "grand opening on Oct. 16 ... Admission is free. No reservation or tickets are "
            "required.\" — and SF Examiner (2026-10-11) reports \"Friday's grand opening will "
            "be held from noon to 3 p.m.\" The organizer's own site (smallchangearcade.com, "
            "fetched 2026-10-18) currently lists only the mini-cabinet rental business "
            "(\"$200/hr - 2.5hr min\", \"All games accept quarters only, no free play!\") and "
            "publishes no storefront events. Per policy, cost and dates are left blank and the "
            "record is flagged for review (flag-small-change-arcade-source); the event already "
            "passed. Promote to a verified row only if the organizer publishes it."
        ),
        "notes": (
            "Added 2026-10-18 (arena/2e5715f9-maltaproj7) as a review record. Press sources: "
            "https://missionlocal.org/2026/09/excelsior-buzz-the-comic-book-store-is-finally-open-coming-soon-an-arcade/ "
            "and https://www.sfexaminer.com/news/community/these-sf-events-turn-frightful-fall-into-a-delightful-month/article_6c3488fa-c30f-4ad3-8c21-ef91d5fe4a1f.html. "
            "Organizer site checked: https://www.smallchangearcade.com/."
        ),
    },
]

NEW_FLAGS = [
    {
        "id": "flag-detour-free-play-condition",
        "event_id": "detour-free-play-tuesday",
        "event": "The Detour — Free Play Tuesday (first Tuesdays)",
        "issue": (
            "Conditional-free wording: the official page states \"enjoy all of our arcade games "
            "for free with a food or beverage purchase\" and labels the night \"Free Play All Day "
            "21+\". Entry and game play are free only with a food or beverage purchase, and the "
            "event is 21+. The row is classed Free with the sourced conditional wording shown "
            "verbatim in the Cost cell; a human reviewer who prefers the stricter reading can "
            "reclassify it as partly free (which would move it to the Paid & partly free page)."
        ),
        "sources": [
            {"label": "The Detour official event page — Free Play Tuesday", "url": "https://www.detoursf.com/event/free-play-tuesday/"},
        ],
        "disposition": (
            "Published as Free with the condition spelled out in the admission text and notes; "
            "flagged so the free/paid boundary decision stays visible. Nonblocking."
        ),
    },
    {
        "id": "flag-detour-weekly-cost-unstated",
        "event_id": "detour-board-game-night",
        "event": "The Detour — Tuesday Board Game Night (and sibling weekly programs)",
        "issue": (
            "Cost gap: the official Happenings page lists Board Game Night (Tuesdays 7:30-10:00) "
            "and the sibling programs (Super Trashed Bros, Killer Queen League Night, --4Play-- "
            "Connect 4 Tournament, Flip'n'Fierce pinball tournament, Trivia Night, Detour Disco) "
            "with times but no admission cost. Cost is left blank for all of them; add a cost "
            "only when an official Detour page states one."
        ),
        "sources": [
            {"label": "The Detour official Happenings page", "url": "https://www.detoursf.com/happenings/"},
        ],
        "disposition": (
            "Board Game Night published with blank cost and listed on the cost-not-stated "
            "register; sibling programs documented in its notes rather than given invented rows "
            "or prices. Nonblocking."
        ),
    },
    {
        "id": "flag-sfpl-free-statement-capture",
        "event_id": "sfpl-gaming-at-the-mix",
        "event": "Gaming at The Mix (San Francisco Public Library)",
        "issue": (
            "Cost-evidence provenance: the program page (sfpl.org/teens/the-mix/gaming) states no "
            "cost. The free label rests on SFPL's own events statement \"All programs and events "
            "are free and open to the public\" (https://sfpl.org/es/teens/events), captured from "
            "the live search index of that SFPL URL on 2026-10-18. The rendered-page fetch of the "
            "same URL returned navigation-heavy extraction that did not surface the sentence in "
            "the extracted body text, so a human reviewer should re-check the sentence on the "
            "live page (any SFPL events page footer) and downgrade the label to \"Not stated\" if "
            "it cannot be confirmed."
        ),
        "sources": [
            {"label": "SFPL — Gaming at The Mix (program page; no cost stated)", "url": "https://sfpl.org/teens/the-mix/gaming"},
            {"label": "SFPL — Upcoming Events (\"All programs and events are free and open to the public\")", "url": "https://sfpl.org/es/teens/events"},
            {"label": "SFPL — The Mix (location and ages 12–18)", "url": "https://sfpl.org/teens/the-mix"},
        ],
        "disposition": (
            "Published with the SFPL free-programs wording cited via admission_source_url and "
            "this provenance flag; re-check advised. Nonblocking."
        ),
    },
    {
        "id": "flag-ai-tinkerers-cost-unstated",
        "event_id": "ai-tinkerers-san-francisco",
        "event": "AI Tinkerers San Francisco",
        "issue": (
            "Cost gap at series level: the official chapter page states no admission cost. Some "
            "past editions' registration listings expose \"$0\" general admission in structured "
            "data (e.g., the AG-UI workshop at Frontier Tower, ended 2025-07-24), but other "
            "editions are screened or invitation-only (\"You MUST apply here\", \"Capacity is "
            "limited to 80 accepted attendees\", \"AI Tinkerers VIP Dinner ... invitation-only\"), "
            "so free admission is not stated for the series and is not assumed."
        ),
        "sources": [
            {"label": "AI Tinkerers San Francisco — official chapter site", "url": "https://sf.aitinkerers.org/"},
            {"label": "Past registration listing with $0 structured data (ended 2025-07-24)", "url": "https://luma.com/ai-tinkerers-workshop"},
        ],
        "disposition": (
            "Published with blank cost on the cost-not-stated register; add a cost only when an "
            "official page states one for the series or a dated edition. Nonblocking."
        ),
    },
    {
        "id": "flag-nye-fireworks-edition-unannounced",
        "event_id": "nye-fireworks-sf",
        "event": "New Year's Eve Fireworks on the San Francisco waterfront",
        "issue": (
            "Two source notes: (1) the official Port of San Francisco page currently describes "
            "the December 31, 2025 edition and no 2026–27 edition is posted as of 2026-10-18, so "
            "the row carries no dates (an undated annual tradition is not assigned an invented "
            "next occurrence); (2) the Port page states no cost — the \"FREE\" wording comes from "
            "the Downtown SF Partnership listing (downtownsf.org), a downtown community benefit "
            "district rather than an organizer or government page, labeled a trusted civic source "
            "for the cost statement only."
        ),
        "sources": [
            {"label": "Port of San Francisco — Celebrate New Year's Eve on the Waterfront (no cost stated; 2025 edition)", "url": "https://www.sfport.com/blog/nye"},
            {"label": "Downtown SF Partnership — \"annual FREE fireworks show over the Bay\"", "url": "https://downtownsf.org/do/san-francisco-new-years-eve-fireworks-at-midnight"},
        ],
        "disposition": (
            "Published as an undated annual tradition with the cost-evidence class disclosed; "
            "re-check the Port page for the 2026–27 edition date before December. Nonblocking."
        ),
    },
    {
        "id": "flag-small-change-arcade-source",
        "event_id": "small-change-arcade-grand-opening-2026",
        "event": "Small Change Arcade grand opening (Excelsior)",
        "issue": (
            "Press-only evidence: the new Excelsior arcade's grand opening (reported Oct 16, "
            "2026, noon–3 p.m., \"Admission is free. No reservation or tickets are required.\") "
            "appears only in Mission Local and SF Examiner coverage quoting the organizer's "
            "flyer/Instagram. The organizer's own site currently lists only mini-cabinet rentals "
            "and publishes no storefront events, so nothing is confirmed from an official page "
            "and the record stays on Flagged for Review with blank cost and blank dates."
        ),
        "sources": [
            {"label": "Mission Local (press) — grand opening report", "url": "https://missionlocal.org/2026/09/excelsior-buzz-the-comic-book-store-is-finally-open-coming-soon-an-arcade/"},
            {"label": "SF Examiner (press) — fall events roundup", "url": "https://www.sfexaminer.com/news/community/these-sf-events-turn-frightful-fall-into-a-delightful-month/article_6c3488fa-c30f-4ad3-8c21-ef91d5fe4a1f.html"},
            {"label": "Small Change Arcade official site (rentals only; no events)", "url": "https://www.smallchangearcade.com/"},
        ],
        "disposition": (
            "Held as a needs_review record with blank fields; promote only if the organizer "
            "publishes the event. Nonblocking."
        ),
    },
    {
        "id": "flag-akihabara-sf-mondays-out-of-city",
        "event_id": "",
        "event": "Rejected candidate: Akihabara Arcade \"SF Mondays\" (not San Francisco)",
        "issue": (
            "Process finding so no later pass re-adds this: the arcade calendar at "
            "akihabaraarcade.com advertises \"SF Mondays — Street Fighter night 3rd Strike Free "
            "to Play\" and \"Losers Bracket\" near San Francisco search results, but the events' "
            "own map and calendar links give \"8901 Harlan Street, Westminster, CO, 80031\". "
            "\"SF Mondays\" means Street Fighter Mondays at a Colorado venue; the events are "
            "outside the City and County of San Francisco and are excluded from the catalog."
        ),
        "sources": [
            {"label": "Akihabara Arcade — Tournaments & Special Events (venue map link: Westminster, CO)", "url": "https://www.akihabaraarcade.com/tournaments-special-events"},
        ],
        "disposition": (
            "Rejected as out-of-city; recorded for manual review and future-pass awareness. "
            "Nonblocking."
        ),
    },
]

DISPOSITION_UPDATES = {
    "flag-free-gaming-coverage-gap": (
        "Partially closed 2026-10-18 (arena/2e5715f9-maltaproj7): verified free gaming "
        "PROGRAMS are now catalogued with official sources — The Detour Free Play Tuesday "
        "(\"all of our arcade games for free with a food or beverage purchase\", monthly first "
        "Tuesdays, 21+) and Gaming at The Mix at SFPL (free per SFPL's programs statement; "
        "monthly gaming tournaments). Neither publishes dated future occurrences, so the "
        "dated-free-gaming count on the dashboard remains 0 and the honest \"no dated, free "
        "upcoming event\" notice stays. Day of the Devs' next SF edition remains unannounced and "
        "GDC 2027 remains paid. Nonblocking."
    ),
    "flag-free-ai-coverage-gap": (
        "Partially closed 2026-10-18 (arena/2e5715f9-maltaproj7): a verified FREE AI program "
        "series is now catalogued — AI Engineering SF (Latent.Space), whose official organizer "
        "page states \"This is a free event, thanks to AWS for the lovely venue!\" — and AI "
        "Tinkerers San Francisco (25 events in the last 12 months per its chapter page) is "
        "catalogued with cost unstated (flag-ai-tinkerers-cost-unstated). Neither publishes a "
        "dated future edition as of 2026-10-18, so the dated-free-AI count remains 0 and the "
        "notice stays. The Open Source AI Week programs remain cost-unstated and stay out of the "
        "free section (flag-open-source-ai-cost unchanged). Nonblocking."
    ),
}


def upsert(rows: list[dict], events: list[dict]) -> int:
    index = {event["id"]: i for i, event in enumerate(events)}
    added = 0
    for row in rows:
        if row["id"] in index:
            events[index[row["id"]]] = row  # idempotent: same content re-applied
        else:
            events.append(row)
            added += 1
    return added


def upsert_flags(flags: list[dict]) -> int:
    index = {flag["id"]: i for i, flag in enumerate(flags)}
    added = 0
    for flag in NEW_FLAGS:
        if flag["id"] in index:
            flags[index[flag["id"]]] = flag
        else:
            flags.append(flag)
            added += 1
    for flag_id, disposition in DISPOSITION_UPDATES.items():
        if flag_id in index:
            flags[index[flag_id]]["disposition"] = disposition
        else:
            raise SystemExit(f"expected existing flag {flag_id} for disposition update")
    return added


def main() -> None:
    data = json.loads(DATA.read_text())
    added_events = upsert(NEW_PUBLISHED, data["events"]) + upsert(NEW_REVIEW, data["events"])
    added_flags = upsert_flags(data["flags"])
    marker = "arena/2e5715f9-maltaproj7 coverage-gap closure"
    if marker not in data["catalog"].get("updated_by", ""):
        data["catalog"]["updated_by"] = (
            data["catalog"].get("updated_by", "").rstrip()
            + " arena/2e5715f9-maltaproj7 coverage-gap closure (free music/gaming/AI programs, "
            "NYE fireworks tradition, +9 records, +7 flags, 2 coverage-gap dispositions updated); "
        )
    DATA.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    published = [e for e in data["events"] if e.get("status") == "verified" and e.get("bucket") in {"recurring", "special"}]
    recurring = [e for e in published if e["bucket"] == "recurring"]
    special = [e for e in published if e["bucket"] == "special"]
    review = [e for e in data["events"] if e.get("bucket") == "review"]
    print(
        f"added events={added_events} flags={added_flags} -> "
        f"published={len(published)} recurring={len(recurring)} special={len(special)} "
        f"review={len(review)} flags={len(data['flags'])}"
    )


if __name__ == "__main__":
    main()
