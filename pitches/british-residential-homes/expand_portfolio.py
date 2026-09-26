import os
import json
import re
import base64
import io
from PIL import Image

base_img_dir = r"C:\Users\Jardin\OneDrive\Pictures\English"
web_index_path = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-british-homes-web\index.html"
standalone_path = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Standalone.html"

def encode_img(rel_path):
    full = os.path.join(base_img_dir, rel_path)
    if not os.path.exists(full):
        print(f"Warning: File {full} not found!")
        return ""
    with Image.open(full) as im:
        im = im.convert("RGB")
        im.thumbnail((1200, 800), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=82)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

# Define the 3 new locations
new_locations = [
    {
        "id": "english-elegance",
        "name": "English Elegance",
        "area": "Constantia / Bishopscourt, Cape Town",
        "style": "English Country Farmhouse & Veranda",
        "match_score": "95% Match",
        "tagline": "Classic English farmhouse warmth, white pillar veranda, multi-pane sash French doors, tiered gardens, and a private sunken turf tennis court.",
        "rate_shoot": "£2,100 / day (ZAR 47,250)",
        "rate_prep": "£1,050 / day (ZAR 23,625)",
        "availability": "Confirmed Open for March 2027 (Filming Experienced Owner)",
        "restrictions": "Standard residential curfew (22:00 wrap); maximum 50 crew interior; soft-sole shoes or protection on heritage timber floors.",
        "parking": "Long private paved driveway accommodates 5 technical vans; secure turning circle inside gates; crew basecamp on paved apron.",
        "filming_areas": "Pergola Veranda, Grandfather Staircase Foyer, Formal Dining Room, Shaker Kitchen, Breakfast Booth, Living Lounge, Sunken Tennis Court, Pool Lawn.",
        "living_summary": "Authentic British country interior with warm timber flooring, grandfather staircase hall, country shaker kitchen with butcher-block island, breakfast corner booth, and comfortable lived-in family lounge.",
        "living_features": [
            "Formal English dining room with grandfather staircase and chandeliers",
            "Farmhouse shaker kitchen with wooden butcher-block island and breakfast booth",
            "Warm family lounge with deep armchairs, rugs, and soft directional daylight",
            "High ceilings with exposed white rafters in upper attic studio",
            "Multiple French doors offering seamless interior-to-exterior tracking"
        ],
        "garden_summary": "Extensive mature English country gardens featuring a deep covered veranda with green-trimmed pergola, tiered stone garden stairways, swimming pool in flat lawn, and a private sunken turf tennis court surrounded by perimeter hedging.",
        "garden_features": [
            "Traditional white-column veranda with green pergola and wicker garden chairs",
            "Private sunken grass tennis court surrounded by mature hedges and fencing",
            "Level manicured lawn space ideal for British garden-party dressing",
            "Multi-tiered stone steps and rose borders providing cinematic depth of field",
            "Fully enclosed private boundary with automated security gates"
        ],
        "folder": "English-Elegance",
        "hero": "SMH_English-Elegance_Image1.jpg",
        "gallery": [
            {"file": "SMH_English-Elegance_Image1.jpg", "cat": "exterior", "title": "Pergola Veranda with Green Trim & French Doors"},
            {"file": "English-Elegance_SMH_Image1.jpg", "cat": "exterior", "title": "Paved Approach Driveway & Perimeter Hedges"},
            {"file": "English-Elegance_SMH_Image2.jpg", "cat": "exterior", "title": "Gated Entrance & Tree-Lined Boundary"},
            {"file": "SMH_English-Elegance_Image2.jpg", "cat": "garden", "title": "Rear Lawn, Swimming Pool & Manor Facade"},
            {"file": "SMH_English-Elegance_Image20.jpg", "cat": "garden", "title": "Verdant Sunken Stone Garden Walkway"},
            {"file": "SMH_English-Elegance_Image21.jpg", "cat": "garden", "title": "Tiered Lawn & Rose Terrace"},
            {"file": "SMH_English-Elegance_Image22.jpg", "cat": "garden", "title": "Sunken Grass Tennis Court with Hedge Perimeter"},
            {"file": "SMH_English-Elegance_Image23.jpg", "cat": "garden", "title": "Tennis Court & Boundary Foliage (Wide Shot)"},
            {"file": "SMH_English-Elegance_Image4.jpg", "cat": "living", "title": "Grand English Dining Hall & Staircase Foyer"},
            {"file": "SMH_English-Elegance_Image5.jpg", "cat": "living", "title": "Country Dining Room with Sash Window Alcove"},
            {"file": "SMH_English-Elegance_Image7.jpg", "cat": "living", "title": "Farmhouse Kitchen with Shaker Cabinetry & Island"},
            {"file": "SMH_English-Elegance_Image8.jpg", "cat": "living", "title": "Breakfast Nook Corner Booth Seating"},
            {"file": "SMH_English-Elegance_Image10.jpg", "cat": "living", "title": "Warm Lived-In Lounge with Armchairs & Hearth"},
            {"file": "SMH_English-Elegance_Image11.jpg", "cat": "living", "title": "Family Lounge & Directional Garden Daylight"},
            {"file": "SMH_English-Elegance_Image3.jpg", "cat": "living", "title": "Attic Studio Lounge with Exposed White Rafters"}
        ],
        "gbp_shoot": "£2,100",
        "zar_shoot": "ZAR 47,250",
        "gbp_prep": "£1,050",
        "zar_prep": "ZAR 23,625",
        "base_zar": "ZAR 40,000"
    },
    {
        "id": "villa-ten",
        "name": "Villa Ten (#10)",
        "area": "Upper Constantia, Cape Town",
        "style": "Traditional Painted Brick English Manor",
        "match_score": "94% Match",
        "tagline": "Private gated estate featuring white painted brick architecture, expansive flat rear lawn bordered by mature trees, and a glass conservatory sunroom.",
        "rate_shoot": "£2,250 / day (ZAR 50,625)",
        "rate_prep": "£1,125 / day (ZAR 25,310)",
        "availability": "Confirmed Open for March 2027 (Filming Welcomed)",
        "restrictions": "Standard residential curfew (22:00 wrap); max 55 crew interior; protective mats on wide-plank oak flooring.",
        "parking": "Expansive paved forecourt and double garage parking for 6 technical vehicles; dedicated street staging.",
        "filming_areas": "Gated Driveway, Front Courtyard, Foyer & Gallery Staircase, 12-Seater Dining Hall, Skylit Chef Kitchen, Sunroom Conservatory, Rear Party Lawn.",
        "living_summary": "Magnificent open-plan entertaining wing with wide oak floorboards, giant 12-seater country dining table, skylit chef's kitchen with navy butcher island, and a separate glass-enclosed conservatory sunroom opening directly onto the pool lawn.",
        "living_features": [
            "Grand 12-seater country timber dining table in expansive open-plan hall",
            "Lived-in deep modular sofa seating area with garden sash windows",
            "Chef's kitchen with overhead atrium skylight and dark blue timber island",
            "Glass conservatory sunroom lounge with wicker furniture and pool views",
            "Double-height entrance foyer with open gallery staircase"
        ],
        "garden_summary": "Vast flat rear lawn fully enclosed by mature forest trees and private brick boundary walls, complete with a brick pool apron, shaded umbrella dining, and complete visual seclusion from neighbors.",
        "garden_features": [
            "Expansive, perfectly level lawn ideal for full-scale garden-party scenes",
            "Dense perimeter tree canopy of mature pines and oaks creating British estate feel",
            "Brick-paved pool terrace with direct access from glass conservatory",
            "Numbered entrance gate pillars and grand private approach driveway",
            "Paved turnaround courtyard ideal for technical vehicles and catering"
        ],
        "folder": "# 10",
        "hero": "#10 (1).jpg",
        "gallery": [
            {"file": "#10 (1).jpg", "cat": "exterior", "title": "Gated Manor Entrance & White Brick Pillars"},
            {"file": "#10 (2).jpg", "cat": "exterior", "title": "Sweeping Paved Driveway & Mature Oak Trees"},
            {"file": "#10 (3).jpg", "cat": "exterior", "title": "Front Turnaround Courtyard & Double Garages"},
            {"file": "#10 (41).jpg", "cat": "exterior", "title": "Painted Brick Manor Facade from Front Grounds"},
            {"file": "#10 (10).jpg", "cat": "garden", "title": "Expansive Garden-Party Lawn & Swimming Pool"},
            {"file": "#10 (11).jpg", "cat": "garden", "title": "Rear Lawn with Mature Forest Boundary Trees"},
            {"file": "#10 (12).jpg", "cat": "garden", "title": "Brick Terrace & Rear Manor Architecture"},
            {"file": "#10 (14).jpg", "cat": "garden", "title": "Private Garden Lawn & Boundary Wall"},
            {"file": "#10 (15).jpg", "cat": "living", "title": "Glass Sunroom & Conservatory Lounge"},
            {"file": "#10 (26).jpg", "cat": "living", "title": "Conservatory Glass Doors to Garden & Pool"},
            {"file": "#10 (16).jpg", "cat": "living", "title": "Grand Open-Plan Reception & 12-Seater Dining Hall"},
            {"file": "#10 (17).jpg", "cat": "living", "title": "Lived-In Modular Lounge with Garden Sash Windows"},
            {"file": "#10 (18).jpg", "cat": "living", "title": "Expansive Living Hall & Country Timber Dining"},
            {"file": "#10 (20).jpg", "cat": "living", "title": "Skylit Chef's Kitchen with Navy Butcher Island"},
            {"file": "#10 (21).jpg", "cat": "living", "title": "Kitchen Atrium Skylight & Cabinetry"},
            {"file": "#10 (28).jpg", "cat": "living", "title": "Grand Foyer & Double-Height Staircase Hall"}
        ],
        "gbp_shoot": "£2,250",
        "zar_shoot": "ZAR 50,625",
        "gbp_prep": "£1,125",
        "zar_prep": "ZAR 25,310",
        "base_zar": "ZAR 42,000"
    },
    {
        "id": "arumbrook",
        "name": "Arumbrook Estate",
        "area": "Constantia Valley / Hout Bay, Cape Town",
        "style": "Cape-English Country Manor & Orchard",
        "match_score": "92% Match",
        "tagline": "Idyllic country residence approached via a long tree-lined driveway, featuring white-beamed banquet dining, stone hearth, and manicured topiary grounds.",
        "rate_shoot": "£2,000 / day (ZAR 45,000)",
        "rate_prep": "£1,000 / day (ZAR 22,500)",
        "availability": "Confirmed Open for March 2027 (Filming Welcomed)",
        "restrictions": "Standard residential curfew (22:00 wrap); max 45 crew interior; protected sound zone (low ambient noise).",
        "parking": "Long driveway approach with separate vehicle staging; spacious turnaround courtyard for technical trucks.",
        "filming_areas": "Tree-Lined Driveway, Manor Facade, Great Banquet Hall, Stone Fireplace, Island Kitchen, Crittall Partition Room, Orchard Lawns.",
        "living_summary": "Atmospheric great hall dining and lounge featuring exposed white-beamed ceilings, large multi-pane windows, black stone fireplace hearth, open island kitchen, and Crittall-style glass double doors connecting formal living spaces.",
        "living_features": [
            "Exposed white-beamed ceilings with authentic country timber chandeliers",
            "Feature black stone fireplace hearth providing warm focal point",
            "Chef's island kitchen with marble countertops and breakfast bar seating",
            "Multi-pane garden windows offering directional soft daylight",
            "Crittall-style glass partition doors dividing dining and lounge areas"
        ],
        "garden_summary": "Picture-perfect country grounds featuring a long tree-lined orchard driveway, manicured topiary hedges, mature fruit trees, and an English double-dormer manor facade.",
        "garden_features": [
            "Extensive tree-lined gravel driveway providing dramatic camera tracking approach",
            "Manicured topiary balls, layered evergreen hedges, and boundary walls",
            "Quiet country atmosphere with zero road traffic noise interference",
            "Classic English country manor facade with double roof dormers and upper terrace",
            "Wide lawn corridors framed by established deciduous trees"
        ],
        "folder": "Arumbrook",
        "hero": "Arumbrook (1).jpg",
        "gallery": [
            {"file": "Arumbrook (1).jpg", "cat": "exterior", "title": "Tree-Lined Country Orchard Driveway"},
            {"file": "Arumbrook (11).jpg", "cat": "exterior", "title": "Approaching Country Lane with Manicured Hedges"},
            {"file": "Arumbrook (13).jpg", "cat": "exterior", "title": "Orchard Grounds & Private Perimeter Boundary"},
            {"file": "Arumbrook (15).jpg", "cat": "exterior", "title": "Country Manor Facade with Double Dormer Windows"},
            {"file": "Arumbrook (16).jpg", "cat": "exterior", "title": "Manor Courtyard & Turnaround Staging"},
            {"file": "Arumbrook (2).jpg", "cat": "living", "title": "Grand Banquet Hall with White-Beamed Ceilings"},
            {"file": "Arumbrook (3).jpg", "cat": "living", "title": "Black Stone Hearth Fireplace & Dining Setup"},
            {"file": "Arumbrook (4).jpg", "cat": "living", "title": "Banquet Hall Looking onto Garden Grounds"},
            {"file": "Arumbrook (6).jpg", "cat": "living", "title": "Open Country Kitchen with Island & Breakfast Bar"},
            {"file": "Arumbrook (7).jpg", "cat": "living", "title": "Kitchen Marble Countertops & Warm Lighting"},
            {"file": "Arumbrook (8).jpg", "cat": "living", "title": "Kitchen Prep Station & Garden Windows"},
            {"file": "Arumbrook (9).jpg", "cat": "living", "title": "Crittall Glass Partition Doors & Reception Room"},
            {"file": "Arumbrook (10).jpg", "cat": "living", "title": "Private Study & Secondary Living Space"},
            {"file": "Arumbrook (20).jpg", "cat": "living", "title": "Formal Reception Room with French Doors"}
        ],
        "gbp_shoot": "£2,000",
        "zar_shoot": "ZAR 45,000",
        "gbp_prep": "£1,000",
        "zar_prep": "ZAR 22,500",
        "base_zar": "ZAR 38,000"
    }
]

