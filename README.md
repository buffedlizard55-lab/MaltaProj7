# San Francisco Events · source-linked snapshot

**Live site:** https://buffedlizard55-lab.github.io/MaltaProj7/

A mobile-friendly static dashboard for publicly advertised events **within the City and County of San Francisco**. The **landing page, Upcoming and Free pages contain only dated, source-confirmed free events that have not yet passed**. Admission is displayed in every row. Paid and partly free events have their own [Paid & partly free](paid.html) page; records with an unconfirmed admission cost appear on [Flagged for Review](flagged.html). The secondary recurring, special, category and all-events research catalogs retain past and other admission types, clearly labeled.

## What is actually covered

As of **October 18, 2026**: **148 published rows** (98 recurring, 50 special), **16 excluded/review records**, **35 field-level flags** and nine categories. Of the 148 published rows, **8 have both confirmed free admission and a dated upcoming/ongoing occurrence**, **43 have confirmed free admission across all dates**, **12 are partly free/conditional**, **13 have evidence of paid entry**, and **80 have no confirmed admission cost**. Registration alone or a waived fundraising minimum is **not** evidence of free or paid admission. The client recalculates upcoming status and the executive summary against the visitor’s local date; a no-JavaScript view is explicitly a snapshot as of October 18. An undated weekly/monthly tradition is **not** assigned an invented next occurrence.

Gaming and AI have no dated free upcoming entry verified in this snapshot; the dashboard says so instead of promoting ticketed conferences. Music and other free upcoming events appear with event-level publisher links. The [separate paid section](paid.html) includes paid and partly free events with their original source-stated admission wording. The [Flagged page](flagged.html) exposes unresolved source issues and every unconfirmed cost for manual review.

**Not exhaustive.** This is a reproducible, bounded collection of official-organizer, venue and government sources plus three explicitly labeled trusted civic sources. It cannot guarantee a complete list of all public, private, newly announced or unlisted events. The [method page](method.html), [source audit](research/official-source-audit.md), [this session’s focused recheck](research/review-f65449c5.md), and earlier independent audits in `research/` document source decisions and unresolved issues. Always check the linked publisher for date, tickets and location before going. In particular, the YBG season end date is not an individual performance date and its organizer schedule was not independently accessible during this pass; see the flagged record.

## Rebuild and verify

No package installation is needed for the published site or its standard checks:

```sh
python3 build.py
python3 verify.py
```

`data/events.json` is the source of truth. The build regenerates all root/category HTML pages, `assets/style.css` and `data/events.csv`. The verifier checks row sets and official source links on the free, paid and review pages; date and cost separation; duplicate IDs; local links; and data shape. It **does not live-fetch all external URLs**; evidence from the earlier audits and the targeted current recheck is documented in `research/`. A local browser-DOM smoke test of the live client-side date logic is recorded in `research/review-f65449c5.md`.

GitHub Pages is deployed by `.github/workflows/pages.yml` from `main`. Coordination, PRs, source review and deployment status are recorded in [COORDINATION.md](COORDINATION.md).
