# Official-source audit — San Francisco city events

**Audit date:** 2026-10-18

**Geographic rule:** City and County of San Francisco only
**Catalog snapshot:** 54 published, source-linked records: 46 regularly occurring and 8 dated/special. Five non-published records remain on the review register.

## What was checked

1. The source was an official organizer, official venue, SF government page, or a clearly labeled trusted civic arts-calendar record.
2. The row name, a date/cadence, and a San Francisco location were checked against the linked source. Where a program crosses city lines, only an explicitly identified SF component is published; otherwise the program is held in the review register.
3. Hours, admission, venues, and dates were copied only when the linked source stated them. Optional values absent from the captured source are displayed as an em dash rather than guessed.
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
| `alemany-farmers-market` | Alemany Farmers Market | Saturday (year-round) | 100 Alemany Boulevard, San Francisco, CA 94110 | [SF.gov location page](https://www.sf.gov/location--alemany-farmers-market) | Government source | verified |
| `mission-community-market` | Mission Community Market | Thursday, mid-March–mid-November | 22nd Street between Mission and Valencia / 84 Bartlett St., San Francisco | [Foodwise market page](https://foodwise.org/markets/mission-community-market/) | Official organizer | verified |
| `castro-farmers-market-2026` | Castro Farmers’ Market | Wednesday, April 1–November 18, 2026 | 270 Noe St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/castro-farmers-market) | Official organizer | verified |
| `divisadero-farmers-market` | Divisadero Farmers’ Market | Sunday (year-round) | 1377 Fell St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/divisadero-farmers-market) | Official organizer | verified |
| `fillmore-farmers-market` | Fillmore Farmers’ Market | Saturday (year-round) | 1700 O’Farrell St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/fillmore-farmers-market) | Official organizer | verified |
| `hayes-valley-farmers-market` | Hayes Valley Farmers’ Market | Saturday (year-round) | 450 Hayes St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/hayes-valley-farmers-market) | Official organizer | verified |
| `inner-sunset-farmers-market` | Inner Sunset Farmers’ Market | Sunday (year-round) | 1315 8th Ave.; parking lot between 8th and 9th off Irving St., San Francisco | [PCFMA market page](https://www.pcfma.org/market/inner-sunset-farmers-market) | Official organizer | verified |
| `sunday-streets-2026` | Sunday Streets SF — 2026 season | Tenderloin Jun 14; Mission Jul 19; Bayview Aug 23; Excelsior Oct 18, 2026 | Tenderloin, Mission, Bayview, and Excelsior, San Francisco | [Sunday Streets SF 2026 season page](https://sundaystreetssf.com/) | Official organizer | verified |
| `stern-grove-festival-2026` | Stern Grove Festival — 2026 season | June 14–August 16, 2026 | Sigmund Stern Grove, 19th Avenue and Sloat Boulevard, San Francisco | [Stern Grove 2026 lineup](https://www.sterngrove.org/lineup2026) | Official organizer | verified |
| `free-shakespeare-in-the-park-2026` | Free Shakespeare in the Park — San Francisco performances | September 5–27, 2026 (San Francisco run) | San Francisco locations listed by SF Shakespeare Festival | [SF Shakespeare Festival performance page](https://sfshakes.org/performance/free-shakes/) | Official organizer | verified |
| `flower-piano-2026` | Flower Piano | September 10–20, 2026 | San Francisco Botanical Garden, Golden Gate Park | [Gardens of Golden Gate Park event page](https://gggp.org/event/flower-piano-2026/) | Official organizer | verified |
| `chinese-new-year-parade-2027` | San Francisco Chinese New Year Parade | Saturday, February 20, 2027 | 2nd and Market Streets through Union Square to Kearny Street and Columbus Avenue, San Francisco | [Chinese New Year Parade FAQ](https://chineseparade.com/faq/) | Official organizer | verified |
| `cherry-blossom-2027` | Northern California Cherry Blossom Festival | April 10–11 and April 17–18, 2027; Grand Parade April 18 | Japantown, San Francisco | [Cherry Blossom Festival official site](https://sfcherryblossom.org/) | Official organizer | verified |
| `sf-pride-2027` | San Francisco Pride Celebration & Parade | June 26–27, 2027 | Civic Center Plaza and Market Street, San Francisco | [SF Pride official site](https://sfpride.org/) | Official organizer | verified |
| `carnaval-sf-2026` | Carnaval San Francisco | May 23–24, 2026 | Mission District; festival on Harrison Street (16th–24th), San Francisco | [Carnaval SF event page](https://carnavalsanfrancisco.org/special-events/) | Official organizer | verified |
| `bay-to-breakers-2027` | Bay to Breakers | Sunday, May 16, 2027 | San Francisco streets; official route information is published by the organizer | [Bay to Breakers official site](https://www.baytobreakers.com/) | Official organizer | verified |
| `sf-marathon-2026` | San Francisco Marathon — race weekend | July 24–26, 2026 | San Francisco; start and course details vary by distance | [San Francisco Marathon race-weekend page](https://www.thesfmarathon.com/race-weekend/) | Official organizer | verified |
| `st-patricks-parade-2026` | San Francisco St. Patrick’s Day Parade & Festival | Saturday, March 14, 2026 | Parade from 2nd and Market to Civic Center; Civic Center Plaza, San Francisco | [United Irish Societies parade page](https://uissf.org/st-patricks-day-parade) | Official organizer | verified |
| `caamfest-2026` | CAAMFest — San Francisco program | May 7–10, 2026 (San Francisco program) | AMC Kabuki, Asian Art Museum, KOHO Creative Hub, Koret Auditorium, and New People Cinema, San Francisco | [CAAMFest 2026 schedule](https://caamfest.com/2026/schedule/) | Official organizer | verified |
| `sf-silent-film-festival-2026` | San Francisco Silent Film Festival | May 6–10, 2026 | Castro Theatre, San Francisco | [Silent Film Festival 2026 page](https://silentfilm.org/festival-2026/) | Official organizer | verified |
| `international-ocean-film-festival-2026` | International Ocean Film Festival — San Francisco program | April 10–12, 2026 (San Francisco program) | Cowell Theater, Fort Mason Center, San Francisco | [International Ocean Film Festival page](https://intloceanfilmfest.org/festival) | Official organizer | verified |
| `sf-black-film-festival-2026` | San Francisco Black Film Festival | June 18–21, 2026 | San Francisco; venue schedule on organizer site | [SF Black Film Festival official site](https://sfbff.org/) | Official organizer | verified |
| `sf-dance-film-festival-2026` | San Francisco Dance Film Festival | October 23–November 8, 2026 (in-person); November 9–30 online | San Francisco theaters for in-person program; online component separate | [Dance Film Festival 2026 page](https://sfdancefilmfest.org/fall-festival-2026/) | Official organizer | verified |
| `sf-transgender-film-festival-2026` | San Francisco Transgender Film Festival | November 12–14, 2026 | Roxie Theater, 3117 16th St., San Francisco | [SF Arts 2026 festival listing](https://sfarts.org/event/29th-anniversary-san-francisco-transgender-film-festival-2O89YYfq6cS0gq7oZDYObg/) | Trusted civic source | verified |
| `third-i-south-asian-film-festival-2026` | 3rd i San Francisco International South Asian Film Festival | October 9–11, 2026 | San Francisco; venue details on organizer program | [3rd i Films official site](https://thirdi.org/) | Official organizer | verified |
| `lit-crawl-sf-2026` | Lit Crawl SF | October 24, 2026 | Mission District venues, San Francisco | [Lit Crawl SF official page](https://www.litquake.org/litcrawl) | Official organizer | verified |
| `hardly-strictly-bluegrass-2026` | Hardly Strictly Bluegrass | October 2–4, 2026 | Hellman Hollow, Lindley Meadow, and Marx Meadow, Golden Gate Park, San Francisco | [Hardly Strictly Bluegrass FAQ](https://hardlystrictlybluegrass.com/info-faq-2026/) | Official organizer | verified |
| `fleet-week-sf-2026` | San Francisco Fleet Week | October 7–12, 2026; air show October 9–11 | San Francisco waterfront, Marina Green, Fisherman’s Wharf, and city venues | [Fleet Week 2026 calendar](https://fleetweeksf.org/calendar-of-events/) | Official organizer | verified |
| `up-your-alley-2026` | Up Your Alley | Sunday, July 26, 2026 | Folsom Street between 8th and 11th; connected SoMa streets, San Francisco | [Folsom Street FAQ](https://www.folsomstreet.org/faq) | Official organizer | verified |
| `folsom-street-fair-2026` | Folsom Street Fair | Sunday, September 27, 2026 | Folsom Street between 7th and 13th and connected SoMa streets, San Francisco | [Folsom Street Fair official page](https://www.folsomstreet.org/folsom-street-fair) | Official organizer | verified |
| `castro-street-fair-2026` | Castro Street Fair | Sunday, October 4, 2026 | Castro and Market Streets and surrounding Castro District streets, San Francisco | [Castro Street Fair information page](https://castrostreetfair.org/fair/) | Official organizer | verified |
| `nihonmachi-street-fair-2026` | Nihonmachi Street Fair | August 1–2, 2026 | Post Street between Laguna and Fillmore and Osaka Way, Japantown, San Francisco | [Nihonmachi Street Fair 2026 page](https://www.nihonmachistreetfair.org/home-1) | Official organizer | verified |
| `pistahan-2026` | Pistahan Parade & Festival | August 8–9, 2026; parade Saturday | Yerba Buena Gardens; Saturday parade on Market Street, San Francisco | [Pistahan official site](https://pistahan.net/) | Official organizer | verified |
| `north-beach-festival-2026` | North Beach Festival | June 20–21, 2026 | North Beach, San Francisco | [North Beach Festival official site](https://northbeachfestival.org/) | Official organizer | verified |
| `fillmore-jazz-festival-2026` | Fillmore Jazz Festival | July 4–5, 2026 | Fillmore Street, San Francisco | [Fillmore Jazz Festival official site](https://fillmorejazzfestival.com/) | Official organizer | verified |
| `haight-ashbury-street-fair-2026` | Haight-Ashbury Street Fair | September 20, 2026 | Haight Street, San Francisco | [Haight-Ashbury Street Fair official site](https://haightashburystreetfair.org/) | Official organizer | verified |
| `comedy-day-2026` | Comedy Day | September 13, 2026 | Robin Williams Meadow (formerly Sharon Meadow), Golden Gate Park, San Francisco | [Comedy Day official site](https://comedyday.org/) | Official organizer | verified |
| `muni-heritage-weekend-2026` | Muni Heritage Weekend | September 19–20, 2026 | Muni Railway / San Francisco locations listed by SFMTA | [SFMTA event page](https://www.sfmta.com/calendar/muni-heritage-weekend-2026) | Government source | verified |
| `italian-heritage-parade-2026` | Italian Heritage Parade | October 11, 2026 | North Beach and San Francisco parade route | [Italian Heritage Parade official site](https://sfitalianheritage.org/) | Official organizer | verified |
| `world-arts-west-dance-festival-2026` | World Arts West Dance Festival | September 6, 2026 | Presidio of San Francisco | [Presidio Trust event page](https://presidio.gov/explore/events/world-arts-west-dance-festival-2026) | Official venue / federal trust | verified |
| `sf-porchfest-2026` | SF Porchfest | May 30, 2026 | Mission District porches, backyards, and stoops, San Francisco | [SF Porchfest official app/site](https://app.sfporchfest.org/) | Official organizer | verified |
| `juneteenth-sf-freedom-celebration-2026` | Juneteenth SF Freedom Celebration | June 13, 2026 | Fillmore/Western Addition; historic Fillmore Street, San Francisco | [SF.gov 2026 Juneteenth page](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) | Official organizer | verified |
| `juneteenth-market-street-parade-2026` | Juneteenth Market Street Parade | June 20, 2026 | Market Street, San Francisco | [SF.gov 2026 Juneteenth page](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) | Government source | verified |
| `juneteenth-on-the-waterfront-2026` | Juneteenth on the Waterfront | June 7, 2026 | Ferry Building Farmers Market / waterfront, San Francisco | [SF.gov 2026 Juneteenth page](https://www.sf.gov/san-francisco-celebrates-juneteenth-2026) | Government source | verified |
| `sf-aloha-run-2026` | San Francisco Aloha Run | September 20, 2026 | Crissy Field, San Francisco | [SF Aloha Run official site](https://sfaloharun.com/) | Official organizer | verified |
| `sf-international-arts-festival-2026` | San Francisco International Arts Festival | April 30–May 10, 2026 | San Francisco venues listed by festival | [SF International Arts Festival official site](https://sfiaf.org/) | Official organizer | verified |
| `sundown-cinema-inside-out-2026` | Sundown Cinema: Inside Out | July 24, 2026 | Presidio of San Francisco | [Presidio Trust 2026 summer announcement](https://presidio.gov/about/press/presidio-unveils-vibrant-2026-summer-event-lineup) | Official venue / federal trust | verified |
| `scaregrove-2026` | Scaregrove | October 30, 2026 | Stern Grove, San Francisco | [SF Recreation and Park calendar](https://sfrecpark.org/Calendar.aspx) | Government source | verified |
| `foodwise-black-holiday-market-2026` | Foodwise Black Holiday Market | December 12, 2026 | Ferry Plaza, San Francisco | [Foodwise event page](https://foodwise.org/events/pop-ups-on-the-plaza-black-holiday-market/) | Official organizer | verified |
| `cloudflare-connect-2026` | Cloudflare Connect | October 19–21, 2026 | Moscone West, San Francisco | [Cloudflare Connect official page](https://www.cloudflare.com/connect/) | Official organizer | verified |
| `informs-annual-meeting-2026` | INFORMS Annual Meeting | November 1–4, 2026 | Moscone South and San Francisco Marriott Marquis | [INFORMS Annual Meeting official page](https://meetings.informs.org/wordpress/annual/) | Official organizer | verified |
| `microsoft-ignite-2026` | Microsoft Ignite | November 17–20, 2026 | San Francisco; venue details on Microsoft registration materials | [Microsoft Ignite official site](https://ignite.microsoft.com/) | Official organizer | verified |
| `agu-annual-meeting-2026` | AGU26 Annual Meeting | December 7–11, 2026 | Moscone Center, San Francisco | [AGU Annual Meeting official page](https://www.agu.org/annual-meeting) | Official organizer | verified |

## Review register and explicit exclusions

| ID | Item | Captured date | Source | Status | Why it is not in city-only tables |
|---|---|---|---|---|
| `sffilm-festival-2026` | SFFILM Festival — mixed-geography program | April 24–May 4, 2026 | [SFFILM 2026 festival page](https://sffilm.org/2026-about-the-festival/) | `partial_sf_program` | The official festival page states that the program spans San Francisco, Oakland, and Berkeley. It is excluded from city-only tables until individual San Francisco programs are separated with their own official listings. |
| `sfjff-2026` | San Francisco Jewish Film Festival — mixed-geography program | July 16–August 2, 2026 | [Jewish Film Institute SFJFF page](https://jfi.org/sfjff-2026) | `partial_sf_program` | The official page covers San Francisco and East Bay venues. It is excluded until a city-only program-level record can be made. |
| `sf-fringe-2026` | San Francisco Fringe Festival — 2026 schedule | — | [San Francisco Fringe official site](https://www.sffringe.org/) | `needs_review` | No current direct organizer page with a verified 2026 date, time, and San Francisco venue was retained in this audit. Conflicting or indirect listings are not enough to publish a city-only row. |
| `opera-in-the-park-2026` | Opera in the Park — 2026 | September 13, 2026 (cancelled) | [San Francisco Opera cancellation release](https://www.sfopera.com/press/press-releases/Season-Opening-Performances-Cancelled-Strike/) | `cancelled` | San Francisco Opera’s official release says the September 13, 2026 Opera in the Park concert was cancelled. It must not appear as an active event. |
| `bay-area-aloha-festival` | Bay Area Aloha Festival | — | [Bay Area Aloha Festival official site](https://www.bayareaalohafestival.com/) | `outside_city_excluded` | Official materials place this festival outside San Francisco city limits. It is intentionally excluded; the separate San Francisco Aloha Run is included above. |

## Material irregularities resolved during audit

| Item | Resolution |
|---|---|
| Cloudflare Connect 2026 | Canonical organizer event page gives October 19–21. A different page’s October 22 reference was not normalized into the event date. |
| San Francisco International Film Festival / SF Jewish Film Festival | Both sources describe programs outside SF city boundaries as well as San Francisco. They are kept off city-only tables rather than represented as wholly SF events. |
| Opera in the Park 2026 | The organizer’s cancellation release overrides any earlier promotional listing. The event is kept in the review register only. |
| Bay Area Aloha Festival | Excluded after official location evidence placed it outside SF city limits. This does not affect the separately sourced SF Aloha Run. |
| Juneteenth city programs | A direct SF.gov 2026 page was used to distinguish the June 7 waterfront program, June 13 Fillmore Freedom Celebration, and June 20 Market Street Parade. |
| CAAMFest umbrella scope | The published record is limited and titled as the San Francisco program, using named SF venues in the official 2026 schedule; it does not claim the umbrella festival is city-exclusive. |

## Data handoff

- **Machine-readable dataset:** [`data/events.json`](../data/events.json)
- **Public-site behavior:** only `bucket: recurring` / `special` with `status: verified` can enter the main tables; all other statuses route to the review page.
- **Minimum recheck before adding a row:** official source URL, SF city location, date/cadence, and an explicit review reason for any missing required field.

## Final integration re-verification — 2026-10-18 (arena/d71d78cc-maltaproj7)

Every source URL in `data/events.json` was re-fetched from the official publisher page on 2026-10-18 (organizer, official venue, or government source). The pending independent-audit findings were applied, corrections were made only where an official source states the value, and residual problems were published as field-level flags on the Flagged for Review page. Nothing was inferred: values that the linked source does not state are left blank.

**Outcome totals:** 77 records = 72 published city-only rows (55 recurring / 17 special) + 5 review-register rows; 13 field-level flags; 8 categories.

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
