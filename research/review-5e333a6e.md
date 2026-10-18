# Repo review and coverage-gap pass — arena/5e333a6e-maltaproj7 (2026-10-18)

Scope: (S1) structural review of `data/events.json` and spot re-verification against official pages; (S2) adding missing City-and-County-of-San-Francisco events, each verified on an official organizer, venue, or government page fetched on 2026-10-18. Nothing was inferred: a value is published only when the linked page states it, and conflicts are blanked and flagged.

## S1 — Structural review findings

| # | Finding | Rows | Disposition |
|---|---|---|---|
| 1 | Two editions of the same event appear as separate rows, and their sources are inconsistent (www vs non-www; the IOFF 2027 row has no time or admission because the organizer has not published them) | `fillmore-jazz-festival-2026/2027`, `international-ocean-film-festival-2026/2027`, `italian-heritage-parade-2026/2027` | Kept. Separate editions are legitimate and each row cites the page that states its date. Documented here, no change. |
| 2 | Recurring rows tagged `weekly` without a `start_date` | `exclusion-presidio-exhibition-2026`, `i-am-an-american-exhibition-2026` | Kept. The Presidio Trust press release states a weekly schedule (Fri–Sun / Fri–Tue) through Aug 31, 2026 but no opening date, so `start_date` correctly stays blank. Both exhibitions have closed as of 2026-10-18. |
| 3 | Many 2026 rows are in the past relative to `as_of` 2026-10-18 | about 60 rows | This is by design: the catalog is a 2026–27 snapshot. A computed upcoming/past badge would help readers; recommended as a follow-up for `build.py` (not changed here, to keep this PR to data). |
| 4 | Bay to Breakers homepage has stale "before May 18!" copy beside the May 16, 2027 headline | `bay-to-breakers-2027` | Already flagged (`flag-bay-to-breakers-copy`, `flag-bay-to-breakers-page-copy`). The row is correct. |
| 5 | Review rows with blank cadence | `bay-area-aloha-festival`, `sf-fringe-2026`, `how-weird-street-faire`, `union-street-festival` | Correct. No live official page states a cadence. |

Spot re-verification (all PASS, official pages): Fourth of July fireworks (sf.gov: July 4, 2026, 9:30–9:45pm, free); Bay to Breakers 2027 (May 16, 2027); Chinese New Year Parade 2027 (chineseparade.com FAQ and home: Feb 20, 2027); SF Pride 2027 (sfpride.org: June 26–27, 2027); Microsoft Ignite 2026 (moscone.com: Nov 17–20, Moscone Center); AGU 2026 (moscone.com: Dec 7–11, Moscone Center); Dreamforce 2026 (moscone.com: Sept 15–17, "San Francisco & Salesforce+").

## S2 — Rows added (32 published) and flags (5)

### Moscone Center conventions (official venue pages, `https://www.moscone.com/events/<slug>`)

| Row | Dates stated | Hall stated |
|---|---|---|
| AI Engineer World's Fair | June 30–July 2, 2026 | Moscone Center |
| AMD Advancing AI | July 22–23 (page heading "Advancing AI 2026") | Moscone Center |
| NPH 47th Annual Affordable Housing Conference | September 24, 2026 | Moscone Center |
| CoreWeave Fully Connected | Sept 29–Oct 1, 2026 | Moscone Center |
| SEMICON West | October 13–15, 2026 | Moscone Center |
| Current San Francisco (Confluent) | November 4–5, 2026 | Moscone West |
| Specialty Food Association Winter FancyFaire | January 17–19, 2027 | not stated |
| ASCO GI Cancers Symposium | January 21–23, 2027 | Moscone West |
| SPIE Photonics West | Jan 30–Feb 4, 2027 | not stated |
| ASCO GU Cancers Symposium | February 11–13, 2027 | Moscone West |
| Orthopaedic Research Society Annual Meeting | February 19–23, 2027 | not stated |
| TDX 2027 (Salesforce) | March 10–11, 2027 | Moscone Center |
| AAD Annual Meeting | March 19–23, 2027 | not stated |
| AMCP 2027 | April 13–16, 2027 | not stated |
| Atlassian Team '27 | April 20–22, 2027 | Moscone Center |
| ASRS Annual Meeting | July 28–31, 2027 | not stated |

Where the hall is not stated, the location reads "Listed on the Moscone Center events calendar, San Francisco (hall not stated)". The Moscone pages also confirm the peer rows for GDC 2027 (Mar 1–5), RSAC 2027 (Apr 5–8), and TechCrunch Disrupt 2026 (Oct 13–15).

