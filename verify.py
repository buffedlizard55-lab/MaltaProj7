#!/usr/bin/env python3
import json, pathlib, re, sys
ROOT=pathlib.Path(__file__).parent
events=json.loads((ROOT/"data/events.json").read_text())
errs=[]
for i,e in enumerate(events):
    for k in ("name","type","category","source_url","source_publisher"):
        if not e.get(k): errs.append(f"row {i} missing {k}")
    if not e["source_url"].startswith("https://"): errs.append(f"row {i} bad url")
    if any(x in e["name"] for x in ("Super Bowl","Mill Valley")): errs.append(f"excluded event present: {e['name']}")
pages=["index.html","recurring.html","annual-special.html","all-events.html","flagged.html","method.html"]
for p in pages:
    t=(ROOT/p).read_text()
    for href in re.findall(r'href="([^"#]+)"',t):
        if href.startswith("http"): continue
        if not (ROOT/href).exists(): errs.append(f"{p}: broken internal link {href}")
    if "Official source" not in t and p not in ("flagged.html","method.html"): errs.append(f"{p}: no source links")
print(f"rows={len(events)} recurring={sum(e['type']=='Recurring' for e in events)} annual={sum(e['type']!='Recurring' for e in events)} blank_cost={sum(not e.get('cost') for e in events)} blank_location={sum(not e.get('location') for e in events)} blank_when={sum(not e.get('when') for e in events)}")
print("ERRORS:" if errs else "ALL CHECKS PASSED", *errs, sep="\n")
sys.exit(1 if errs else 0)
