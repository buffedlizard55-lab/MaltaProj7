# Coverage-gap review and spot re-verification — session `arena/646f6727-maltaproj7` — 2026-10-18 (UTC)

Method: candidate events well known to recur in San Francisco but absent from `data/events.json` were checked **by direct fetch of the official organizer / venue page** (no third-party listings, no search snippets used as evidence). A row is published only when the official page states the name, date/cadence and a San Francisco location. Fields the page does not state are blank. Pages that were hijacked, expired, blocked, or silent on an essential field are recorded as review records or flags, never inferred.

Reproducible patch: `research/coverage-patch-646f6727.py` (idempotent; inserts by id).

## A. New published rows (11) — evidence

| # | Row id | Official source (fetched 2026-10-18) | Quoted evidence | Result |
| --- | --- | --- | --- | --- |
| 1 | `gdc-festival-of-gaming-2027` | https://gdconf.com/ | "March 1-5, 2027 — Moscone Center, San Francisco, CA" (homepage header and hero) | PASS — published; admission blank (pricing on separate page) |
| 2 | `rsa-conference-2027` | https://www.rsaconference.com/library/press-release/2026-closing-release | "RSAC 2027 Conference will take place April 5-8, 2027, in San Francisco at the Moscone Center." | PASS — published; the /usa homepage shows the same April 5–8, 2027 dates and Early-Bird pass prices (Core $1,695, Premium $2,595 until Dec 18, 2026) which are not recorded in the row |
| 3 | `dreamforce-2027` | https://www.salesforce.com/dreamforce/df27-save-the-date/ | "September 21-23, 2027 \| San Francisco and Salesforce+" | PASS — published; venue not named → flag `flag-dreamforce-2027-venue` |
| 4 | `jpm-healthcare-conference-2027` | https://www.jpmorgan.com/about-us/events-conferences/health-care-conference | "The 45th Annual Healthcare Conference will take place on January 11-14, 2027 in San Francisco, California"; "This event is by invitation only and invitations are not transferable." | PASS — published with admission "By invitation only" |
| 5 | `techcrunch-disrupt-2026` | https://techcrunch.com/events/ | Table row "Oct 13 – 15, 2026 / San Francisco, CA / TechCrunch Disrupt 2026"; sidebar "Join 10,000 founders, VCs, and operators on October 13-15" | PASS — published; dedicated page blocked by Cloudflare challenge / 404 → flag `flag-techcrunch-disrupt-event-page` |
| 6 | `chinatown-autumn-moon-festival-2026` | https://www.moonfestival.org/ | "September 19 - 20 • 11am - 5pm / 2026 SF Chinatown Autumn Moon Festival / Presented by the Chinatown Merchants Association"; "Location GRANT Avenue Between California & Broadway"; "Cost FREE!" | PASS — published with hours, location, free admission |
| 7 | `chinese-new-year-flower-market-fair-2027` | https://chineseparade.com/flowermarketfair/ | "The 2027 Flower Market Fair is scheduled for Sat. & Sun. Jan. 30 & 31 @Grant between Clay and Broadway." | PASS — published; hours/admission not stated → blank |
| 8 | `trans-march-2026` | https://transmarch.org/ | "Trans March kicks off Pride weekend on Friday every year. Dolores Park: 3 - 6pm, March @ 6pm."; embedded video title "Trans March 2026: June 26 @ Dolores Park" | PASS — published (2026 edition); 2027 date not posted |
| 9 | `golden-gate-park-band-2026-season` | https://goldengateparkband.org/ | "Our season runs from April through September, with shows every Sunday plus July 4 and Labor Day at the Spreckels Temple of Music in the Music Concourse of Golden Gate Park."; "2026 season … 25 high-quality concerts"; "keep this treasured cultural tradition free for all" | PASS — published as seasonal/free; exact dates and start time are on the calendar page and left blank. Distinct from the existing review record `golden-gate-bandshell-concerts` (SF Rec & Park Bandshell series page, still unreadable) |
| 10 | `sf-ballet-nutcracker-2026` | https://www.sfballet.org/productions/nutcracker/ | "DEC 4–27"; performance list from "Fri Dec 04 7:00 pm" to "Sun Dec 27 4:00 pm"; "Location War Memorial Opera House" | PASS — published; ticket prices not on page → admission blank |
| 11 | `off-the-grid-fort-mason-night-market-2026` | https://offthegrid.com/event/fort-mason-center/ | "Upcoming Schedule: Fri 11/6 5PM - 10PM"; "Free admission. All ages welcome. May through December."; "2026 Dates: Friday, May 22 / June 19 / July 24 / August 21 / September 18 / October through December dates to be announced"; "2 Marina Blvd, San Francisco" | PASS — published as seasonal; end date blank |

