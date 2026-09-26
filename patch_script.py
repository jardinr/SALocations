import os

deck_script = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\zen-mirage-media-web\generate_html_deck.py"

with open(deck_script, "r", encoding="utf-8") as f:
    c = f.read()

replacements = [
    ('<span class="comp-badge">Cape Town Scouted Match</span>', '<span class="comp-badge">Scouted Images Database</span>'),
    ('<div class="comp-sub" style="margin-top: 0.2rem;">Pre-Screened Real-World Location</div>', '<div class="comp-sub" style="margin-top: 0.2rem;">Cape Town Production Database Match</div>'),
    ('<strong>Scouted Environment:</strong>', '<strong>Database Match:</strong>'),
    ('📍 Scouted Locations', '📁 Scouted Images Database'),
    ("const tagLabel = item.source === 'ref' ? 'Reference' : 'Scouted';", "const tagLabel = item.source === 'ref' ? 'Reference' : 'Database';"),
    ('9 Categories (Refs + Matched Locations + Studios)', '8 Curated Categories & Soundstages'),
    ("Stardust, Chapman's Peak, Blackwood Cabin, V&A", "Harringtons, Blackwood Cabin, Chapman's Peak, Stardust"),
    ("Curated Location & Studio Categories", "Director Visual References & Scouted Images Database"),
    ("Select a category to view the Director's Visual Reference side-by-side with Cape Town matched scouting photography", "Select a category to view the Director's Visual Reference side-by-side with Cape Town's Scouted Images Database"),
    ("ZAR 6,000 <span class=\"sub\">/ day (~£266)</span>", "ZAR 6,000 <span class=\"sub\">/ day (~₹29,500 INR)</span>"),
    ("ZAR 7,500 <span class=\"sub\">/ shoot day</span>", "ZAR 7,500 <span class=\"sub\">/ shoot day (~₹37,000 INR)</span>")
]

for old_str, new_str in replacements:
    if old_str in c:
        c = c.replace(old_str, new_str)

with open(deck_script, "w", encoding="utf-8") as f:
    f.write(c)

print("generate_html_deck.py updated successfully!")