print("Encoding new images...")
new_images = {}
for loc in new_locations:
    fld = loc["folder"]
    print(f"Encoding images for {loc['name']} ({fld})...")
    for g in loc["gallery"]:
        fn = g["file"]
        rel = f"{fld}/{fn}"
        if rel not in new_images:
            b64 = encode_img(rel)
            if b64:
                new_images[rel] = b64
    # Ensure hero is encoded
    hero_rel = f"{fld}/{loc['hero']}"
    if hero_rel not in new_images:
        b64 = encode_img(hero_rel)
        if b64:
            new_images[hero_rel] = b64

print(f"Total new images encoded: {len(new_images)}")

# Update files
for target_html in [web_index_path, standalone_path]:
    if not os.path.exists(target_html):
        print(f"File not found: {target_html}")
        continue
    
    print(f"\nUpdating {os.path.basename(target_html)}...")
    with open(target_html, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update EMBEDDED_IMAGES
    m_imgs = re.search(r"const EMBEDDED_IMAGES = (\{.*?\});", content, re.DOTALL)
    if m_imgs:
        existing_imgs = json.loads(m_imgs.group(1))
        existing_imgs.update(new_images)
        imgs_json = json.dumps(existing_imgs)
        content = content[:m_imgs.start()] + f"const EMBEDDED_IMAGES = {imgs_json};" + content[m_imgs.end():]
        print(" -> Updated EMBEDDED_IMAGES with 3 new locations")

    # 2. Update locations array
    m_locs = re.search(r"const locations = (\[.*?\]);\s*function getGoogleCalendarScoutUrl", content, re.DOTALL)
    if not m_locs:
        # Check without helper function
        m_locs = re.search(r"const locations = (\[.*?\]);\s*let currentLocId", content, re.DOTALL)

    if m_locs:
        existing_locs = json.loads(m_locs.group(1))
        # Keep existing 6, check if any of the new ones already present
        existing_ids = {l["id"] for l in existing_locs}
        for nl in new_locations:
            if nl["id"] not in existing_ids:
                existing_locs.append(nl)
        
        locs_json = json.dumps(existing_locs, indent=4)
        prefix = content[:m_locs.start()]
        suffix = content[m_locs.end() - len("function getGoogleCalendarScoutUrl"):] if "function getGoogleCalendarScoutUrl" in m_locs.group(0) else content[m_locs.end() - len("let currentLocId"):]
        content = prefix + f"const locations = {locs_json};\n\n        " + suffix
        print(f" -> Updated locations array to {len(existing_locs)} locations")

    # 3. Update brief scope text from 6 to 9 options
    content = content.replace("6 Curated Heritage Locations", "9 Curated Heritage Locations")
    content = content.replace("6 Character Properties", "9 Character Properties")
    content = content.replace("6 residential properties", "9 residential properties")
    content = content.replace("6 options", "9 options")

    with open(target_html, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully saved {os.path.basename(target_html)}")

print("\nPortfolio expansion completed successfully!")