## B. New review-only records (4)

| Row id | Source | Finding | Status |
| --- | --- | --- | --- |
| `how-weird-street-faire` | https://howweird.org/ | "2000 — 2024 … The Faire is done." Organizer confirms the event ended after 25 years. | `cancelled` (discontinued) — audit exception so it is not re-added |
| `union-street-festival` | https://www.unionstreetfestival.com/ ; https://www.sresproductions.com/events/union-street-festival/ | First domain serves Turkish casino spam; second redirects to an unrelated sports-streaming host. No official page located. | `needs_review`, all fields blank; flag `flag-union-street-festival-domains` |
| `sf-dyke-march-2027` | https://www.thedykemarch.org/ (FAQ URL 404) | Homepage states only "Saturday, June 26, 2027"; no location/time stated. | `needs_review` — location blank, not inferred |
| `litquake-2026` | https://litquake2026.sched.com/ | Schedule begins Sunday Oct 11, 2026; venue list includes Oakland, Berkeley, Sausalito and a Marin filter; no end date stated on index. | `partial_sf_program` — Lit Crawl SF (Oct 24) remains the published city-only component |

## C. Candidates checked and NOT added (no usable official source)

- **SF Dragon Boat Festival** — `sfdragonboat.com` returns "Squarespace — Website Expired". No row created (no official text to cite).
- **Union Square holiday ice rink / tree lighting** — `visitunionsquaresf.com/events/` renders only a cookie banner and footer (JavaScript-only content). Not added.
- **San Francisco Symphony 2026–27** — `sfsymphony.org/Buy-Tickets/2026-27` returns a loading shell only. Not added.
- **Kaiser Permanente SF Half Marathon** — `runsfhalf.com` fetch failed. Not added.

## D. Spot re-verification of existing rows (G2)

| Row | Source re-fetched | Result |
| --- | --- | --- |
| `downtown-first-thursdays` | https://www.dftsf.com/ | PASS — "Next UP: NOV 5, 2026", "Free w/ RSVP", "2nd St. between Market and Howard in SF \| 5-10PM" matches row |
| `sf-sketchfest-2027` | https://sfsketchfest.com/ | PASS — "Jan 14 - 31, 2027 / SF Sketchfest 2027" |
| `cloudflare-connect-2026` | https://www.cloudflare.com/connect/ | PASS — "Oct 19-21 · Moscone West, SF", Conference Pass $595 |
| `bay-to-breakers-2027` | https://www.baytobreakers.com/ | PASS with irregularity — headline/title "May 16, 2027" but sidebar copy says "before May 18"; flagged `flag-bay-to-breakers-page-copy` |

## E. Build / verification

`python3 research/coverage-patch-646f6727.py` → added 15 events, 4 flags. `python3 build.py` → "Built 104 published events: 85 recurring, 19 special, 8 categories; 16 review records." `python3 verify.py` → ALL LOCAL CATALOG, SOURCE-LINK, AND NAVIGATION CHECKS PASSED. Count guards in `verify.py` updated 93/74/19/12 → 104/85/19/16 together with this entry (and the matching note in `research/official-source-audit.md`).
