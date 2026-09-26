import os
import json
import re
import base64
import io
import shutil
import fitz
from PIL import Image
from playwright.sync_api import sync_playwright

base_img_dir = r"C:\Users\Jardin\OneDrive\Pictures\English"
web_index_path = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-british-homes-web\index.html"
standalone_path = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Standalone.html"
printable_html_path = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\pitch_dossier_printable.html"
pdf_out_path = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Location_Pitch_Complete.pdf"

def encode_img(subfolder, filename):
    full = os.path.join(base_img_dir, subfolder, filename)
    if not os.path.exists(full):
        print(f"Error: {full} does not exist!")
        return ""
    with Image.open(full) as im:
        im = im.convert("RGB")
        im.thumbnail((1200, 800), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=82)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

smh_locations = [
    {
        "id": "enchanted",
        "name": "Enchanted",
        "area": "Bishopscourt / Constantia, Cape Town",
        "style": "English Country Residence & Estate Lawn",
        "match_score": "97% Match",
        "tagline": "Elegant English country residence featuring high-ceilinged reception rooms, working fireplace hearth, classic white shaker kitchen, and a manicured private lawn with perimeter tree hedges.",
        "rate_shoot": "£2,100 / day (ZAR 47,250)",
        "rate_prep": "£1,050 / day (ZAR 23,625)",
        "availability": "Confirmed Open for March 2027 (Shoot My House Collection)",
        "restrictions": "Standard residential curfew (22:00 wrap); maximum 50 crew interior; shoe covers or floor protection on polished timber floors.",
        "parking": "Private paved driveway and courtyard for 6 technical vans; dedicated catering/unit base staging area within gates.",
        "filming_areas": "Main Living Room & Fireplace, Shaded Veranda Lounge, Country Kitchen & Island, Dining Terrace, Master Balcony Suite, Rear Party Lawn.",
        "living_summary": "Classic English country interior with deep neutral sofas, built-in white library shelving, working stone fireplace hearth, traditional shaker kitchen with range cooker, and French doors leading out to the veranda.",
        "living_features": [
            "Generous main lounge with built-in library bookcases and stone fireplace hearth",
            "Comfortable neutral sofa arrangement accommodating a group of 6–8 friends",
            "Double French doors delivering directional soft daylight and garden views",
            "Spacious white shaker country kitchen with large prep island and breakfast bar",
            "Master suite featuring French doors onto private balcony overlooking the grounds"
        ],
        "garden_summary": "Expansive flat rear garden party lawn completely framed by mature deciduous shade trees, flowering borders, and tall perimeter evergreen hedges. Features a shaded covered veranda terrace with outdoor dining and seating.",
        "garden_features": [
            "Level manicured lawn perfectly sized for dressed garden-party tracking shots",
            "Prominent mature shade tree providing natural soft dappled lighting",
            "High boundary evergreen hedges and perimeter walls ensuring 100% camera privacy",
            "Deep covered veranda terrace with teak dining table and modular outdoor lounge",
            "Direct interior-to-exterior flow for seamless camera dolly transitions"
        ],
        "folder": r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Enchanted\Enchanted",
        "hero": "Enchanted_1.jpg",
        "gallery": [
            {"file": "Enchanted_1.jpg", "cat": "living", "title": "Main Living Room — Fireplace & Built-In Library"},
            {"file": "Enchanted_2.jpg", "cat": "living", "title": "Lounge French Doors to Shaded Veranda"},
            {"file": "Enchanted_11.jpg", "cat": "living", "title": "Secondary Family TV Lounge"},
            {"file": "Enchanted_3.jpg", "cat": "living", "title": "Country Kitchen with Range Cooker & Island"},
            {"file": "Enchanted_4.jpg", "cat": "living", "title": "Kitchen Prep Counter & Garden Windows"},
            {"file": "Enchanted_5.jpg", "cat": "living", "title": "Entertaining Bar & Pass-Through to Veranda"},
            {"file": "Enchanted_8.jpg", "cat": "living", "title": "Master Suite with Mountain & Garden Balcony"},
            {"file": "Enchanted_25.jpg", "cat": "garden", "title": "Covered Veranda Dining & Outdoor Lounge"},
            {"file": "Enchanted_26.jpg", "cat": "garden", "title": "Veranda Terrace & Manicured Rear Lawn"},
            {"file": "Enchanted_27.jpg", "cat": "garden", "title": "Swimming Pool, Sunken Terrace & Manor Facade"},
            {"file": "Enchanted_28.jpg", "cat": "garden", "title": "Protected Pool Area & Established Tree Canopy"},
            {"file": "Enchanted_29.jpg", "cat": "garden", "title": "Expansive Garden-Party Lawn & Mature Shade Tree"},
            {"file": "Enchanted_30.jpg", "cat": "garden", "title": "Lawn Corridors with Layered Evergreen Hedging"},
            {"file": "Enchanted_31.jpg", "cat": "garden", "title": "Full Rear Manor Architecture & Rolling Lawn"},
            {"file": "Enchanted_32.jpg", "cat": "garden", "title": "Garden Play Zone & Perimeter Tree Boundary"}
        ],
        "gbp_shoot": "£2,100",
        "zar_shoot": "ZAR 47,250",
        "gbp_prep": "£1,050",
        "zar_prep": "ZAR 23,625",
        "base_zar": "ZAR 40,000"
    },
    {
        "id": "english-elegance",
        "name": "English Elegance",
        "area": "Constantia / Bishopscourt, Cape Town",
        "style": "English Country Farmhouse & Veranda",
        "match_score": "95% Match",
        "tagline": "Classic English farmhouse warmth, white pillar veranda, multi-pane sash French doors, tiered gardens, and a private sunken turf tennis court.",
        "rate_shoot": "£2,100 / day (ZAR 47,250)",
        "rate_prep": "£1,050 / day (ZAR 23,625)",
        "availability": "Confirmed Open for March 2027 (Shoot My House Collection)",
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
        "folder": r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - English Elegance\English Elegance",
        "hero": "English Elegance_1.jpg",
        "gallery": [
            {"file": "English Elegance_1.jpg", "cat": "exterior", "title": "White Pillar Veranda with Green Pergola"},
            {"file": "English Elegance_2.jpg", "cat": "garden", "title": "Rear Lawn, Swimming Pool & Manor Facade"},
            {"file": "English Elegance_20.jpg", "cat": "garden", "title": "Verdant Sunken Stone Garden Walkway"},
            {"file": "English Elegance_21.jpg", "cat": "garden", "title": "Tiered Lawn & Rose Terrace"},
            {"file": "English Elegance_22.jpg", "cat": "garden", "title": "Sunken Grass Tennis Court with Hedge Perimeter"},
            {"file": "English Elegance_23.jpg", "cat": "garden", "title": "Tennis Court & Boundary Foliage (Wide Angle)"},
            {"file": "English Elegance_4.jpg", "cat": "living", "title": "Grand English Dining Hall & Staircase Foyer"},
            {"file": "English Elegance_5.jpg", "cat": "living", "title": "Country Dining Room with Sash Window Alcove"},
            {"file": "English Elegance_7.jpg", "cat": "living", "title": "Farmhouse Kitchen with Shaker Cabinetry & Island"},
            {"file": "English Elegance_8.jpg", "cat": "living", "title": "Breakfast Nook Corner Booth Seating"},
            {"file": "English Elegance_10.jpg", "cat": "living", "title": "Warm Lived-In Lounge with Armchairs & Hearth"},
            {"file": "English Elegance_11.jpg", "cat": "living", "title": "Family Lounge with Soft Directional Daylight"},
            {"file": "English Elegance_3.jpg", "cat": "living", "title": "Attic Studio Lounge with Exposed White Rafters"},
            {"file": "English Elegance_16.jpg", "cat": "exterior", "title": "Paved Approach Driveway & Perimeter Hedges"},
            {"file": "English Elegance_17.jpg", "cat": "exterior", "title": "Gated Entrance & Tree-Lined Boundary"}
        ],
        "gbp_shoot": "£2,100",
        "zar_shoot": "ZAR 47,250",
        "gbp_prep": "£1,050",
        "zar_prep": "ZAR 23,625",
        "base_zar": "ZAR 40,000"
    },
    {
        "id": "solace-house",
        "name": "Solace House",
        "area": "Newlands / Rondebosch Heritage Belt, Cape Town",
        "style": "English Tudor / Arts & Crafts Cottage",
        "match_score": "96% Match",
        "tagline": "Authentic English cottage architecture with pitched dark shingle roof, arched brick entrance, long private walled lawn, and sheltered brick pool patio with pizza oven.",
        "rate_shoot": "£2,150 / day (ZAR 48,375)",
        "rate_prep": "£1,075 / day (ZAR 24,185)",
        "availability": "Confirmed Open for March 2027 (Shoot My House Collection)",
        "restrictions": "Standard residential curfew (22:00 wrap); maximum 45 crew interior; protective runners on interior timber flooring.",
        "parking": "Dedicated paved driveway for 4 technical vans; ample quiet residential street parking with traffic management.",
        "filming_areas": "Front Cottage Garden & Gate, Pitched Roof Facade, Long Rear Lawn & High Hedge, Covered Atrium Breezeway, Brick Pool Terrace, Pizza Oven Dining.",
        "living_summary": "Inviting cottage living spaces with exposed brickwork, multi-pane bay windows, covered glass atrium breezeway connecting wings, and cozy, authentic British residential atmosphere.",
        "living_features": [
            "Cozy friend-group living rooms with leaded sash and bay windows",
            "Covered glass atrium breezeway with arched brick doorway and courtyard feel",
            "Authentic British cottage architectural textures, exposed brick, and warm timber",
            "Direct French door access from interior living areas to the sheltered pool terrace",
            "Soft directional northern daylight filtering through mature garden greenery"
        ],
        "garden_summary": "Exceptional garden party and boundary environments featuring a long manicured flat lawn fully flanked by tall evergreen perimeter hedges, plus a brick-paved pool terrace with built-in wood-fired pizza oven and banquet dining table.",
        "garden_features": [
            "Long, level lawn corridor bordered by dense tall hedges — prime boundary fence location",
            "Covered outdoor entertaining terrace with rustic timber dining table and pizza oven",
            "Sheltered brick swimming pool terrace with sun loungers and mountain backdrop",
            "Picturesque front cottage garden pathway with picket fence and iron gate",
            "High degree of privacy with no overlooking neighboring buildings"
        ],
        "folder": r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Solace House\Solace House",
        "hero": "Solace House_1.jpg",
        "gallery": [
            {"file": "Solace House_1.jpg", "cat": "exterior", "title": "English Cottage Facade with Pitched Shingle Roof"},
            {"file": "Solace House_2.jpg", "cat": "garden", "title": "Long Manicured Lawn & High Evergreen Hedge Boundary"},
            {"file": "Solace House_3.jpg", "cat": "exterior", "title": "Rear Architecture, Brick Terrace & Bay Windows"},
            {"file": "Solace House_4.jpg", "cat": "garden", "title": "Lush Side Garden Path & Flowering Shrubbery"},
            {"file": "Solace House_5.jpg", "cat": "garden", "title": "Brick Patio & Pool Loungers Framed by Greenery"},
            {"file": "Solace House_6.jpg", "cat": "garden", "title": "Sheltered Brick Pool Terrace with Mountain Backdrop"},
            {"file": "Solace House_7.jpg", "cat": "garden", "title": "Turquoise Pool Set in Brickwork & Perimeter Hedge"},
            {"file": "Solace House_9.jpg", "cat": "garden", "title": "Covered Outdoor Entertaining Terrace & Dining"},
            {"file": "Solace House_10.jpg", "cat": "garden", "title": "Rustic Timber Banquet Table & Wood-Fired Pizza Oven"},
            {"file": "Solace House_11.jpg", "cat": "living", "title": "Covered Glass Atrium Breezeway & Arched Doorway"},
            {"file": "Solace House_12.jpg", "cat": "living", "title": "Glass-Roof Courtyard Lounge with Brick Paving"},
            {"file": "Solace House_13.jpg", "cat": "exterior", "title": "Cottage Garden Gateway with Dark Timber Pickets"},
            {"file": "Solace House_15.jpg", "cat": "garden", "title": "Outdoor Dining Staging Area Overlooking Pool"},
            {"file": "Solace House_17.jpg", "cat": "living", "title": "Warm Interior Living Space with Leaded Sash Windows"},
            {"file": "Solace House_20.jpg", "cat": "living", "title": "Cozy Friend-Group Cottage Lounge"}
        ],
        "gbp_shoot": "£2,150",
        "zar_shoot": "ZAR 48,375",
        "gbp_prep": "£1,075",
        "zar_prep": "ZAR 24,185",
        "base_zar": "ZAR 41,000"
    }
]