### Other additions

| Row | Key values | Source |
|---|---|---|
| FAMSF Free Saturdays (weekly) | Free general admission (permanent collection) for nine-county Bay Area residents | https://www.famsf.org/visit/free-reduced-admission |
| FAMSF Free First Tuesdays (monthly) | Free general admission | same |
| SF Open Studios (52nd annual) | Preview Sept 19–27, 2026, 1–7pm, SOMArts; studios through Oct 25 | https://somarts.org/exhibition/sfopenstudios2026/ |
| Cole Valley Street Fair (annual) | Sun Sept 27, 2026, 10am–5pm | SFMTA travel update |
| Bearrison Street Fair (third annual) | Sat Oct 17, 2026, noon–6pm, Harrison 10th–13th | SFMTA weekly advisory Oct 15–21 |
| Potrero Hill Festival (annual) | Sat Oct 17, 2026, 20th St; hours blank (conflict) | SFMTA weekly advisory and travel update |
| Clement Street Art Fair | Sat Oct 17, 2026, noon–5pm | SFMTA weekly advisory |
| Brava Block Party | Sat Oct 17, 2026, noon–5pm | SFMTA weekly advisory |
| SF Lowriders King of the Streets | Sat Sept 19, 2026, Mission St 18th–26th | SFMTA travel update |
| Diplo's Run Club SF 5K | Sun Oct 18, 2026, 8:30am start, Robin Williams Meadow | SFMTA weekly advisory |
| Lower Polk Live | Fri Oct 23, 2026, 4–9pm | SFMTA travel update |
| From the E Excelsior Night Market | Fri Oct 23, 2026, 4:30–8:30pm | SFMTA travel update |
| Noe Valley Night Market | Tue Oct 27, 2026, 4:30–8:30pm | SFMTA travel update |
| SF Half Marathon & 5K | Feb 7, 2027, Golden Gate Park / Sunset Dunes | https://sanfranciscohalfmarathon.org/race-information/ |
| The Pink Triangle | Sun June 7, 2026, Twin Peaks | https://sfpride.org/events/ |
| SF Dyke March 2026 (annual) | Sat June 27, 2026; march 5pm after Dolores Park rally | https://www.sfmta.com/project-updates/dyke-march |

### Flags added

- `flag-jpm-2027-venue`: the organizer page names no venue for the 2027 conference.
- `flag-sf-open-studios-start`: the studio-weekend start date and hours are not on an official page fetched; ArtSpan's own page is an empty shell.
- `flag-autumn-moon-hours`: the organizer gives 11am–5pm and SFMTA gives 11am–6pm. This flag is attached to the peer row `chinatown-autumn-moon-festival-2026`.
- `flag-fort-mason-night-market-season`: the Fort Mason venue page lists Oct 16, which Off the Grid's date list omits. This flag is attached to the peer row `off-the-grid-fort-mason-night-market-2026`.
- `flag-potrero-hill-festival-hours`: two SFMTA pages disagree (10am–4:30pm vs 11am–4pm).

### Peer overlap (PR #18, arena/646f6727)

Nine rows prepared here were already merged by the peer session and were skipped: GDC 2027, RSAC 2027, Dreamforce 2027, J.P. Morgan 2027, TechCrunch Disrupt 2026, Autumn Moon 2026, Trans March 2026, Fort Mason Night Market, and Litquake 2026. The peer rows were kept unchanged.

## Not added (coverage boundary)

| Candidate | Reason |
|---|---|
| New Year's Eve fireworks | No official organizer or City page found; only downtown association and BART blog coverage |
| Union Square tree lighting | No official lighting ceremony page found |
| SF Veterans Day Parade 2026 | Only band and third-party listings found; no official City or organizer page |
| FOG Design+Art 2027 | Dates (Jan 21–24, 2027) seen only in search snippets of the SFMOMA series page; the event page returned 404 |
| Sunset Night Market, Sunset Oktoberfest Block Party | Seen only in search snippets of SFMTA pages; not fetched directly |
| Pro sports schedules (Giants, Warriors, Valkyries) | Out of scope: these are game schedules rather than catalogued events |
| Data+AI Summit, Snowflake Summit, Turkey Trot, Earth Day SF, DocFest/IndieFest, Mostly British, LNY Flower Fair 2026, Friday Nights at de Young, Noe and Outer Sunset farmers markets | Not verified on an official page within this pass |
| Top of the Hill Festival, Daly City Street Festival | Located in Daly City (outside city limits) |
