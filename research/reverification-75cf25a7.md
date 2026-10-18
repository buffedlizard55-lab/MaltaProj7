# Conservative admission recheck — session `arena/75cf25a7-maltaproj7`

**Checked:** 2026-10-18 (UTC)

**Scope:** The admission fields on the two published Sunday Streets 2026 rows, and the corresponding existing flag `flag-sundaystreets-free-wording`. This is a narrow correction, not a claim that the entire catalog was independently live-fetched in this pass.

## Official organizer pages fetched

| Page | Exact relevant text returned | What it establishes |
| --- | --- | --- |
| [Sunday Streets SF — 2026 season](https://sundaystreetssf.com/) | “2026 Events”: “Tenderloin • June 14th”, “Mission • July 19th”, “Bayview • August 23rd”, “Excelsior • October 18th”; “Sunday Streets is San Francisco’s open streets program that transforms miles of city streets into car-free community spaces” | Confirms the four 2026 edition dates and the open-streets programme. It does not state an admission price. |
| [Sunday Streets SF — About](https://sundaystreetssf.com/about/) | “Event routes are 1-4 miles in length, with fun, free activities provided by local nonprofits, community groups and small businesses.” The page separately states: “Exhibitor spaces start at $35 and are free for organizations and businesses on the route.” | Confirms that activities are described as free. It does **not** say that event admission is free or state a general-attendee admission price. The exhibitor fee is not an attendee price. |
| [Sunday Streets SF — Excelsior 2026](https://sundaystreetssf.com/sunday-streets-excelsior-2026/) | “Sunday, October 18, 2026 · 11 AM – 4 PM”; “Mission Street between Geneva Avenue and Theresa Street”; “Come out and join us for a day of car-free fun!” The programme separately lists “Excelsior 5k Walktober (9:30am @ Cayuga Playground)” followed by “Click here to register.” | Confirms the date, time, and location. The page links to registration for a distinct 5K but does not state its price or an admission cost for the open-streets event. No price is inferred for either. |

All returned page chunks were read on 2026-10-18. The [About](https://sundaystreetssf.com/about/) and [Excelsior](https://sundaystreetssf.com/sunday-streets-excelsior-2026/) pages each had a second chunk; that returned remaining content contained no additional event-admission price statement.

## Decision and changes

The previous `admission` values began with “Free” while also explaining that no admission charge was stated. That contradicted the catalog's rule that admission fields must be source-confirmed. “Free activities” is not evidence of a source-stated event admission amount, and an absent price is not evidence of a $0 price.

- Cleared `admission` on `sunday-streets-2026` and `sunday-streets-excelsior-2026`. Their official source links and confirmed date/location details remain unchanged.
- Reworded their notes and the existing `flag-sundaystreets-free-wording` to document the source wording and this conservative disposition. No new flag was added; the existing issue remains visible on **Flagged for Review**.
- Both rows now display **Not stated** and are excluded from the Dashboard, Upcoming, and Free upcoming lists. They remain in the full/recurring/special catalogs and in the Flagged page's cost-not-stated register. This records an unconfirmed cost; it does **not** claim that an admission fee is charged.
- The 5K's registration price remains unverified; it was not copied into the open-streets event row.

## Derived snapshot impact

As of the catalog snapshot date, the correction changes the derived counts from **20 to 18** confirmed-free dated upcoming events, **56 to 54** confirmed-free rows overall, and **78 to 80** rows with admission cost not stated. The 12 partly-free, 16 paid/ticketed, 67 upcoming-overall, 162 published, 17 review, and 51 flag counts are unchanged. These counts are generated from `data/events.json`; the rebuilt pages and verifier provide the row-set checks.
