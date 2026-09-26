import os
from PIL import Image

base = r"C:\Users\Jardin\OneDrive\Pictures\English"
folders = {
    "Enchanted": os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Enchanted\Enchanted"),
    "English Elegance": os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - English Elegance\English Elegance"),
    "Solace House": os.path.join(base, r"Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Solace House\Solace House"),
    "Villa Ten": os.path.join(base, r"# 10"),
    "Arumbrook": os.path.join(base, r"Arumbrook")
}

for name, folder in folders.items():
    print(f"=== {name} ({folder}) ===")
    if not os.path.exists(folder):
        print("Does not exist!")
        continue
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    print(f"Total files: {len(files)}")
    print(sorted(files)[:30])
