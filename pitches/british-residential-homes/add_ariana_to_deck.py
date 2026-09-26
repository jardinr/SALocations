import os
import json
import re
import base64
import io
from PIL import Image

ariana_img_dir = r"C:\Users\Jardin\OneDrive\Pictures\English\Ariana"
web_index_path = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-british-homes-web\index.html"
standalone_paths = [
    r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Standalone.html",
    r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\British_Residential_Homes_Standalone.html"
]

def encode_image(filename):
    full = os.path.join(ariana_img_dir, filename)
    if not os.path.exists(full):
        raise FileNotFoundError(f"File not found: {full}")
    with Image.open(full) as im:
        im = im.convert("RGB")
        im.thumbnail((1200, 800), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=82)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

ariana_obj = {
    "id": "ariana",
    "name": "Ariana",
    "area": "Constantia Valley / Bergvliet, Cape Town",
    "style": "English Country Cottage & Grounds",
    "match_score": "95% Match",
    "tagline": "Quintessential English country cottage with yellow ochre gables, multi-pane casement windows, a sweeping gravel driveway approach, expansive front lawn with mature shade tree & swing, and lived-in hearth lounge.",
    "rate_shoot": "£2,050 / day (ZAR 46,125)",
    "rate_prep": "£1,025 / day (ZAR 23,060)",
    "availability": "Confirmed Open for March 2027 (Filming Welcomed)",
    "restrictions": "Standard residential curfew (22:00 wrap); maximum 45 crew interior; protective floor mats on terracotta tiles and timber flooring.",
    "parking": "Wide private gravel driveway and forecourt accommodates 5 technical vehicles; spacious turnaround area within gates.",
    "filming_areas": "Gravel Approach Driveway, Front Lawn & Tree Swing, Colonnaded Veranda, Main Hearth Lounge, Garden-Facing Sunroom Corner, Shaker Island Kitchen, Dining Room with French Doors, Vine-Covered Courtyard Pergola, Rear Swimming Pool Lawn.",
    "living_summary": "Warm, characterful British cottage living spaces featuring a working stone fireplace hearth, wrap-around multi-pane bay windows with garden vistas, traditional country shaker kitchen with central island and range, and dining room opening via French doors to the patio.",
    "living_features": [
        "Main reception lounge with brick/stone fireplace hearth and comfortable fireside seating",
        "Sunlit living corner with wrap-around multi-pane windows overlooking the expansive lawn",
        "Generous friend-group lounge flow connecting seating, dining, and outdoor garden access",
        "Country shaker kitchen with central prep island, open shelving, and garden views",
        "Dining room with long wooden table opening directly onto the veranda terrace",
        "Secondary garden-facing study/lounge room with terracotta tile flooring and armchairs"
    ],
    "garden_summary": "Spectacular established English cottage grounds featuring a long curving gravel driveway, expansive manicured front lawn anchored by a magnificent mature shade tree with a tree swing, full boundary fencing and mature hedges, plus a rear garden with swimming pool and vine-covered dining pergola.",
    "garden_features": [
        "Curving gravel approach driveway allowing long establishing tracking shots of house from a distance",
        "Expansive flat front lawn corridor perfect for camera dollies and garden party staging",
        "Iconic mature deciduous shade tree with working tree swing adding authentic family character",
        "Private rear garden lawn with turquoise swimming pool and sun terrace",
        "Deep vine-covered courtyard pergola providing sheltered outdoor dining and entertaining",
        "High perimeter boundary fences and mature trees ensuring complete visual privacy"
    ],
    "folder": "Ariana",
    "hero": "Ariana (2).jpg",
    "gallery": [
        {"file": "Ariana (2).jpg", "cat": "exterior", "title": "Establishing View of Country Residence from Across Gravel Driveway & Lawn with Tree Swing"},
        {"file": "Ariana (1).jpg", "cat": "exterior", "title": "English Country House Facade Framed by Mature Deciduous Trees & Front Lawn"},
        {"file": "Ariana (31).jpg", "cat": "exterior", "title": "Front Facade, Chimney Stack, Dormer Windows & Colonnaded Veranda Approach"},
        {"file": "Ariana (3).jpg", "cat": "exterior", "title": "Side Garden Lawn, Paved Pathway & Multi-Pane Casement Windows"},
        {"file": "Ariana (5).jpg", "cat": "exterior", "title": "Rear Facade, Paved Garden Terrace & Outdoor Dining Patio"},
        {"file": "Ariana (6).jpg", "cat": "garden", "title": "Rear Garden with Swimming Pool, Brick Apron & French Doors"},
        {"file": "Ariana (4).jpg", "cat": "garden", "title": "Dappled Garden Walkway under Mature Tree Canopy with Flower Borders"},
        {"file": "Ariana (29).jpg", "cat": "garden", "title": "Enclosed Courtyard Veranda with Climbing Vine Canopy & Outdoor Seating"},
        {"file": "Ariana (30).jpg", "cat": "garden", "title": "Pergola Terrace with Vine Trellis & French Door Access"},
        {"file": "Ariana (14).jpg", "cat": "living", "title": "Main Reception Lounge with Working Fireplace Hearth & Fireside Sofas"},
        {"file": "Ariana (15).jpg", "cat": "living", "title": "Sunlit Lounge Corner with Wrap-Around Multi-Pane Windows Overlooking Lawn"},
        {"file": "Ariana (16).jpg", "cat": "living", "title": "Spacious Friend-Group Living Room Connecting Lounge & Dining Areas"},
        {"file": "Ariana (8).jpg", "cat": "living", "title": "Country Shaker Kitchen with Central Prep Island & Garden Window"},
        {"file": "Ariana (7).jpg", "cat": "living", "title": "Dining Area with Timber Table & French Doors Opening to Garden Patio"},
        {"file": "Ariana (26).jpg", "cat": "living", "title": "Secondary Garden-Facing Study & Lounge with Armchairs & Terracotta Tiles"},
        {"file": "Ariana (9).jpg", "cat": "living", "title": "Entrance Hallway with Terracotta Flooring, Arched Openings & Timber Staircase"}
    ],
    "gbp_shoot": "£2,050",
    "zar_shoot": "ZAR 46,125",
    "gbp_prep": "£1,025",
    "zar_prep": "ZAR 23,060",
    "base_zar": "ZAR 39,000"
}