print("Encoding 45 curated images for the 3 Shoot My House locations...")
smh_images = {}
for loc in smh_locations:
    fld = loc["folder"]
    print(f" -> Encoding {loc['name']}...")
    for item in loc["gallery"]:
        fn = item["file"]
        key = f"{fld}/{fn}"
        if key not in smh_images:
            b64 = encode_img(fld, fn)
            if b64:
                smh_images[key] = b64

print(f"Total encoded images: {len(smh_images)}")

# Update index.html and standalone HTML
for target_html in [web_index_path, standalone_path]:
    if not os.path.exists(target_html):
        continue
    print(f"\nUpdating {os.path.basename(target_html)} to Shoot My House only...")
    with open(target_html, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace EMBEDDED_IMAGES
    m_imgs = re.search(r"const EMBEDDED_IMAGES = (\{.*?\});", content, re.DOTALL)
    if m_imgs:
        imgs_json = json.dumps(smh_images)
        content = content[:m_imgs.start()] + f"const EMBEDDED_IMAGES = {imgs_json};" + content[m_imgs.end():]
        print(" -> EMBEDDED_IMAGES replaced with SMH photos")

    # 2. Replace locations array
    m_locs = re.search(r"const locations = (\[.*?\]);\s*function getGoogleCalendarScoutUrl", content, re.DOTALL)
    if not m_locs:
        m_locs = re.search(r"const locations = (\[.*?\]);\s*let currentLocId", content, re.DOTALL)

    if m_locs:
        locs_json = json.dumps(smh_locations, indent=4)
        prefix = content[:m_locs.start()]
        suffix = content[m_locs.end() - len("function getGoogleCalendarScoutUrl"):] if "function getGoogleCalendarScoutUrl" in m_locs.group(0) else content[m_locs.end() - len("let currentLocId"):]
        content = prefix + f"const locations = {locs_json};\n\n        " + suffix
        print(" -> locations array updated with 3 SMH properties")

    # 3. Update copy to reflect 3 Shoot My House locations
    content = re.sub(r"\b9 Curated Heritage Locations\b", "3 New Shoot My House Locations", content)
    content = re.sub(r"\b6 Curated Heritage Locations\b", "3 New Shoot My House Locations", content)
    content = re.sub(r"\b9 Character Properties\b", "3 Curated Properties (Shoot My House)", content)
    content = re.sub(r"\b6 Character Properties\b", "3 Curated Properties (Shoot My House)", content)
    content = re.sub(r"\bAll 9 options\b", "All 3 new options", content)
    content = re.sub(r"\bAll 6 options\b", "All 3 new options", content)
    content = re.sub(r"\bAll 9 featured properties\b", "All 3 featured properties", content)
    content = re.sub(r"\bAll 6 featured properties\b", "All 3 featured properties", content)

    with open(target_html, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully saved {os.path.basename(target_html)}")

# Now generate the clean 12-page PDF
print("\nBuilding 12-page printable HTML dossier for Shoot My House...")
def get_img_src(folder, filename):
    key = f"{folder}/{filename}"
    return smh_images.get(key, "")

html_parts = []
html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>British Residential Homes & Gardens - Shoot My House Collection</title>
    <style>
        @page {
            size: A4 portrait;
            margin: 12mm 14mm 14mm 14mm;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        body {
            background-color: #0d1110;
            color: #f5f5f2;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 9.5pt;
            line-height: 1.45;
        }

        .pdf-page {
            page-break-after: always;
            break-after: page;
            height: 100%;
            min-height: 270mm;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding-bottom: 5mm;
        }

        .page-content {
            flex: 1;
        }

        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(197, 160, 89, 0.3);
            padding-bottom: 3mm;
            margin-bottom: 5mm;
        }
        .header-badge {
            font-size: 7.5pt;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: #dfb76c;
        }
        .header-sub {
            font-size: 7.5pt;
            color: #9ba6a1;
            letter-spacing: 0.5px;
        }

        .page-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 3mm;
            margin-top: 4mm;
            font-size: 7.5pt;
            color: #9ba6a1;
        }
        .footer-brand {
            font-weight: 600;
            letter-spacing: 1px;
            color: #c5a059;
        }

        .cover-hero {
            background: linear-gradient(145deg, #141a18 0%, #1f3d30 100%);
            border: 1px solid rgba(197, 160, 89, 0.4);
            border-radius: 8px;
            padding: 8mm 9mm;
            margin-bottom: 6mm;
        }
        .cover-eyebrow {
            font-size: 8pt;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #dfb76c;
            font-weight: 700;
            margin-bottom: 2mm;
        }
        .cover-title {
            font-family: Georgia, serif;
            font-size: 26pt;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.15;
            margin-bottom: 3mm;
        }
        .cover-subtitle {
            font-size: 9.5pt;
            color: #dce2de;
            line-height: 1.5;
            max-width: 95%;
        }

        .scope-pills {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 3mm;
            margin-bottom: 6mm;
        }
        .scope-pill {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            padding: 3mm 3.5mm;
        }
        .pill-label {
            font-size: 6.5pt;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #dfb76c;
            margin-bottom: 1mm;
        }
        .pill-val {
            font-size: 8.5pt;
            font-weight: 600;
            color: #ffffff;
        }

        .index-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 3.5mm;
        }
        .index-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            padding: 4mm 5mm;
            border-left: 4px solid #c5a059;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .index-num {
            font-size: 7.5pt;
            font-weight: 700;
            letter-spacing: 1px;
            color: #dfb76c;
            text-transform: uppercase;
            margin-bottom: 1mm;
        }
        .index-name {
            font-family: Georgia, serif;
            font-size: 13pt;
            font-weight: 700;
            color: #ffffff;
        }
        .index-meta {
            font-size: 8pt;
            color: #9ba6a1;
        }
        .index-rate-box {
            text-align: right;
        }
        .index-rate-lbl {
            font-size: 7pt;
            text-transform: uppercase;
            color: #9ba6a1;
        }
        .index-rate {
            font-size: 10pt;
            color: #6ee7b7;
            font-weight: 700;
        }

        .loc-hero-header {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            padding: 4mm 5mm;
            margin-bottom: 4mm;
        }
        .loc-meta-bar {
            display: flex;
            align-items: center;
            gap: 2.5mm;
            margin-bottom: 1.5mm;
            flex-wrap: wrap;
        }
        .badge {
            font-size: 7pt;
            font-weight: 600;
            padding: 1mm 2.5mm;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.06);
            color: #f5f5f2;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .badge-gold {
            background: rgba(197, 160, 89, 0.15);
            color: #dfb76c;
            border-color: rgba(197, 160, 89, 0.4);
        }
        .badge-green {
            background: rgba(46, 89, 70, 0.3);
            color: #6ee7b7;
            border-color: rgba(110, 231, 183, 0.4);
        }
        .loc-title {
            font-family: Georgia, serif;
            font-size: 19pt;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.2;
            margin-bottom: 1mm;
        }
        .loc-tagline {
            font-size: 9pt;
            color: #dce2de;
            line-height: 1.4;
            margin-bottom: 3mm;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2.5mm;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            padding-top: 2.5mm;
        }
        .metric-box {
            background: rgba(0, 0, 0, 0.35);
            border-radius: 5px;
            padding: 2mm 3mm;
            border: 1px solid rgba(255, 255, 255, 0.04);
        }
        .metric-lbl {
            font-size: 6.5pt;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: #9ba6a1;
            margin-bottom: 0.5mm;
        }
        .metric-val {
            font-size: 10pt;
            font-weight: 700;
            color: #dfb76c;
        }
        .metric-sub {
            font-size: 6.5pt;
            color: #9ba6a1;
        }

        .hero-photo-wrap {
            margin-bottom: 4mm;
            border-radius: 7px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            background: #000;
            height: 65mm;
        }
        .hero-photo-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .worlds-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3.5mm;
        }
        .world-box {
            background: #141a18;
            border-radius: 7px;
            padding: 3.5mm 4.5mm;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .world-box.living {
            border-left: 3px solid #dfb76c;
        }
        .world-box.garden {
            border-left: 3px solid #2ed573;
        }
        .world-head {
            display: flex;
            align-items: center;
            gap: 2mm;
            margin-bottom: 1.5mm;
        }
        .world-head h4 {
            font-family: Georgia, serif;
            font-size: 10.5pt;
            color: #ffffff;
        }
        .world-head span.sub {
            font-size: 7.5pt;
            color: #9ba6a1;
        }
        .world-desc {
            font-size: 8pt;
            color: #cfd5d1;
            line-height: 1.4;
            margin-bottom: 2mm;
        }
        .feature-ul {
            list-style: none;
            padding: 0;
        }
        .feature-ul li {
            font-size: 7.5pt;
            color: #e0e5e2;
            margin-bottom: 1mm;
            padding-left: 3.5mm;
            position: relative;
            line-height: 1.35;
        }
        .feature-ul li::before {
            content: "•";
            position: absolute;
            left: 0;
            color: #dfb76c;
            font-weight: 700;
        }

        .logistics-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3.5mm;
            margin-bottom: 4mm;
        }
        .log-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 7px;
            padding: 3.5mm 4.5mm;
        }
        .log-title {
            font-size: 8pt;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #dfb76c;
            margin-bottom: 2mm;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            padding-bottom: 1.5mm;
        }
        .log-item {
            display: flex;
            justify-content: space-between;
            font-size: 7.8pt;
            margin-bottom: 1.5mm;
            line-height: 1.35;
        }
        .log-item span.k {
            color: #9ba6a1;
            width: 40%;
        }
        .log-item span.v {
            color: #f5f5f2;
            font-weight: 500;
            width: 60%;
            text-align: right;
        }

        .highlights-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 3mm;
        }
        .hl-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            overflow: hidden;
        }
        .hl-photo {
            height: 38mm;
            background: #000;
        }
        .hl-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .hl-caption {
            padding: 2mm 3mm;
            font-size: 7.2pt;
            color: #cfd5d1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .gallery-grid-9 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 3mm;
        }
        .gallery-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            overflow: hidden;
        }
        .gallery-img-wrap {
            height: 48mm;
            background: #000;
        }
        .gallery-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .gallery-card-cap {
            padding: 1.5mm 2.5mm;
            font-size: 6.8pt;
            color: #dce2de;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: flex;
            justify-content: space-between;
        }

        .rate-card-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 8.5pt;
            margin-bottom: 4mm;
        }
        .rate-card-table th {
            background: rgba(197, 160, 89, 0.15);
            color: #dfb76c;
            text-align: left;
            padding: 2.5mm 3mm;
            font-size: 7.5pt;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            border-bottom: 1px solid #dfb76c;
        }
        .rate-card-table td {
            padding: 2.5mm 3mm;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            color: #e0e5e2;
        }

        .matrix-tbl {
            width: 100%;
            border-collapse: collapse;
            font-size: 8pt;
        }
        .matrix-tbl th {
            background: rgba(197, 160, 89, 0.15);
            color: #dfb76c;
            text-align: left;
            padding: 2.5mm 3mm;
            font-size: 7.5pt;
            text-transform: uppercase;
            border-bottom: 1px solid #dfb76c;
        }
        .matrix-tbl td {
            padding: 2.5mm 3mm;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            color: #dce2de;
            vertical-align: middle;
        }

        .cta-box {
            background: linear-gradient(145deg, #141a18 0%, #1f3d30 100%);
            border: 1px solid rgba(197, 160, 89, 0.4);
            border-radius: 8px;
            padding: 5mm 7mm;
            text-align: center;
            margin-top: 4mm;
        }
        .cta-box h3 {
            font-family: Georgia, serif;
            font-size: 14pt;
            color: #ffffff;
            margin-bottom: 1.5mm;
        }
        .cta-box p {
            font-size: 8.5pt;
            color: #dce2de;
            margin-bottom: 3mm;
        }
        .cta-email {
            display: inline-block;
            background: #c5a059;
            color: #0b0f0e;
            font-size: 9.5pt;
            font-weight: 700;
            padding: 2mm 5mm;
            border-radius: 5px;
            text-decoration: none;
        }
    </style>
</head>
<body>
""")

# Page 1: COVER
html_parts.append(f"""
<div class="pdf-page">
    <div class="page-content">
        <div class="page-header">
            <span class="header-badge">SALOCATIONS // CURATED LOCATION PRESENTATION</span>
            <span class="header-sub">MARCH 2027 PRODUCTION WINDOW</span>
        </div>

        <div class="cover-hero">
            <div class="cover-eyebrow">Production Scouting Dossier · Shoot My House Collection</div>
            <h1 class="cover-title">British Residential Homes & Gardens</h1>
            <p class="cover-subtitle">
                A fresh curated selection of 3 premier character properties from the Shoot My House archive
                (Bishopscourt, Constantia & Newlands Heritage Belt) that authentically replicate traditional
                British domestic architecture, lived-in friend-group lounges, and established garden party lawns.
            </p>
        </div>

        <div class="scope-pills">
            <div class="scope-pill">
                <div class="pill-label">Target Architecture</div>
                <div class="pill-val">English Manor / Farmhouse / Cottage</div>
            </div>
            <div class="scope-pill">
                <div class="pill-label">Interior Target</div>
                <div class="pill-val">Lived-In Friends Group Lounge</div>
            </div>
            <div class="scope-pill">
                <div class="pill-label">Exterior Target</div>
                <div class="pill-val">Garden Party Lawn & Fence</div>
            </div>
            <div class="scope-pill">
                <div class="pill-label">Shoot Window</div>
                <div class="pill-val">March 2027 (Confirmed Open)</div>
            </div>
        </div>

        <div style="margin-bottom: 3mm;">
            <h3 style="font-family: Georgia, serif; font-size: 12pt; color: #fff;">Today's New Location Options (Shoot My House Collection)</h3>
            <span style="font-size: 8pt; color: #9ba6a1;">All 3 options fully detailed with high-resolution photography, technical specs, and day rates</span>
        </div>

        <div class="index-grid">
""")

for idx, loc in enumerate(smh_locations):
    html_parts.append(f"""
            <div class="index-card">
                <div>
                    <div class="index-num">Option 0{idx+1} // {loc['match_score']}</div>
                    <div class="index-name">{loc['name']}</div>
                    <div class="index-meta">{loc['area']} · {loc['style']}</div>
                </div>
                <div class="index-rate-box">
                    <div class="index-rate-lbl">Indicative Shoot Rate</div>
                    <div class="index-rate">{loc['gbp_shoot']} <span style="font-size:7.5pt; color:#9ba6a1;">({loc['zar_shoot']})</span></div>
                </div>
            </div>
    """)

html_parts.append("""
        </div>
    </div>

    <div class="page-footer">
        <span class="footer-brand">SALOCATIONS // PROFESSIONAL LOCATION MANAGEMENT</span>
        <span>Direct Enquiries: jardin@salocations.com · Page 1</span>
    </div>
</div>
""")

# Detail pages for the 3 SMH locations (3 pages each)
page_num = 2
for idx, loc in enumerate(smh_locations):
    hero_img = get_img_src(loc['folder'], loc['hero'])
    gallery_items = loc.get('gallery', [])

    highlight_photos = gallery_items[:4]
    remaining_photos = gallery_items[4:13]

    # PAGE A
    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()}</span>
                <span class="header-sub">{loc['area']} · MARCH 2027</span>
            </div>

            <div class="loc-hero-header">
                <div class="loc-meta-bar">
                    <span class="badge badge-gold">{loc['style']}</span>
                    <span class="badge">📍 {loc['area']}</span>
                    <span class="badge badge-gold">{loc['match_score']}</span>
                    <span class="badge badge-green">✓ March 2027: Available</span>
                </div>
                <h2 class="loc-title">{loc['name']}</h2>
                <p class="loc-tagline">{loc['tagline']}</p>

                <div class="metrics-grid">
                    <div class="metric-box">
                        <div class="metric-lbl">Shoot Day (12h)</div>
                        <div class="metric-val">{loc['gbp_shoot']}</div>
                        <div class="metric-sub">{loc['zar_shoot']}</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-lbl">Prep / Strike (10h)</div>
                        <div class="metric-val">{loc['gbp_prep']}</div>
                        <div class="metric-sub">{loc['zar_prep']} (50%)</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-lbl">Scouting Package</div>
                        <div class="metric-val">ZAR 6,000</div>
                        <div class="metric-sub">~£266 (Scout + Vehicle)</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-lbl">March 2027 Status</div>
                        <div class="metric-val" style="color: #6ee7b7; font-size: 9pt;">Confirmed Open</div>
                        <div class="metric-sub">Shoot My House Collection</div>
                    </div>
                </div>
            </div>

            <div class="hero-photo-wrap">
                <img src="{hero_img}" alt="{loc['name']}">
            </div>

            <div class="worlds-container">
                <div class="world-box living">
                    <div class="world-head">
                        <span>🛋️</span>
                        <div>
                            <h4>World 1: Living Room / Lounge</h4>
                            <span class="sub">Friends Group · Character & Warmth</span>
                        </div>
                    </div>
                    <p class="world-desc">{loc['living_summary']}</p>
                    <ul class="feature-ul">
                        {''.join(f'<li>{f}</li>' for f in loc['living_features'])}
                    </ul>
                </div>

                <div class="world-box garden">
                    <div class="world-head">
                        <span>🌿</span>
                        <div>
                            <h4>World 2: Garden & Boundary</h4>
                            <span class="sub">Garden Party · Depth & Fence</span>
                        </div>
                    </div>
                    <p class="world-desc">{loc['garden_summary']}</p>
                    <ul class="feature-ul">
                        {''.join(f'<li>{f}</li>' for f in loc['garden_features'])}
                    </ul>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name'].upper()}</span>
            <span>Direct Film Enquiries: jardin@salocations.com · Page {page_num}</span>
        </div>
    </div>
    """)
    page_num += 1

    # PAGE B
    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()} - LOGISTICS & SPACES</span>
                <span class="header-sub">TECHNICAL PRODUCTION SPECIFICATIONS</span>
            </div>

            <div class="logistics-grid">
                <div class="log-card">
                    <div class="log-title">Unit Base & Parking Capacity</div>
                    <div class="log-item">
                        <span class="k">Technical Parking:</span>
                        <span class="v">{loc['parking']}</span>
                    </div>
                    <div class="log-item">
                        <span class="k">Generator Access:</span>
                        <span class="v">Street & on-site tie-in compliant</span>
                    </div>
                    <div class="log-item">
                        <span class="k">Unit Base Location:</span>
                        <span class="v">Dedicated staging area within 500m</span>
                    </div>
                    <div class="log-item">
                        <span class="k">Catering Setup:</span>
                        <span class="v">Shaded paved area on property</span>
                    </div>
                </div>

                <div class="log-card">
                    <div class="log-title">Filming Protocols & Daylight</div>
                    <div class="log-item">
                        <span class="k">Permit Lead Time:</span>
                        <span class="v">5–7 business days (City of Cape Town)</span>
                    </div>
                    <div class="log-item">
                        <span class="k">Restrictions:</span>
                        <span class="v">{loc['restrictions']}</span>
                    </div>
                    <div class="log-item">
                        <span class="k">Daylight Profile:</span>
                        <span class="v">High natural daylight orientation</span>
                    </div>
                    <div class="log-item">
                        <span class="k">Noise Curfew:</span>
                        <span class="v">22:00 residential standard wrap</span>
                    </div>
                </div>
            </div>

            <div style="margin-bottom: 2.5mm;">
                <h3 style="font-family: Georgia, serif; font-size: 11pt; color: #fff;">Featured Interior & Exterior Space Highlights</h3>
                <span style="font-size: 7.5pt; color: #9ba6a1;">Filming zones cleared and screened for camera tracks, lighting rigs, and crew flow</span>
            </div>

            <div class="highlights-grid">
    """)

    for photo in highlight_photos:
        p_img = get_img_src(loc['folder'], photo['file'])
        html_parts.append(f"""
                <div class="hl-card">
                    <div class="hl-photo">
                        <img src="{p_img}" alt="{photo.get('title', '')}">
                    </div>
                    <div class="hl-caption">
                        <strong>[{photo.get('cat', 'space').upper()}]</strong> {photo.get('title', loc['name'])}
                    </div>
                </div>
        """)

    html_parts.append(f"""
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name'].upper()}</span>
            <span>Production Office: +27 21 000 0000 · jardin@salocations.com · Page {page_num}</span>
        </div>
    </div>
    """)
    page_num += 1

    # PAGE C
    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()} - EXTENDED GALLERY</span>
                <span class="header-sub">HIGH-RESOLUTION ARCHITECTURAL PERSPECTIVES</span>
            </div>

            <div style="margin-bottom: 3mm;">
                <h3 style="font-family: Georgia, serif; font-size: 11pt; color: #fff;">Additional Scouting Angles & Spatial Details</h3>
                <span style="font-size: 7.5pt; color: #9ba6a1;">High-resolution curated angles illustrating authentic British texture and production versatility</span>
            </div>

            <div class="gallery-grid-9">
    """)

    for photo in remaining_photos:
        p_img = get_img_src(loc['folder'], photo['file'])
        html_parts.append(f"""
                <div class="gallery-card">
                    <div class="gallery-img-wrap">
                        <img src="{p_img}" alt="{photo.get('title', '')}">
                    </div>
                    <div class="gallery-card-cap">
                        <span>{photo.get('title', 'Detail')}</span>
                        <span style="color:#dfb76c; text-transform:uppercase;">{photo.get('cat', 'detail')}</span>
                    </div>
                </div>
        """)

    html_parts.append(f"""
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name'].upper()}</span>
            <span>Full Web Gallery: sal-british-homes.vercel.app · Page {page_num}</span>
        </div>
    </div>
    """)
    page_num += 1

