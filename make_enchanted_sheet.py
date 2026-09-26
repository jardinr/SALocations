import os
from PIL import Image, ImageDraw, ImageFont

fld = r"C:\Users\Jardin\OneDrive\Pictures\English\Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Enchanted\Enchanted"
files = [f"Enchanted_{i}.jpg" for i in range(1, 43) if os.path.exists(os.path.join(fld, f"Enchanted_{i}.jpg"))]

cols = 6
rows = (len(files) + cols - 1) // cols
w, h = 320, 220
sheet = Image.new("RGB", (cols * w, rows * h), (20, 20, 20))
draw = ImageDraw.Draw(sheet)

for idx, fn in enumerate(files):
    r = idx // cols
    c = idx % cols
    path = os.path.join(fld, fn)
    try:
        with Image.open(path) as im:
            im = im.convert("RGB")
            im.thumbnail((w, h))
            # paste centered in cell
            x_off = c * w + (w - im.width) // 2
            y_off = r * h + (h - im.height) // 2
            sheet.paste(im, (x_off, y_off))
            # Draw label
            draw.rectangle([c * w, r * h, c * w + 90, r * h + 24], fill=(0, 0, 0, 180))
            draw.text((c * w + 5, r * h + 4), fn.replace("Enchanted_", "#"), fill=(255, 255, 0))
    except Exception as e:
        print(f"Error {fn}: {e}")

out_path = r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\enchanted_all.jpg"
sheet.save(out_path, quality=85)
print(f"Saved contact sheet to {out_path}")
