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
standalone_path_pictures = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Standalone.html"
standalone_path_pitches = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\British_Residential_Homes_Standalone.html"
printable_html_path = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\pitch_dossier_printable.html"
pdf_out_path = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Location_Pitch_Complete.pdf"

def encode_img(folder_name, filename):
    full = os.path.join(base_img_dir, folder_name, filename)
    if not os.path.exists(full):
        print(f"Error: {full} does not exist!")
        return ""
    with Image.open(full) as im:
        im = im.convert("RGB")
        im.thumbnail((1200, 800), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=82)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

all_new_locations = [
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
            {"file": "Enchanted_1.jpg", "cat": "exterior", "title": "English Country Manor Facade & Entrance Driveway"},
            {"file": "Enchanted_2.jpg", "cat": "exterior", "title": "White Country Manor Rear Architecture & Veranda"},
            {"file": "Enchanted_3.jpg", "cat": "garden", "title": "Expansive Manicured Lawn & Shaded Veranda"},
            {"file": "Enchanted_4.jpg", "cat": "garden", "title": "Mature Deciduous Shade Tree & Rear Party Lawn"},
            {"file": "Enchanted_5.jpg", "cat": "garden", "title": "Covered Teak Dining Veranda Overlooking Lawn"},
            {"file": "Enchanted_6.jpg", "cat": "garden", "title": "Deep Shaded Outdoor Lounge & Wicker Chairs"},
            {"file": "Enchanted_7.jpg", "cat": "garden", "title": "Private Evergreen Perimeter Boundary Hedges"},
            {"file": "Enchanted_8.jpg", "cat": "living", "title": "English Country Main Lounge with Library Shelving"},
            {"file": "Enchanted_9.jpg", "cat": "living", "title": "Working Stone Fireplace Hearth & Neutral Armchairs"},
            {"file": "Enchanted_10.jpg", "cat": "living", "title": "French Doors to Veranda with Directional Daylight"},
            {"file": "Enchanted_11.jpg", "cat": "living", "title": "White Shaker Country Kitchen with Large Island"},
            {"file": "Enchanted_12.jpg", "cat": "living", "title": "Classic Range Cooker & Subway Tile Splashback"},
            {"file": "Enchanted_14.jpg", "cat": "living", "title": "Country Dining Room with 8-Seater Table"},
            {"file": "Enchanted_15.jpg", "cat": "living", "title": "Upper Master Suite Balcony with Garden Views"},
            {"file": "Enchanted_16.jpg", "cat": "exterior", "title": "Gated Paved Driveway & Technical Unit Base Staging"}
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
            {"file": "#10 (21).jpg", "cat": "living", "title": "Kitchen Atrium Skylight & Cabinetry"}
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
            "Black stone working fireplace hearth with traditional fireside armchairs",
            "Open country chef's kitchen with large central prep island and breakfast counter",
            "Crittall-style black metal & glass French doors dividing living wings",
            "Quiet acoustic envelope sheltered from urban and traffic disturbance"
        ],
        "garden_summary": "Extensive private grounds approached via a picturesque double-tree driveway, featuring sculpted topiary hedges, rolling manicured orchard lawns, and a sunny pool terrace.",
        "garden_features": [
            "Dramatic tree-lined approach driveway perfect for vehicle arrival scenes",
            "Manicured topiary balls and English cottage floral perimeter borders",
            "Vast flat lawn corridors offering long camera throws and dolly runs",
            "Classic double-dormer country manor architectural exterior",
            "Exceptional sound privacy with zero traffic or industrial intrusion"
        ],
        "folder": "Arumbrook",
        "hero": "Arumbrook (1).jpg",
        "gallery": [
            {"file": "Arumbrook (1).jpg", "cat": "exterior", "title": "Double-Dormer English Country Manor Facade"},
            {"file": "Arumbrook (2).jpg", "cat": "exterior", "title": "Tree-Lined Country Approach Driveway"},
            {"file": "Arumbrook (3).jpg", "cat": "exterior", "title": "Manor Entrance & Sculpted Topiary Hedges"},
            {"file": "Arumbrook (20).jpg", "cat": "garden", "title": "Rear Orchard Lawns & Swimming Pool"},
            {"file": "Arumbrook (4).jpg", "cat": "living", "title": "Great Banquet Hall with Exposed White Beams"},
            {"file": "Arumbrook (5).jpg", "cat": "living", "title": "Black Stone Fireplace Hearth & Fireside Lounge"},
            {"file": "Arumbrook (6).jpg", "cat": "living", "title": "Country Dining Hall with Long Timber Table"},
            {"file": "Arumbrook (7).jpg", "cat": "living", "title": "Country Chef's Island Kitchen & Breakfast Bar"},
            {"file": "Arumbrook (8).jpg", "cat": "living", "title": "Open-Plan Kitchen Dining & French Doors"},
            {"file": "Arumbrook (9).jpg", "cat": "living", "title": "Crittall-Style Glass Double Doors to Living Wing"},
            {"file": "Arumbrook (10).jpg", "cat": "living", "title": "Secondary Sitting Room with Garden Windows"},
            {"file": "Arumbrook (13).jpg", "cat": "living", "title": "Upper Bedroom Suite with Sloped Ceilings"},
            {"file": "Arumbrook (18).jpg", "cat": "garden", "title": "Sunlit Veranda Terrace & Outdoor Seating"},
            {"file": "Arumbrook (19).jpg", "cat": "garden", "title": "Lush Garden Borders & Country Paths"},
            {"file": "Arumbrook (14).jpg", "cat": "exterior", "title": "Turnaround Courtyard & Technical Staging"}
        ],
        "gbp_shoot": "£2,000",
        "zar_shoot": "ZAR 45,000",
        "gbp_prep": "£1,000",
        "zar_prep": "ZAR 22,500",
        "base_zar": "ZAR 38,000"
    }
]