# Rate Cards page
html_parts.append(f"""
<div class="pdf-page">
    <div class="page-content">
        <div class="page-header">
            <span class="header-badge">SALOCATIONS // PROFESSIONAL SERVICES</span>
            <span class="header-sub">LOCATION SCOUTING & MANAGEMENT RATE CARD</span>
        </div>

        <div style="margin-bottom: 4mm;">
            <h2 style="font-family: Georgia, serif; font-size: 17pt; color: #fff; margin-bottom: 1.5mm;">Location Scouting & Management Services</h2>
            <p style="font-size: 8.5pt; color: #9ba6a1;">
                Dedicated commercial & film production services for international producers, production designers,
                and directors shooting in Cape Town and the Western Cape.
            </p>
        </div>

        <table class="rate-card-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Service Package</th>
                    <th style="width: 20%;">Tariff (ZAR)</th>
                    <th style="width: 15%;">Indicative (GBP)</th>
                    <th style="width: 40%;">Scope of Services & Deliverables</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Location Scout Day Rate</strong></td>
                    <td><strong style="color: #dfb76c;">ZAR 5,000 / day</strong></td>
                    <td>~£222 / day</td>
                    <td>Full 10-hour scout day, landowner negotiations, preliminary photography package, access coordination.</td>
                </tr>
                <tr>
                    <td><strong>Scout Vehicle & Fuel</strong></td>
                    <td><strong style="color: #dfb76c;">ZAR 1,000 / day</strong></td>
                    <td>~£44 / day</td>
                    <td>4x4 production scout vehicle equipped with scouting equipment, GPS loggers, and fuel allowance.</td>
                </tr>
                <tr>
                    <td><strong>Combined Daily Package</strong></td>
                    <td><strong style="color: #dfb76c;">ZAR 6,000 / day</strong></td>
                    <td>~£266 / day</td>
                    <td>Scout + Vehicle + Fuel standard package. Standard rate for official scouting days and technical recces.</td>
                </tr>
                <tr>
                    <td><strong>Technical Recce Accompaniment</strong></td>
                    <td><strong style="color: #dfb76c;">ZAR 6,000 / day</strong></td>
                    <td>~£266 / day</td>
                    <td>Director & HOD technical recce navigation, municipal parking coordination, sound & daylight briefings.</td>
                </tr>
                <tr>
                    <td><strong>City Film Permit Facilitation</strong></td>
                    <td><strong style="color: #dfb76c;">ZAR 2,500 / permit</strong></td>
                    <td>~£111 / permit</td>
                    <td>Permit processing with City of Cape Town Film Permit Office, traffic management, SAPS & Metro Police sign-offs.</td>
                </tr>
            </tbody>
        </table>

        <div style="background: #141a18; border-radius: 7px; padding: 4mm 5mm; border: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 4mm;">
            <h4 style="font-family: Georgia, serif; font-size: 10pt; color: #dfb76c; margin-bottom: 2mm;">Film Permit Lead Times & Standard Working Conditions</h4>
            <ul class="feature-ul">
                <li><strong>Permit Lead Times:</strong> Standard residential Cape Town locations require 5 to 7 working days for municipal approval.</li>
                <li><strong>Shooting Hours:</strong> Standard residential hours: 07:00 to 22:00. Night filming permits require neighbor consent waivers.</li>
                <li><strong>Prep & Strike Tariff:</strong> Standard industry practice is 50% of the daily shoot tariff for prep and de-rig days.</li>
                <li><strong>Currency Conversion:</strong> Quoted rates converted at indicative benchmark of £1 ≈ ZAR 22.50. Exact invoices rendered in ZAR.</li>
            </ul>
        </div>
    </div>

    <div class="page-footer">
        <span class="footer-brand">SALOCATIONS // RATE CARD</span>
        <span>Direct Enquiries: jardin@salocations.com · Page {page_num}</span>
    </div>
</div>
""")
page_num += 1

