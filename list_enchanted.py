import os
from PIL import Image

fld = r"C:\Users\Jardin\OneDrive\Pictures\English\Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Enchanted\Enchanted"
files = [f for f in os.listdir(fld) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]) if '_' in x and x.split('_')[1].split('.')[0].isdigit() else 999)

print(f"Total files in Enchanted: {len(files)}")
print(files)
