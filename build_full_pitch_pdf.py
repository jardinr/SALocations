import json
import re
import os
import shutil
import fitz
from playwright.sync_api import sync_playwright

def main():
    source_html = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Standalone.html"
    print(f"Reading {source_html}...")
    with open(source_html, "r", encoding="utf-8") as f:
        content = f.read()

    m_locs = re.search(r"const locations = (\[.*?\]);\s*(?:function|let)", content, re.DOTALL)
    m_imgs = re.search(r"const EMBEDDED_IMAGES = (\{.*?\});", content, re.DOTALL)

    if not m_locs or not m_imgs:
        print("Error: Could not extract locations or images from Standalone HTML.")
        return

    locs = json.loads(m_locs.group(1))
    imgs = json.loads(m_imgs.group(1))
    print(f"Extracted {len(locs)} locations and {len(imgs)} embedded images.")

    def get_img_src(folder, filename):
        key = f"{folder}/{filename}"
        return imgs.get(key, "")

    # Build A4 printable HTML
    html_parts = []
    html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>British Residential Homes & Gardens - 9 Location Pitch Dossier</title>
    <style>
        @page {
            size: A4 portrait;
            margin: 12mm 14mm 14mm 14mm;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        body {
            background-color: #0d1110;
            color: #f5f5f2;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 9.5pt;
            line-height: 1.45;
        }

        .pdf-page {
            page-break-after: always;
            break-after: page;
            height: 100%;
            min-height: 270mm;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding-bottom: 5mm;
        }

        .page-content {
            flex: 1;
        }

        /* Page Headers & Footers */
        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(197, 160, 89, 0.3);
            padding-bottom: 3mm;
            margin-bottom: 5mm;
        }
        .header-badge {
            font-size: 7.5pt;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: #dfb76c;
        }
        .header-sub {
            font-size: 7.5pt;
            color: #9ba6a1;
            letter-spacing: 0.5px;
        }

        .page-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 3mm;
            margin-top: 4mm;
            font-size: 7.5pt;
            color: #9ba6a1;
        }
        .footer-brand {
            font-weight: 600;
            letter-spacing: 1px;
            color: #c5a059;
        }

        /* Cover Page */
        .cover-hero {
            background: linear-gradient(145deg, #141a18 0%, #1f3d30 100%);
            border: 1px solid rgba(197, 160, 89, 0.4);
            border-radius: 8px;
            padding: 7mm 8mm;
            margin-bottom: 5mm;
        }
        .cover-eyebrow {
            font-size: 8pt;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #dfb76c;
            font-weight: 700;
            margin-bottom: 2mm;
        }
        .cover-title {
            font-family: Georgia, serif;
            font-size: 26pt;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.15;
            margin-bottom: 3mm;
        }
        .cover-subtitle {
            font-size: 9.5pt;
            color: #dce2de;
            line-height: 1.5;
            max-width: 95%;
        }

        .scope-pills {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2.5mm;
            margin-bottom: 4mm;
        }
        .scope-pill {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            padding: 2.5mm 3mm;
        }
        .pill-label {
            font-size: 6pt;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #dfb76c;
            margin-bottom: 1mm;
        }
        .pill-val {
            font-size: 8pt;
            font-weight: 600;
            color: #ffffff;
        }

        .index-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2.5mm;
        }
        .index-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            padding: 2.5mm 3mm;
            border-left: 3px solid #c5a059;
        }
        .index-num {
            font-size: 6.5pt;
            font-weight: 700;
            letter-spacing: 1px;
            color: #dfb76c;
            text-transform: uppercase;
        }
        .index-name {
            font-family: Georgia, serif;
            font-size: 9.5pt;
            font-weight: 700;
            color: #ffffff;
            margin: 0.5mm 0;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .index-meta {
            font-size: 6.5pt;
            color: #9ba6a1;
            margin-bottom: 1mm;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .index-rate {
            font-size: 6.8pt;
            color: #6ee7b7;
            font-weight: 600;
        }

        /* Location Overview Page (Page A) */
        .loc-hero-header {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            padding: 4mm 5mm;
            margin-bottom: 4mm;
        }
        .loc-meta-bar {
            display: flex;
            align-items: center;
            gap: 2.5mm;
            margin-bottom: 1.5mm;
            flex-wrap: wrap;
        }
        .badge {
            font-size: 7pt;
            font-weight: 600;
            padding: 1mm 2.5mm;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.06);
            color: #f5f5f2;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .badge-gold {
            background: rgba(197, 160, 89, 0.15);
            color: #dfb76c;
            border-color: rgba(197, 160, 89, 0.4);
        }
        .badge-green {
            background: rgba(46, 89, 70, 0.3);
            color: #6ee7b7;
            border-color: rgba(110, 231, 183, 0.4);
        }
        .loc-title {
            font-family: Georgia, serif;
            font-size: 19pt;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.2;
            margin-bottom: 1mm;
        }
        .loc-tagline {
            font-size: 9pt;
            color: #dce2de;
            line-height: 1.4;
            margin-bottom: 3mm;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2.5mm;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            padding-top: 2.5mm;
        }
        .metric-box {
            background: rgba(0, 0, 0, 0.35);
            border-radius: 5px;
            padding: 2mm 3mm;
            border: 1px solid rgba(255, 255, 255, 0.04);
        }
        .metric-lbl {
            font-size: 6.5pt;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: #9ba6a1;
            margin-bottom: 0.5mm;
        }
        .metric-val {
            font-size: 10pt;
            font-weight: 700;
            color: #dfb76c;
        }
        .metric-sub {
            font-size: 6.5pt;
            color: #9ba6a1;
        }

        .hero-photo-wrap {
            margin-bottom: 4mm;
            border-radius: 7px;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.1);
            background: #000;
            height: 65mm;
        }
        .hero-photo-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .worlds-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3.5mm;
        }
        .world-box {
            background: #141a18;
            border-radius: 7px;
            padding: 3.5mm 4.5mm;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .world-box.living {
            border-left: 3px solid #dfb76c;
        }
        .world-box.garden {
            border-left: 3px solid #2ed573;
        }
        .world-head {
            display: flex;
            align-items: center;
            gap: 2mm;
            margin-bottom: 1.5mm;
        }
        .world-head h4 {
            font-family: Georgia, serif;
            font-size: 10.5pt;
            color: #ffffff;
        }
        .world-head span.sub {
            font-size: 7.5pt;
            color: #9ba6a1;
        }
        .world-desc {
            font-size: 8pt;
            color: #cfd5d1;
            line-height: 1.4;
            margin-bottom: 2mm;
        }
        .feature-ul {
            list-style: none;
            padding: 0;
        }
        .feature-ul li {
            font-size: 7.5pt;
            color: #e0e5e2;
            margin-bottom: 1mm;
            padding-left: 3.5mm;
            position: relative;
            line-height: 1.35;
        }
        .feature-ul li::before {
            content: "•";
            position: absolute;
            left: 0;
            color: #dfb76c;
            font-weight: 700;
        }

        /* Technical Logistics Page (Page B) */
        .logistics-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3.5mm;
            margin-bottom: 4mm;
        }
        .log-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 7px;
            padding: 3.5mm 4.5mm;
        }
        .log-title {
            font-size: 8pt;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #dfb76c;
            margin-bottom: 2mm;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            padding-bottom: 1.5mm;
        }
        .log-item {
            display: flex;
            justify-content: space-between;
            font-size: 7.8pt;
            margin-bottom: 1.5mm;
            line-height: 1.35;
        }
        .log-item span.k {
            color: #9ba6a1;
            width: 40%;
        }
        .log-item span.v {
            color: #f5f5f2;
            font-weight: 500;
            width: 60%;
            text-align: right;
        }

        /* 4 Highlights Gallery */
        .highlights-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 3mm;
        }
        .hl-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            overflow: hidden;
        }
        .hl-photo {
            height: 38mm;
            background: #000;
        }
        .hl-photo img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .hl-caption {
            padding: 2mm 3mm;
            font-size: 7.2pt;
            color: #cfd5d1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* Extended Gallery Page (Page C) - 3x3 Grid */
        .gallery-grid-9 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 3mm;
        }
        .gallery-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            overflow: hidden;
        }
        .gallery-img-wrap {
            height: 48mm;
            background: #000;
        }
        .gallery-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .gallery-card-cap {
            padding: 1.5mm 2.5mm;
            font-size: 6.8pt;
            color: #dce2de;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            display: flex;
            justify-content: space-between;
        }

        /* Rate Card & Matrix Tables */
        .rate-card-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 8.5pt;
            margin-bottom: 4mm;
        }
        .rate-card-table th {
            background: rgba(197, 160, 89, 0.15);
            color: #dfb76c;
            text-align: left;
            padding: 2.5mm 3mm;
            font-size: 7.5pt;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            border-bottom: 1px solid #dfb76c;
        }
        .rate-card-table td {
            padding: 2.5mm 3mm;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            color: #e0e5e2;
        }

        .matrix-tbl {
            width: 100%;
            border-collapse: collapse;
            font-size: 7.5pt;
        }
        .matrix-tbl th {
            background: rgba(197, 160, 89, 0.15);
            color: #dfb76c;
            text-align: left;
            padding: 2mm 2.5mm;
            font-size: 7pt;
            text-transform: uppercase;
            border-bottom: 1px solid #dfb76c;
        }
        .matrix-tbl td {
            padding: 2mm 2.5mm;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            color: #dce2de;
            vertical-align: middle;
        }

        .cta-box {
            background: linear-gradient(145deg, #141a18 0%, #1f3d30 100%);
            border: 1px solid rgba(197, 160, 89, 0.4);
            border-radius: 8px;
            padding: 4mm 6mm;
            text-align: center;
            margin-top: 3mm;
        }
        .cta-box h3 {
            font-family: Georgia, serif;
            font-size: 13pt;
            color: #ffffff;
            margin-bottom: 1mm;
        }
        .cta-box p {
            font-size: 8pt;
            color: #dce2de;
            margin-bottom: 2.5mm;
        }
        .cta-email {
            display: inline-block;
            background: #c5a059;
            color: #0b0f0e;
            font-size: 9pt;
            font-weight: 700;
            padding: 2mm 5mm;
            border-radius: 5px;
            text-decoration: none;
        }
    </style>
</head>
<body>
""")

    # 1. COVER PAGE
    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">SALOCATIONS // CURATED LOCATION PRESENTATION</span>
                <span class="header-sub">MARCH 2027 PRODUCTION WINDOW</span>
            </div>

            <div class="cover-hero">
                <div class="cover-eyebrow">Production Scouting Dossier</div>
                <h1 class="cover-title">British Residential Homes & Gardens</h1>
                <p class="cover-subtitle">
                    A comprehensive curated portfolio of {len(locs)} characterful residential properties in Cape Town's premier heritage belts
                    (Newlands, Fernwood, Bishopscourt, Rondebosch & Constantia) that convincingly replicate authentic
                    British domestic architecture, lived-in friend-group lounges, and established garden party lawns.
                </p>
            </div>

            <div class="scope-pills">
                <div class="scope-pill">
                    <div class="pill-label">Target Architecture</div>
                    <div class="pill-val">English Arts & Crafts / Manor</div>
                </div>
                <div class="scope-pill">
                    <div class="pill-label">Interior Target</div>
                    <div class="pill-val">Lived-In Friends Group Lounge</div>
                </div>
                <div class="scope-pill">
                    <div class="pill-label">Exterior Target</div>
                    <div class="pill-val">Garden Party Lawn & Fence</div>
                </div>
                <div class="scope-pill">
                    <div class="pill-label">Shoot Window</div>
                    <div class="pill-val">March 2027 (Confirmed Open)</div>
                </div>
            </div>

            <div style="margin-bottom: 2.5mm;">
                <h3 style="font-family: Georgia, serif; font-size: 11pt; color: #fff;">Curated Location Options Summary ({len(locs)} Heritage Properties)</h3>
                <span style="font-size: 7.5pt; color: #9ba6a1;">All {len(locs)} options fully detailed with high-resolution photography, technical specs, and day rates</span>
            </div>

            <div class="index-grid">
    """)

    for idx, loc in enumerate(locs):
        html_parts.append(f"""
                <div class="index-card">
                    <div class="index-num">Option 0{idx+1} // {loc['match_score']}</div>
                    <div class="index-name">{loc['name']}</div>
                    <div class="index-meta">{loc['area']} · {loc['style']}</div>
                    <div class="index-rate">Indicative: {loc.get('gbp_shoot') or loc.get('rate_shoot')} ({loc.get('zar_shoot', '')})</div>
                </div>
        """)

    html_parts.append("""
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-brand">SALOCATIONS // PROFESSIONAL LOCATION MANAGEMENT</span>
            <span>Direct Enquiries: jardin@salocations.com · Page 1</span>
        </div>
    </div>
    """)

    # 2. DETAIL PAGES FOR EACH LOCATION (3 PAGES EACH)
    page_num = 2
    for idx, loc in enumerate(locs):
        hero_img = get_img_src(loc['folder'], loc['hero'])
        gallery_items = loc.get('gallery', [])

        highlight_photos = gallery_items[:4]
        remaining_photos = gallery_items[4:13]

        # PAGE A: Location Profile & Two Worlds Breakdown
        html_parts.append(f"""
        <div class="pdf-page">
            <div class="page-content">
                <div class="page-header">
                    <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()}</span>
                    <span class="header-sub">{loc['area']} · MARCH 2027</span>
                </div>

                <div class="loc-hero-header">
                    <div class="loc-meta-bar">
                        <span class="badge badge-gold">{loc['style']}</span>
                        <span class="badge">📍 {loc['area']}</span>
                        <span class="badge badge-gold">{loc['match_score']}</span>
                        <span class="badge badge-green">✓ March 2027: Available</span>
                    </div>
                    <h2 class="loc-title">{loc['name']}</h2>
                    <p class="loc-tagline">{loc['tagline']}</p>

                    <div class="metrics-grid">
                        <div class="metric-box">
                            <div class="metric-lbl">Shoot Day (12h)</div>
                            <div class="metric-val">{loc.get('gbp_shoot') or loc.get('rate_shoot')}</div>
                            <div class="metric-sub">{loc.get('zar_shoot', '')}</div>
                        </div>
                        <div class="metric-box">
                            <div class="metric-lbl">Prep / Strike (10h)</div>
                            <div class="metric-val">{loc.get('gbp_prep', '50% tariff')}</div>
                            <div class="metric-sub">{loc.get('zar_prep', '')} (50%)</div>
                        </div>
                        <div class="metric-box">
                            <div class="metric-lbl">Scouting Package</div>
                            <div class="metric-val">ZAR 6,000</div>
                            <div class="metric-sub">~£266 (Scout + Vehicle)</div>
                        </div>
                        <div class="metric-box">
                            <div class="metric-lbl">March 2027 Status</div>
                            <div class="metric-val" style="color: #6ee7b7; font-size: 9pt;">Confirmed Open</div>
                            <div class="metric-sub">Available for hold</div>
                        </div>
                    </div>
                </div>

                <div class="hero-photo-wrap">
                    <img src="{hero_img}" alt="{loc['name']}">
                </div>

                <div class="worlds-container">
                    <div class="world-box living">
                        <div class="world-head">
                            <span>🛋️</span>
                            <div>
                                <h4>World 1: Living Room / Lounge</h4>
                                <span class="sub">Friends Group · Character & Warmth</span>
                            </div>
                        </div>
                        <p class="world-desc">{loc['living_summary']}</p>
                        <ul class="feature-ul">
                            {''.join(f'<li>{f}</li>' for f in loc['living_features'])}
                        </ul>
                    </div>

                    <div class="world-box garden">
                        <div class="world-head">
                            <span>🌿</span>
                            <div>
                                <h4>World 2: Garden & Boundary</h4>
                                <span class="sub">Garden Party · Depth & Fence</span>
                            </div>
                        </div>
                        <p class="world-desc">{loc['garden_summary']}</p>
                        <ul class="feature-ul">
                            {''.join(f'<li>{f}</li>' for f in loc['garden_features'])}
                        </ul>
                    </div>
                </div>
            </div>

            <div class="page-footer">
                <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name'].upper()}</span>
                <span>Direct Film Enquiries: jardin@salocations.com · Page {page_num}</span>
            </div>
        </div>
        """)
        page_num += 1

        # PAGE B: Technical Logistics, Spatial Breakdown & Scouting Rate Card
        html_parts.append(f"""
        <div class="pdf-page">
            <div class="page-content">
                <div class="page-header">
                    <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()} - LOGISTICS & SPACES</span>
                    <span class="header-sub">TECHNICAL PRODUCTION SPECIFICATIONS</span>
                </div>

                <div class="logistics-grid">
                    <div class="log-card">
                        <div class="log-title">Unit Base & Parking Capacity</div>
                        <div class="log-item">
                            <span class="k">Technical Parking:</span>
                            <span class="v">{loc['parking']}</span>
                        </div>
                        <div class="log-item">
                            <span class="k">Generator Access:</span>
                            <span class="v">Street & on-site tie-in compliant</span>
                        </div>
                        <div class="log-item">
                            <span class="k">Unit Base Location:</span>
                            <span class="v">Dedicated staging area within 500m</span>
                        </div>
                        <div class="log-item">
                            <span class="k">Catering Setup:</span>
                            <span class="v">Shaded paved area on property</span>
                        </div>
                    </div>

                    <div class="log-card">
                        <div class="log-title">Filming Protocols & Daylight</div>
                        <div class="log-item">
                            <span class="k">Permit Lead Time:</span>
                            <span class="v">5–7 business days (City of Cape Town)</span>
                        </div>
                        <div class="log-item">
                            <span class="k">Restrictions:</span>
                            <span class="v">{loc['restrictions']}</span>
                        </div>
                        <div class="log-item">
                            <span class="k">Daylight Profile:</span>
                            <span class="v">High south & west facing natural light</span>
                        </div>
                        <div class="log-item">
                            <span class="k">Noise Curfew:</span>
                            <span class="v">22:00 residential standard wrap</span>
                        </div>
                    </div>
                </div>

                <div style="margin-bottom: 2.5mm;">
                    <h3 style="font-family: Georgia, serif; font-size: 11pt; color: #fff;">Featured Interior & Exterior Space Highlights</h3>
                    <span style="font-size: 7.5pt; color: #9ba6a1;">Filming zones cleared and screened for camera tracks, lighting rigs, and crew flow</span>
                </div>

                <div class="highlights-grid">
        """)

        for photo in highlight_photos:
            p_img = get_img_src(loc['folder'], photo['file'])
            html_parts.append(f"""
                    <div class="hl-card">
                        <div class="hl-photo">
                            <img src="{p_img}" alt="{photo.get('title', '')}">
                        </div>
                        <div class="hl-caption">
                            <strong>[{photo.get('cat', 'space').upper()}]</strong> {photo.get('title', loc['name'])}
                        </div>
                    </div>
            """)

        html_parts.append(f"""
                </div>
            </div>

            <div class="page-footer">
                <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name'].upper()}</span>
                <span>Production Office: +27 21 000 0000 · jardin@salocations.com · Page {page_num}</span>
            </div>
        </div>
        """)
        page_num += 1

        # PAGE C: Extended High-Resolution Gallery (3x3 Grid)
        html_parts.append(f"""
        <div class="pdf-page">
            <div class="page-content">
                <div class="page-header">
                    <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()} - EXTENDED GALLERY</span>
                    <span class="header-sub">HIGH-RESOLUTION ARCHITECTURAL PERSPECTIVES</span>
                </div>

                <div style="margin-bottom: 3mm;">
                    <h3 style="font-family: Georgia, serif; font-size: 11pt; color: #fff;">Additional Scouting Angles & Spatial Details</h3>
                    <span style="font-size: 7.5pt; color: #9ba6a1;">High-resolution curated angles illustrating authentic British texture and production versatility</span>
                </div>

                <div class="gallery-grid-9">
        """)

        for photo in remaining_photos:
            p_img = get_img_src(loc['folder'], photo['file'])
            html_parts.append(f"""
                    <div class="gallery-card">
                        <div class="gallery-img-wrap">
                            <img src="{p_img}" alt="{photo.get('title', '')}">
                        </div>
                        <div class="gallery-card-cap">
                            <span>{photo.get('title', 'Detail')}</span>
                            <span style="color:#dfb76c; text-transform:uppercase;">{photo.get('cat', 'detail')}</span>
                        </div>
                    </div>
            """)

        html_parts.append(f"""
                </div>
            </div>

            <div class="page-footer">
                <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name'].upper()}</span>
                <span>Full Web Gallery: sal-british-homes.vercel.app · Page {page_num}</span>
            </div>
        </div>
        """)
        page_num += 1

    # 3. PRODUCTION SERVICES & SCOUTING RATE CARDS
    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">SALOCATIONS // PROFESSIONAL SERVICES</span>
                <span class="header-sub">LOCATION SCOUTING & MANAGEMENT RATE CARD</span>
            </div>

            <div style="margin-bottom: 4mm;">
                <h2 style="font-family: Georgia, serif; font-size: 17pt; color: #fff; margin-bottom: 1.5mm;">Location Scouting & Management Services</h2>
                <p style="font-size: 8.5pt; color: #9ba6a1;">
                    Dedicated commercial & film production services for international producers, production designers,
                    and directors shooting in Cape Town and the Western Cape.
                </p>
            </div>

            <table class="rate-card-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Service Package</th>
                        <th style="width: 20%;">Tariff (ZAR)</th>
                        <th style="width: 15%;">Indicative (GBP)</th>
                        <th style="width: 40%;">Scope of Services & Deliverables</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Location Scout Day Rate</strong></td>
                        <td><strong style="color: #dfb76c;">ZAR 5,000 / day</strong></td>
                        <td>~£222 / day</td>
                        <td>Full 10-hour scout day, landowner negotiations, preliminary photography package, access coordination.</td>
                    </tr>
                    <tr>
                        <td><strong>Scout Vehicle & Fuel</strong></td>
                        <td><strong style="color: #dfb76c;">ZAR 1,000 / day</strong></td>
                        <td>~£44 / day</td>
                        <td>4x4 production scout vehicle equipped with scouting equipment, GPS loggers, and fuel allowance.</td>
                    </tr>
                    <tr>
                        <td><strong>Combined Daily Package</strong></td>
                        <td><strong style="color: #dfb76c;">ZAR 6,000 / day</strong></td>
                        <td>~£266 / day</td>
                        <td>Scout + Vehicle + Fuel standard package. Standard rate for official scouting days and technical recces.</td>
                    </tr>
                    <tr>
                        <td><strong>Technical Recce Accompaniment</strong></td>
                        <td><strong style="color: #dfb76c;">ZAR 6,000 / day</strong></td>
                        <td>~£266 / day</td>
                        <td>Director & HOD technical recce navigation, municipal parking coordination, sound & daylight briefings.</td>
                    </tr>
                    <tr>
                        <td><strong>City Film Permit Facilitation</strong></td>
                        <td><strong style="color: #dfb76c;">ZAR 2,500 / permit</strong></td>
                        <td>~£111 / permit</td>
                        <td>Permit processing with City of Cape Town Film Permit Office, traffic management, SAPS & Metro Police sign-offs.</td>
                    </tr>
                </tbody>
            </table>

            <div style="background: #141a18; border-radius: 7px; padding: 4mm 5mm; border: 1px solid rgba(255, 255, 255, 0.08); margin-bottom: 4mm;">
                <h4 style="font-family: Georgia, serif; font-size: 10pt; color: #dfb76c; margin-bottom: 2mm;">Film Permit Lead Times & Standard Working Conditions</h4>
                <ul class="feature-ul">
                    <li><strong>Permit Lead Times:</strong> Standard residential Cape Town locations require 5 to 7 working days for municipal approval.</li>
                    <li><strong>Shooting Hours:</strong> Standard residential hours: 07:00 to 22:00. Night filming permits require neighbor consent waivers.</li>
                    <li><strong>Prep & Strike Tariff:</strong> Standard industry practice is 50% of the daily shoot tariff for prep and de-rig days.</li>
                    <li><strong>Currency Conversion:</strong> Quoted rates converted at indicative benchmark of £1 ≈ ZAR 22.50. Exact invoices rendered in ZAR.</li>
                </ul>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-brand">SALOCATIONS // RATE CARD</span>
            <span>Direct Enquiries: jardin@salocations.com · Page {page_num}</span>
        </div>
    </div>
    """)
    page_num += 1

    # 4. BRIEF ALIGNMENT MATRIX
    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">SALOCATIONS // BRIEF ALIGNMENT MATRIX</span>
                <span class="header-sub">SIDE-BY-SIDE PRODUCTION EVALUATION</span>
            </div>

            <div style="margin-bottom: 3mm;">
                <h2 style="font-family: Georgia, serif; font-size: 15pt; color: #fff; margin-bottom: 1mm;">Brief Alignment Comparison Matrix</h2>
                <p style="font-size: 7.8pt; color: #9ba6a1;">
                    Side-by-side technical evaluation of all {len(locs)} curated properties against the client's creative brief
                    and March 2027 shooting schedule.
                </p>
            </div>

            <table class="matrix-tbl">
                <thead>
                    <tr>
                        <th style="width: 17%;">Option & Area</th>
                        <th style="width: 17%;">British Style / Character</th>
                        <th style="width: 22%;">Living Room Suitability</th>
                        <th style="width: 20%;">Garden Party Lawn</th>
                        <th style="width: 12%;">Day Rate (12h)</th>
                        <th style="width: 12%;">March 2027</th>
                    </tr>
                </thead>
                <tbody>
    """)

    for idx, loc in enumerate(locs):
        html_parts.append(f"""
                    <tr>
                        <td>
                            <strong style="color:#fff; font-size: 8pt;">{loc['name']}</strong><br>
                            <span style="color:#9ba6a1; font-size: 6.8pt;">Option 0{idx+1} · {loc['area']}</span>
                        </td>
                        <td><span class="badge badge-gold" style="font-size: 6.5pt;">{loc['style']}</span></td>
                        <td style="font-size: 7.2pt;">{loc['living_features'][0]}</td>
                        <td style="font-size: 7.2pt;">{loc['garden_features'][0]}</td>
                        <td>
                            <strong style="color:#dfb76c; font-size: 8pt;">{loc.get('gbp_shoot') or loc.get('rate_shoot')}</strong><br>
                            <span style="color:#9ba6a1; font-size: 6.5pt;">{loc.get('zar_shoot', '')}</span>
                        </td>
                        <td><span style="color:#6ee7b7; font-weight:600; font-size: 7.2pt;">✓ Confirmed Open</span></td>
                    </tr>
        """)

    html_parts.append(f"""
                </tbody>
            </table>

            <div class="cta-box">
                <h3>Ready to Confirm or Scout These Locations?</h3>
                <p>
                    We recommend placing a <strong>48-hour first option pencil</strong> on your preferred options immediately
                    to secure priority holds for the March 2027 shooting window.
                </p>
                <div style="font-size: 8.5pt; color: #dfb76c; font-weight: 600; margin-bottom: 2mm;">
                    SALocations / Jardin Roestorff · Cape Town, South Africa
                </div>
                <a class="cta-email" href="mailto:jardin@salocations.com?subject=British%20Homes%20Pitch%20-%20March%202027">
                    Direct Film Enquiries: jardin@salocations.com
                </a>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-brand">SALOCATIONS // COMPARISON MATRIX</span>
            <span>Direct Enquiries: jardin@salocations.com · Page {page_num}</span>
        </div>
    </div>
    """)

    html_parts.append("""
</body>
</html>
    """)

    full_html = "".join(html_parts)

    out_html_path = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\pitch_dossier_printable.html"
    print(f"Writing printable HTML to {out_html_path} ({len(full_html)} bytes)...")
    with open(out_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print("Rendering complete PDF via Playwright Chromium...")
    out_pdf_path = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Location_Pitch_Complete.pdf"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file:///" + os.path.abspath(out_html_path).replace("\\", "/"))
        page.wait_for_timeout(2000)
        page.pdf(
            path=out_pdf_path,
            format="A4",
            landscape=False,
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"}
        )
        browser.close()

    print(f"Generated PDF at {out_pdf_path} ({os.path.getsize(out_pdf_path)} bytes)")

    # Verify with PyMuPDF
    doc = fitz.open(out_pdf_path)
    print(f"Total Pages in generated PDF: {len(doc)}")
    for i, l in enumerate(locs):
        name = l['name']
        pages_found = [p_idx + 1 for p_idx in range(len(doc)) if name.lower() in doc[p_idx].get_text().lower()]
        print(f"  Option 0{i+1}: {name} -> pages {pages_found}")

    # Copy to destination paths
    dests = [
        r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\British_Residential_Homes_Location_Pitch.pdf",
        r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\British_Residential_Homes_Location_Pitch.pdf"
    ]
    for d in dests:
        shutil.copy2(out_pdf_path, d)
        print(f"Copied to {d}")

if __name__ == "__main__":
    main()
