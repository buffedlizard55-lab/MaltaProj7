# Official-source audit — San Francisco city events

**Audit date:** 2026-10-18 (original audit, same-day final-integration re-verification of every row, and reconciliation with peer PR #9)

**Geographic rule:** City and County of San Francisco only
**Catalog snapshot:** 69 published, source-linked records: 58 regularly occurring and 11 dated/special. 16 non-published records remain on the review register.

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
| `muni-heritage-weekend-2026` | Muni Heritage Weekend | September 19–20, 2026 | 77 Steuart Street (San Francisco Railway Museum area), Embarcadero, San Francisco | [SFMTA event page](https://www.sfmta.com/calendar/muni-heritage-weekend-2026) | Government source | verified |
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
| `calacademy-nightlife` | NightLife at the California Academy of Sciences | Most Thursdays | California Academy of Sciences, 55 Music Concourse Drive, Golden Gate Park, San Francisco | [California Academy of Sciences — NightLife page](https://www.calacademy.org/nightlife) | Official organizer | verified |
| `downtown-first-thursdays` | Downtown First Thursdays | First Thursday monthly; next listed November 5, 2026 | Second Street between Market and Howard Streets, San Francisco, CA 94105 | [Downtown First Thursdays official site](https://www.dftsf.com/) | Official organizer | verified |
| `valencia-live` | Valencia LIVE! | Second Thursday monthly, May–October 2026 (May 14; June 11; July 9; August 13; September 10; October 8) | Valencia Street between 16th and 21st Streets, San Francisco (blocks shift by month) | [Valencia LIVE! — VCMA official page](https://www.visitvalenciastreet.com/live) | Official organizer | verified |
| `aids-walk-san-francisco-2026` | AIDS Walk San Francisco | Sunday, July 19, 2026 | Robin Williams Meadow, Golden Gate Park, San Francisco | [AIDS Walk San Francisco — FAQ](https://sf.aidswalk.net/FAQ) | Official organizer | verified |
| `sf-sketchfest-2027` | SF Sketchfest | January 14–31, 2027 | San Francisco | [SF Sketchfest official site](https://sfsketchfest.com/) | Official organizer | verified |
| `ybg-festival-2026` | YBG Festival (Yerba Buena Gardens Festival) | May 9–November 13, 2026 | Yerba Buena Gardens, San Francisco | [SF Travel press release — 2026 live music lineup (June 11, 2026)](https://www.sftravel.com/media/press-release/san-francisco-amplifies-its-2026-live-music-scene-expanded-lineup-festivals) | Trusted civic source | verified |
| `outside-lands-2026` | Outside Lands Music & Arts Festival | August 7–9, 2026 | Golden Gate Park, San Francisco | [SFMTA travel update — Outside Lands, August 7–9, 2026](https://www.sfmta.com/travel-updates/outside-lands-august-7-9-2026) | Government source | verified |
| `portola-music-festival-2026` | Portola Music Festival | September 26–27, 2026 | Pier 80, San Francisco | [SFMTA travel update — Portola Music Festival, September 26 & 27, 2026](https://www.sfmta.com/travel-updates/portola-music-festival-september-26-27-2026) | Government source | verified |
| `jerry-day-2026` | Jerry Day | August 1, 2026 | Jerry Garcia Amphitheater, McLaren Park, San Francisco | [Jerry Day official site](https://www.jerryday.org/) | Official organizer | verified |
| `escape-from-alcatraz-triathlon-2026` | Escape from Alcatraz Triathlon | Sunday, June 7, 2026 | Alcatraz Island to St. Francis Yacht Club; Presidio, Golden Gate Park, and Baker Beach; finish at Marina Green, San Francisco | [SFMTA — Escape from Alcatraz Triathlon, June 7, 2026](https://www.sfmta.com/project-updates/escape-alcatraz-triathlon) | Government source | verified |
| `day-of-the-dead-procession-2026` | Day of the Dead (Día de los Muertos) Procession | November 2, 2026 | Mission District, San Francisco | [SF Travel — San Francisco festivals and events in November](https://www.sftravel.com/article/san-francisco-festivals-events-november) | Trusted civic source | verified |
| `illuminate-sf-2026` | Illuminate SF Festival of Light | Begins November 27, 2026 | Citywide, San Francisco | [SF Travel — San Francisco festivals and events in November](https://www.sftravel.com/article/san-francisco-festivals-events-november) | Trusted civic source | verified |
| `sf-marathon-expo-2026` | San Francisco Marathon Expo | July 24–25, 2026 | Fort Mason Festival Pavilion, 2 Marina Boulevard, San Francisco | [San Francisco Marathon race-weekend page](https://www.thesfmarathon.com/race-weekend/) | Official organizer | verified |
| `juneteenth-mayor-kickoff-2026` | Juneteenth Mayor's Kickoff Celebration | June 5, 2026 | City Hall, San Francisco | [SF.gov 2026 Juneteenth page](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) | Government source | verified |
| `fourth-of-july-fireworks-golden-gate-2026` | Fourth of July Fireworks on Golden Gate Bridge | Saturday, July 4, 2026 | Golden Gate Bridge, San Francisco, CA 94129 | [SF.gov event page — Fourth of July fireworks on Golden Gate Bridge](https://www.sf.gov/event-20260704-fourth-of-july-fireworks-on-golden-gate-bridge) | Government source | verified |
| `people-in-plazas` | People in Plazas — Market Street Music Festival | Summer season | 15 venues on or near Market Street, from the Embarcadero to Fourth Street, San Francisco | [People in Plazas official site](https://peopleinplazas.org/) | Official organizer | verified |
| `merola-summer-festival` | Merola Opera Program Summer Festival | Summer 2026 | San Francisco | [Merola Opera Program — Summer Festival 2026 page](https://merola.org/summerfestival/) | Official organizer | verified |

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
| `golden-gate-bandshell-concerts` | Golden Gate Park Bandshell Concerts | April–November | [SF Recreation and Parks Bandshell page](https://sfrecpark.org/1570/Golden-Gate-Bandshell-Concerts) | `needs_review` | Contributed by peer session arena/08676041 (PR #9) citing the SF Recreation and Parks Bandshell page. At final-integration re-check on 2026-10-18 that page returned only a script/navigation shell with no program text, so the April–November season, named weekly series, and free admission could not be reconfirmed from the linked source. Held until a readable official page states them. |
| `sfjazz-summer-sessions` | SFJAZZ Summer Sessions | June–August | [SFJAZZ official site](https://www.sfjazz.org/) | `needs_review` | Contributed by peer session arena/08676041 (PR #9) citing the SFJAZZ homepage. At re-check the homepage presents the 2026–27 season and retains no 'Summer Sessions' program, June–August span, or listed artists, so the record is held until an organizer page states the summer program. |
| `third-thursdays-on-ellis` | Third Thursdays On Ellis | Third Thursday of each month | [Third Thursdays On Ellis official site](https://www.onellis.com/) | `needs_review` | Contributed by peer session arena/08676041 (PR #9) citing onellis.com. At re-check the homepage is image-only with no textual cadence, location detail, or admission terms, so the monthly free series cannot be confirmed from the linked source. |
| `sf-opera-summer-season` | San Francisco Opera Summer Season | May 28–June 27, 2026 | [San Francisco Opera official site](https://www.sfopera.com/) | `needs_review` | Contributed by peer session arena/08676041 (PR #9) citing the SF Opera homepage. At re-check the homepage presents the 2026–27 season; the May 28–June 27, 2026 summer span and its productions are not retained on the linked page, so the record is held rather than published from secondary listings. |

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
| Fillmore Jazz Festival | The previously linked fillmorejazzfestival.com is dead/hijacked (peer session observed a redirect to an unrelated commercial site); organizer content lives at fillmorejazzfest.com. The catalog documents the next edition, July 3–4, 2027, free; the peer session independently confirmed a July 4–5, 2026 edition from the same site's 2026 pages. |
| Flower Piano | Published 10am–6pm hours were not on the captured official page and were blanked; admission corrected to the page's Free–$18. |
| AGU26 | The captured AGU page does not name a venue; the previously listed Moscone Center was removed rather than inferred. |
| Microsoft Ignite | The organizer homepage renders only a script shell; the row now cites the official venue (Moscone Center) event page, which states November 17–20, 2026 at Moscone Center. Prices seen only in search snippets were not published. |
| Illuminate SF | illuminatesf.com returned HTTP 500 and illuminatesf.org redirects to an unrelated crowdfunding campaign; neither is usable evidence. The row cites SF Travel's November guide (begins November 27, 2026, citywide). |
| North Beach Festival | The festival homepage states no 2026 dates in text; the row now cites the producer's (Sunset Mercantile) 2026 event page. |
| SF International Arts Festival | Start corrected to April 29, 2026 per the organizer's 2026 festival page (both sessions independently); location set to Mission District venues per the organizer homepage (the office address is never used as a venue). |
| SF Dance Film Festival | The city-only in-person component ends November 8, 2026; the ISO end date no longer absorbs the online window. |
| Stern Grove Festival | Saturday, August 15 added to the Sunday series; unstated concert times blanked. |
| Fleet Week | Published at component level (ship tours Oct 7–12, Fleet Fest Oct 10–11, ticketed air show Oct 9–11) from the organizer calendar; peer session additionally noted umbrella headings of Oct 6–12 and an SF Travel guide range of Oct 4–12, which is why no single umbrella range or admission is asserted. |
| SF Fringe | sffringe.org redirects to an unrelated 404 domain; the register now labels it an unverified legacy URL instead of an official source. |

## Records demoted at re-verification (could not be reconfirmed live)

Comedy Day (official site: free, noon–5pm, Robin Williams Meadow — no date), Haight-Ashbury Street Fair (no date anywhere on the captured official site), International Ocean Film Festival (/festival page not found; homepage states no textual dates/venue), San Francisco Aloha Run (organizer site unreachable), plus the San Francisco Marathon umbrella (scope, above). Four peer-contributed records were also held at reconciliation (Golden Gate Park Bandshell Concerts, SFJAZZ Summer Sessions, Third Thursdays On Ellis, SF Opera Summer Season) because their linked homepages did not retain the stated programs in readable text. Captured prior values remain visible on Flagged for Review with reasons; none were silently kept or deleted.

## Records added at re-verification and reconciliation

Weekly/monthly: Heart of the City Farmers Market and Fort Mason Center Farmers Market (organizer pages), Exploratorium After Dark and Cal Academy NightLife (organizer pages), Downtown First Thursdays and Valencia LIVE! (organizer pages; new `monthly` cadence). Annual/seasonal: AIDS Walk San Francisco (organizer FAQ; 40th anniversary), SF Sketchfest 2027 (organizer site), YBG Festival (SF Travel official release; festival homepage was reCAPTCHA-blocked), Jerry Day (organizer site jerryday.org), Outside Lands and Portola (SFMTA government travel updates; organizer site errored), Escape from Alcatraz Triathlon (SFMTA; course entirely in SF), Day of the Dead Procession and Illuminate SF (SF Travel), People in Plazas and Merola Summer Festival (peer contributions re-verified against organizer pages and trimmed to what those pages state). Dated specials: SF Marathon Expo, Juneteenth Mayor's Kickoff (SF.gov), Fourth of July Fireworks on Golden Gate Bridge (SF.gov; one-off America 250 display).

## Peer reconciliation (PR #9, arena/08676041)

The peer session merged in parallel (its work commit landed four minutes after the final-integration claim). Overlaps were deduplicated event-by-event: NightLife, Portola, YBG Festival, Fort Mason market, and Fillmore Jazz resolve to single rows (the final-integration captures, which link the page actually used as evidence — e.g., SFMTA for Portola, the SF Travel release for YBG). Peer-verified improvements adopted: NightLife street address (55 Music Concourse Drive), Muni Heritage location detail and "Free rides and activities," and the jerryday.org organizer source (with 11:30am–5:45pm and Jerry Garcia Amphitheater). Peer rows that restated placeholder text or kept events published without addressing missing-date evidence were superseded by the stricter re-verified values; the peer's own irregularity notes remain in COORDINATION.md.

## Dead or unusable sources encountered (do not cite as evidence)

fillmorejazzfestival.com (dead/hijacked), intloceanfilmfest.org/festival (not found), sfaloharun.com and bayareaalohafestival.com (unreachable), sffringe.org (redirects off-site to 404), ignite.microsoft.com homepage (script shell only — venue page used), ybgfestival.org (reCAPTCHA wall — SF Travel release used), sfoutsidelands.com and illuminatesf.com (HTTP 500), illuminatesf.org (redirects to crowdfunding), sfrecpark.org Bandshell page and onellis.com (no readable program text in capture).

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

## Final integration re-verification — 2026-10-18 (arena/d71d78cc-maltaproj7)

Every source URL in `data/events.json` was re-fetched from the official publisher page on 2026-10-18 (organizer, official venue, or government source). The pending independent-audit findings were applied, corrections were made only where an official source states the value, and residual problems were published as field-level flags on the Flagged for Review page. Nothing was inferred: values that the linked source does not state are left blank.

**Outcome totals of this session before cross-session reconciliation:** 77 records = 72 published city-only rows (55 recurring / 17 special) + 5 review-register rows; 13 field-level flags; 8 categories. After reconciliation with the parallel `arena/08676041`/`arena/1bde1cd1` integration (PRs #9–#12), the final dataset is 103 records = 90 published city-only rows (71 recurring / 19 special) + 13 review-register rows; 13 field-level flags. See the reconciliation appendix below.

### Corrections applied to published rows

| Row | Correction | Source(s) used |
|---|---|---|
| `fillmore-jazz-festival-2026` | Official source replaced with fillmorejazzfest.com (old domain fillmorejazzfestival.com is no longer organizer-controlled); dates stated as July 4–5, 2026 per SF Travel July guide + organizer July-Fourth-weekend press. | [fillmorejazzfest.com](https://www.fillmorejazzfest.com/) · [SF Travel July 2026](https://www.sftravel.com/article/san-francisco-festivals-events-july) |
| `comedy-day-2026` | Date corrected Sep 13 → Sunday, September 20, 2026; time 12:00–5:00pm; admission Free. Sep 13 was the Opera in the Park date at the same meadow. | [comedyday.org](https://comedyday.org/) · [SF Rec & Parks Tentative Calendars](https://sfrecpark.org/1310/Tentative-Calendars-of-Special-Events) · [SF Travel Sep 2026](https://www.sftravel.com/article/san-francisco-festivals-events-september) |
| `fleet-week-sf-2026` | Source switched to fleetweeksf.org (calendar page has no posted events); date_text lists umbrella Oct 4–12 (SF Travel) with organizer components: ship tours Oct 7–12, air show Oct 9–11 noon–4pm, Fleet Fest Oct 10–11. | [fleetweeksf.org](https://fleetweeksf.org/) · [air show page](https://fleetweeksf.org/air-show/) · [SF Travel Fleet Week guide](https://www.sftravel.com/article/where-you-need-to-watch-blue-angels-fly-over-san-francisco-during-fleet-week) |
| `sf-international-arts-festival-2026` | Dates corrected Apr 30–May 10 → April 29–May 10, 2026 per official 2026 archive heading. | [SFIAF 2026 archive](https://www.sfiaf.org/2026_festival) |
| `international-ocean-film-festival-2026` | Source replaced (organizer /festival and /awards now 404) with Fort Mason venue listing; venues Cowell Theater Pier 2 + BATS Bayfront; admission $20–$450; Saturday hours copied verbatim and flagged. | [Fort Mason event listing](https://fortmason.org/event/international-ocean-film-festival-2026/2026-04-12/) |
| `world-arts-west-dance-festival-2026` | Source replaced (event URL now 404) with Presidio Trust press release; filled Sun Sep 6, 2026, 1–4pm, East Meadow at Presidio Tunnel Tops, Free; third/final weekend of three-weekend festival. | [Presidio Trust press release](https://presidio.gov/about/press/world-arts-west-enlivens-presidio-tunnel-tops-sept-6/) |
| `muni-heritage-weekend-2026` | Filled 10:00am–4:00pm, SF Railway Museum 77 Steuart St, free rides/entry. | [SFMTA event page](https://www.sfmta.com/calendar/muni-heritage-weekend-2026) |
| `italian-heritage-parade-2026` | Edition-specific organizer retrospective used; Oct 11, 2026 (158th annual) confirmed; route not restated on source. | [Organizer retrospective](https://sfitalianheritage.org/san-francisco-italian-heritage-parade-celebrates-158-years-with-grand-marshal-joe-mantegna/) |
| `juneteenth-sf-freedom-celebration-2026` | Filled Jun 13, 2026, eight-block Fillmore St; authority relabeled Government source (SF.gov); no-cost. | [SF.gov Juneteenth 2026](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) |
| `juneteenth-market-street-parade-2026` | Filled Jun 20, 2026 (fourth annual), 11:00am start at Market & Second → Embarcadero Plaza; no-cost. | [SF.gov Juneteenth 2026](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) |
| `juneteenth-on-the-waterfront-2026` | Source switched to Foodwise organizer page; Jun 7, 2026 (sixth annual), 11am–4pm, Ferry Building front plaza, free entry. | [Foodwise event page](https://foodwise.org/events/pop-ups-on-the-plaza-juneteenth-on-the-waterfront/) |
| `sundown-cinema-inside-out-2026` | Filled 7:00pm, Civil War Parade Ground (Graham St), Free. | [Presidio Trust press release](https://presidio.gov/about/press/presidio-unveils-vibrant-2026-summer-event-lineup) |
| `scaregrove-2026` | Filled Fri Oct 30, 2026, 3–9pm, Sigmund Stern Grove (19th & Sloat), Free; Mobile Rec 12–8pm listing documented as a separate program. | [SF Rec & Parks calendar](https://sfrecpark.org/Calendar.aspx) |
| `foodwise-black-holiday-market-2026` | Filled Dec 12, 2026, 9am–2pm, south arcade Ferry Building, free entry. | [Foodwise event page](https://foodwise.org/events/pop-ups-on-the-plaza-black-holiday-market/) |
| `cloudflare-connect-2026` | Filled Oct 19–21, 2026, Moscone West, $595 conference pass ($495 group/University). | [cloudflare.com/connect](https://www.cloudflare.com/connect/) |
| `informs-annual-meeting-2026` | Filled Nov 1–4, 2026, Moscone Center South & Marriott Marquis. | [INFORMS 2026 page](https://meetings.informs.org/wordpress/annual/) |
| `microsoft-ignite-2026` | Filled Nov 17–20, 2026, Moscone Center 747 Howard St; admission left blank (not on linked page). | [ignite.microsoft.com](https://ignite.microsoft.com/) · [Moscone Center listing](https://www.moscone.com/events/microsoft-ignite-2026) |
| `agu-annual-meeting-2026` | Filled Dec 7–11, 2026; location limited to 'San Francisco, CA' (venue not named on source). | [AGU26 page](https://www.agu.org/annual-meeting) |
| `sf-marathon-2026` | Dates July 24–26, 2026 (page body; 2027 header is next-year marketing); location scoped to SF components; bridge-crossing geography flagged. | [race-weekend](https://www.thesfmarathon.com/race-weekend/) · [full-marathon course](https://www.thesfmarathon.com/full-marathon/) |
| `carnaval-sf-2026` | Location replaced with source-stated description (17 blocks Mission District; parade 24th & Bryant → Mission → 15th); filled festival 11am–6pm, parade 10am–2pm; 'Harrison Street' detail dropped and flagged. | [Carnaval SF special events](https://carnavalsanfrancisco.org/special-events/) |
| `hardly-strictly-bluegrass-2026` | Filled Oct 2–4, 2026; gates 11am Fri / 9am Sat–Sun, music ends 7pm; free; RecPark Oct 2–5 window flagged. | [HSB 2026 FAQ](https://hardlystrictlybluegrass.com/info-faq-2026/) |
| `up-your-alley-2026` | Filled Sun Jul 26, 2026, 11am–6pm, precise Folsom/9th/10th/Dore footprint, donation at gate. | [Folsom Street FAQ](https://www.folsomstreet.org/faq) |
| `folsom-street-fair-2026` | Filled Sun Sep 27, 2026, 11am–6pm, Folsom 7th–13th footprint, donation at gate. | [Folsom Street Fair page](https://www.folsomstreet.org/folsom-street-fair) |
| `castro-street-fair-2026` | Filled Sun Oct 4, 2026 (52nd annual), 11am–6pm, Castro & Market, suggested donation $10–20. | [Castro Street Fair page](https://castrostreetfair.org/fair/) |
| `nihonmachi-street-fair-2026` | Filled Aug 1–2, 2026 (52nd annual), Japantown; unverified street span dropped and flagged. | [Nihonmachi Street Fair](https://www.nihonmachistreetfair.org/home-1) |
| `pistahan-2026` | Filled Aug 8–9, 2026 (33rd annual); parade Sat 11am–12noon from Civic Center Plaza along Market (8th–4th) to 4th & Mission at Yerba Buena Gardens; festival free. | [pistahan.net](https://www.pistahan.net/) · [parade page](https://www.pistahan.net/parade) |
| `north-beach-festival-2026` | Filled Jun 20–21, 2026 (70th annual), Filbert–Broadway / Stockton–Grant footprint. | [North Beach Festival](https://www.northbeachfestival.org/) |
| `haight-ashbury-street-fair-2026` | Filled Sun Sep 20, 2026, 11am–5:30pm, Haight St between Masonic and Stanyan, free. | [SFMTA travel update](https://www.sfmta.com/travel-updates/haight-ashbury-street-fair-sunday-september-20-2026) · [organizer vending page](https://www.haightashburystreetfair.org/vending) |
| `sf-aloha-run-2026` | No field changes; re-verification failure recorded in notes and flags (organizer site unreachable). | [sfaloharun.com](https://sfaloharun.com/) (unreachable) |
| `sf-porchfest-2026` | Filled Free; notes: 8th annual, 100 acts in the Mission; set times left blank; kick-off May 29 at Hotel Utah. | [app.sfporchfest.org](https://app.sfporchfest.org/) |
| `sf-dance-film-festival-2026` | Filled SF venue list (Lucasfilm Premier, Delancey Street, Catharine Clark, SHACK15, Brava) and ticketing note. | [SFDFF Fall Festival 2026](https://sfdancefilmfest.org/fall-festival-2026/) |
| `sf-transgender-film-festival-2026` | Filled Nov 12–14, 2026 in-person 7–10pm; online hybrid through Nov 22. | [SF/Arts listing](https://sfarts.org/event/29th-anniversary-san-francisco-transgender-film-festival-2O89YYfq6cS0gq7oZDYObg/) |
| `chinese-new-year-parade-2027` | Filled 5:15pm start; free along route / bleacher tickets sold. | [Chinese New Year Parade FAQ](https://chineseparade.com/faq/) |
| `st-patricks-parade-2026` | Filled Mar 14, 2026 (175th annual), 11:30am start, 2nd & Market → Civic Center. | [UISF parade page](https://uissf.org/st-patricks-day-parade) |
| `flower-piano-2026` | Admission filled Free–$18 (Zoox Lounge ticketed); 11th year / 12 pianos noted. | [GGGP event page](https://gggp.org/event/flower-piano-2026/) |
| `sfjff-2026` | Source URL updated to the working JFI 2026 archive; July 16 – August 2, 2026 (SFJFF 46) confirmed; review-only retained (mixed geography). | [JFI SFJFF 2026 archive](https://jfi.org/film-festival/festival-archive/sfjff-2026) |
| `sf-fringe-2026` | Source authority corrected to 'Legacy source — NOT verified official'; legacy domain now serves unrelated 404 content; review-only retained. | [sffringe.org](https://www.sffringe.org/) (now unrelated content) |
| `bay-area-aloha-festival` | Outside-city exclusion retained; source unreachable at re-verification recorded. | [bayareaalohafestival.com](https://www.bayareaalohafestival.com/) (unreachable) |

Rows re-verified as already correct (no field changes): all PCFMA market rows (Castro, Divisadero, Fillmore, Hayes Valley, Inner Sunset), Alemany Farmers Market, Ferry Plaza Farmers Market, Mission Community Market, Sunday Streets SF, Stern Grove Festival, Free Shakespeare in the Park (SF run Sep 5–27 at McLaren + Sue Bierman), Cherry Blossom Festival 2027, SF Pride 2027, Bay to Breakers 2027 (May 16, 2027 hero date; stray May 18 copy flagged), CAAMFest 2026 SF program (May 7–10; five SF venues), SF Silent Film Festival 2026 (May 6–10, Castro Theatre), SF Black Film Festival 2026 (Jun 18–21), 3rd i South Asian Film Festival 2026 (Oct 9–11), Lit Crawl SF 2026 (Oct 24), Opera in the Park cancellation, and SFFILM 2026 review row (Apr 24 – May 4).

### Rows added during final integration (each verified from an official source)

| New row | Date(s) | Source |
|---|---|---|
| `mayors-juneteenth-kickoff-2026` | Jun 5, 2026, City Hall | SF.gov |
| `juneteenth-bayview-fathers-day-festival-2026` | Jun 21, 2026, Gilman Park | SF.gov |
| `memorial-day-commemoration-presidio-2026` | May 25, 2026 (159th annual) | Presidio Trust press release |
| `parks4all-brewfest-2026` | May 30, 2026 (4th annual) | Presidio Trust press release |
| `bay-area-international-deaf-dance-festival-2026` | Aug 16, 2026 (14th annual) | Presidio Trust press release |
| `community-arts-market-presidio-2026` | Jul 18–19, 2026 (2nd annual) | Presidio Trust press release |
| `fiesta-en-el-parque-2026` | Aug 1, 2026 | Presidio Trust press release |
| `i-am-an-american-exhibition-2026` | Fridays–Tuesdays through Aug 31, 2026 | Presidio Trust press release |
| `exclusion-presidio-exhibition-2026` | Fridays–Sundays through Aug 31, 2026 | Presidio Trust press release |
| `spring-awakening-art-cumbia-2026` | May 16, 2026 | Presidio Trust press release |
| `intertribal-dance-gathering-2026` | May 30, 2026 | Presidio Trust press release |
| `presidio-soccer-festival-2026` | Jun 13, 2026 | Presidio Trust press release |
| `carnaval-fat-tuesday-2026` | Feb 17, 2026 | Carnaval SF |
| `carnaval-king-queen-competition-2026` | Mar 28, 2026 | Carnaval SF |
| `carnaval-cubacaribe-2026` | Apr 15, 2026 (20th annual) | Carnaval SF |
| `carnaval-pride-night-2026` | Apr 24, 2026 | Carnaval SF |
| `carnaval-nightlife-calacademy-2026` | May 7, 2026 | Carnaval SF |
| `carnaval-business-mixer-2026` | Oct 14, 2026 | Carnaval SF |

### Field-level flags published for manual review

13 flags are rendered on `flagged.html` with source links: Comedy Day date evidence (image-only on organizer site), Fillmore Jazz domain swap, Fleet Week umbrella-date discrepancy, SF Marathon bridge-course geography + 2027 header confusion, Hardly Strictly Oct 2–4 vs RecPark Oct 2–5, IOFF dead organizer URLs + posted Saturday hours typo, SF Aloha Run source unreachable at re-verification, Bay Area Aloha source unreachable at re-verification, Scaregrove dual listings (main vs Mobile Rec), Carnaval unverified Harrison Street detail removed, Nihonmachi street span not restated on source, Bay to Breakers stray May 18 copy, SF Fringe domain serving unrelated content.

### Re-verification method

- Fetch tool re-retrieved each `source_url` on 2026-10-18 and confirmed the row's core claims (name, date/cadence, location) in the returned text.
- A value is published only when the linked source states it; optional fields stay blank otherwise (em dash policy).
- Where two official sources disagree, both are cited and the disagreement is flagged; the organizer's own dates win for event dates unless unavailable.
- The reproducible patch applied during this session is preserved at `research/integration-patch-2026-10-18.py`.


## Cross-session reconciliation appendix — 2026-10-18 (arena/d71d78cc-maltaproj7)

Two parallel integration sessions (`arena/08676041-maltaproj7`, `arena/1bde1cd1-maltaproj7`, PRs #9–#12) and this session (`arena/d71d78cc-maltaproj7`) independently re-verified the catalog on 2026-10-18 and published overlapping corrections. The final dataset is a strict union of both datasets with the following row-level dispositions:

| Contested row(s) | Disposition | Rationale |
|---|---|---|
| `comedy-day-2026` | **Published** (Sunday, September 20, 2026) with field flag | The date is stated by official sources: SF Recreation and Parks' Tentative Calendars of Special Events (government) and the SF Travel September guide; the organizer page confirms the edition, venue, hours, and free admission but states the date only in a banner image. The parallel session demoted the row because the organizer text lacks a date; the government-source evidence resolves that gap and the flag preserves the residual image-only caveat. |
| `haight-ashbury-street-fair-2026` | **Published** (Sunday, September 20, 2026) with source switched to the organizer's vending page | The organizer's own vending page states 'Event Date: Sunday, September 20, 2026' and the SFMTA travel-update page (government) states the date, hours, and Haight Street (Masonic–Stanyan) span. The parallel demotion (organizer homepage text lacks a date) is resolved by the organizer subpage. |
| `sf-marathon-2026` | **Review register** (parallel session's treatment), with `sf-marathon-expo-2026` published separately | Strict city-only consistency: the full-marathon and first-half courses cross the Golden Gate Bridge into the Marin headlands side, matching the mixed-geography treatment used for multi-city film festivals. Course detail, 2026 date evidence, and the organizer's 2027 marketing header are recorded in the review row and flags. |
| `sf-aloha-run-2026` | **Review register** (parallel session's treatment) | The organizer site is unreachable at re-verification, so no value can be confirmed from a live official source and the row must not be published as verified. Captured values are retained on the review page with the unreachability flag. |
| `international-ocean-film-festival-2026` | **Published** (this session's treatment) | The parallel session demoted the row because the organizer's festival page is dead; this session substituted the official Fort Mason venue listing (which states the April 10–12 dates, Cowell Theater/Bayfront Theatre venues, and $20–$450 range) per the independent audit's 'replace the source' instruction. The venue listing's posted Saturday hours typo remains flagged. |
| `fillmore-jazz-festival-2026` + `fillmore-jazz-festival-2027` | **Both published** (separate edition rows) | 2026 edition documented with the canonical organizer domain; 2027 edition (July 3–4, 2027) from the organizer site as the next edition. |
| `juneteenth-mayor-kickoff-2026` (parallel) vs `mayors-juneteenth-kickoff-2026` (this session) | **Duplicate collapsed** into `mayors-juneteenth-kickoff-2026` | Same June 5, 2026 City Hall kickoff; the retained row carries the source-stated 5–8 p.m. hours and registration note. |
| `calacademy-nightlife` (recurring series) + `carnaval-nightlife-calacademy-2026` (dated co-presentation) | **Both published** | Different records: the weekly NightLife series and the specific Carnaval-branded May 7, 2026 evening. |
| All other parallel-only rows (Heart of the City and Fort Mason farmers markets, Exploratorium After Dark, Downtown First Thursdays, Valencia LIVE, AIDS Walk, SF Sketchfest 2027, YBG Festival, Outside Lands, Portola, Jerry Day, Escape from Alcatraz Triathlon, Day of the Dead Procession, Illuminate SF, Fourth of July Fireworks, People in Plazas, Merola Summer Festival, and the review rows Frameline50, Noise Pop, Golden Gate Bandshell Concerts, SFJAZZ Summer Sessions, Third Thursdays On Ellis, SF Opera Summer Season) | **Imported unchanged** | Peer verification accepted as published/flagged there. |

Final dataset: **103 records = 90 published city-only rows (71 recurring / 19 special) + 13 review-register rows; 13 field-level flags; 8 categories.** Both sessions' full audit narratives are preserved in this file and in COORDINATION.md.

## Coverage-gap additions — `arena/646f6727-maltaproj7` — 2026-10-18

Stable counts in `verify.py` changed **96 published (76 recurring / 20 special, after PR #17) + 12 review → 107 published (87 recurring / 20 special) + 16 review; flags 16 → 20**. Eleven rows were added from directly fetched official pages (GDC 2027, RSAC 2027, Dreamforce 2027, J.P. Morgan Healthcare Conference 2027, TechCrunch Disrupt 2026, Chinatown Autumn Moon Festival 2026, Chinese New Year Flower Market Fair 2027, Trans March 2026, Golden Gate Park Band 2026 season, SF Ballet Nutcracker 2026, Off the Grid Fort Mason Night Market 2026) and four review records (How Weird Street Faire — discontinued per organizer; Union Street Festival — both domains hijacked; SF Dyke March 2027 — location not stated; Litquake 2026 — multi-city). Row-level quoted evidence: `research/coverage-gap-646f6727.md`; reproducible patch: `research/coverage-patch-646f6727.py`.


## Coverage-gap pass — arena/5e333a6e-maltaproj7 (2026-10-18)

Count-guard change in `verify.py`: **107 → 139 published (87 → 94 recurring, 20 → 45 special); review unchanged at 16; flags 20 → 25.** Every added value was read on 2026-10-18 from the linked official page. The reproducible patch is `research/patch-5e333a6e.py`; it is idempotent and skips rows the peer session arena/646f6727 (PR #18) had already merged. The review narrative is in `research/review-5e333a6e.md`.

| Group | Rows added | Official source type |
|---|---|---|
| Conventions on the Moscone Center calendar (2026 past and 2027 upcoming) | AI Engineer World's Fair, AMD Advancing AI, NPH Affordable Housing Conference, CoreWeave Fully Connected, SEMICON West, Current SF, Winter FancyFaire, ASCO GI, SPIE Photonics West, ASCO GU, ORS, TDX, AAD, AMCP, Atlassian Team '27, ASRS (16) | Official venue (`moscone.com/events/…`) |
| Museum free days | FAMSF Free Saturdays (weekly), FAMSF Free First Tuesdays (monthly) | Official venue |
| Arts | SF Open Studios, 52nd annual (studio start date flagged) | Official venue (SOMArts) |
| Neighborhood events | Cole Valley Street Fair, Bearrison Street Fair, Potrero Hill Festival (hours flagged), Clement Street Art Fair, Brava Block Party, SF Lowriders King of the Streets, Diplo's Run Club 5K, Lower Polk Live, From the E Night Market, Noe Valley Night Market | SFMTA (government) |
| Sports | SF Half Marathon & 5K 2027 | Official organizer |
| Pride week 2026 | Pink Triangle (SF Pride events page), SF Dyke March 2026 (SFMTA) | Official organizer / government |

Flags added (5): J.P. Morgan 2027 venue not stated; SF Open Studios studio-weekend start date not stated; Autumn Moon hours conflict (organizer 11–5 vs SFMTA 11–6); Fort Mason Night Market date lists disagree (venue page vs Off the Grid); Potrero Hill Festival hours conflict between two SFMTA pages.

Classification rule applied: a row is *recurring* only where the linked source says "annual", "every", "monthly", or similar. Single-date SFMTA notices that state no recurrence, and conferences, are *special*. Sunday Streets Excelsior (Oct 18) is already covered by `sunday-streets-2026`.
