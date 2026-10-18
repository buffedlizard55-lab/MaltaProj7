# Independent re-verification log — session arena/55c58947-maltaproj7

**Method:** Every published row and review record in `data/events.json` is re-checked by direct
fetch of its `source_url` (full page inspection, not search snippets) on 2026-10-18 (UTC).
For each row the check is: (a) URL resolves to the stated official source; (b) the source
states the event name; (c) the source states the date/cadence shown in the row; (d) the
source places the event inside the City and County of San Francisco. Optional fields
(time/admission) are checked for presence when the row states them.

Legend: PASS = all claimed values found in the linked source. PASS* = core values found;
minor detail noted. FAIL = a claimed value contradicts or is absent from the source
(row corrected or flagged).

| # | Row id | Source URL fetched | Result | Evidence found in source (quoted/paraphrased) |
|---|--------|--------------------|--------|-----------------------------------------------|
| 1 | ferry-plaza-farmers-market | https://foodwise.org/markets/ferry-plaza-farmers-market/ | PASS* | "Saturday (8 am – 2 pm) and Tuesday & Thursday (10 am – 2 pm), year round"; "operated by Foodwise at the San Francisco Ferry Building". Note: page header gives "Ferry Building, Embarcadero and Market Streets"; the row's "One Ferry Building" number is not printed on this page (check visitor-info page). |
| 2 | alemany-farmers-market | https://www.sf.gov/location--alemany-farmers-market | PASS | "every Saturday, 7am - 2pm"; address "100 Alemany Boulevard, San Francisco, CA 94110"; "Since February 2026, local nonprofit Foodwise operates Alemany Farmers Market"; operated "in partnership with the San Francisco Real Estate Division". |
| 3 | mission-community-market | https://foodwise.org/markets/mission-community-market/ | PASS* | "Thursday (3 pm – 7 pm), mid March – mid November"; "22nd Street between Mission and Valencia"; header "22nd and Bartlett Streets". Note: row's "84 Bartlett St." number not printed on this page (check visitor-info page). |
| 4 | castro-farmers-market-2026 | https://www.pcfma.org/market/castro-farmers-market | PASS | "270 Noe St., San Francisco"; "Wednesdays 3:00 pm - 7:00 pm"; "April 1st 2026 - November 18th 2026". Exact match. |
| 5 | divisadero-farmers-market | https://www.pcfma.org/market/divisadero-farmers-market | PASS | "1377 Fell St., San Francisco"; "Sundays 9:00 am - 1:00 pm"; "Year-Round". Exact match. |
| 6 | fillmore-farmers-market | https://www.pcfma.org/market/fillmore-farmers-market | PASS | "1700 O'Farrell St., San Francisco"; "Saturdays 9:00 am - 1:00 pm"; "Year-Round". Exact match. |
| 7 | hayes-valley-farmers-market | https://www.pcfma.org/market/hayes-valley-farmers-market | PASS | "450 Hayes Street, San Francisco"; "Saturdays 10:00 am - 2:00 pm"; "Year-Round". Exact match. |
| 8 | inner-sunset-farmers-market | https://www.pcfma.org/market/inner-sunset-farmers-market | PASS | "1315 8th Ave., San Francisco"; "Sundays 9:00 am - 1:00 pm"; "Year-Round"; "parking lot between 9th & 8th streets off of Irving Street"; "partnership with the Inner Sunset Park Neighbors". Exact match. |
| 9 | sunday-streets-2026 | https://sundaystreetssf.com/ | PASS | "2026 Events: Tenderloin • June 14th; Mission • July 19th; Bayview • August 23rd; Excelsior • October 18th". Exact match to row dates. |
| 10 | stern-grove-festival-2026 | https://www.sterngrove.org/lineup2026 + https://www.sterngrove.org/getting-here | PASS | Lineup runs "Sunday, June 14" (Peter Cat Recording Co.) through "Sunday, August 16" (Al Green) → June 14–August 16, 2026 confirmed. Getting-here page: "Sigmund Stern Grove... corner of 19th Avenue and Sloat Boulevard in San Francisco"; "Gates open at 12:00 PM"; "Show: 2pm"; free tickets ("Every attendee needs to have a free ticket"). Note: time/address text cites the getting-here page while source_url is the lineup page — both are official organizer pages on sterngrove.org. |
| 11 | free-shakespeare-in-the-park-2026 | https://sfshakes.org/performance/free-shakes/ + https://sfshakes.org/performance/free-shakes/ac/ | PASS | 2026 production "Antony and Cleopatra"; SF venues "McLaren Park" (Sept 5, 6, 7, 12, 13) and "Sue Bierman Park" (Sept 19, 20, 26, 27) → "September 5–27, 2026 (San Francisco run)" confirmed; "no tickets... required" (free) confirmed. Full run also covers Cupertino/Redwood City/Orinda — row correctly limited to SF performances. |
| 12 | flower-piano-2026 | https://gggp.org/event/flower-piano-2026/ | PASS* | "September 10-20, 2026"; venue "SF Botanical Garden"; "Cost: Free – $18". Corrections applied: row's admission text ("free for San Francisco residents with qualifying ID") is not stated on the linked event page → set admission to the page's stated "Free – $18"; daily-hours claim "10am–6pm" is not stated (page gives event-window start/end times) → time_text blanked per field policy. |
