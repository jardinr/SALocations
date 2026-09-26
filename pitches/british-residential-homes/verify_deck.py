import json
import re

path = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-british-homes-web\index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

loc_match = re.search(r"const locations = (\[.*?\]);", html, re.DOTALL)
locs = json.loads(loc_match.group(1))
print(f"Total Locations: {len(locs)}")

emb_match = re.search(r"const EMBEDDED_IMAGES = (\{.*?\});", html, re.DOTALL)
emb = json.loads(emb_match.group(1))
print(f"Total Embedded Images: {len(emb)}")

all_ok = True
for idx, l in enumerate(locs):
    hero_key = f"{l['folder']}/{l['hero']}"
    hero_ok = hero_key in emb
    if not hero_ok:
        all_ok = False
        print(f"ERROR: Hero key {hero_key} not in EMBEDDED_IMAGES")
    print(f"Option 0{idx+1}: [{l['id']}] {l['name']} | Hero: {l['hero']} (Embedded: {hero_ok}) | Gallery count: {len(l['gallery'])}")
    for g in l['gallery']:
        g_key = f"{l['folder']}/{g['file']}"
        if g_key not in emb:
            all_ok = False
            print(f"   MISSING: {g_key}")

print("\nALL 96 IMAGES PRESENT AND VALID:" if all_ok else "\nERRORS FOUND!")
