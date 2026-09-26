import os
from PIL import Image

base = r"C:\Users\Jardin\OneDrive\Pictures\English"
heroes = {
    "Enchanted": os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Enchanted\Enchanted", "Enchanted_31.jpg"),
    "English Elegance 7": os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - English Elegance\English Elegance", "English Elegance_7.jpg"),
    "English Elegance 5": os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - English Elegance\English Elegance", "English Elegance_5.jpg"),
    "Solace House 8": os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Solace House\Solace House", "Solace House_8.jpg"),
    "Solace House 1": os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Solace House\Solace House", "Solace House_1.jpg"),
    "Villa Ten 43": os.path.join(base, r"# 10", "#10 (43).jpg"),
    "Arumbrook 3": os.path.join(base, r"Arumbrook", "Arumbrook (3).jpg")
}

for name, path in heroes.items():
    print(name, "exists:", os.path.exists(path))
    if os.path.exists(path):
        with Image.open(path) as im:
            print(f"  size: {im.size}, aspect: {im.width/im.height:.2f}")

# Make a contact sheet of heroes
cols = len(heroes)
w, h = 400, 260
sheet = Image.new("RGB", (cols * w, h), (30, 30, 30))
for i, (name, path) in enumerate(heroes.items()):
    with Image.open(path) as im:
        im = im.convert("RGB")
        im.thumbnail((w, h))
        x_off = i * w + (w - im.width) // 2
        y_off = (h - im.height) // 2
        sheet.paste(im, (x_off, y_off))

out_sheet = r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\proposed_heroes.jpg"
sheet.save(out_sheet)
print("Saved proposed heroes to", out_sheet)
