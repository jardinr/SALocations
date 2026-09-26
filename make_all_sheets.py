import os
from PIL import Image, ImageDraw

base = r"C:\Users\Jardin\OneDrive\Pictures\English"
targets = {
    "english_elegance": (
        os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - English Elegance\English Elegance"),
        lambda fn: int(fn.split('_')[1].split('.')[0]) if '_' in fn and fn.split('_')[1].split('.')[0].isdigit() else 999
    ),
    "solace_house": (
        os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Solace House\Solace House"),
        lambda fn: int(fn.split('_')[1].split('.')[0]) if '_' in fn and fn.split('_')[1].split('.')[0].isdigit() else 999
    ),
    "villa_ten": (
        os.path.join(base, r"# 10"),
        lambda fn: int(fn.replace("#10 (", "").replace(").jpg", "")) if "#10 (" in fn else 999
    ),
    "arumbrook": (
        os.path.join(base, r"Arumbrook"),
        lambda fn: int(fn.replace("Arumbrook (", "").replace(").jpg", "")) if "Arumbrook (" in fn else 999
    )
}

for name, (folder, sort_key) in targets.items():
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    try:
        files.sort(key=sort_key)
    except:
        files.sort()
    
    cols = 6
    rows = (len(files) + cols - 1) // cols
    w, h = 320, 220
    sheet = Image.new("RGB", (cols * w, rows * h), (20, 20, 20))
    draw = ImageDraw.Draw(sheet)

    for idx, fn in enumerate(files):
        r = idx // cols
        c = idx % cols
        path = os.path.join(folder, fn)
        try:
            with Image.open(path) as im:
                im = im.convert("RGB")
                im.thumbnail((w, h))
                x_off = c * w + (w - im.width) // 2
                y_off = r * h + (h - im.height) // 2
                sheet.paste(im, (x_off, y_off))
                draw.rectangle([c * w, r * h, c * w + 110, r * h + 24], fill=(0, 0, 0, 180))
                short_fn = fn.replace("English Elegance_", "#").replace("Solace House_", "#").replace("#10 (", "#").replace(").jpg", "").replace("Arumbrook (", "#")
                draw.text((c * w + 5, r * h + 4), short_fn, fill=(255, 255, 0))
        except Exception as e:
            print(f"Error {fn}: {e}")

    out_path = fr"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\{name}_all.jpg"
    sheet.save(out_path, quality=85)
    print(f"Saved {name} contact sheet to {out_path}")