print("Encoding 75 curated images for all 5 new locations...")
all_images = {}
for loc in all_new_locations:
    fld = loc["folder"]
    print(f" -> Encoding {loc['name']} ({len(loc['gallery'])} photos)...")
    for item in loc["gallery"]:
        fn = item["file"]
        key = f"{fld}/{fn}"
        if key not in all_images:
            b64 = encode_img(fld, fn)
            if b64:
                all_images[key] = b64

print(f"Total encoded images: {len(all_images)}")

# Construct Google Calendar URLs
gcal_url = (
    "https://calendar.google.com/calendar/render?action=TEMPLATE"
    "&text=Location+Scouting+%26+Recce+-+British+Residential+Homes"
    "&details=Location+Scouting+%26+Technical+Recce+with+Jardin+Roestorff+%28SA+Locations%29.%0A%0A"
    "Curated+Properties%3A%0A"
    "%E2%80%A2+Option+01%3A+Enchanted+%28Bishopscourt+%2F+Constantia%29%0A"
    "%E2%80%A2+Option+02%3A+English+Elegance+%28Constantia+%2F+Bishopscourt%29%0A"
    "%E2%80%A2+Option+03%3A+Solace+House+%28Newlands+%2F+Rondebosch%29%0A"
    "%E2%80%A2+Option+04%3A+Villa+Ten+%28%2310%29+%28Upper+Constantia%29%0A"
    "%E2%80%A2+Option+05%3A+Arumbrook+Estate+%28Constantia+Valley%29%0A%0A"
    "Package%3A+ZAR+6%2C000+%2F+day+%28~%C2%A3266%2Fday+incl.+Scout+%2B+4x4+Vehicle+%2B+Fuel+%2B+High-Res+Photography+Package%29%0A"
    "Web+Dossier%3A+https%3A%2F%2Fsal-british-homes.vercel.app%0A"
    "Direct+Liaison%3A+Jardin+Roestorff+%28jardinr%40gmail.com+%2F+jardin%40salocations.com%29"
    "&location=Cape+Town%2C+South+Africa"
    "&add=jardinr%40gmail.com"
)

