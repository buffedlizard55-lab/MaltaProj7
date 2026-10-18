#!/usr/bin/env python3
"""Add verified free upcoming SF events found in the Z2 coverage pass (arena/83fc57b1-maltaproj7)."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "events.json"
doc = json.loads(DATA.read_text(encoding="utf-8"))
events = doc["events"]
flags = doc["flags"]
existing_ids = {e["id"] for e in events}
SESSION = "arena/83fc57b1-maltaproj7"
TODAY_STR = "2026-10-18"

def add_event(e):
    if e["id"] in existing_ids:
        print(f"skip (exists): {e['id']}"); return
    events.append(e); existing_ids.add(e["id"])
    print(f"add: {e['id']}  ({e.get('start_date')}, {e.get('category')})")

def add_flag(flag_id, event_id, issue, disposition):
    for f in flags:
        if f.get("flag_id") == flag_id:
            print(f"skip flag (exists): {flag_id}"); return
    flags.append({
        "flag_id": flag_id, "event_id": event_id,
        "event": next((ev["name"] for ev in events if ev["id"] == event_id), event_id),
        "issue": issue, "disposition": disposition,
        "added_by": SESSION, "added": TODAY_STR,
    })
    print(f"add flag: {flag_id}")

add_event({
    "id": "daytona-oracle-ai-builders-sf-2026-10-20",
    "name": "Daytona & Oracle AI Builders — SF, October 2026",
    "bucket": "special", "cadence": "single-date",
    "category": "Technology, AI & gaming",
    "date_text": "Tuesday, October 20, 2026",
    "start_date": "2026-10-20", "end_date": "2026-10-20",
    "time_text": "5:30–8:00 p.m.",
    "location": "San Francisco (address released to approved registrants)",
    "organizer": "Daytona (event partner: Oracle)",
    "admission": "Free (registration and host approval required)",
    "admission_source_url": "https://luma.com/ai-builders-sf-oct",
    "source_url": "https://www.daytona.io/events",
    "source_label": "Daytona official events listing (daytona.io/events)",
    "source_authority": "Official organizer",
    "status": "verified", "review_reason": "",
    "notes": "Added 2026-10-18. Daytona's official events page lists 'Daytona & Oracle AI Builders - SF, October 2026' as a meetup in San Francisco on Oct 20, 2026. The official Luma registration lists price 0 USD (General Admission, free), 5:30–8:00 PM PDT, 'Approval Required', 'Register to See Address'."
})
add_flag("flag-daytona-ai-builders-address-hidden", "daytona-oracle-ai-builders-sf-2026-10-20",
    "Daytona's official Luma registration hides the exact SF address until attendee approval ('Register to See Address'). Daytona.io lists only 'San Francisco, United States'.",
    "Recorded with city-only location; venue will update when Daytona publishes an address.")

add_event({
    "id": "overmind-arcade-osai-week-2026-10-20",
    "name": "Overmind Arcade (Open Source AI Week)",
    "bucket": "special", "cadence": "single-date",
    "category": "Technology, AI & gaming",
    "date_text": "Tuesday, October 20, 2026",
    "start_date": "2026-10-20", "end_date": "2026-10-20",
    "time_text": "6:00 p.m.",
    "location": "Joey the Cat's Arcade, 3252 19th Street, San Francisco",
    "organizer": "Open Source AI Week (hosted by Tyler Edwards)",
    "admission": "",
    "source_url": "https://opensourceaiweek.com/#calendar",
    "source_label": "Open Source AI Week official calendar (opensourceaiweek.com)",
    "source_authority": "Official organizer",
    "status": "verified", "review_reason": "",
    "notes": "Added 2026-10-18. The official Open Source AI Week calendar lists Overmind Arcade at 'Oct 20, 2026 · 6:00 PM · Joey the Cat's Arcade, San Francisco' with description 'Open source has always been a multiplayer game — for one night it's literal.' The calendar does not publish a ticket price; the linked Luma listing shows 'Approval Required' with no price tier, so admission is left blank."
})
add_flag("flag-overmind-arcade-cost", "overmind-arcade-osai-week-2026-10-20",
    "Open Source AI Week's official calendar lists Overmind Arcade but does not state a ticket price; the linked Luma listing shows Approval Required with no price tier.",
    "Leave admission blank; treat as cost-not-stated until OSAI Week publishes pricing.")

add_event({
    "id": "sf-diwali-festival-yerba-buena-gardens-2026",
    "name": "San Francisco Diwali Festival at Yerba Buena Gardens",
    "bucket": "special", "cadence": "single-date",
    "category": "Community & culture",
    "date_text": "Sunday, November 8, 2026",
    "start_date": "2026-11-08", "end_date": "2026-11-08",
    "time_text": "1:00–5:00 p.m.",
    "location": "Yerba Buena Gardens (750 Howard Street), San Francisco",
    "organizer": "Yerba Buena Gardens Conservancy (in partnership with Creative Collective SF)",
    "admission": "Free (RSVP encouraged)",
    "source_url": "https://www.eventbrite.com/e/san-francisco-diwali-festival-sunday-nov-8-tickets-1996184565772",
    "source_label": "Yerba Buena Gardens Special Events — SF Diwali Festival official Eventbrite",
    "source_authority": "Official venue",
    "admission_source_url": "https://www.eventbrite.com/e/san-francisco-diwali-festival-sunday-nov-8-tickets-1996184565772",
    "status": "verified", "review_reason": "",
    "notes": "Added 2026-10-18. Organizer's official Eventbrite, hosted by Yerba Buena Gardens Special Events, states Sunday November 8, 1-5 PM, Yerba Buena Gardens, 750 Howard Street, with performers Alam Khan, Raaga School of Music, Rang De Bollywood, DJ Mumbai Rani, and The Dhol King. Free (RSVP encouraged)."
})

add_event({
    "id": "noisebridge-godot-gamedev-meetup",
    "name": "Godot Gamedev Meetup at Noisebridge",
    "bucket": "recurring", "cadence": "monthly",
    "category": "Technology, AI & gaming",
    "date_text": "Third Saturday monthly, 2:00–6:00 p.m.",
    "start_date": "", "end_date": "",
    "time_text": "2:00–6:00 p.m.",
    "location": "Noisebridge Hackerspace, 272 Capp Street, San Francisco",
    "organizer": "Noisebridge Hackerspace (Bay Area Godot Meetup)",
    "admission": "Free (donations to Noisebridge welcome)",
    "source_url": "https://www.noisebridge.net/wiki/Category:Global_Game_Jam",
    "source_label": "Noisebridge wiki — game dev / Godot programs (Games Guild, Godot Meetup 3rd Saturday)",
    "source_authority": "Official venue",
    "admission_source_url": "https://www.noisebridge.net/wiki/GDC_2026_IndieSmash",
    "status": "verified", "review_reason": "",
    "notes": "Added 2026-10-18. Noisebridge wiki lists 'Godot Meetup 3rd Saturday' as a recurring free program; GDC_2026_IndieSmash page says 'Cost: Free, donate to Noisebridge welcome.' No single dated 2026 session published on an official page, so dated fields are blank."
})

add_event({
    "id": "voxel51-physical-ai-workshop-sf-2026-10-28",
    "name": "San Francisco Physical AI Workshop and Meetup (Voxel51 × Nebius)",
    "bucket": "special", "cadence": "single-date",
    "category": "Technology, AI & gaming",
    "date_text": "Wednesday, October 28, 2026",
    "start_date": "2026-10-28", "end_date": "2026-10-28",
    "time_text": "5:30–8:30 p.m.",
    "location": "Antler San Francisco (3rd Floor), 144 Townsend Street, San Francisco",
    "organizer": "Voxel51 (co-presented with Nebius)",
    "admission": "",
    "source_url": "https://voxel51.com/events/san-francisco-physical-ai-workshop-and-meetup-october-28-2026",
    "source_label": "Voxel51 official event page — San Francisco Physical AI Workshop & Meetup",
    "source_authority": "Official organizer",
    "status": "verified", "review_reason": "",
    "notes": "Added 2026-10-18. Voxel51's event page lists Oct 28, 2026, 5:30-8:30 PM PDT at Antler San Francisco, 144 Townsend St, with networking/food/drinks, hands-on FiftyOne workshop and lightning talks. The page does not state a price; the linked Eventbrite also does not list a price tier, so admission is left blank."
})
add_flag("flag-voxel51-physical-ai-cost", "voxel51-physical-ai-workshop-sf-2026-10-28",
    "Voxel51's official event page does not state a ticket price; the Eventbrite registration shows 'Get tickets' but no tier price.",
    "Leave admission blank; re-check Voxel51 and Eventbrite for pricing before marking as free.")

add_flag("flag-no-confirmed-free-dated-gaming-oct-dec-2026", "",
    "As of 2026-10-18, no San Francisco gaming event with both a confirmed free-admission statement AND a confirmed upcoming single date in Oct-Dec 2026 was found on an official organizer page.",
    "Re-run coverage search as new events are announced.")
add_flag("flag-ybfestival-november-programs-tba", "",
    "Yerba Buena Gardens Festival press materials state 'November programs to be announced'; ybgfestival.org is behind reCAPTCHA as of 2026-10-18.",
    "Re-verify ybgfestival.org in November.")

doc["events"] = events
doc["flags"] = flags
DATA.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Wrote {len(events)} events, {len(flags)} flags to {DATA}")
