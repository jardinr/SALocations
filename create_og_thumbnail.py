import base64
import os
import shutil
from playwright.sync_api import sync_playwright

def get_b64(path):
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")

img_hero = get_b64(r"C:\Users\Jardin\OneDrive\Pictures\English\Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - Enchanted\Enchanted\Enchanted_31.jpg")
img_elegance = get_b64(r"C:\Users\Jardin\OneDrive\Pictures\English\Shoot My House - SHOOT MY HOUSE _ ENGLISH HOMES  - English Elegance\English Elegance\English Elegance_5.jpg")
img_villaten = get_b64(r"C:\Users\Jardin\OneDrive\Pictures\English\# 10\#10 (43).jpg")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');
    
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    body {{
        width: 1200px;
        height: 630px;
        overflow: hidden;
        background-color: #0c100f;
        font-family: 'Inter', sans-serif;
        color: #f5f5f2;
        position: relative;
        display: flex;
    }}

    /* Background image layout */
    .bg-canvas {{
        position: absolute;
        top: 0;
        right: 0;
        width: 65%;
        height: 100%;
        display: grid;
        grid-template-columns: 1.2fr 1fr;
        grid-template-rows: 1fr 1fr;
        gap: 4px;
        z-index: 1;
    }}
    .bg-cell {{
        position: relative;
        overflow: hidden;
    }}
    .bg-cell.hero-cell {{
        grid-row: span 2;
    }}
    .bg-cell img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}

    /* Overlays */
    .gradient-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 2;
        background: linear-gradient(90deg, 
            #0a0e0d 0%, 
            #0a0e0de6 38%, 
            #0a0e0db3 52%, 
            rgba(10, 14, 13, 0.4) 75%, 
            rgba(10, 14, 13, 0.2) 100%
        );
    }}

    .gold-border-top {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: linear-gradient(90deg, #c5a059, #dfb76c, #1f3d30);
        z-index: 10;
    }}

    /* Content Area */
    .card-content {{
        position: relative;
        z-index: 3;
        width: 620px;
        height: 100%;
        padding: 48px 52px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}

    .top-meta {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}
    .brand-pill {{
        background: #1f3d30;
        color: #dfb76c;
        border: 1px solid #c5a059;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        padding: 5px 12px;
        border-radius: 4px;
    }}
    .client-tag {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 11px;
        color: #9ba6a1;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }}

    .title-block {{
        margin-top: 10px;
    }}
    .main-title {{
        font-family: 'Cinzel', serif;
        font-size: 38px;
        font-weight: 800;
        line-height: 1.15;
        color: #ffffff;
        letter-spacing: 0.5px;
        margin-bottom: 12px;
        text-shadow: 0 4px 12px rgba(0,0,0,0.6);
    }}
    .gold-accent {{
        color: #dfb76c;
    }}
    .tagline {{
        font-size: 15px;
        line-height: 1.55;
        color: #b8c4bf;
        font-weight: 400;
        max-width: 520px;
    }}

    .features-grid {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin: 18px 0;
    }}
    .feature-pill {{
        background: rgba(27, 36, 33, 0.75);
        border: 1px solid rgba(197, 160, 89, 0.25);
        border-radius: 6px;
        padding: 8px 12px;
        display: flex;
        align-items: center;
        gap: 8px;
        backdrop-filter: blur(8px);
    }}
    .feature-pill span.icon {{
        font-size: 14px;
    }}
    .feature-pill span.text {{
        font-size: 12px;
        font-weight: 600;
        color: #f5f5f2;
        letter-spacing: 0.2px;
    }}

    .footer-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 16px;
    }}
    .url-badge {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 13px;
        font-weight: 700;
        color: #dfb76c;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
        gap: 6px;
    }}
    .specs-badge {{
        font-size: 11px;
        color: #9ba6a1;
        font-weight: 500;
        letter-spacing: 0.5px;
    }}

    /* Floating property preview badges on the right side */
    .preview-badge-container {{
        position: absolute;
        bottom: 30px;
        right: 32px;
        z-index: 4;
        display: flex;
        gap: 10px;
    }}
    .match-badge {{
        background: rgba(13, 17, 16, 0.88);
        border: 1px solid #c5a059;
        border-radius: 6px;
        padding: 8px 14px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.6);
        text-align: center;
    }}
    .match-score {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 16px;
        font-weight: 700;
        color: #2ed573;
    }}
    .match-sub {{
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #9ba6a1;
    }}
</style>
</head>
<body>
    <div class="gold-border-top"></div>
    
    <div class="bg-canvas">
        <div class="bg-cell hero-cell">
            <img src="{img_hero}" alt="Enchanted Manor from Lawn">
        </div>
        <div class="bg-cell">
            <img src="{img_elegance}" alt="English Elegance Manor Terrace">
        </div>
        <div class="bg-cell">
            <img src="{img_villaten}" alt="Villa Ten Manor & Lawn">
        </div>
    </div>

    <div class="gradient-overlay"></div>

    <div class="card-content">
        <div class="top-meta">
            <div class="brand-pill">SA LOCATIONS</div>
            <div class="client-tag">Curated Location Pitch</div>
        </div>

        <div class="title-block">
            <h1 class="main-title">British Residential <span class="gold-accent">Homes & Gardens</span></h1>
            <p class="tagline">Exclusive Cape Town portfolio of 6 premier heritage estates: wide-angle exterior country lawns, authentic English architecture, and lived-in friend-group hearth lounges.</p>
        </div>

        <div class="features-grid">
            <div class="feature-pill">
                <span class="icon">🏰</span>
                <span class="text">6 Character Estates</span>
            </div>
            <div class="feature-pill">
                <span class="icon">🛋️</span>
                <span class="text">Lived-In Lounges & Hearths</span>
            </div>
            <div class="feature-pill">
                <span class="icon">🌳</span>
                <span class="text">Expansive Lawns & Hedges</span>
            </div>
            <div class="feature-pill">
                <span class="icon">🎬</span>
                <span class="text">Unit Base & Power Specs</span>
            </div>
        </div>

        <div class="footer-bar">
            <div class="url-badge">
                <span>🔗</span> sal-british-homes.vercel.app
            </div>
            <div class="specs-badge">
                Interactive Client Deck
            </div>
        </div>
    </div>

    <div class="preview-badge-container">
        <div class="match-badge">
            <div class="match-score">98% MATCH</div>
            <div class="match-sub">Enchanted</div>
        </div>
        <div class="match-badge">
            <div class="match-score">96% MATCH</div>
            <div class="match-sub">English Elegance</div>
        </div>
    </div>
</body>
</html>
"""

temp_html = "og_temp.html"
with open(temp_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Capturing 1200x630 preview card screenshot via Playwright...")
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
    page.goto("file:///" + os.path.abspath(temp_html).replace("\\", "/"))
    page.wait_for_timeout(1000)
    page.screenshot(path="og-preview.jpg", quality=92, type="jpeg")
    browser.close()

if os.path.exists(temp_html):
    os.remove(temp_html)

print("Generated og-preview.jpg successfully!")

# Copy to destinations
destinations = [
    r"C:\Users\Jardin\OneDrive\Pictures\English\og-preview.jpg",
    r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\og-preview.jpg"
]
for dest in destinations:
    shutil.copy2("og-preview.jpg", dest)
    print(f"Copied to {dest}")
