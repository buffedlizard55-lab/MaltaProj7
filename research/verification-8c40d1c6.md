# Line-by-line verification — session `arena/8c40d1c6-maltaproj7` (2026-10-18)

Scope of this pass: re-fetch the linked **official** page for the rows that matter most to the brief —
everything still upcoming or ongoing as of **18 October 2026**, plus the focus disciplines
(gaming, music, AI) and the free/cost-labelling rules — and record what each page actually says.

Rules applied, unchanged from earlier sessions:

* A value is written only when the official page states it. If a page publishes no price, the
  admission field stays blank and a field-level flag records the gap.
* No figure is ever inferred from a ticket vendor, a reseller or "common knowledge".
* Every URL below was fetched on 2026-10-18 and returned live content unless stated otherwise.

Machine-readable patch: `research/patch-8c40d1c6.py` (re-runnable; idempotent).

---

## 1. Rows re-verified and confirmed unchanged (source text quoted)

| Row | Official source (fetched 2026-10-18) | What the page states | Outcome |
| --- | --- | --- | --- |
| Foodwise Sunday Supper — A Farm to City Feast (Oct 18, 2026) | [Foodwise event page](https://foodwise.org/events/foodwise-sunday-supper/) | "Sunday, October 18, 2026, 4:30 pm - 9:30 pm"; Ferry Plaza; FAQ: "The fair market value of a single dinner ticket is $200, and a single reception-only ticket is $75"; "This event is for guests 21 and over"; reception-only tickets admit 4:30–6:00 p.m. | Confirmed (ticketed). Note updated. |
| Lit Crawl SF (Oct 24, 2026) | [Litquake Lit Crawl page](https://www.litquake.org/litcrawl) | "OCTOBER 24, 2026"; "the world's largest free pop-up literary event"; "all programs from 6:30—7:30 PM" | Confirmed (free). |
| Día de los Muertos and Halloween at Mission Community Market (Oct 29) | [Foodwise](https://foodwise.org/events/dia-de-los-muertos-and-halloween-at-mission-community-market/) | "Thursday, October 29, 2026, 3:00 pm - 7:00 pm"; DJ Lamont 5–7 p.m.; free samples at the Seasonal Spotlight tent; market on 22nd St between Mission and Valencia | Confirmed. No admission charge stated → cost stays blank. |
| Foodwise Fall Fruit Celebration (Oct 31) | [Foodwise](https://foodwise.org/events/fall-fruit-celebration/) | "Saturday, October 31, 2026, 11:00 am - 1:00 pm"; Ferry Plaza; "Free samples, recipes, and cooking tips at the Seasonal Spotlight tent (front plaza)" | Confirmed. No admission charge stated → cost stays blank. |
| Mission Community Market — Last Day of the 2026 Season (Nov 12) | [Foodwise](https://foodwise.org/events/mission-community-market-last-day-of-the-season/) | "Thursday, November 12, 2026, 3:00 pm - 7:00 pm"; "We'll be back on March 18, 2027." | Confirmed. |
| Foodwise Fall Holiday Farmers Market (Nov 24) | [Foodwise](https://foodwise.org/events/fall-holiday-farmers-market/) | "Tuesday, November 24, 2026, 10:00 am - 2:00 pm" | Confirmed. |
| Foodwise Black Holiday Market (Dec 12) | [Foodwise](https://foodwise.org/events/pop-ups-on-the-plaza-black-holiday-market/) and [events index](https://foodwise.org/events/) | "Saturday, December 12, 2026, 9:00 am - 2:00 pm"; free entry | Confirmed (free). |
| San Francisco Dance Film Festival (Oct 23 – Nov 8) | [SFDFF Fall Festival 2026](https://sfdancefilmfest.org/fall-festival-2026/) | "Eighteen in-person screenings take place October 23-November 8 at venues throughout San Francisco"; "Online Festival runs November 9-30"; masterclass on Nov 7 marked "free!"; dated schedule (Oct 23, 28, 29, 30; Nov 4, 5, 6, 7, 8) | Confirmed. Time text corrected to a source-stated sentence (opening night Oct 23, 7:00 p.m.); the earlier wording contained a forbidden "see schedule" placeholder fragment caught by `verify.py`. |
| San Francisco Transgender Film Festival (Nov 12–14) | [SFTFF 2026 schedule](https://sftff.org/festival/2026-festival-schedule/) | Programs at the Roxie Theater Nov 12 (7pm, 9pm), Nov 13 (7pm, 9pm), Nov 14 (7pm, 9pm); ASL interpretation; KN95 masking required | Confirmed (ticketed per program). |
| San Francisco International Hip Hop DanceFest (Nov 14–15) | [Official site](https://www.sfhiphopdancefest.com/) | "28th Annual … November 14 & 15, 2026"; "Tickets On Sale Now!" via City Box Office; no price on the organizer page | Confirmed (ticketed). |
| Renegade Craft Fair — SF Winter (Nov 14–15) | [Renegade Craft](https://www.renegadecraft.com/event/san-francisco-winter/) | "November 14 + 15", "Saturday/Sunday, 11 am — 5 pm", Fort Mason Center Festival Pavilion, 2 Marina Blvd; "a suggested $5 entry fee can be paid via QR code onsite" | Confirmed (partly free / suggested). |
| Bhangra & Beats Night Market (Nov 13, Diwali edition) | [Bhangra & Beats](https://www.bhangraandbeats.com/) | "FRIDAY NOV, 13th", "YERBA BUENA GARDENS / JESSIE SQUARE / YERBA BUENA LANE", "PRICE: FREE", "TIME: 4 PM - 9 PM", "ALL AGES" | Confirmed (free). Organizer's venue wording again contradicts SF Travel's "Clay and Battery streets" listing — see existing `flag-bhangra-location-conflict`. |
| SF Open Studios (ArtSpan, through Oct 25) | [SOMArts](https://somarts.org/exhibition/sfopenstudios2026/) | Preview Exhibition "September 19, 2026 thru September 27, 2026", gallery "open 1–7 PM daily", artist studio events "through October 25, 2026"; ArtLaunch Sept 18, 21+, $25 | Confirmed. |
| Castro Farmers' Market (Wednesdays to Nov 18) | [PCFMA](https://www.pcfma.org/market/castro-farmers-market) | "Wednesdays 3:00 pm - 7:00 pm", "April 1st 2026 - November 18th 2026", 270 Noe St. | Confirmed. No admission charge stated. |
| Day of the Dead Procession (Nov 2) | [SF Travel November guide](https://www.sftravel.com/article/san-francisco-festivals-events-november) | "November 2, 2026", Mission District, links dayofthedeadsf.org | Unchanged — still rests on the trusted civic source (see `flag-day-of-the-dead-date`). |
| Illuminate SF Festival of Light (from Nov 27) | [SF Travel November guide](https://www.sftravel.com/article/san-francisco-festivals-events-november) | "More than 60 permanent and temporary eco-friendly light art installations"; "Begins November 27, 2026" | Confirmed; end date still blank (organizer site unreachable). |
| Lower Polk Live (Oct 23) | [SFMTA](https://www.sfmta.com/travel-updates/lower-polk-live-friday-october-23-2026) | "Lower Polk Live will be held on Friday, October 23, from 4 to 9 p.m."; Polk (Bush–Sutter) and Fern (Van Ness–Larkin) closed 2–10:30 p.m. | Confirmed. No admission charge stated. |
| From the E Excelsior Night Market (Oct 23) | [SFMTA](https://www.sfmta.com/travel-updates/e-night-market-friday-october-23-2026) | "…Friday, October 23, from 4:30 to 8:30 p.m." on Ocean Avenue | Confirmed. No admission charge stated. |
| Noe Valley Night Market (Oct 27) | [SFMTA](https://www.sfmta.com/travel-updates/noe-valley-night-market-tuesday-october-27-2026) | "Noe Valley Merchants will host the Noe Valley Night Market on Tuesday, October 27, from 4:30 to 8:30 p.m." | Confirmed. No admission charge stated. |
| Sunday Streets SF — 2026 season | [Sunday Streets](https://sundaystreetssf.com/) + [About](https://sundaystreetssf.com/about) | 2026 events: Tenderloin Jun 14, Mission Jul 19, Bayview Aug 23, Excelsior Oct 18; "fun, free activities provided by local nonprofits, community groups and small businesses"; program of Livable City with SFMTA / SFDPH / City and County | Dates confirmed; admission filled as **Free** on the strength of that organizer sentence (no admission charge is stated anywhere). Flagged: `flag-sundaystreets-free-wording`. |
| Union Square Plaza — Free Park Programs | [Union Square Alliance](https://visitunionsquaresf.com/park-programs) | "Free Programming in Union Square Plaza"; October schedule runs through Oct 20; pause Oct 21 – Nov 3 for ice-rink load-in; amenities resume Nov 4; winter crafts begin Nov 5 | Confirmed (free). |
| Golden Gate Park Band — 2026 season | [goldengateparkband.org](https://goldengateparkband.org/) | Season runs April–September, Sundays plus July 4 and Labor Day, Spreckels Temple of Music; "filled San Francisco with **free**, world-class music" | Confirmed (free). |
| People in Plazas | [peopleinplazas.org](https://peopleinplazas.org/) | "the 'People in Plazas' (PiP) **free** summer music festival in San Francisco produces more than 130 concerts in 15 different venues on or near Market Street" | Confirmed (free). |
| de Young & Legion of Honor free days | [FAMSF](https://www.famsf.org/visit/free-reduced-admission) | "Every Saturday we offer free general admission to all residents of the nine Bay Area counties" (permanent collection only); "General admission is free the first Tuesday of every month"; both suspended during Bouquets to Art | Confirmed (free, with stated limits). |
| Downtown First Thursdays | [dftsf.com](https://www.dftsf.com/) | "Next UP: NOV 5, 2026"; "Downtown SF's Free Monthly Street Party"; "Free w/ RSVP"; 2nd St between Market and Howard, 5–10 p.m. | Confirmed (free with RSVP). |
| Cloudflare Connect (Oct 19–21) | [cloudflare.com/connect](https://www.cloudflare.com/connect/) | "Oct 19-21 · Moscone West, SF"; Conference Pass $595; University +$495 (listed "Sold out" at check time); group/team $495 per pass (5–9; 50% off 10+); $100 off gov/mil/nonprofit/edu | Confirmed (paid). |
| AI Engineer Code Summit 2026 (Nov 10–12) | [ai.engineer/code/2026](https://ai.engineer/code/2026) | "NOV 10-12, 2026 // SF, CA"; "Invitations by application only"; Regular $1,299 + fees (talks + expo Nov 11–12); Final & At-Door $1,499 + fees; Workshop Add-On $299 + fees (Nov 10) | Confirmed (paid). |
| Current San Francisco (Confluent) (Nov 4–5) | [Moscone](https://www.moscone.com/events/current-san-francisco-2026) | "IN-PERSON \| November 4–5, 2026 \| Moscone West \| San Francisco, CA, USA"; registration-interest form only | Confirmed. No price stated. |
| Microsoft Ignite (Nov 17–20) | [ignite.microsoft.com](https://ignite.microsoft.com/) | "Nov 17-20, 2026 / San Francisco, Moscone Center" | Confirmed. No price stated. |
| AGU26 Annual Meeting (Dec 7–11) | [agu.org](https://www.agu.org/annual-meeting) | "7–11 December 2026 \| San Francisco, CA"; registration open; early-rate deadline 5 November | Confirmed. No price stated on the page. |
| San Francisco Ballet — Nutcracker (Dec 4–27) | [sfballet.org](https://www.sfballet.org/productions/nutcracker/) | "DEC 4–27"; War Memorial Opera House; full dated calendar; "Programming, casting, and prices subject to change"; Nutcracker Nightcap afterparty $150 (excludes performance ticket) | Dates/venue confirmed; **admission filled** as "Tickets sold; prices are not listed on the production page" → `flag-nutcracker-price-unstated`. |
| GDC Festival of Gaming (Mar 1–5, 2027) | [gdconf.com/passes-pricing](https://gdconf.com/passes-pricing/) | "March 1-5, 2027 / Moscone Center San Francisco, CA"; Festival $549 early ($499 super early to Oct 9, 2026); Game Changer $1,249; Indie/Start-Up/Academic $299; Festival Hall only $175; Business Hall only $125; 1-Day Career $125 | Confirmed (paid). |
| TDX 2027 (Mar 10–11) | [Moscone](https://www.moscone.com/events/tdx-2027) | "IN-PERSON \| March 10–11, 2027 \| Moscone Center \| San Francisco, CA USA" | Confirmed. No price stated. |
| SPIE Photonics West 2027 (Jan 30 – Feb 4) | [Moscone](https://www.moscone.com/events/spie-photonics-west-2027) | "January 30 – February 4, 2027 \| San Francisco, CA, USA" | Confirmed. No price stated. |
| San Francisco Half Marathon & 5K (Feb 7, 2027) | [sanfranciscohalfmarathon.org](https://sanfranciscohalfmarathon.org/race-information/) | "Event Date: FEBRUARY 7, 2027"; optional bib mailing $20 fee; no entry fee published | Confirmed. No entry price stated. |
| SF Sketchfest 2027 (Jan 14–31) | [sfsketchfest.com](https://sfsketchfest.com/) | "Jan 14 - 31, 2027"; "Lineup announcing in November!" | Confirmed. No price stated. |
| Chinese New Year Flower Market Fair (Jan 30–31, 2027) | [chineseparade.com](https://chineseparade.com/flowermarketfair/) | "The 2027 Flower Market Fair is scheduled for Sat. & Sun. Jan. 30 & 31 @ Grant between Clay and Broadway"; 120+ booths | Confirmed. No admission charge stated. |

Rows verified through the SFMTA weekly advisory of Oct 15–21, 2026
([press release](https://www.sfmta.com/press-releases/sfmta-transit-and-traffic-advisory-week-thursday-october-15-through-wednesday-october-21-2026)):
Diplo's Run Club 5K (Oct 18, 8:30 a.m., Robin Williams Meadow, post-race concert) and Sunday Streets
Excelsior (Oct 18, 11 a.m.–4 p.m.). The same advisory also lists Oct 17 events (Potrero Hill Festival,
Bearrison Street Fair, Brava Block Party, Clement Street Art Fair) that had already passed by the
check date, and the Top of the Hill Festival, which is in Daly City and therefore out of scope.

---

## 2. Values filled in this pass

| Row | Field | Value written | Why it is sourced |
| --- | --- | --- | --- |
| Diplo's Run Club San Francisco 5K | admission | "Tickets sold (registration required; the official event page listed the event 95% sold out on 2026-10-18). Registration price is not stated on the official page." | [Organizer page](https://diplosrunclub.com/san-francisco) shows a registration checkout and "95% SOLD OUT"; no price is published. Flagged: `flag-diplos-price-unstated`. |
| Diplo's Run Club San Francisco 5K | time_text | "8:30 a.m. race start; festival open 8:30 a.m.; Jax Jones 9:30 a.m.; Diplo 10:30 a.m." | Organizer page's "RACE WEEKEND / START LINE / FESTIVAL" blocks. |
| Exploratorium After Dark | admission | "Tickets required (18+; advance tickets recommended). Price is not stated on the official After Dark page." | [After Dark page](https://www.exploratorium.edu/visit/calendar/after-dark) states tickets are required and advance purchase is strongly recommended; no price. Flagged: `flag-exploratorium-price-unstated`. |
| San Francisco Ballet — Nutcracker | admission | "Tickets sold; prices are not listed on the production page." | Production page sells tickets but lists no price. Flagged: `flag-nutcracker-price-unstated`. |
| Sunday Streets SF — 2026 season | admission | Free, with the organizer's "fun, free activities" quote | [About page](https://sundaystreetssf.com/about). Flagged: `flag-sundaystreets-free-wording`. |
| San Francisco Dance Film Festival | time_text | "Programme times vary by date; opening night is Oct 23 at 7:00 p.m." | Schedule-at-a-glance on the official festival page. |

All other rows in the tables above had their **notes** refreshed with the re-fetch date and the quoted
source text, including several where the correct behaviour is to leave a field blank (markets, night
markets and city advisories that publish no admission charge).

---

## 3. New rows added (each from a live official page fetched 2026-10-18)

| Row | Source | Stated dates / times | Stated cost |
| --- | --- | --- | --- |
| Sunday Streets Excelsior — 2026 season finale | [Sunday Streets SF](https://sundaystreetssf.com/sunday-streets-excelsior-2026/) (corroborated by [SFMTA](https://www.sfmta.com/travel-updates/)) | Sunday, October 18, 2026, 11 a.m.–4 p.m.; Mission St between Geneva Ave and Theresa St | Free (organizer: "fun, free activities") — see flag |
| SFIAC and Olympic Club Cornhole Tournament | [SFMTA travel update](https://www.sfmta.com/travel-updates/sfiac-and-olympic-club-cornhole-tournament-friday-october-23-2026) | Friday, October 23, 2026, 11 a.m.–4 p.m.; Stockton St between Filbert and Union, North Beach | Not stated ("afternoon of fundraising") — see flag |
| Foodwise cooking demo — Sofía Jiménez, Tutuli Mexican Bakery | [Foodwise](https://foodwise.org/events/sofia-jimenez-tutuli-mexican-bakery/) | Saturday, October 31, 2026, 11:00–11:45 a.m. | Free ("free to the public, with recipes and samples for all") |
| Foodwise cooking demo — Ann M. Evans and Georgeanne Brennan | [Foodwise](https://foodwise.org/events/ann-m-evans-and-georgeanne-brennan-market-memories-cookbook/) | Saturday, November 21, 2026, 11:00–11:45 a.m. | Free (same sentence on every demo page) |
| Foodwise cooking demo — Anna Voloshyna, *Ukraïne* | [Foodwise](https://foodwise.org/events/anna-voloshyna-ukraine/) | Saturday, December 5, 2026, 11:00–11:45 a.m. | Free |
| Foodwise cooking demo — Florencia Ramirez, *The Kitchen Activist* | [Foodwise](https://foodwise.org/events/florencia-ramirez-the-kitchen-activist/) | Saturday, December 19, 2026, 11:00–11:45 a.m. | Free |

All six are inside the City and County of San Francisco (Ferry Plaza / Mission St / Stockton St,
North Beach) and all six are free except the cornhole tournament, whose cost is genuinely unstated.

Candidate items **considered and not added** (no confirmed official date or out of scope): the
Embarcadero Center Building Lighting Ceremony, Union Square Tree Lighting and Ghirardelli Square Tree
Lighting are all listed as "Date TBD" by SF Travel; the Great Dickens Christmas Fair is at the Cow
Palace in Daly City (outside the city); the Oct 17 street fairs in the SFMTA advisory had already
passed by the check date and are not re-listed as upcoming.

---

## 4. Irregularities found

1. **Prior-session ledger mismatch (flagged).** The COORDINATION entry for session
   `arena/e79e0de2-maltaproj7` (and the audit note in `verify.py`) states that an "SFIAC & Olympic
   Club Cornhole Tournament" row was added in PR #25. No such record exists in `data/events.json` —
   searching every id, name and source URL on 2026-10-18 returns nothing. The row was added in this
   pass from the SFMTA source instead. Recorded in `COORDINATION.md` and on the Flagged for Review
   page.
2. **Scaregrove could not be re-read.** `sfrecpark.org/Calendar.aspx` renders its listings with
   JavaScript; a text fetch returns only the loading state. The row is retained on the earlier
   verification and flagged for manual re-check (`flag-scaregrove-recheck`).
3. **Three price gaps remain** where an official page states a ticket requirement but no figure:
   Diplo's Run Club (`flag-diplos-price-unstated`), Exploratorium After Dark
   (`flag-exploratorium-price-unstated`) and SF Ballet's Nutcracker
   (`flag-nutcracker-price-unstated`). They are classed as paid so they are never presented as free.
4. **Sunday Streets wording.** No page uses the phrase "free admission"; the free label rests on the
   organizer's "fun, free activities" statement. Documented in `flag-sundaystreets-free-wording` so a
   reviewer can apply a stricter reading.
5. **Bhangra & Beats location conflict persists** between the organizer (Yerba Buena Gardens) and
   SF Travel (Clay & Battery streets); the row follows the organizer, as before.
6. **`verify.py` guard fixed during this pass.** The placeholder-fragment check rejected the dance
   festival's "see schedule" time text, which is correct behaviour; the field now carries a
   source-stated sentence instead.

## 5. Result of the pass

* Re-fetched official pages for **41 rows** (all still-upcoming rows in the focus window plus the
  gaming/music/AI rows and the free-recurring programs).
* 4 cost fills, 1 time-text fill, 6 new published rows, 6 new field-level flags, ~35 note updates.
* `python3 build.py` → 154 published rows (98 recurring + 56 special), 16 review records, 40 flags.
* `python3 verify.py` → `ALL LOCAL CATALOG, SOURCE-LINK, AND NAVIGATION CHECKS PASSED`.
