# Official-source audit — San Francisco city events

**Audit date:** 2026-10-18 (original audit plus same-day final-integration re-verification of every row against a live official page)

**Geographic rule:** City and County of San Francisco only  
**Catalog snapshot:** 67 published, source-linked records: 56 regularly occurring and 11 dated/special. 12 non-published records remain on the review register.

## What was checked

1. The source was an official organizer, official venue, SF government page, or a clearly labeled trusted civic source (SF Travel, the City and County's official destination marketing organization, or a municipal arts calendar).
2. The row name, a date/cadence, and a San Francisco location were checked against the linked source. Where a program crosses city lines, only an explicitly identified SF component is published; otherwise the program is held in the review register.
3. Hours, admission, venues, and dates were copied only when the linked source stated them. Optional values absent from the captured source are displayed as an em dash rather than guessed. Placeholder text such as "See organizer schedule" was removed everywhere in the re-verification.
4. A status other than `verified` is not included in the public recurring or special-event tables. It appears only on **Flagged for Review** with the reason for exclusion.

This is a reproducible catalog, not a claim that every private, newly announced, or unlisted SF event exists in the data. External event details can change after this audit; the linked organizer source remains the final planning reference.

## Status key

| Status | Treatment |
|---|---|
| `verified` | Published in the city-only catalog. Required source/date/location checks passed. |
| `partial_sf_program` | The named festival is multi-city. Not published until city-specific programs can be separated. |
| `needs_review` | Essential date or location evidence was not retained from a direct source. Fields remain blank. |
| `cancelled` | Official organizer reported the event cancelled; never shown as active. |
| `outside_city_excluded` | Official material places the event outside the City and County of San Francisco. |

## Published records

Every row below has a source link; dates and locations are the audit-captured values used in `data/events.json`.

| ID | Event | Verified date / cadence | Verified SF location | Source | Authority | Status |
|---|---|---|---|---|---|---|
| `ferry-plaza-farmers-market` | Ferry Plaza Farmers Market | Tuesday, Thursday, and Saturday (year-round) | Ferry Building, One Ferry Building, San Francisco | [Foodwise market page](https://foodwise.org/markets/ferry-plaza-farmers-market/) | Official organizer | verified |
| `alemany-farmers-market` | Alemany Farmers Market | Saturday | 100 Alemany Boulevard, San Francisco, CA 94110 | [SF.gov location page](https://www.sf.gov/location--alemany-farmers-market) | Government source | verified |
| `mission-community-market` | Mission Community Market | Thursday, mid-March–mid-November | 22nd Street between Mission and Valencia / 84 Bartlett St., San Francisco | [Foodwise market page](https://foodwise.org/markets/mission-community-market/) | Official organizer | verified |
| `castro-farmers-market-2026` | Castro Farmers’ Market | Wednesday, April 1–November 18, 2026 | 270 Noe St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/castro-farmers-market) | Official organizer | verified |
| `divisadero-farmers-market` | Divisadero Farmers’ Market | Sunday (year-round) | 1377 Fell St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/divisadero-farmers-market) | Official organizer | verified |
| `fillmore-farmers-market` | Fillmore Farmers’ Market | Saturday (year-round) | 1700 O’Farrell St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/fillmore-farmers-market) | Official organizer | verified |
| `hayes-valley-farmers-market` | Hayes Valley Farmers’ Market | Saturday (year-round) | 450 Hayes St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/hayes-valley-farmers-market) | Official organizer | verified |
| `inner-sunset-farmers-market` | Inner Sunset Farmers’ Market | Sunday (year-round) | 1315 8th Ave.; parking lot between 8th and 9th off Irving St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/inner-sunset-farmers-market) | Official organizer | verified |
| `sunday-streets-2026` | Sunday Streets SF — 2026 season | Tenderloin Jun 14; Mission Jul 19; Bayview Aug 23; Excelsior Oct 18, 2026 | Tenderloin, Mission, Bayview, and Excelsior, San Francisco | [Sunday Streets SF 2026 season page](https://sundaystreetssf.com/) | Official organizer | verified |
| `stern-grove-festival-2026` | Stern Grove Festival — 2026 season | Sundays June 14–August 16, 2026, plus Saturday, August 15 | Sigmund Stern Grove, San Francisco | [Stern Grove 2026 lineup](https://www.sterngrove.org/lineup2026) | Official organizer | verified |
| `free-shakespeare-in-the-park-2026` | Free Shakespeare in the Park — San Francisco performances | September 5–27, 2026 (San Francisco run) | McLaren Park and Sue Bierman Park, San Francisco | [SF Shakespeare Festival — Free Shakespeare performance page](https://sfshakes.org/performance/free-shakes/ac/) | Official organizer | verified |
| `flower-piano-2026` | Flower Piano | September 10–20, 2026 | San Francisco Botanical Garden, Golden Gate Park | [Gardens of Golden Gate Park event page](https://gggp.org/event/flower-piano-2026/) | Official organizer | verified |
| `chinese-new-year-parade-2027` | San Francisco Chinese New Year Parade | Saturday, February 20, 2027 | 2nd and Market Streets through Union Square to Kearny Street and Columbus Avenue, San Francisco | [Chinese New Year Parade FAQ](https://chineseparade.com/faq/) | Official organizer | verified |
| `cherry-blossom-2027` | Northern California Cherry Blossom Festival | April 10–11 and April 17–18, 2027; Grand Parade April 18 | Japantown, San Francisco | [Cherry Blossom Festival official site](https://sfcherryblossom.org/) | Official organizer | verified |
| `sf-pride-2027` | San Francisco Pride Celebration & Parade | June 26–27, 2027 | Civic Center, San Francisco | [SF Pride official site](https://sfpride.org/) | Official organizer | verified |
| `carnaval-sf-2026` | Carnaval San Francisco | May 23–24, 2026 | Mission District, San Francisco | [Carnaval SF event page](https://carnavalsanfrancisco.org/special-events/) | Official organizer | verified |
| `bay-to-breakers-2027` | Bay to Breakers | Sunday, May 16, 2027 | San Francisco streets; official route information is published by the organizer | [Bay to Breakers official site](https://www.baytobreakers.com/) | Official organizer | verified |
| `st-patricks-parade-2026` | San Francisco St. Patrick’s Day Parade & Festival | Saturday, March 14, 2026 | Parade from 2nd and Market to Civic Center; Civic Center Plaza, San Francisco | [United Irish Societies parade page](https://uissf.org/st-patricks-day-parade) | Official organizer | verified |
| `caamfest-2026` | CAAMFest — San Francisco program | May 7–10, 2026 (San Francisco program) | AMC Kabuki, Asian Art Museum, KOHO Creative Hub, Koret Auditorium, and New People Cinema, San Francisco | [CAAMFest 2026 schedule](https://caamfest.com/2026/schedule/) | Official organizer | verified |
| `sf-silent-film-festival-2026` | San Francisco Silent Film Festival | May 6–10, 2026 | Castro Theatre, San Francisco | [Silent Film Festival 2026 page](https://silentfilm.org/festival-2026/) | Official organizer | verified |
| `sf-black-film-festival-2026` | San Francisco Black Film Festival | June 18–21, 2026 | San Francisco | [SF Black Film Festival official site](https://sfbff.org/) | Official organizer | verified |
| `sf-dance-film-festival-2026` | San Francisco Dance Film Festival | October 23–November 8, 2026 (in-person); online window follows | San Francisco theaters for in-person program; online component separate | [Dance Film Festival 2026 page](https://sfdancefilmfest.org/fall-festival-2026/) | Official organizer | verified |
| `sf-transgender-film-festival-2026` | San Francisco Transgender Film Festival | November 12–14, 2026 | Roxie Theater, San Francisco | [SF Transgender Film Festival — 2026 festival schedule](https://sftff.org/festival/2026-festival-schedule/) | Official organizer | verified |
| `third-i-south-asian-film-festival-2026` | 3rd i San Francisco International South Asian Film Festival | October 9–11, 2026 | San Francisco | [3rd i Films official site](https://thirdi.org/) | Official organizer | verified |
| `lit-crawl-sf-2026` | Lit Crawl SF | October 24, 2026 | Mission District venues, San Francisco | [Lit Crawl SF official page](https://www.litquake.org/litcrawl) | Official organizer | verified |
| `hardly-strictly-bluegrass-2026` | Hardly Strictly Bluegrass | October 2–4, 2026 | Hellman Hollow, Lindley Meadow, and Marx Meadow, Golden Gate Park, San Francisco | [Hardly Strictly Bluegrass FAQ](https://hardlystrictlybluegrass.com/info-faq-2026/) | Official organizer | verified |
| `fleet-week-sf-2026` | San Francisco Fleet Week | Ship tours October 7–12; Fleet Fest October 10–11; air show October 9–11, 2026 | San Francisco waterfront, Marina Green, Fisherman’s Wharf, and city venues | [Fleet Week 2026 calendar](https://fleetweeksf.org/calendar-of-events/) | Official organizer | verified |
| `up-your-alley-2026` | Up Your Alley | Sunday, July 26, 2026 | Folsom Street between 8th and 11th; connected SoMa streets, San Francisco | [Folsom Street FAQ](https://www.folsomstreet.org/faq) | Official organizer | verified |
| `folsom-street-fair-2026` | Folsom Street Fair | Sunday, September 27, 2026 | Folsom Street between 7th and 13th and connected SoMa streets, San Francisco | [Folsom Street Fair official page](https://www.folsomstreet.org/folsom-street-fair) | Official organizer | verified |
| `castro-street-fair-2026` | Castro Street Fair | Sunday, October 4, 2026 | Castro and Market Streets and surrounding Castro District streets, San Francisco | [Castro Street Fair information page](https://castrostreetfair.org/fair/) | Official organizer | verified |
| `nihonmachi-street-fair-2026` | Nihonmachi Street Fair | August 1–2, 2026 | Japantown, San Francisco | [Nihonmachi Street Fair 2026 page](https://www.nihonmachistreetfair.org/home-1) | Official organizer | verified |
| `pistahan-2026` | Pistahan Parade & Festival | August 8–9, 2026; parade Saturday | Yerba Buena Gardens; Saturday parade on Market Street, San Francisco | [Pistahan official site](https://pistahan.net/) | Official organizer | verified |
| `north-beach-festival-2026` | North Beach Festival | June 20–21, 2026 | North Beach, San Francisco | [Sunset Mercantile — North Beach Festival 2026 page](https://sunsetmercantilesf.com/northbeachfestival2026/) | Official organizer | verified |
| `fillmore-jazz-festival-2027` | Fillmore Jazz Festival | July 3–4, 2027 | Fillmore District, San Francisco | [Fillmore Jazz Festival official site (fillmorejazzfest.com)](https://fillmorejazzfest.com/) | Official organizer | verified |
| `muni-heritage-weekend-2026` | Muni Heritage Weekend | September 19–20, 2026 | 77 Steuart Street, San Francisco | [SFMTA event page](https://www.sfmta.com/calendar/muni-heritage-weekend-2026) | Government source | verified |
| `italian-heritage-parade-2026` | Italian Heritage Parade | October 11, 2026 | San Francisco | [Italian Heritage Parade official site](https://sfitalianheritage.org/) | Official organizer | verified |
| `world-arts-west-dance-festival-2026` | World Arts West Dance Festival | September 6, 2026 | Presidio Tunnel Tops, Presidio of San Francisco | [Presidio Trust event page](https://presidio.gov/explore/events/world-arts-west-dance-festival-2026) | Official venue / federal trust | verified |
| `sf-porchfest-2026` | SF Porchfest | May 30, 2026 | Mission District porches, backyards, and stoops, San Francisco | [SF Porchfest official app/site](https://app.sfporchfest.org/) | Official organizer | verified |
| `juneteenth-sf-freedom-celebration-2026` | Juneteenth SF Freedom Celebration | June 13, 2026 | Fillmore/Western Addition; historic Fillmore Street, San Francisco | [SF.gov 2026 Juneteenth page](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) | Government source | verified |
| `juneteenth-market-street-parade-2026` | Juneteenth Market Street Parade | June 20, 2026 | Market Street, San Francisco | [SF.gov 2026 Juneteenth page](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) | Government source | verified |
| `juneteenth-on-the-waterfront-2026` | Juneteenth on the Waterfront | June 7, 2026 | Ferry Building Farmers Market / waterfront, San Francisco | [SF.gov 2026 Juneteenth page](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) | Government source | verified |
| `sf-international-arts-festival-2026` | San Francisco International Arts Festival | April 29–May 10, 2026 | Venues in the Mission District, San Francisco | [SFIAF 2026 festival page](https://www.sfiaf.org/2026_festival) | Official organizer | verified |
| `sundown-cinema-inside-out-2026` | Sundown Cinema: Inside Out | July 24, 2026 | Presidio of San Francisco | [Presidio Trust 2026 summer announcement](https://presidio.gov/about/press/presidio-unveils-vibrant-2026-summer-event-lineup) | Official venue / federal trust | verified |
| `scaregrove-2026` | Scaregrove | October 30, 2026 | Sigmund Stern Grove, 19th Avenue and Sloat Boulevard, San Francisco, CA 94132 | [SF Recreation and Park calendar (Scaregrove listing, event EID 10822)](https://sfrecpark.org/Calendar.aspx) | Government source | verified |
| `foodwise-black-holiday-market-2026` | Foodwise Black Holiday Market | December 12, 2026 | Ferry Plaza, San Francisco | [Foodwise event page](https://foodwise.org/events/pop-ups-on-the-plaza-black-holiday-market/) | Official organizer | verified |
| `cloudflare-connect-2026` | Cloudflare Connect | October 19–21, 2026 | Moscone West, San Francisco | [Cloudflare Connect official page](https://www.cloudflare.com/connect/) | Official organizer | verified |
| `informs-annual-meeting-2026` | INFORMS Annual Meeting | November 1–4, 2026 | Moscone South and San Francisco Marriott Marquis | [INFORMS Annual Meeting official page](https://meetings.informs.org/wordpress/annual/) | Official organizer | verified |
| `microsoft-ignite-2026` | Microsoft Ignite | November 17–20, 2026 | Moscone Center, San Francisco | [Moscone Center — Microsoft Ignite 2026 event page](https://www.moscone.com/events/microsoft-ignite-2026) | Official venue | verified |
| `agu-annual-meeting-2026` | AGU26 Annual Meeting | December 7–11, 2026 | San Francisco, CA | [AGU Annual Meeting official page](https://www.agu.org/annual-meeting) | Official organizer | verified |
| `heart-of-the-city-farmers-market` | Heart of the City Farmers Market | Sunday and Wednesday | Civic Center, Fulton Street and Larkin Street, San Francisco | [Heart of the City Farmers Market official site](https://hotcfarmersmarket.org/) | Official organizer | verified |
| `fort-mason-center-farmers-market` | Fort Mason Center Farmers Market | Sunday | Fort Mason Center, Marina Boulevard, San Francisco, CA 94109 | [California Farmers' Markets Association — Fort Mason market page](https://www.cafarmersmkts.com/fort-mason-center-farmers-market) | Official organizer | verified |
| `exploratorium-after-dark` | Exploratorium After Dark | Thursday | Exploratorium, Pier 15, San Francisco | [Exploratorium — After Dark calendar page](https://www.exploratorium.edu/visit/calendar/after-dark) | Official organizer | verified |
| `calacademy-nightlife` | NightLife at the California Academy of Sciences | Most Thursdays | California Academy of Sciences, Golden Gate Park, San Francisco | [California Academy of Sciences — NightLife page](https://www.calacademy.org/nightlife) | Official organizer | verified |
| `downtown-first-thursdays` | Downtown First Thursdays | First Thursday monthly; next listed November 5, 2026 | Second Street between Market and Howard Streets, San Francisco, CA 94105 | [Downtown First Thursdays official site](https://www.dftsf.com/) | Official organizer | verified |
| `valencia-live` | Valencia LIVE! | Second Thursday monthly, May–October 2026 (May 14; June 11; July 9; August 13; September 10; October 8) | Valencia Street between 16th and 21st Streets, San Francisco (blocks shift by month) | [Valencia LIVE! — VCMA official page](https://www.visitvalenciastreet.com/live) | Official organizer | verified |
| `aids-walk-san-francisco-2026` | AIDS Walk San Francisco | Sunday, July 19, 2026 | Robin Williams Meadow, Golden Gate Park, San Francisco | [AIDS Walk San Francisco — FAQ](https://sf.aidswalk.net/FAQ) | Official organizer | verified |
| `sf-sketchfest-2027` | SF Sketchfest | January 14–31, 2027 | San Francisco | [SF Sketchfest official site](https://sfsketchfest.com/) | Official organizer | verified |
| `ybg-festival-2026` | YBG Festival (Yerba Buena Gardens Festival) | May 9–November 13, 2026 | Yerba Buena Gardens, San Francisco | [SF Travel press release — 2026 live music lineup (June 11, 2026)](https://www.sftravel.com/media/press-release/san-francisco-amplifies-its-2026-live-music-scene-expanded-lineup-festivals) | Trusted civic source | verified |
| `outside-lands-2026` | Outside Lands Music & Arts Festival | August 7–9, 2026 | Golden Gate Park, San Francisco | [SFMTA travel update — Outside Lands, August 7–9, 2026](https://www.sfmta.com/travel-updates/outside-lands-august-7-9-2026) | Government source | verified |
| `portola-music-festival-2026` | Portola Music Festival | September 26–27, 2026 | Pier 80, San Francisco | [SFMTA travel update — Portola Music Festival, September 26 & 27, 2026](https://www.sfmta.com/travel-updates/portola-music-festival-september-26-27-2026) | Government source | verified |
| `jerry-day-2026` | Jerry Day | August 1, 2026 | McLaren Park, San Francisco | [SF Travel press release — 2026 live music lineup (June 11, 2026)](https://www.sftravel.com/media/press-release/san-francisco-amplifies-its-2026-live-music-scene-expanded-lineup-festivals) | Trusted civic source | verified |
| `escape-from-alcatraz-triathlon-2026` | Escape from Alcatraz Triathlon | Sunday, June 7, 2026 | Alcatraz Island to St. Francis Yacht Club; Presidio, Golden Gate Park, and Baker Beach; finish at Marina Green, San Francisco | [SFMTA — Escape from Alcatraz Triathlon, June 7, 2026](https://www.sfmta.com/project-updates/escape-alcatraz-triathlon) | Government source | verified |
| `day-of-the-dead-procession-2026` | Day of the Dead (Día de los Muertos) Procession | November 2, 2026 | Mission District, San Francisco | [SF Travel — San Francisco festivals and events in November](https://www.sftravel.com/article/san-francisco-festivals-events-november) | Trusted civic source | verified |
| `illuminate-sf-2026` | Illuminate SF Festival of Light | Begins November 27, 2026 | Citywide, San Francisco | [SF Travel — San Francisco festivals and events in November](https://www.sftravel.com/article/san-francisco-festivals-events-november) | Trusted civic source | verified |
| `sf-marathon-expo-2026` | San Francisco Marathon Expo | July 24–25, 2026 | Fort Mason Festival Pavilion, 2 Marina Boulevard, San Francisco | [San Francisco Marathon race-weekend page](https://www.thesfmarathon.com/race-weekend/) | Official organizer | verified |
| `juneteenth-mayor-kickoff-2026` | Juneteenth Mayor's Kickoff Celebration | June 5, 2026 | City Hall, San Francisco | [SF.gov 2026 Juneteenth page](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) | Government source | verified |
| `fourth-of-july-fireworks-golden-gate-2026` | Fourth of July Fireworks on Golden Gate Bridge | Saturday, July 4, 2026 | Golden Gate Bridge, San Francisco, CA 94129 | [SF.gov event page — Fourth of July fireworks on Golden Gate Bridge](https://www.sf.gov/event-20260704-fourth-of-july-fireworks-on-golden-gate-bridge) | Government source | verified |

## Review register and explicit exclusions

| ID | Item | Captured date | Source | Status | Why it is not in city-only tables |
|---|---|---|---|---|---|
| `sf-marathon-2026` | San Francisco Marathon — race weekend | July 24–26, 2026 | [San Francisco Marathon race-weekend page](https://www.thesfmarathon.com/race-weekend/) | `needs_review` | The organizer's full-marathon course crosses the Golden Gate Bridge into Marin County, so the race-weekend umbrella is not city-only. The San Francisco-only Expo is published separately as a dated special event; no umbrella row is published. |
| `international-ocean-film-festival-2026` | International Ocean Film Festival — San Francisco program | April 10–12, 2026 (San Francisco program) | [International Ocean Film Festival page](https://intloceanfilmfest.org/festival) | `needs_review` | At the 2026-10-18 re-check the linked /festival page returned a not-found response and the organizer homepage stated no textual dates or San Francisco venue. The previously captured April 10–12 Cowell Theater program could not be reconfirmed from a live official page. |
| `haight-ashbury-street-fair-2026` | Haight-Ashbury Street Fair | September 20, 2026 | [Haight-Ashbury Street Fair official site](https://haightashburystreetfair.org/) | `needs_review` | The organizer homepage (all captured sections) states no 2026 date. The previously listed September 20, 2026 date could not be reconfirmed from the official site at the 2026-10-18 re-check. |
| `comedy-day-2026` | Comedy Day | September 13, 2026 | [Comedy Day official site](https://comedyday.org/) | `needs_review` | The official site confirms a free noon–5pm event at Robin Williams Meadow but states no date. The previously listed September 13, 2026 date could not be reconfirmed from the official site at the 2026-10-18 re-check. |
| `sf-aloha-run-2026` | San Francisco Aloha Run | September 20, 2026 | [SF Aloha Run official site](https://sfaloharun.com/) | `needs_review` | The organizer site could not be fetched at the 2026-10-18 re-check, so the previously captured September 20, 2026 Crissy Field edition cannot be reconfirmed from a live official page. |
| `sffilm-festival-2026` | SFFILM Festival — mixed-geography program | April 24–May 4, 2026 | [SFFILM 2026 festival page](https://sffilm.org/2026-about-the-festival/) | `partial_sf_program` | The official festival page states that the program spans San Francisco, Oakland, and Berkeley. It is excluded from city-only tables until individual San Francisco programs are separated with their own official listings. |
| `sfjff-2026` | San Francisco Jewish Film Festival — mixed-geography program | July 16–August 2, 2026 | [Jewish Film Institute — SFJFF46 archive page](https://jfi.org/film-festival/festival-archive/sfjff-2026) | `partial_sf_program` | The official SFJFF46 page (July 16–August 2, 2026) covers a festival whose venue program spans beyond a confirmed city-only listing; no separated San Francisco-only program page was retained. Excluded until a city-only program-level record can be made. |
| `sf-fringe-2026` | San Francisco Fringe Festival — 2026 schedule | — | [Legacy SF Fringe URL (redirects off-site; not a verified official source)](https://www.sffringe.org/) | `needs_review` | At the 2026-10-18 re-check, sffringe.org redirected to an unrelated domain returning 404, so the legacy URL is retained only to document the dead end. No current organizer page with a verified date and San Francisco venue was found; nothing is inferred. |
| `opera-in-the-park-2026` | Opera in the Park — 2026 | September 13, 2026 (cancelled) | [San Francisco Opera cancellation release](https://www.sfopera.com/press/press-releases/Season-Opening-Performances-Cancelled-Strike/) | `cancelled` | San Francisco Opera’s official release says the September 13, 2026 Opera in the Park concert was cancelled. It must not appear as an active event. |
| `bay-area-aloha-festival` | Bay Area Aloha Festival | — | [Bay Area Aloha Festival official site (unreachable at 2026-10-18 re-check)](https://www.bayareaalohafestival.com/) | `outside_city_excluded` | Official materials place this festival outside San Francisco city limits, so it is intentionally excluded from the city-only catalog. (The separate San Francisco Aloha Run is also flagged in this register because its organizer site was unreachable at the 2026-10-18 re-check; the festival site itself could not be fetched then either.) |
| `frameline-2026` | Frameline50 — San Francisco International LGBTQ+ Film Festival (mixed-geography program) | June 17–27, 2026 | [Frameline50 dates announcement (official press release)](https://www.frameline.org/news/frameline50-dates-announced-press-release) | `partial_sf_program` | Frameline's own announcement places Frameline50 (June 17–27, 2026) in venues in San Francisco and Oakland, and its Attend page adds Berkeley. The umbrella festival is therefore not city-only and is excluded until a San Francisco-only program record can be separated, like SFFILM and SFJFF. |
| `noise-pop-festival-2026` | Noise Pop Festival — venue geography unresolved | February 19–March 1, 2026 | [Noise Pop official event calendar](https://www.noisepop.com/event-calendar) | `needs_review` | The organizer's 2026 event page markets the festival as 'San Francisco,' but the fetched official calendar does not enumerate venue cities, and contemporaneous reporting lists East Bay venues among its 25+ venues. The city-only scope is unresolved, so no catalog row is published. |

## Material irregularities resolved during audit

| Item | Resolution |
|---|---|
| Cloudflare Connect 2026 | Canonical organizer event page gives October 19–21. A different page's October 22 reference was not normalized into the event date. Re-verification added the $595 registration stated on the page. |
| SFFILM / SF Jewish Film Festival / Frameline50 | All three official programs span venues outside SF (Oakland/Berkeley/East Bay) as well as San Francisco. They are kept off city-only tables rather than represented as wholly SF events. Frameline50 was added to the register in the re-verification on the same basis. |
| Opera in the Park 2026 | The organizer's cancellation release overrides earlier promotional listing (SF Travel had listed Robin Williams Meadow, September 13). The event stays in the register only, with the venue field blank because the cancellation release names none. |
| San Francisco Marathon | The organizer's full-marathon course crosses into Marin County. The umbrella row was demoted; the SF-only Expo (Fort Mason, July 24–25, 2026) is published as a dated special event. |
| Bay Area Aloha Festival | Excluded after official location evidence placed it outside SF city limits. |
| Juneteenth city programs | SF.gov's 2026 page distinguishes the June 7 waterfront program, June 13 Fillmore Freedom Celebration, June 20 Market Street Parade, and the June 5 City Hall kickoff (added as a dated special). A Bayview Juneteenth candidate remains unresolved: its official homepage states no textual 2026 date or location. |
| CAAMFest umbrella scope | The published record is limited and titled as the San Francisco program, using named SF venues in the official 2026 schedule; it does not claim the umbrella festival is city-exclusive. |
| Fillmore Jazz Festival | The previously linked fillmorejazzfestival.com is unreachable; organizer content lives at fillmorejazzfest.com, which lists the next edition July 3–4, 2027, free. The row now documents the 2027 edition. |
| Flower Piano | Published 10am–6pm hours were not on the captured official page and were blanked; admission corrected to the page's Free–$18. |
| AGU26 | The captured AGU page does not name a venue; the previously listed Moscone Center was removed rather than inferred. |
| Microsoft Ignite | The organizer homepage renders only a script shell; the row now cites the official venue (Moscone Center) event page, which states November 17–20, 2026 at Moscone Center. Prices seen only in search snippets were not published. |
| North Beach Festival | The festival homepage states no 2026 dates in text; the row now cites the producer's (Sunset Mercantile) 2026 event page. |
| SF International Arts Festival | Start corrected to April 29, 2026 per the organizer's 2026 festival page; location set to Mission District venues per the organizer homepage (the office address is never used as a venue). |
| SF Dance Film Festival | The city-only in-person component ends November 8, 2026; the ISO end date no longer absorbs the online window. |
| Stern Grove Festival | Saturday, August 15 added to the Sunday series; unstated concert times blanked. |
| SF Fringe | sffringe.org redirects to an unrelated 404 domain; the register now labels it an unverified legacy URL instead of an official source. |

## Records demoted at re-verification (could not be reconfirmed live)

Comedy Day (official site: free, noon–5pm, Robin Williams Meadow — no date), Haight-Ashbury Street Fair (no date anywhere on the captured official site), International Ocean Film Festival (/festival page not found; homepage states no textual dates/venue), San Francisco Aloha Run (organizer site unreachable), plus the San Francisco Marathon umbrella (scope, above). Captured prior values remain visible on Flagged for Review with the reason; none were silently kept or deleted.

## Records added at re-verification

Weekly/monthly: Heart of the City Farmers Market and Fort Mason Center Farmers Market (organizer pages), Exploratorium After Dark and Cal Academy NightLife (organizer pages), Downtown First Thursdays and Valencia LIVE! (organizer pages; new `monthly` cadence). Annual/seasonal: AIDS Walk San Francisco (organizer FAQ; 40th anniversary), SF Sketchfest 2027 (organizer site), YBG Festival and Jerry Day (SF Travel official release; festival homepage was reCAPTCHA-blocked), Outside Lands and Portola (SFMTA government travel updates; organizer site errored), Escape from Alcatraz Triathlon (SFMTA; course entirely in SF), Day of the Dead Procession and Illuminate SF (SF Travel). Dated specials: SF Marathon Expo, Juneteenth Mayor's Kickoff (SF.gov), Fourth of July Fireworks on Golden Gate Bridge (SF.gov; one-off America 250 display).

## Dead or unusable sources encountered (do not cite as evidence)

fillmorejazzfestival.com (unreachable), intloceanfilmfest.org/festival (not found), sfaloharun.com and bayareaalohafestival.com (unreachable), sffringe.org (redirects off-site to 404), ignite.microsoft.com homepage (script shell only — venue page used), ybgfestival.org (reCAPTCHA wall — SF Travel release used), sfoutsidelands.com and illuminatesf.com (HTTP 500 — SFMTA/SF Travel used).

## Known coverage boundaries (not silently omitted)

- Calendar-style programming is linked as directories on the Method page (SF Public Library events, SF City Guides tours, SF Recreation and Park calendar) rather than forced into event rows without a stated cadence.
- Candidates seen only in roundup/secondary coverage (e.g., Bhangra & Beats Night Market, SF Hip-Hop Dance Festival, Renegade Craft Fair SF) await direct organizer/government verification.
- Look-alikes outside the City and County are excluded: Great Dickens Christmas Fair (Cow Palace, Daly City), SFO terminal programs (San Mateo County).
- Noise Pop Festival is registered unresolved: the organizer markets it as San Francisco but does not enumerate venue cities, while reporting lists East Bay venues.

## Verifier hardening

`verify.py` still cannot prove external truth (no live crawl), but after mutation testing it now also rejects: example/local source hosts, published locations with no San Francisco indicator, unknown status/cadence/authority enums (cadence tied to bucket), malformed or inverted ISO dates, date-text years that disagree with ISO dates, duplicate name+start-date under a new id, and placeholder time/admission text. All five original mutation cases (example.com source, Oakland venue, fabricated cadence/date, duplicate under new id, end before start) now fail verification.

## Data handoff

- **Machine-readable dataset:** [`data/events.json`](../data/events.json); CSV export at [`data/events.csv`](../data/events.csv).
- **Public-site behavior:** only `bucket: recurring` / `special` with `status: verified` can enter the main tables; all other statuses route to the review page.
- **Minimum recheck before adding a row:** official source URL, SF city location, date/cadence, and an explicit review reason for any missing required field. Update the stable counts in `verify.py` only together with an entry in this audit.