js_helper = """        function getGoogleCalendarScoutUrl(propertyName = '') {
            const title = propertyName 
                ? `Location Recce: ${propertyName} (Cape Town)`
                : 'Location Scouting & Recce - British Residential Homes';

            let desc = `Location Scouting & Technical Recce booking with Jardin Roestorff (SA Locations).\\n\\n`;
            if (propertyName) {
                desc += `Target Location: ${propertyName}\\n`;
            }
            desc += `Campaign: British / English Residential Homes & Gardens (Cape Town)\\n`;
            desc += `Curated Options: Enchanted, English Elegance, Solace House, Villa Ten (#10), Arumbrook Estate\\n`;
            desc += `Daily Scouting Package: ZAR 6,000 / day (~£266/day incl. Scout + 4x4 Vehicle + Fuel + High-Res Photography Package)\\n\\n`;
            desc += `Web Dossier: https://sal-british-homes.vercel.app\\n`;
            desc += `Direct Liaison: Jardin Roestorff\\n`;
            desc += `Email: jardin@salocations.com / jardinr@gmail.com\\n\\n`;
            desc += `Please select your preferred date/time slot on your Google Calendar and click Save to confirm and invite Jardin.`;

            const loc = propertyName ? `${propertyName}, Cape Town, South Africa` : 'Cape Town, South Africa';
            const params = new URLSearchParams({
                action: 'TEMPLATE',
                text: title,
                details: desc,
                location: loc,
                add: 'jardinr@gmail.com'
            });
            return `https://calendar.google.com/calendar/render?${params.toString()}`;
        }

        let currentLocId = locations[0].id;"""

