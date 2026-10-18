# MaltaProj7 — San Francisco Events

A verified, source-linked list of events **within the City of San Francisco only**, split into **Recurring** (weekly / monthly / seasonal) and **Annual / Special** (once-a-year festivals, parades, races).

- **Site (GitHub Pages):** landing dashboard + subpages per type, all-events search/filter, Flagged for Review, and Method & Sources.
- **Data:** `data/events.json` and `data/events.csv` — every row has an official source URL; unverifiable fields are left blank, never inferred.
- **Rebuild:** `python3 build.py` · **Verify:** `python3 verify.py`
- **Coordination & audit log:** `COORDINATION.md`

Checked 18 Oct 2026. See the Flagged for Review page on the site for exclusions (e.g. events actually held outside SF), discrepancies between official sources, and unverified fields.