def update_file(path):
    print(f"\nProcessing {path}...")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update locations array
    loc_match = re.search(r"const locations = (\[.*?\]);", html, re.DOTALL)
    if not loc_match:
        print("ERROR: could not find locations array")
        return
    
    locs = json.loads(loc_match.group(1))
    # Remove existing ariana if present
    locs = [l for l in locs if l.get("id") != "ariana"]
    locs.append(ariana_obj)
    print(f"Updated locations array: now {len(locs)} properties.")

    # 2. Encode Ariana images
    print("Encoding 16 Ariana images...")
    new_embedded = {}
    for item in ariana_obj["gallery"]:
        fname = item["file"]
        key = f"Ariana/{fname}"
        b64 = encode_image(fname)
        new_embedded[key] = b64
        print(f"  Encoded {key} ({len(b64)} chars)")

    # 3. Update EMBEDDED_IMAGES in html
    emb_match = re.search(r"const EMBEDDED_IMAGES = (\{.*?\});", html, re.DOTALL)
    if not emb_match:
        print("ERROR: could not find EMBEDDED_IMAGES")
        return
    
    emb_dict = json.loads(emb_match.group(1))
    emb_dict.update(new_embedded)
    print(f"Updated EMBEDDED_IMAGES: now {len(emb_dict)} images.")

    # Format new locations string
    new_locs_str = "const locations = " + json.dumps(locs, indent=4) + ";"
    # Format new EMBEDDED_IMAGES string
    new_emb_str = "const EMBEDDED_IMAGES = " + json.dumps(emb_dict) + ";"

    # Replace in html
    html = html[:loc_match.start()] + new_locs_str + html[loc_match.end():]
    
    # Re-search EMBEDDED_IMAGES since indices changed
    emb_match2 = re.search(r"const EMBEDDED_IMAGES = (\{.*?\});", html, re.DOTALL)
    html = html[:emb_match2.start()] + new_emb_str + html[emb_match2.end():]

    # 4. Update text copy
    html = re.sub(r"5 curated character properties", "6 curated character properties", html)
    html = re.sub(r"5 Curated Character Properties", "6 Curated Character Properties", html)

    # Update calendar link details in HTML
    old_cal_details = r"Curated\+Properties.*?%0A%0APackage"
    new_cal_details = (
        "Curated+Properties+%28Cape+Town+Heritage%29%3A%0A"
        "%E2%80%A2+Option+01%3A+Enchanted+%28Bishopscourt+%2F+Constantia%29%0A"
        "%E2%80%A2+Option+02%3A+English+Elegance+%28Constantia+%2F+Bishopscourt%29%0A"
        "%E2%80%A2+Option+03%3A+Solace+House+%28Newlands+%2F+Rondebosch%29%0A"
        "%E2%80%A2+Option+04%3A+Villa+Ten+%28Upper+Constantia%29%0A"
        "%E2%80%A2+Option+05%3A+Arumbrook+Estate+%28Constantia+Valley%29%0A"
        "%E2%80%A2+Option+06%3A+Ariana+%28Constantia+Valley+%2F+Bergvliet%29%0A%0A"
        "Package"
    )
    html = re.sub(old_cal_details, new_cal_details, html)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully wrote {path} (size: {os.path.getsize(path)} bytes)")

if __name__ == "__main__":
    update_file(web_index_path)
    for p in standalone_paths:
        if os.path.exists(p):
            update_file(p)
    print("\nALL FILES UPDATED!")
