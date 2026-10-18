#!/usr/bin/env python3
"""Generate static GitHub Pages site from data/events.json. Every row requires official source URL; blank = unverified."""
import json, csv, html, pathlib, collections
ROOT=pathlib.Path(__file__).parent
events=json.loads((ROOT/"data/events.json").read_text())
# validation
for e in events:
    assert e.get("source_url","").startswith("http"), e
    assert e["type"] in ("Recurring","Annual / Special"), e
CSS="""*{box-sizing:border-box}body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;margin:0;color:#17202a;background:#f7f8fa;line-height:1.5}header{background:#0b3d5f;color:#fff;padding:28px 20px}header a{color:#fff}.wrap{max-width:1180px;margin:auto;padding:20px}nav{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0}nav a{background:#fff;border:1px solid #d5dde5;padding:8px 12px;border-radius:999px;text-decoration:none;color:#0b3d5f}nav a.active{background:#0b3d5f;color:#fff}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}.card{background:#fff;border:1px solid #e1e7ee;border-radius:12px;padding:16px}.card b{font-size:28px;display:block}table{width:100%;border-collapse:collapse;background:#fff;font-size:14px}th,td{border:1px solid #dfe6ee;padding:8px;text-align:left;vertical-align:top}th{background:#eaf1f7;position:sticky;top:0}input,select{padding:10px;border:1px solid #cbd6e2;border-radius:8px;margin:6px 6px 14px 0} .note{background:#fff8e1;border:1px solid #ffe08a;padding:12px;border-radius:10px} .flag{background:#fff1f1;border-color:#ffb3b3}footer{color:#5a6b7d;font-size:13px;padding:24px} a{color:#075e9e} .tag{font-size:12px;background:#e8f2fb;padding:2px 7px;border-radius:999px}"""
(ROOT/"assets").mkdir(exist_ok=True); (ROOT/"assets/style.css").write_text(CSS)
def esc(x): return html.escape(x or "")
def table(rows):
    out=['<div style="overflow:auto"><table><thead><tr><th>Event</th><th>Type</th><th>Category</th><th>When (as stated by source)</th><th>Location (SF only)</th><th>Cost</th><th>Official source</th></tr></thead><tbody>']
    for e in rows:
        cost=e.get("cost","") or '<span class="tag">unverified — blank in data</span>'
        loc=e.get("location","") or '<span class="tag">unverified — blank in data</span>'
        when=e.get("when","") or '<span class="tag">unverified — blank in data</span>'
        out.append(f'<tr><td><b>{esc(e["name"])}</b></td><td>{esc(e["type"])}</td><td>{esc(e["category"])}</td><td>{esc(when) if e.get("when") else when}</td><td>{esc(loc) if e.get("location") else loc}</td><td>{esc(cost) if e.get("cost") else cost}</td><td><a href="{esc(e["source_url"])}" target="_blank" rel="noopener">Official source ↗</a><br><small>{esc(e.get("source_publisher",""))}</small></td></tr>')
    out.append('</tbody></table></div>'); return "\n".join(out)
def page(title,body,active=""):
    nav=[("index.html","Home"),("recurring.html","Recurring"),("annual-special.html","Annual / Special"),("all-events.html","All events"),("flagged.html","Flagged for Review"),("method.html","Method & Sources")]
    links="".join(f'<a class="{"active" if h==active else ""}" href="{h}">{l}</a>' for h,l in nav)
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} — SF Events</title><link rel="stylesheet" href="assets/style.css"></head><body><header><div class="wrap"><h1>San Francisco Events</h1><p>City of San Francisco only · Recurring vs. Annual / Special · Every row linked to an official source · Checked 18 Oct 2026</p></div></header><main class="wrap"><nav>{links}</nav>{body}</main><footer class="wrap">Scope note: this is a verified, source-linked list from official city, organizer and official destination sources found at check date — not a claim that every private or one-off event in SF is included. Unverifiable fields are left blank in the data and shown as “unverified”. See Method & Sources.</footer><script>const q=document.querySelector("#q"),c=document.querySelector("#cat");function f(){{let s=(q?q.value.toLowerCase():""),k=c?c.value:"";document.querySelectorAll("tbody tr").forEach(r=>{{r.style.display=(!s||r.textContent.toLowerCase().includes(s))&&(!k||r.textContent.includes(k))?"":"none"}})}};if(q)q.oninput=f;if(c)c.onchange=f;</script></body></html>'
rec=[e for e in events if e["type"]=="Recurring"]; ann=[e for e in events if e["type"]!="Recurring"]
cats=sorted(set(e["category"] for e in events))
controls='<input id="q" type="search" placeholder="Search events, places, categories…" aria-label="Search"><select id="cat"><option value="">All categories</option>'+ "".join(f'<option>{esc(c)}</option>' for c in cats)+'</select>'
bycat="".join(f'<div class="card"><b>{len([e for e in events if e["category"]==c])}</b>{esc(c)}</div>' for c in cats)
home=f'''<h2>Dashboard</h2><div class="cards"><div class="card"><b>{len(events)}</b>Total verified entries</div><div class="card"><b>{len(rec)}</b>Recurring (weekly / monthly / seasonal)</div><div class="card"><b>{len(ann)}</b>Annual / Special</div><div class="card"><b>{len(cats)}</b>Categories</div></div><h3>By category</h3><div class="cards">{bycat}</div><div class="note"><b>How to use:</b> Start with <a href="recurring.html">Recurring</a> for things that happen every week/month or each season, or <a href="annual-special.html">Annual / Special</a> for once-a-year festivals, races and parades. <a href="all-events.html">All events</a> has search + category filter. Anything that could not be confirmed from an official source is on <a href="flagged.html">Flagged for Review</a> — it does not block the site.</div><h3>All events</h3>{controls}{table(events)}'''
(ROOT/"index.html").write_text(page("Home",home,"index.html"))
(ROOT/"recurring.html").write_text(page("Recurring events",f'<h2>Recurring events</h2><p>Weekly, monthly, or seasonal series that repeat within the year. Each row\'s timing is exactly as the official source states it.</p>{controls}{table(rec)}',"recurring.html"))
(ROOT/"annual-special.html").write_text(page("Annual / Special events",f'<h2>Annual / Special events</h2><p>Once-a-year festivals, parades, races and special editions. 2026 dates are shown only where the linked official source states them; otherwise the field is blank in the data.</p>{controls}{table(ann)}',"annual-special.html"))
(ROOT/"all-events.html").write_text(page("All events",f'<h2>All events (SF only)</h2>{controls}{table(events)}',"all-events.html"))
flagged=(ROOT/"flagged_content.html").read_text()
(ROOT/"flagged.html").write_text(page("Flagged for Review",flagged,"flagged.html"))
method=(ROOT/"method_content.html").read_text()
(ROOT/"method.html").write_text(page("Method & Sources",method,"method.html"))
# CSV export
with open(ROOT/"data/events.csv","w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["name","type","category","when","location","cost","source_publisher","source_url"]); w.writeheader(); w.writerows(events)
print(f"Built {len(events)} events: {len(rec)} recurring, {len(ann)} annual/special, {len(cats)} categories")