# Matrix page
html_parts.append(f"""
<div class="pdf-page">
    <div class="page-content">
        <div class="page-header">
            <span class="header-badge">SALOCATIONS // BRIEF ALIGNMENT MATRIX</span>
            <span class="header-sub">SIDE-BY-SIDE PRODUCTION EVALUATION</span>
        </div>

        <div style="margin-bottom: 3.5mm;">
            <h2 style="font-family: Georgia, serif; font-size: 16pt; color: #fff; margin-bottom: 1.5mm;">Brief Alignment Comparison Matrix</h2>
            <p style="font-size: 8.5pt; color: #9ba6a1;">
                Side-by-side technical evaluation of the 3 Shoot My House character properties against the creative brief
                and March 2027 shooting schedule.
            </p>
        </div>

        <table class="matrix-tbl">
            <thead>
                <tr>
                    <th style="width: 20%;">Option & Area</th>
                    <th style="width: 18%;">British Style / Character</th>
                    <th style="width: 22%;">Living Room Suitability</th>
                    <th style="width: 20%;">Garden Party Lawn</th>
                    <th style="width: 10%;">Day Rate (12h)</th>
                    <th style="width: 10%;">March 2027</th>
                </tr>
            </thead>
            <tbody>
""")

for idx, loc in enumerate(smh_locations):
    html_parts.append(f"""
                <tr>
                    <td>
                        <strong style="color:#fff; font-size: 9pt;">{loc['name']}</strong><br>
                        <span style="color:#9ba6a1; font-size: 7.2pt;">Option 0{idx+1} · {loc['area']}</span>
                    </td>
                    <td><span class="badge badge-gold" style="font-size: 7pt;">{loc['style']}</span></td>
                    <td style="font-size: 7.8pt;">{loc['living_features'][0]}</td>
                    <td style="font-size: 7.8pt;">{loc['garden_features'][0]}</td>
                    <td>
                        <strong style="color:#dfb76c; font-size: 8.5pt;">{loc['gbp_shoot']}</strong><br>
                        <span style="color:#9ba6a1; font-size: 6.8pt;">{loc['zar_shoot']}</span>
                    </td>
                    <td><span style="color:#6ee7b7; font-weight:600; font-size: 7.5pt;">✓ Confirmed Open</span></td>
                </tr>
    """)

