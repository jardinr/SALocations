import os
import re

files_to_clean = [
    r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-british-homes-web\index.html",
    r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Standalone.html",
    r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\British_Residential_Homes_Standalone.html"
]

old_prop_cal_encoded = (
    "Curated+Properties%3A%0A"
    "%E2%80%A2+Storybook+House+%28Newlands+%2F+Fernwood%29%0A"
    "%E2%80%A2+Invergara+Estate+%28Bishopscourt+%2F+Constantia%29%0A"
    "%E2%80%A2+Orchard+House+%28Constantia+Upper%29%0A"
    "%E2%80%A2+Silwood+Manor+%28Rondebosch+Heritage+Belt%29%0A"
    "%E2%80%A2+Cloudbreak+%28Bishopscourt%29%0A"
    "%E2%80%A2+Marlbrook+%28Bishopscourt+%2F+Newlands%29%0A%0A"
)

new_prop_cal_encoded = (
    "Curated+Properties+%28Shoot+My+House%29%3A%0A"
    "%E2%80%A2+Enchanted+%28Bishopscourt+%2F+Constantia%29%0A"
    "%E2%80%A2+English+Elegance+%28Constantia+%2F+Bishopscourt%29%0A"
    "%E2%80%A2+Solace+House+%28Newlands+%2F+Rondebosch%29%0A%0A"
)

for path in files_to_clean:
    if not os.path.exists(path):
        continue
    print(f"Cleaning {os.path.basename(path)}...")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace the calendar property list
    if old_prop_cal_encoded in content:
        content = content.replace(old_prop_cal_encoded, new_prop_cal_encoded)
        print(" -> Replaced old property list in Google Calendar URL")

    # 2. Replace meta tag mentions of 6 character properties
    content = content.replace("6 character properties with specs & rate cards", "3 exclusive Shoot My House character properties with specs & rate cards")
    content = content.replace("6 character properties", "3 exclusive Shoot My House properties")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    # Verification
    old_names = ["Storybook", "Invergara", "Orchard", "Silwood", "Cloudbreak", "Marlbrook"]
    found = [n for n in old_names if n.lower() in content.lower()]
    if found:
        print(f" WARNING: Found lingering references in {os.path.basename(path)}: {found}")
    else:
        print(f" CLEAN: Zero references to yesterday's properties in {os.path.basename(path)}")

print("\nDone cleaning HTML files!")