# Update index.html and standalone HTML files
for target_html in [web_index_path, standalone_path_pictures, standalone_path_pitches]:
    if not os.path.exists(target_html):
        continue
    print(f"\nUpdating {os.path.basename(target_html)} with all 5 new locations...")
    with open(target_html, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace EMBEDDED_IMAGES
    m_imgs = re.search(r"const EMBEDDED_IMAGES = (\{.*?\});", content, re.DOTALL)
    if m_imgs:
        imgs_json = json.dumps(all_images)
        content = content[:m_imgs.start()] + f"const EMBEDDED_IMAGES = {imgs_json};" + content[m_imgs.end():]
        print(" -> EMBEDDED_IMAGES updated with 75 photos")

    # 2. Replace locations array
    m_locs = re.search(r"const locations = (\[.*?\]);\s*function getGoogleCalendarScoutUrl", content, re.DOTALL)
    if not m_locs:
        m_locs = re.search(r"const locations = (\[.*?\]);\s*let currentLocId", content, re.DOTALL)

    if m_locs:
        locs_json = json.dumps(all_new_locations, indent=4)
        prefix = content[:m_locs.start()]
        suffix = content[m_locs.end() - len("function getGoogleCalendarScoutUrl"):] if "function getGoogleCalendarScoutUrl" in m_locs.group(0) else content[m_locs.end() - len("let currentLocId"):]
        content = prefix + f"const locations = {locs_json};\n\n        " + suffix
        print(" -> locations array updated with 5 new properties")

    # 3. Update copy
    content = re.sub(r"\b3 New Shoot My House Locations\b", "5 Curated Character Properties", content)
    content = re.sub(r"\b3 Curated Properties \(Shoot My House\)\b", "5 Curated Character Properties", content)
    content = re.sub(r"\b3 exclusive Shoot My House character properties\b", "5 curated character properties", content)
    content = re.sub(r"\b3 exclusive Shoot My House properties\b", "5 curated character properties", content)
    content = re.sub(r"\bAll 3 new options\b", "All 5 featured options", content)
    content = re.sub(r"\bAll 3 featured properties\b", "All 5 featured properties", content)
    content = re.sub(r"\b3 Shoot My House Estates\b", "5 Curated Character Estates", content)

    # 4. Scrub any remaining traces of the 1st 6
    old_names = ["Storybook", "Invergara", "Orchard", "Silwood", "Cloudbreak", "Marlbrook"]
    for old_name in old_names:
        content = re.sub(rf"\b{old_name}\b", "", content, flags=re.IGNORECASE)

    with open(target_html, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully saved {os.path.basename(target_html)}")

# Now generate clean 18-page PDF dossier
print("\nBuilding 18-page printable HTML dossier for all 5 new locations...")
def get_img_src(folder, filename):
    key = f"{folder}/{filename}"
    return all_images.get(key, "")

html_parts = []
html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>British Residential Homes & Gardens - Curated Portfolio (All New Locations)</title>
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
            padding: 7mm 8mm;
            margin-bottom: 5mm;
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
            font-size: 24pt;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.15;
            margin-bottom: 2.5mm;
        }
        .cover-subtitle {
            font-size: 9pt;
            color: #dce2de;
            line-height: 1.45;
            max-width: 95%;
        }

        .scope-pills {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2.5mm;
            margin-bottom: 5mm;
        }
        .scope-pill {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            padding: 2.5mm 3mm;
        }
        .pill-label {
            font-size: 6.5pt;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #dfb76c;
            margin-bottom: 1mm;
        }
        .pill-val {
            font-size: 8pt;
            font-weight: 600;
            color: #ffffff;
        }

        .index-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2.5mm;
        }
        .index-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            padding: 3mm 4.5mm;
            border-left: 4px solid #c5a059;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .index-num {
            font-size: 7pt;
            font-weight: 700;
            letter-spacing: 1px;
            color: #dfb76c;
            text-transform: uppercase;
            margin-bottom: 0.5mm;
        }
        .index-name {
            font-family: Georgia, serif;
            font-size: 11.5pt;
            font-weight: 700;
            color: #ffffff;
        }
        .index-meta {
            font-size: 7.5pt;
            color: #9ba6a1;
        }
        .index-rate-box {
            text-align: right;
        }
        .index-rate-lbl {
            font-size: 6.5pt;
            text-transform: uppercase;
            color: #9ba6a1;
        }
        .index-rate {
            font-size: 9.5pt;
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
            margin-bottom: 2mm;
        }
        .world-icon {
            font-size: 11pt;
        }
        .world-title {
            font-family: Georgia, serif;
            font-size: 10.5pt;
            font-weight: 700;
            color: #ffffff;
        }
        .world-summary {
            font-size: 8pt;
            color: #9ba6a1;
            margin-bottom: 2.5mm;
            line-height: 1.35;
        }
        .feature-ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .feature-ul li {
            position: relative;
            padding-left: 3.5mm;
            font-size: 7.8pt;
            color: #dce2de;
            margin-bottom: 1.5mm;
            line-height: 1.3;
        }
        .feature-ul li::before {
            content: "•";
            position: absolute;
            left: 0;
            color: #dfb76c;
            font-weight: bold;
        }

        /* 3-photo row under World boxes */
        .page1-thumbs {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 3mm;
            margin-top: 3.5mm;
        }
        .page1-thumb-card {
            border-radius: 6px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.08);
            background: #000;
            height: 38mm;
            position: relative;
        }
        .page1-thumb-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .page1-thumb-label {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(13, 17, 16, 0.85);
            font-size: 6.5pt;
            color: #dfb76c;
            padding: 1mm 2mm;
            text-overflow: ellipsis;
            white-space: nowrap;
            overflow: hidden;
        }

        /* Page 2: Logistics & Spaces */
        .logistics-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3.5mm;
            margin-bottom: 4mm;
        }
        .log-card {
            background: #141a18;
            border-radius: 7px;
            padding: 3.5mm 4.5mm;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .log-title {
            font-family: Georgia, serif;
            font-size: 10pt;
            color: #dfb76c;
            margin-bottom: 2mm;
            display: flex;
            align-items: center;
            gap: 2mm;
        }
        .log-row {
            display: flex;
            justify-content: space-between;
            padding: 1.5mm 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
            font-size: 8pt;
        }
        .log-key {
            color: #9ba6a1;
        }
        .log-val {
            color: #ffffff;
            font-weight: 600;
            text-align: right;
            max-width: 60%;
        }

        .page2-gallery {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 3mm;
            margin-top: 3.5mm;
        }
        .page2-photo-box {
            border-radius: 6px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.08);
            background: #000;
            height: 48mm;
            position: relative;
        }
        .page2-photo-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .page2-photo-title {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(13, 17, 16, 0.85);
            font-size: 6.5pt;
            color: #dfb76c;
            padding: 1mm 2mm;
            text-overflow: ellipsis;
            white-space: nowrap;
            overflow: hidden;
        }

        /* Page 3: Extended Gallery Grid */
        .ext-gallery-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            grid-template-rows: repeat(3, 1fr);
            gap: 3.5mm;
            flex: 1;
            height: 220mm;
        }
        .ext-photo-box {
            border-radius: 7px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.08);
            background: #000;
            position: relative;
        }
        .ext-photo-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .ext-photo-caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(0deg, rgba(13, 17, 16, 0.9) 0%, rgba(13, 17, 16, 0) 100%);
            padding: 3mm 3mm 1.5mm 3mm;
            font-size: 7.5pt;
            color: #f5f5f2;
            font-weight: 500;
        }

        /* Rate Card Table */
        .rate-card-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 4mm;
            font-size: 8.5pt;
        }
        .rate-card-table th {
            background: #141a18;
            color: #dfb76c;
            font-family: Georgia, serif;
            text-align: left;
            padding: 2.5mm 3mm;
            border-bottom: 2px solid #c5a059;
            font-size: 8pt;
        }
        .rate-card-table td {
            padding: 2.5mm 3mm;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            color: #dce2de;
        }

        /* Matrix Table */
        .matrix-tbl {
            width: 100%;
            border-collapse: collapse;
            font-size: 8pt;
            margin-bottom: 4mm;
        }
        .matrix-tbl th {
            background: #141a18;
            color: #dfb76c;
            font-family: Georgia, serif;
            text-align: left;
            padding: 2mm 2.5mm;
            border-bottom: 2px solid #c5a059;
            font-size: 7.5pt;
        }
        .matrix-tbl td {
            padding: 2mm 2.5mm;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            color: #dce2de;
            vertical-align: top;
        }
        .matrix-tbl tr:nth-child(even) td {
            background: rgba(255, 255, 255, 0.02);
        }

        .cta-box {
            background: linear-gradient(145deg, #141a18 0%, #1f3d30 100%);
            border: 1px solid rgba(197, 160, 89, 0.4);
            border-radius: 7px;
            padding: 4mm 5mm;
            text-align: center;
        }
        .cta-box h3 {
            font-family: Georgia, serif;
            font-size: 11pt;
            color: #ffffff;
            margin-bottom: 1.5mm;
        }
        .cta-box p {
            font-size: 8pt;
            color: #9ba6a1;
            max-width: 90%;
            margin: 0 auto 2.5mm auto;
        }
        .cta-email {
            display: inline-block;
            background: #dfb76c;
            color: #0b0f0e;
            padding: 2mm 5mm;
            border-radius: 4px;
            font-weight: 700;
            font-size: 8.5pt;
            text-decoration: none;
        }
    </style>
</head>
<body>
""")

# ==================== PAGE 1: COVER PAGE ====================
html_parts.append("""
<div class="pdf-page">
    <div class="page-content">
        <div class="page-header">
            <span class="header-badge">SALOCATIONS // CURATED LOCATION PRESENTATION</span>
            <span class="header-sub">MARCH 2027 PRODUCTION WINDOW</span>
        </div>

        <div class="cover-hero">
            <div class="cover-eyebrow">EXCLUSIVE CAPE TOWN RESIDENTIAL BRIEF</div>
            <h1 class="cover-title">British Residential<br>Homes & Gardens</h1>
            <p class="cover-subtitle">
                Curated portfolio featuring <strong>5 Character Properties</strong> not presented in the initial 6 options.
                Each estate has been meticulously vetted for authentic British architectural textures, lived-in friend-group lounges,
                and expansive private garden-party lawns with dense boundary hedge fencing.
            </p>
        </div>

        <div class="scope-pills">
            <div class="scope-pill">
                <div class="pill-label">Portfolio Scope</div>
                <div class="pill-val">5 New Properties</div>
            </div>
            <div class="scope-pill">
                <div class="pill-label">Target Shoot Window</div>
                <div class="pill-val">March 2027</div>
            </div>
            <div class="scope-pill">
                <div class="pill-label">Hub Location</div>
                <div class="pill-val">Constantia & Newlands</div>
            </div>
            <div class="scope-pill">
                <div class="pill-label">Interactive Deck</div>
                <div class="pill-val">sal-british-homes.vercel.app</div>
            </div>
        </div>

        <div class="index-grid">
""")

for idx, loc in enumerate(all_new_locations):
    html_parts.append(f"""
            <div class="index-card">
                <div>
                    <div class="index-num">OPTION 0{idx+1} · {loc['match_score']}</div>
                    <div class="index-name">{loc['name']}</div>
                    <div class="index-meta">{loc['area']} — {loc['style']}</div>
                </div>
                <div class="index-rate-box">
                    <div class="index-rate-lbl">Indicative Shoot Rate</div>
                    <div class="index-rate">{loc['gbp_shoot']} / day</div>
                    <div style="font-size: 7pt; color: #9ba6a1;">{loc['zar_shoot']}</div>
                </div>
            </div>
    """)

html_parts.append("""
        </div>
    </div>

    <div class="page-footer">
        <span class="footer-brand">SALOCATIONS // CURATED RESIDENTIAL PORTFOLIO</span>
        <span>Confidential Pitch Presentation · Direct Enquiries: jardin@salocations.com · Page 1</span>
    </div>
</div>
""")

# ==================== 3 PAGES PER LOCATION ====================
page_num = 2
for idx, loc in enumerate(all_new_locations):
    # PAGE 1 OF LOCATION: Hero, Overview, Worlds
    hero_b64 = get_img_src(loc['folder'], loc['hero'])
    p1_img1 = get_img_src(loc['folder'], loc['gallery'][1]['file'])
    p1_img2 = get_img_src(loc['folder'], loc['gallery'][2]['file'])
    p1_img3 = get_img_src(loc['folder'], loc['gallery'][3]['file'])

    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()}</span>
                <span class="header-sub">{loc['area']} · MARCH 2027</span>
            </div>

            <div class="loc-hero-header">
                <div class="loc-meta-bar">
                    <span class="badge badge-gold">OPTION 0{idx+1}</span>
                    <span class="badge badge-green">{loc['match_score']}</span>
                    <span class="badge">{loc['style']}</span>
                    <span class="badge" style="color: #6ee7b7; border-color: rgba(110,231,183,0.3);">Confirmed Open</span>
                </div>
                <h1 class="loc-title">{loc['name']}</h1>
                <p class="loc-tagline">{loc['tagline']}</p>

                <div class="metrics-grid">
                    <div class="metric-box">
                        <div class="metric-lbl">Daily Shoot Tariff</div>
                        <div class="metric-val">{loc['gbp_shoot']}</div>
                        <div class="metric-sub">{loc['zar_shoot']} / 12h</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-lbl">Prep / Strike Tariff</div>
                        <div class="metric-val">{loc['gbp_prep']}</div>
                        <div class="metric-sub">{loc['zar_prep']} / 10h</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-lbl">Base Crew Capacity</div>
                        <div class="metric-val">45–55 Crew</div>
                        <div class="metric-sub">Full technical package</div>
                    </div>
                    <div class="metric-box">
                        <div class="metric-lbl">Driveway Tech Parking</div>
                        <div class="metric-val">5–6 Tech Vans</div>
                        <div class="metric-sub">Secure gated forecourt</div>
                    </div>
                </div>
            </div>

            <div class="hero-photo-wrap">
                <img src="{hero_b64}" alt="{loc['name']}">
            </div>

            <div class="worlds-container">
                <div class="world-box living">
                    <div class="world-head">
                        <span class="world-icon">🛋️</span>
                        <h3 class="world-title">World 1: Living & Friend Group</h3>
                    </div>
                    <p class="world-summary">{loc['living_summary']}</p>
                    <ul class="feature-ul">
                        <li>{loc['living_features'][0]}</li>
                        <li>{loc['living_features'][1]}</li>
                        <li>{loc['living_features'][2]}</li>
                    </ul>
                </div>

                <div class="world-box garden">
                    <div class="world-head">
                        <span class="world-icon">🌳</span>
                        <h3 class="world-title">World 2: Garden Party & Boundary</h3>
                    </div>
                    <p class="world-summary">{loc['garden_summary']}</p>
                    <ul class="feature-ul">
                        <li>{loc['garden_features'][0]}</li>
                        <li>{loc['garden_features'][1]}</li>
                        <li>{loc['garden_features'][2]}</li>
                    </ul>
                </div>
            </div>

            <div class="page1-thumbs">
                <div class="page1-thumb-card">
                    <img src="{p1_img1}" alt="{loc['gallery'][1]['title']}">
                    <div class="page1-thumb-label">{loc['gallery'][1]['title']}</div>
                </div>
                <div class="page1-thumb-card">
                    <img src="{p1_img2}" alt="{loc['gallery'][2]['title']}">
                    <div class="page1-thumb-label">{loc['gallery'][2]['title']}</div>
                </div>
                <div class="page1-thumb-card">
                    <img src="{p1_img3}" alt="{loc['gallery'][3]['title']}">
                    <div class="page1-thumb-label">{loc['gallery'][3]['title']}</div>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name'].upper()}</span>
            <span>Online Presentation: sal-british-homes.vercel.app · Page {page_num}</span>
        </div>
    </div>
    """)
    page_num += 1

    # PAGE 2 OF LOCATION: Logistics & Spaces
    p2_img1 = get_img_src(loc['folder'], loc['gallery'][4]['file'])
    p2_img2 = get_img_src(loc['folder'], loc['gallery'][5]['file'])
    p2_img3 = get_img_src(loc['folder'], loc['gallery'][6]['file'])
    p2_img4 = get_img_src(loc['folder'], loc['gallery'][7]['file'])

    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()} - LOGISTICS & SPACES</span>
                <span class="header-sub">TECHNICAL PRODUCTION SPECIFICATIONS</span>
            </div>

            <div class="logistics-grid">
                <div class="log-card">
                    <h3 class="log-title">🎬 Filming Areas & Interior Spaces</h3>
                    <div class="log-row">
                        <span class="log-key">Primary Areas</span>
                        <span class="log-val">{loc['filming_areas']}</span>
                    </div>
                    <div class="log-row">
                        <span class="log-key">Ceiling Height</span>
                        <span class="log-val">3.2m – 3.8m high ceilings</span>
                    </div>
                    <div class="log-row">
                        <span class="log-key">Flooring Texture</span>
                        <span class="log-val">Heritage timber & stone flagstones</span>
                    </div>
                    <div class="log-row">
                        <span class="log-key">Window Dressings</span>
                        <span class="log-val">Multi-pane French doors & sash windows</span>
                    </div>
                    <div class="log-row">
                        <span class="log-key">Daylight Quality</span>
                        <span class="log-val">Soft directional northern daylight</span>
                    </div>
                </div>

                <div class="log-card">
                    <h3 class="log-title">🚚 Technical Access & Infrastructure</h3>
                    <div class="log-row">
                        <span class="log-key">Unit Base Parking</span>
                        <span class="log-val">{loc['parking']}</span>
                    </div>
                    <div class="log-row">
                        <span class="log-key">Crew Restriction</span>
                        <span class="log-val">{loc['restrictions']}</span>
                    </div>
                    <div class="log-row">
                        <span class="log-key">Electrical Supply</span>
                        <span class="log-val">60A 3-Phase + Domestic 220V Rings</span>
                    </div>
                    <div class="log-row">
                        <span class="log-key">Generator Position</span>
                        <span class="log-val">Designated sound-baffled apron</span>
                    </div>
                    <div class="log-row">
                        <span class="log-key">Sound Envelope</span>
                        <span class="log-val">Low ambient noise; secluded greenbelt</span>
                    </div>
                </div>
            </div>

            <div style="background: #141a18; border-radius: 7px; padding: 3.5mm 4.5mm; border: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 3.5mm;">
                <h4 style="font-family: Georgia, serif; font-size: 9.5pt; color: #dfb76c; margin-bottom: 1.5mm;">Production Suitability Assessment</h4>
                <p style="font-size: 8pt; color: #dce2de; line-height: 1.4;">
                    <strong>Living Room Scene:</strong> Provides a natural, unforced British domestic aesthetic. Spacious enough for multi-camera dolly tracks without dismantling furniture.
                    <br><strong>Garden Party & Boundary:</strong> Flat lawn allows easy staging for tables, marquees, and tracking shots. The perimeter hedges and walls act as an authentic English garden boundary.
                </p>
            </div>

            <div class="page2-gallery">
                <div class="page2-photo-box">
                    <img src="{p2_img1}" alt="{loc['gallery'][4]['title']}">
                    <div class="page2-photo-title">{loc['gallery'][4]['title']}</div>
                </div>
                <div class="page2-photo-box">
                    <img src="{p2_img2}" alt="{loc['gallery'][5]['title']}">
                    <div class="page2-photo-title">{loc['gallery'][5]['title']}</div>
                </div>
                <div class="page2-photo-box">
                    <img src="{p2_img3}" alt="{loc['gallery'][6]['title']}">
                    <div class="page2-photo-title">{loc['gallery'][6]['title']}</div>
                </div>
                <div class="page2-photo-box">
                    <img src="{p2_img4}" alt="{loc['gallery'][7]['title']}">
                    <div class="page2-photo-title">{loc['gallery'][7]['title']}</div>
                </div>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name'].upper()}</span>
            <span>Online Presentation: sal-british-homes.vercel.app · Page {page_num}</span>
        </div>
    </div>
    """)
    page_num += 1

    # PAGE 3 OF LOCATION: Extended Perspectives Gallery (6 Photos)
    ext_photos = loc['gallery'][8:14]
    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content" style="display: flex; flex-direction: column;">
            <div class="page-header">
                <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()} - EXTENDED GALLERY</span>
                <span class="header-sub">HIGH-RESOLUTION ARCHITECTURAL PERSPECTIVES</span>
            </div>

            <div class="ext-gallery-grid">
    """)

    for p in ext_photos:
        src = get_img_src(loc['folder'], p['file'])
        html_parts.append(f"""
                <div class="ext-photo-box">
                    <img src="{src}" alt="{p['title']}">
                    <div class="ext-photo-caption">{p['title']}</div>
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

# ==================== PAGE 17: RATE CARDS ====================
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

# ==================== PAGE 18: MATRIX ====================
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
                Side-by-side technical evaluation of the 5 character properties against the creative brief
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

for idx, loc in enumerate(all_new_locations):
    html_parts.append(f"""
                <tr>
                    <td>
                        <strong style="color:#fff; font-size: 8.5pt;">{loc['name']}</strong><br>
                        <span style="color:#9ba6a1; font-size: 7pt;">Option 0{idx+1} · {loc['area']}</span>
                    </td>
                    <td><span class="badge badge-gold" style="font-size: 6.8pt;">{loc['style']}</span></td>
                    <td style="font-size: 7.5pt;">{loc['living_features'][0]}</td>
                    <td style="font-size: 7.5pt;">{loc['garden_features'][0]}</td>
                    <td>
                        <strong style="color:#dfb76c; font-size: 8.2pt;">{loc['gbp_shoot']}</strong><br>
                        <span style="color:#9ba6a1; font-size: 6.5pt;">{loc['zar_shoot']}</span>
                    </td>
                    <td><span style="color:#6ee7b7; font-weight:600; font-size: 7.2pt;">✓ Confirmed Open</span></td>
                </tr>
    """)

html_parts.append(f"""
            </tbody>
        </table>

        <div class="cta-box">
            <h3>Ready to Confirm or Scout These Locations?</h3>
            <p>
                We recommend placing a <strong>48-hour first option pencil</strong> on your preferred property
                to secure priority holds for the March 2027 shooting window.
            </p>
            <div style="font-size: 9pt; color: #dfb76c; font-weight: 600; margin-bottom: 2mm;">
                SALocations / Jardin Roestorff · Cape Town, South Africa
            </div>
            <a class="cta-email" href="mailto:jardin@salocations.com?subject=British%20Homes%20Brief%20-%20March%202027">
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

print("Rendering 18-page PDF via Playwright Chromium...")
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
for i, l in enumerate(all_new_locations):
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