html_parts.append(f"""
            </tbody>
        </table>

        <div class="cta-box">
            <h3>Ready to Confirm or Scout These Locations?</h3>
            <p>
                We recommend placing a <strong>48-hour first option pencil</strong> on your preferred Shoot My House property
                to secure priority holds for the March 2027 shooting window.
            </p>
            <div style="font-size: 9pt; color: #dfb76c; font-weight: 600; margin-bottom: 2mm;">
                SALocations / Jardin Roestorff · Cape Town, South Africa
            </div>
            <a class="cta-email" href="mailto:jardin@salocations.com?subject=Shoot%20My%20House%20Brief%20-%20March%202027">
                Direct Film Enquiries: jardin@salocations.com
            </a>
        </div>
    </div>

    <div class="page-footer">
        <span class="footer-brand">SALOCATIONS // COMPARISON MATRIX</span>
        <span>Direct Enquiries: jardin@salocations.com · Page {page_num}</span>
    </div>
</div>
""")

html_parts.append("""
</body>
</html>
""")

full_html = "".join(html_parts)
print(f"Writing printable HTML to {printable_html_path} ({len(full_html)} bytes)...")
with open(printable_html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Rendering 12-page PDF via Playwright Chromium...")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file:///" + os.path.abspath(printable_html_path).replace("\\", "/"))
    page.wait_for_timeout(2000)
    page.pdf(
        path=pdf_out_path,
        format="A4",
        landscape=False,
        print_background=True,
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
    )
    browser.close()

print(f"Rendered PDF at {pdf_out_path} ({os.path.getsize(pdf_out_path)} bytes)")

# Verify with PyMuPDF
doc = fitz.open(pdf_out_path)
print(f"Total Pages in generated PDF: {len(doc)}")
for i, l in enumerate(smh_locations):
    name = l['name']
    pages = [p_idx + 1 for p_idx in range(len(doc)) if name.lower() in doc[p_idx].get_text().lower()]
    print(f"  Option 0{i+1}: {name} -> pages {pages}")

# Copy to destinations
dests = [
    r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\British_Residential_Homes_Location_Pitch.pdf",
    r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\British_Residential_Homes_Location_Pitch.pdf"
]
for d in dests:
    shutil.copy2(pdf_out_path, d)
    print(f"Copied to {d}")

print("\nAll tasks completed successfully!")
