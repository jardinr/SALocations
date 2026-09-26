import os
import json
import re
import base64
import io
import shutil
from PIL import Image

base_img_dir = r"C:\Users\Jardin\OneDrive\Pictures\English"
web_index_path = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-british-homes-web\index.html"
standalone_pictures = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Standalone.html"
standalone_pitches = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\British_Residential_Homes_Standalone.html"

# 1. Create cropped Arumbrook facade (removes modern parked car on left)
arumbrook_orig = os.path.join(base_img_dir, "Arumbrook", "Arumbrook (4).jpg")
arumbrook_cropped_path = os.path.join(base_img_dir, "Arumbrook", "Arumbrook_facade.jpg")
with Image.open(arumbrook_orig) as im:
    w, h = im.size
    cropped = im.crop((int(w * 0.22), 0, w, h))
    cropped.save(arumbrook_cropped_path, quality=92)
print("Saved Arumbrook_facade.jpg without cars!")

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

locations_curated = [
    {
        "id": "enchanted",
        "name": "Enchanted",
        "area": "Bishopscourt / Constantia, Cape Town",
        "style": "English Country Residence & Estate Lawn",
        "match_score": "98% Match",
        "tagline": "Quintessential English country estate featuring a double-storey white manor, expansive manicured rear lawn with a mature shade tree, covered dining veranda, and a lived-in library hearth lounge.",
        "rate_shoot": "£2,100 / day (ZAR 47,250)",
        "rate_prep": "£1,050 / day (ZAR 23,625)",
        "availability": "Confirmed Open for March 2027 (Shoot My House Collection)",
        "restrictions": "Standard residential curfew (22:00 wrap); maximum 50 crew interior; shoe covers or floor protection on polished timber floors.",
        "parking": "Private paved driveway and courtyard for 6 technical vans; dedicated catering/unit base staging area within gates.",
        "filming_areas": "Exterior Manor Lawn & Tree, Covered Dining Veranda, Veranda Lounge, Main Reception Lounge with Stone Hearth, White Shaker Island Kitchen, Country Dining Room.",
        "living_summary": "Classic English country interior with deep neutral sofas, built-in white library shelving, working stone fireplace hearth, traditional white shaker kitchen with prep island and range cooker, and French doors leading to the garden.",
        "living_features": [
            "Main reception lounge with built-in library bookcases and working stone fireplace hearth",
            "Deep neutral sofa arrangement accommodating a group of 6–8 friends comfortably",
            "Double French doors delivering directional soft daylight and direct garden flow",
            "Spacious white shaker country kitchen with large prep island and breakfast bar counter",
            "Formal country dining room with multi-pane windows and garden views"
        ],
        "garden_summary": "Spectacular flat rear garden party lawn completely framed by mature deciduous shade trees, flowering borders, and tall perimeter evergreen hedges. Features a deep covered veranda terrace with 8-seater teak dining table and outdoor sofas.",
        "garden_features": [
            "Level manicured lawn perfectly sized for large dressed garden-party tracking shots",
            "Prominent mature deciduous shade tree providing natural soft dappled lighting",
            "High boundary evergreen hedges and perimeter walls ensuring 100% camera privacy",
            "Deep covered veranda terrace with 8-seater teak dining table and outdoor lounge",
            "Direct interior-to-exterior French door flow for seamless dolly moves"
        ],
        "folder": r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Enchanted\Enchanted",
        "hero": "Enchanted_31.jpg",
        "gallery": [
            {"file": "Enchanted_31.jpg", "cat": "exterior", "title": "White Country Manor Facade from Across Expansive Rear Lawn"},
            {"file": "Enchanted_39.jpg", "cat": "exterior", "title": "Manor & Veranda Perspective Across Manicured Party Lawn"},
            {"file": "Enchanted_40.jpg", "cat": "exterior", "title": "Manor, Covered Veranda, Mature Tree & Swimming Pool"},
            {"file": "Enchanted_42.jpg", "cat": "exterior", "title": "Country Residence Framed by Manicured Topiary Hedges"},
            {"file": "Enchanted_27.jpg", "cat": "garden", "title": "Rear Architecture & Veranda Columns with Pool Terrace"},
            {"file": "Enchanted_29.jpg", "cat": "garden", "title": "Expansive Flat Rear Lawn with Perimeter Evergreen Hedge"},
            {"file": "Enchanted_30.jpg", "cat": "garden", "title": "Dappled Sunlight under Mature Garden Shade Tree"},
            {"file": "Enchanted_25.jpg", "cat": "garden", "title": "Deep Covered Veranda with 8-Seater Teak Dining Table"},
            {"file": "Enchanted_26.jpg", "cat": "garden", "title": "Veranda Outdoor Lounge with Deep Modular Sofas"},
            {"file": "Enchanted_41.jpg", "cat": "garden", "title": "Boundary Evergreen Hedges with Mountain Backdrop"},
            {"file": "Enchanted_1.jpg", "cat": "living", "title": "Main Reception Lounge with Stone Hearth & Library Shelves"},
            {"file": "Enchanted_3.jpg", "cat": "living", "title": "Neutral Sofa Arrangement for 6–8 Friends with Garden Doors"},
            {"file": "Enchanted_6.jpg", "cat": "living", "title": "Directional Soft Daylight Through French Doors onto Wood Floors"},
            {"file": "Enchanted_8.jpg", "cat": "living", "title": "Working Stone Fireplace Hearth & Fireside Armchairs"},
            {"file": "Enchanted_11.jpg", "cat": "living", "title": "Classic White Shaker Country Kitchen with Prep Island"},
            {"file": "Enchanted_12.jpg", "cat": "living", "title": "Heritage Range Cooker, Subway Tiles & Sash Window"}
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
        "match_score": "96% Match",
        "tagline": "Classic English country farmhouse set on an elevated terrace overlooking a vast green lawn, complete with a white-column veranda, sunken turf tennis court, and warm lived-in hearth lounge.",
        "rate_shoot": "£2,100 / day (ZAR 47,250)",
        "rate_prep": "£1,050 / day (ZAR 23,625)",
        "availability": "Confirmed Open for March 2027 (Filming Experienced Owner)",
        "restrictions": "Standard residential curfew (22:00 wrap); maximum 50 crew interior; soft-sole shoes or protection on heritage timber floors.",
        "parking": "Long private paved driveway accommodates 5 technical vans; secure turning circle inside gates; crew basecamp on paved apron.",
        "filming_areas": "Elevated Manor Facade, Terrace Steps & Lawn, Pergola Veranda, Grandfather Staircase Foyer, Formal Dining Hall, Shaker Island Kitchen, Breakfast Booth, Living Lounge, Sunken Tennis Court.",
        "living_summary": "Authentic British country interior with warm timber flooring, grandfather staircase hall, country shaker kitchen with wooden butcher-block island, breakfast corner booth, and comfortable lived-in family lounge with fireplace.",
        "living_features": [
            "Warm family lounge with stone fireplace hearth, bay window, armchairs & Persian rugs",
            "Formal English country dining room with grandfather staircase and chandeliers",
            "Farmhouse shaker kitchen with wooden butcher-block prep island and breakfast booth",
            "Classic entrance foyer with heritage timber staircase and Dutch half-door",
            "High ceilings with exposed white rafters in upper attic studio lounge"
        ],
        "garden_summary": "Extensive mature English country gardens featuring an elevated manor terrace, tiered stone garden stairways with climbing roses, a wide flat lawn, covered veranda with green pergola, and a private sunken turf tennis court surrounded by perimeter hedges.",
        "garden_features": [
            "Elevated manor facade looking down over an expansive manicured lawn corridor",
            "Private sunken grass tennis court completely enclosed by mature hedges",
            "Traditional white-column veranda with green pergola and outdoor wicker armchairs",
            "Multi-tiered stone steps and white rose trellises providing cinematic depth",
            "Long private paved approach driveway lined with mature hydrangea bushes"
        ],
        "folder": r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - English Elegance\English Elegance",
        "hero": "English Elegance_5.jpg",
        "gallery": [
            {"file": "English Elegance_5.jpg", "cat": "exterior", "title": "Manor on Elevated Terrace Across Lawn with Stone Steps"},
            {"file": "English Elegance_7.jpg", "cat": "exterior", "title": "Wide Lawn Perspective of Manor Nestled in Mature Trees"},
            {"file": "English Elegance_6.jpg", "cat": "exterior", "title": "Expansive Flat Green Lawn Sized for Garden Party Scenes"},
            {"file": "English Elegance_2.jpg", "cat": "exterior", "title": "Rear Facade, Swimming Pool & Covered Veranda"},
            {"file": "English Elegance_28.jpg", "cat": "garden", "title": "White Column Veranda with Green Pergola & Armchairs"},
            {"file": "English Elegance_25.jpg", "cat": "garden", "title": "Private Sunken Turf Tennis Court with High Boundary Hedges"},
            {"file": "English Elegance_26.jpg", "cat": "garden", "title": "Sunken Grass Tennis Court (Wide Perspective)"},
            {"file": "English Elegance_23.jpg", "cat": "garden", "title": "Multi-Tiered Stone Staircase with Climbing White Roses"},
            {"file": "English Elegance_24.jpg", "cat": "garden", "title": "Verdant Sunken Garden Walkway & Box Hedging"},
            {"file": "English Elegance_31.jpg", "cat": "exterior", "title": "Long Paved Approach Driveway Lined with Hydrangea Hedges"},
            {"file": "English Elegance_11.jpg", "cat": "living", "title": "Lived-In Family Lounge with Armchairs, Rugs & Soft Daylight"},
            {"file": "English Elegance_19.jpg", "cat": "living", "title": "Hearth Lounge with Stone Fireplace, Bay Windows & Bookcases"},
            {"file": "English Elegance_9.jpg", "cat": "living", "title": "Grand English Dining Hall with Grandfather Clock & Chandelier"},
            {"file": "English Elegance_13.jpg", "cat": "living", "title": "Farmhouse Shaker Kitchen with Wooden Butcher-Block Island"},
            {"file": "English Elegance_15.jpg", "cat": "living", "title": "Built-In Breakfast Nook Corner Booth with Sash Window"},
            {"file": "English Elegance_16.jpg", "cat": "living", "title": "Classic Foyer with Heritage Timber Staircase & French Doors"}
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
        "match_score": "97% Match",
        "tagline": "Authentic English cottage architecture with pitched dark shingle roof, arched brick entrance, long private hedged lawn, glass atrium breezeway, and sheltered brick pool patio with pizza oven.",
        "rate_shoot": "£2,150 / day (ZAR 48,375)",
        "rate_prep": "£1,075 / day (ZAR 24,185)",
        "availability": "Confirmed Open for March 2027 (Shoot My House Collection)",
        "restrictions": "Standard residential curfew (22:00 wrap); maximum 45 crew interior; protective runners on interior timber flooring.",
        "parking": "Dedicated paved driveway for 4 technical vans; ample quiet residential street parking with traffic management.",
        "filming_areas": "Cottage Facade & Garden Path, Long Rear Lawn & High Hedge, Covered Glass Atrium Breezeway, Brick Pool Terrace, Pizza Oven Banquet Dining, Cozy Hearth Lounge.",
        "living_summary": "Inviting cottage living spaces with exposed brickwork, multi-pane bay windows, covered glass atrium breezeway connecting wings, and a cozy, authentic British residential friend-group lounge with working fireplace.",
        "living_features": [
            "Cozy friend-group living rooms with working fireplace hearth and leaded bay windows",
            "Covered glass atrium breezeway with arched brick doorway and courtyard atmosphere",
            "Country dining room with long 8-seater timber table and garden outlook",
            "Built-in bay window reading bench nook with warm directional natural daylight",
            "Shaker kitchen with sage green cabinetry and wide plank timber flooring"
        ],
        "garden_summary": "Exceptional garden party and boundary environments featuring a long manicured flat lawn fully flanked by tall evergreen perimeter hedges, plus a brick-paved pool terrace with built-in wood-fired pizza oven and banquet dining table.",
        "garden_features": [
            "Long, level lawn corridor bordered by dense tall hedges — prime boundary fence location",
            "Covered outdoor entertaining terrace with rustic timber banquet table and pizza oven",
            "Sheltered brick swimming pool terrace with sun loungers and mountain backdrop",
            "Picturesque front cottage garden pathway with picket fence and iron gate",
            "High degree of visual privacy with zero overlooking neighboring buildings"
        ],
        "folder": r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Solace House\Solace House",
        "hero": "Solace House_8.jpg",
        "gallery": [
            {"file": "Solace House_8.jpg", "cat": "exterior", "title": "English Cottage Architecture from Across Lawn & Mature Trees"},
            {"file": "Solace House_1.jpg", "cat": "exterior", "title": "Cottage Facade with Dark Pitched Shingle Roof & Garden Path"},
            {"file": "Solace House_2.jpg", "cat": "exterior", "title": "Picket Fence Gateway, Lush Shrubbery & Brick Pathway"},
            {"file": "Solace House_10.jpg", "cat": "garden", "title": "Long Manicured Lawn Flanked by Tall Boundary Hedges"},
            {"file": "Solace House_11.jpg", "cat": "exterior", "title": "Rear Cottage Architecture with Brick Terrace & Bay Windows"},
            {"file": "Solace House_15.jpg", "cat": "garden", "title": "Turquoise Pool Set in Brick Apron with Mountain Backdrop"},
            {"file": "Solace House_13.jpg", "cat": "garden", "title": "Sheltered Brick Pool Terrace with Sun Loungers"},
            {"file": "Solace House_20.jpg", "cat": "garden", "title": "Covered Terrace with Rustic Timber Table & Pizza Oven"},
            {"file": "Solace House_22.jpg", "cat": "garden", "title": "Sheltered Outdoor Poolside Lounge with Mountain Views"},
            {"file": "Solace House_18.jpg", "cat": "living", "title": "Glass-Roof Courtyard Breezeway & Arched Brick Doorway"},
            {"file": "Solace House_37.jpg", "cat": "living", "title": "Cozy Friend-Group Lounge with Fireplace & Bay Windows"},
            {"file": "Solace House_38.jpg", "cat": "living", "title": "Lived-In Lounge with Modular Blue Rug & Timber Beams"},
            {"file": "Solace House_34.jpg", "cat": "living", "title": "Country Dining Room with Long 8-Seater Timber Table"},
            {"file": "Solace House_36.jpg", "cat": "living", "title": "Built-In Bay Window Reading Bench Nook Overlooking Grounds"},
            {"file": "Solace House_28.jpg", "cat": "living", "title": "Country Shaker Kitchen with Sage Cabinetry & Wood Floors"},
            {"file": "Solace House_27.jpg", "cat": "living", "title": "Cozy Kitchen Corner Breakfast Booth Seating"}
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
        "match_score": "95% Match",
        "tagline": "Private gated estate featuring white painted brick architecture, vast flat rear party lawn bordered by pine and oak forest trees, skylit chef's kitchen, and a glass conservatory sunroom.",
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
        "hero": "#10 (43).jpg",
        "gallery": [
            {"file": "#10 (43).jpg", "cat": "exterior", "title": "White Manor from Distance Across Expansive Lawn & Forecourt"},
            {"file": "#10 (44).jpg", "cat": "exterior", "title": "Wide Manor Facade & Vast Flat Party Lawn Framed by Forest Trees"},
            {"file": "#10 (41).jpg", "cat": "exterior", "title": "Front Manor Approach, Driveway Portico & Manicured Box Hedges"},
            {"file": "#10 (10).jpg", "cat": "garden", "title": "Large Swimming Pool in Brick Apron & Expansive Flat Rear Lawn"},
            {"file": "#10 (11).jpg", "cat": "garden", "title": "Rear Garden Party Lawn Framed by Pine & Oak Forest Canopy"},
            {"file": "#10 (12).jpg", "cat": "garden", "title": "Brick Terrace & Rear Architecture Opening onto Lawn"},
            {"file": "#10 (14).jpg", "cat": "garden", "title": "Private Garden Lawn with Tall Brick Boundary Wall & Umbrella Dining"},
            {"file": "#10 (1).jpg", "cat": "exterior", "title": "Gated Estate Entrance with Numbered White Brick Gate Pillars (#10)"},
            {"file": "#10 (2).jpg", "cat": "exterior", "title": "Sweeping Paved Approach Driveway Lined with Oak Trees"},
            {"file": "#10 (6).jpg", "cat": "garden", "title": "Pergola Brick Terrace with Outdoor Dining Table"},
            {"file": "#10 (16).jpg", "cat": "living", "title": "Grand Open-Plan Reception Hall with 12-Seater Timber Dining Table"},
            {"file": "#10 (17).jpg", "cat": "living", "title": "Lived-In Deep Modular Sofa Lounge with Garden Sash Windows"},
            {"file": "#10 (18).jpg", "cat": "living", "title": "Expansive Living Wing Connecting Dining, Lounge & Bookcases"},
            {"file": "#10 (20).jpg", "cat": "living", "title": "Chef's Kitchen with Overhead Atrium Skylight & Navy Island"},
            {"file": "#10 (15).jpg", "cat": "living", "title": "Glass Conservatory Sunroom Lounge with Wicker Sofas & Pool Views"},
            {"file": "#10 (26).jpg", "cat": "living", "title": "Conservatory Glass Double Doors Opening Directly to Pool & Lawn"}
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
        "match_score": "93% Match",
        "tagline": "Idyllic country residence approached via a picturesque double-tree driveway, featuring white-beamed banquet dining, black stone hearth, and manicured topiary grounds.",
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
        "garden_summary": "Extensive private grounds approached via a picturesque double-tree driveway, featuring sculpted topiary hedges, rolling manicured orchard lawns, and a quiet rural setting.",
        "garden_features": [
            "Dramatic tree-lined approach driveway perfect for vehicle arrival scenes",
            "Manicured topiary balls and English cottage floral perimeter borders",
            "Vast flat lawn corridors offering long camera throws and dolly runs",
            "Classic double-dormer country manor architectural exterior",
            "Exceptional sound privacy with zero traffic or industrial intrusion"
        ],
        "folder": "Arumbrook",
        "hero": "Arumbrook_facade.jpg",
        "gallery": [
            {"file": "Arumbrook_facade.jpg", "cat": "exterior", "title": "Double-Storey Country Manor Facade with Dormer Roof & Balconies"},
            {"file": "Arumbrook (2).jpg", "cat": "exterior", "title": "Picturesque Country Driveway Lined with Pruned Trees & Stone Edging"},
            {"file": "Arumbrook (19).jpg", "cat": "exterior", "title": "Long Tree-Lined Approach Driveway Flanked by Orchard Trees & Hedges"},
            {"file": "Arumbrook (20).jpg", "cat": "exterior", "title": "Driveway Approach Looking Toward Main Grounds"},
            {"file": "Arumbrook (1).jpg", "cat": "garden", "title": "Orchard Grounds, Manicured Perimeter Hedges & Mature Trees"},
            {"file": "Arumbrook (18).jpg", "cat": "garden", "title": "Sunlit English Garden Walkway with Flowering Cottage Borders"},
            {"file": "Arumbrook (3).jpg", "cat": "exterior", "title": "Forecourt Courtyard Staging Area with Topiary Hedges"},
            {"file": "Arumbrook (5).jpg", "cat": "living", "title": "Great Banquet Hall with Crittall Glass Doors & Long Dining Table"},
            {"file": "Arumbrook (6).jpg", "cat": "living", "title": "Country Dining Hall with White-Beamed Ceiling & Sash Windows"},
            {"file": "Arumbrook (7).jpg", "cat": "living", "title": "Black Stone Fireplace Hearth with Fireside Armchairs & Garden Doors"},
            {"file": "Arumbrook (8).jpg", "cat": "living", "title": "Sunlit Fireside Lounge Area Overlooking Country Grounds"},
            {"file": "Arumbrook (9).jpg", "cat": "living", "title": "Great Hall with Exposed Rafters Looking Toward Open Kitchen"},
            {"file": "Arumbrook (10).jpg", "cat": "living", "title": "Lived-In Lounge with Armchairs, Timber Ceiling & Chandelier"},
            {"file": "Arumbrook (14).jpg", "cat": "living", "title": "Country Chef's Island Kitchen with Rustic Prep Counter & Sink"},
            {"file": "Arumbrook (15).jpg", "cat": "living", "title": "Open Kitchen Prep Island Looking Into Great Dining Hall"},
            {"file": "Arumbrook (16).jpg", "cat": "living", "title": "Chef's Kitchen Island with Warm Pendant Lighting"}
        ],
        "gbp_shoot": "£2,000",
        "zar_shoot": "ZAR 45,000",
        "gbp_prep": "£1,000",
        "zar_prep": "ZAR 22,500",
        "base_zar": "ZAR 38,000"
    }
]

print("\nEncoding curated images for all 5 locations...")
all_images = {}
for loc in locations_curated:
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

# Update index.html and standalone HTML files
for target_html in [web_index_path, standalone_pictures, standalone_pitches]:
    if not os.path.exists(target_html):
        continue
    print(f"\nUpdating {os.path.basename(target_html)} with curated photos...")
    with open(target_html, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace EMBEDDED_IMAGES
    m_imgs = re.search(r"const EMBEDDED_IMAGES = (\{.*?\});", content, re.DOTALL)
    if m_imgs:
        imgs_json = json.dumps(all_images)
        content = content[:m_imgs.start()] + f"const EMBEDDED_IMAGES = {imgs_json};" + content[m_imgs.end():]
        print(" -> EMBEDDED_IMAGES updated with curated photos")

    # 2. Replace locations array
    m_locs = re.search(r"const locations = (\[.*?\]);\s*function getGoogleCalendarScoutUrl", content, re.DOTALL)
    if not m_locs:
        m_locs = re.search(r"const locations = (\[.*?\]);\s*let currentLocId", content, re.DOTALL)

    if m_locs:
        locs_json = json.dumps(locations_curated, indent=4)
        prefix = content[:m_locs.start()]
        suffix = content[m_locs.end() - len("function getGoogleCalendarScoutUrl"):] if "function getGoogleCalendarScoutUrl" in m_locs.group(0) else content[m_locs.end() - len("let currentLocId"):]
        content = prefix + f"const locations = {locs_json};\n\n        " + suffix
        print(" -> locations array updated with curated properties & wide hero images")

    # 3. Ensure no bedrooms or 1st 6 linger
    old_names = ["Storybook", "Invergara", "Orchard House", "Silwood", "Cloudbreak", "Marlbrook"]
    for old_name in old_names:
        content = re.sub(rf"\b{old_name}\b", "", content, flags=re.IGNORECASE)

    with open(target_html, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully saved {os.path.basename(target_html)}")

print("\nDone updating deck files!")
