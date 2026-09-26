import json, re, os, subprocess, sys
import fitz

def main():
    source_html = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Standalone.html"
    print(f"Reading {source_html}...")
    with open(source_html, "r", encoding="utf-8") as f:
        content = f.read()

    m_locs = re.search(r"const locations = (\[.*?\]);\s*let currentLocId", content, re.DOTALL)
    m_imgs = re.search(r"const EMBEDDED_IMAGES = (\{.*?\});", content, re.DOTALL)

    if not m_locs or not m_imgs:
        print("Error: Could not extract locations or images from Standalone HTML.")
        sys.exit(1)

    locs = json.loads(m_locs.group(1))
    imgs = json.loads(m_imgs.group(1))
    print(f"Extracted {len(locs)} locations and {len(imgs)} images.")

    def get_img_src(folder, filename):
        key = f"{folder}/{filename}"
        if key in imgs:
            return imgs[key]
        return ""

    # Build HTML document specifically optimized for A4 print-to-pdf
    html_parts = []

    html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>British Residential Homes & Gardens - Location Pitch Dossier</title>
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
            color: #dfb76c;
            font-weight: 600;
        }

        /* Cover Page Styling */
        .cover-hero {
            background: linear-gradient(145deg, #141a18 0%, #1f3d30 100%);
            border: 1px solid rgba(197, 160, 89, 0.4);
            border-left: 5px solid #c5a059;
            border-radius: 8px;
            padding: 7mm 8mm;
            margin-bottom: 6mm;
        }
        .cover-eyebrow {
            font-size: 8pt;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #dfb76c;
            margin-bottom: 2mm;
        }
        .cover-title {
            font-family: Georgia, serif;
            font-size: 24pt;
            line-height: 1.15;
            color: #ffffff;
            margin-bottom: 3mm;
        }
        .cover-subtitle {
            font-size: 10pt;
            color: #dce2de;
            line-height: 1.5;
            max-width: 95%;
        }

        .scope-pills {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 3mm;
            margin-bottom: 6mm;
        }
        .scope-pill {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            padding: 3mm 3.5mm;
        }
        .pill-label {
            font-size: 6.5pt;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #dfb76c;
            margin-bottom: 1mm;
        }
        .pill-val {
            font-size: 8.5pt;
            font-weight: 600;
            color: #ffffff;
        }

        .index-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 3.5mm;
        }
        .index-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            padding: 3.5mm 4mm;
            border-left: 3px solid #c5a059;
        }
        .index-num {
            font-size: 7pt;
            font-weight: 700;
            letter-spacing: 1px;
            color: #dfb76c;
            text-transform: uppercase;
        }
        .index-name {
            font-family: Georgia, serif;
            font-size: 11pt;
            font-weight: 700;
            color: #ffffff;
            margin: 0.5mm 0;
        }
        .index-meta {
            font-size: 7.5pt;
            color: #9ba6a1;
        }
        .index-rate {
            font-size: 8pt;
            font-weight: 600;
            color: #dfb76c;
            margin-top: 1mm;
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
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            padding: 3.5mm 4mm;
        }
        .world-box.living {
            border-left: 3px solid #dfb76c;
        }
        .world-box.garden {
            border-left: 3px solid #489973;
        }
        .world-hdr {
            display: flex;
            align-items: center;
            gap: 2mm;
            margin-bottom: 1.5mm;
        }
        .world-title {
            font-family: Georgia, serif;
            font-size: 10pt;
            font-weight: 700;
            color: #ffffff;
        }
        .world-sub {
            font-size: 7pt;
            color: #dfb76c;
        }
        .world-desc {
            font-size: 8pt;
            color: #9ba6a1;
            margin-bottom: 2mm;
            line-height: 1.35;
        }
        .feature-ul {
            list-style: none;
        }
        .feature-ul li {
            font-size: 7.5pt;
            color: #e0e5e2;
            margin-bottom: 1mm;
            padding-left: 3.5mm;
            position: relative;
            line-height: 1.3;
        }
        .feature-ul li::before {
            content: "•";
            color: #dfb76c;
            position: absolute;
            left: 0;
            font-weight: bold;
        }

        /* Location Logistics & Key Shots (Page B) */
        .specs-table-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 8px;
            padding: 4mm 5mm;
            margin-bottom: 4mm;
        }
        .sec-title {
            font-family: Georgia, serif;
            font-size: 12pt;
            color: #ffffff;
            margin-bottom: 2.5mm;
            display: flex;
            align-items: center;
            gap: 2mm;
        }
        .table-custom {
            width: 100%;
            border-collapse: collapse;
            font-size: 8pt;
        }
        .table-custom tr {
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        .table-custom tr:last-child {
            border-bottom: none;
        }
        .table-custom th {
            text-align: left;
            padding: 1.8mm 2.5mm 1.8mm 0;
            color: #dfb76c;
            font-size: 7.5pt;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            width: 28%;
            vertical-align: top;
        }
        .table-custom td {
            padding: 1.8mm 0;
            color: #dce2de;
            line-height: 1.35;
        }

        .highlight-photos-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 3.5mm;
        }
        .photo-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 6px;
            overflow: hidden;
        }
        .photo-img-wrap {
            height: 48mm;
            background: #000;
            position: relative;
        }
        .photo-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }
        .photo-caption {
            padding: 2mm 3mm;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 7.5pt;
            color: #ffffff;
            background: #141a18;
        }
        .photo-tag {
            font-size: 6.5pt;
            color: #dfb76c;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        /* Extended Gallery Page (Page C) */
        .gallery-3col {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 3mm;
        }
        .gallery-card {
            background: #141a18;
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 5px;
            overflow: hidden;
        }
        .gallery-img-wrap {
            height: 38mm;
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
            font-size: 8pt;
        }
        .matrix-tbl th {
            background: rgba(197, 160, 89, 0.15);
            color: #dfb76c;
            text-align: left;
            padding: 2.5mm 3mm;
            font-size: 7.5pt;
            text-transform: uppercase;
            border-bottom: 1px solid #dfb76c;
        }
        .matrix-tbl td {
            padding: 2.5mm 3mm;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            color: #dce2de;
            vertical-align: middle;
        }

        .cta-box {
            background: linear-gradient(145deg, #141a18 0%, #1f3d30 100%);
            border: 1px solid rgba(197, 160, 89, 0.4);
            border-radius: 8px;
            padding: 6mm 8mm;
            text-align: center;
            margin-top: 4mm;
        }
        .cta-box h3 {
            font-family: Georgia, serif;
            font-size: 15pt;
            color: #ffffff;
            margin-bottom: 1.5mm;
        }
        .cta-box p {
            font-size: 9pt;
            color: #dce2de;
            margin-bottom: 3mm;
        }
        .cta-email {
            display: inline-block;
            background: #c5a059;
            color: #0b0f0e;
            font-size: 10pt;
            font-weight: 700;
            padding: 2.5mm 6mm;
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
                    A curated portfolio of characterful residential properties in Cape Town's premier heritage belts
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
                    <div class="pill-val">Lived-In Group Friends Lounge</div>
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

            <div style="margin-bottom: 3mm;">
                <h3 style="font-family: Georgia, serif; font-size: 12pt; color: #fff;">Curated Location Options Summary</h3>
                <span style="font-size: 8pt; color: #9ba6a1;">All 6 options fully detailed with high-resolution photography, technical specs, and day rates</span>
            </div>

            <div class="index-grid">
    """)

    for idx, loc in enumerate(locs):
        html_parts.append(f"""
                <div class="index-card">
                    <div class="index-num">Option 0{idx+1} // {loc['match_score']}</div>
                    <div class="index-name">{loc['name']}</div>
                    <div class="index-meta">{loc['area']} · {loc['style']}</div>
                    <div class="index-rate">Indicative Shoot Rate: {loc.get('gbp_shoot') or loc.get('rate_shoot')} ({loc.get('zar_shoot', '')})</div>
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

    # 2. DETAIL PAGES FOR EACH OF THE 6 LOCATIONS
    page_num = 2
    for idx, loc in enumerate(locs):
        hero_img = get_img_src(loc['folder'], loc['hero'])
        gallery_items = loc.get('gallery', [])

        # Filter gallery into highlight photos (first 4) and remaining gallery items
        highlight_photos = gallery_items[:4]
        remaining_photos = gallery_items[4:13] # Next 9 photos for clean 3x3 grid

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
                        <div class="world-hdr">
                            <span style="font-size: 11pt;">🛋️</span>
                            <div>
                                <div class="world-title">World 1: Living Room / Lounge</div>
                                <div class="world-sub">Friends Group · Character & Warmth</div>
                            </div>
                        </div>
                        <p class="world-desc">{loc['living_summary']}</p>
                        <ul class="feature-ul">
                            {''.join([f"<li>{f}</li>" for f in loc['living_features']])}
                        </ul>
                    </div>

                    <div class="world-box garden">
                        <div class="world-hdr">
                            <span style="font-size: 11pt;">🌿</span>
                            <div>
                                <div class="world-title">World 2: Garden & Boundary</div>
                                <div class="world-sub">Garden Party · Depth & Fence</div>
                            </div>
                        </div>
                        <p class="world-desc">{loc['garden_summary']}</p>
                        <ul class="feature-ul">
                            {''.join([f"<li>{f}</li>" for f in loc['garden_features']])}
                        </ul>
                    </div>
                </div>
            </div>

            <div class="page-footer">
                <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name']}</span>
                <span>Direct Film Enquiries: jardin@salocations.com · Page {page_num}</span>
            </div>
        </div>
        """)
        page_num += 1

        # PAGE B: Production Logistics Table & Key Photo Highlights
        html_parts.append(f"""
        <div class="pdf-page">
            <div class="page-content">
                <div class="page-header">
                    <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()} - LOGISTICS & KEY SHOTS</span>
                    <span class="header-sub">TECHNICAL SPECIFICATIONS</span>
                </div>

                <div class="specs-table-card">
                    <h3 class="sec-title">📋 Production Logistics & Filming Specifications</h3>
                    <table class="table-custom">
                        <tr>
                            <th>Indicative Day Rates</th>
                            <td>
                                <strong>{loc.get('gbp_shoot') or loc.get('rate_shoot')}</strong> for 12-hour Shoot Day &nbsp;|&nbsp; 
                                <strong>{loc.get('gbp_prep', '50% tariff')}</strong> for 10-hour Prep / Strike Day.<br>
                                <span style="font-size: 7.2pt; color: #9ba6a1;">*Converted at indicative benchmark rate £1 ≈ ZAR 22.50. Exact tariffs subject to contract.</span>
                            </td>
                        </tr>
                        <tr>
                            <th>Scouting & Technical Recce</th>
                            <td>
                                <strong>ZAR 5,000 / day</strong> (~£222) Location Scout &nbsp;|&nbsp; <strong>ZAR 1,000 / day</strong> (~£44) Scout Vehicle & Fuel.<br>
                                Combined daily package: <strong>ZAR 6,000 / day</strong> (~£266 / day).
                            </td>
                        </tr>
                        <tr>
                            <th>March 2027 Availability</th>
                            <td><strong style="color: #6ee7b7;">✓ {loc['availability']}</strong>. 48-hour first option pencil available upon request.</td>
                        </tr>
                        <tr>
                            <th>Permitted Filming Areas</th>
                            <td>{loc['filming_areas']}</td>
                        </tr>
                        <tr>
                            <th>Parking & Crew Access</th>
                            <td>{loc['parking']}</td>
                        </tr>
                        <tr>
                            <th>Restrictions & Curfews</th>
                            <td>{loc['restrictions']}</td>
                        </tr>
                    </table>
                </div>

                <div style="margin-bottom: 2mm;">
                    <h3 style="font-family: Georgia, serif; font-size: 11pt; color: #fff;">Key Architectural & Practical Perspectives</h3>
                </div>

                <div class="highlight-photos-grid">
        """)

        for p_idx, p in enumerate(highlight_photos):
            p_img = get_img_src(loc['folder'], p['file'])
            tag_label = "🛋️ Living Room" if p['cat'] == 'living' else ("🌿 Garden Lawn" if p['cat'] == 'garden' else "🏛️ Facade / Detail")
            html_parts.append(f"""
                    <div class="photo-card">
                        <div class="photo-img-wrap">
                            <img src="{p_img}" alt="{p['title']}">
                        </div>
                        <div class="photo-caption">
                            <span>{p['title']}</span>
                            <span class="photo-tag">{tag_label}</span>
                        </div>
                    </div>
            """)

        html_parts.append(f"""
                </div>
            </div>

            <div class="page-footer">
                <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name']}</span>
                <span>Direct Film Enquiries: jardin@salocations.com · Page {page_num}</span>
            </div>
        </div>
        """)
        page_num += 1

        # PAGE C: Extended Gallery Grid (9 additional high-res photos)
        if remaining_photos:
            html_parts.append(f"""
            <div class="pdf-page">
                <div class="page-content">
                    <div class="page-header">
                        <span class="header-badge">OPTION 0{idx+1} // {loc['name'].upper()} - EXTENDED GALLERY</span>
                        <span class="header-sub">CURATED PHOTOGRAPHIC SURVEY</span>
                    </div>

                    <div style="margin-bottom: 3mm;">
                        <h3 style="font-family: Georgia, serif; font-size: 12pt; color: #fff;">Photographic Gallery · {loc['name']}</h3>
                        <span style="font-size: 7.8pt; color: #9ba6a1;">High-resolution angles showing room depths, lighting transitions, garden boundaries, and architectural textures</span>
                    </div>

                    <div class="gallery-3col">
            """)

            for p in remaining_photos:
                p_img = get_img_src(loc['folder'], p['file'])
                tag_label = "Living" if p['cat'] == 'living' else ("Garden" if p['cat'] == 'garden' else "Exterior")
                html_parts.append(f"""
                        <div class="gallery-card">
                            <div class="gallery-img-wrap">
                                <img src="{p_img}" alt="{p['title']}">
                            </div>
                            <div class="gallery-card-cap">
                                <span>{p['title']}</span>
                                <span style="color: #dfb76c;">{tag_label}</span>
                            </div>
                        </div>
                """)

            html_parts.append(f"""
                    </div>

                    <div style="margin-top: 4mm; background: #141a18; border: 1px solid rgba(197, 160, 89, 0.3); border-radius: 6px; padding: 2.5mm 4mm; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 8pt; color: #dce2de;">Need custom recce photos or 360° video of <strong>{loc['name']}</strong>?</span>
                        <span style="font-size: 8pt; color: #dfb76c; font-weight: 600;">Contact: jardin@salocations.com</span>
                    </div>
                </div>

                <div class="page-footer">
                    <span class="footer-brand">SALOCATIONS // OPTION 0{idx+1} - {loc['name']}</span>
                    <span>Direct Film Enquiries: jardin@salocations.com · Page {page_num}</span>
                </div>
            </div>
            """)
            page_num += 1

    # 3. SCOUTING RATE CARD & PROFESSIONAL SERVICES PAGE
    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">SALOCATIONS // PROFESSIONAL SERVICES</span>
                <span class="header-sub">LOCATION SCOUTING & MANAGEMENT RATE CARD</span>
            </div>

            <div style="margin-bottom: 4mm;">
                <h2 style="font-family: Georgia, serif; font-size: 17pt; color: #fff; margin-bottom: 1.5mm;">Location Scouting & Management Rate Card</h2>
                <p style="font-size: 8.8pt; color: #9ba6a1; line-height: 1.45;">
                    SALocations provides dedicated location scouting, technical recces, contract negotiation, and on-set location management
                    for international feature films, commercials, and photographic productions filming in South Africa.
                </p>
            </div>

            <table class="rate-card-table">
                <thead>
                    <tr>
                        <th style="width: 32%;">Service / Role</th>
                        <th style="width: 25%;">Daily Rate (ZAR)</th>
                        <th style="width: 20%;">Approx. GBP (£)</th>
                        <th>Coverage & Scope</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Location Scout / Manager</strong></td>
                        <td><strong style="color:#dfb76c;">ZAR 5,000 / day</strong></td>
                        <td>~£222 / day</td>
                        <td>10-hour scouting day, property sourcing, curated digital presentation.</td>
                    </tr>
                    <tr>
                        <td><strong>Scout Vehicle & Fuel</strong></td>
                        <td><strong style="color:#dfb76c;">ZAR 1,000 / day</strong></td>
                        <td>~£44 / day</td>
                        <td>Dedicated 4x4 scouting vehicle, fuel allowance up to 150km/day.</td>
                    </tr>
                    <tr>
                        <td><strong>Combined Scouting Package</strong></td>
                        <td><strong style="color:#6ee7b7;">ZAR 6,000 / day</strong></td>
                        <td>~£266 / day</td>
                        <td>Full daily turnkey package: Scout + Vehicle + High-Res Photo Report.</td>
                    </tr>
                    <tr>
                        <td><strong>Technical Recce (Director / DoP)</strong></td>
                        <td><strong style="color:#dfb76c;">ZAR 5,000 / day</strong></td>
                        <td>~£222 / day</td>
                        <td>Full day tech recce accompaniment, sun-tracking, power/logistics plan.</td>
                    </tr>
                    <tr>
                        <td><strong>Municipal Film Permitting</strong></td>
                        <td><strong>ZAR 1,800 / location</strong></td>
                        <td>~£80 / location</td>
                        <td>City of Cape Town film permit application, street parking closures, metro police.</td>
                    </tr>
                    <tr>
                        <td><strong>On-Set Location Manager</strong></td>
                        <td><strong style="color:#dfb76c;">ZAR 5,500 / 12h day</strong></td>
                        <td>~£244 / day</td>
                        <td>Key location manager on set for duration of shoot, prep, and strike.</td>
                    </tr>
                </tbody>
            </table>

            <div style="background: #141a18; border: 1px solid rgba(255,255,255,0.08); border-radius: 7px; padding: 4mm 5mm; margin-top: 4mm;">
                <h4 style="font-family: Georgia, serif; font-size: 10.5pt; color: #dfb76c; margin-bottom: 2mm;">Scouting Deliverables & Guarantee</h4>
                <ul class="feature-ul" style="font-size: 8pt; color: #dce2de;">
                    <li>High-resolution photographic survey delivered via secure private web portal within 24 hours of scout completion.</li>
                    <li>GPS coordinates, sun-path orientation (SunSeeker angles for morning, noon, and golden hour light).</li>
                    <li>Detailed interior measurements, floor plans, electrical capacity, and generator parking coordinates.</li>
                    <li>Initial provisional booking holds placed with property owners at zero cancellation liability.</li>
                </ul>
            </div>
        </div>

        <div class="page-footer">
            <span class="footer-brand">SALOCATIONS // PROFESSIONAL RATE CARD</span>
            <span>Direct Enquiries: jardin@salocations.com · Page {page_num}</span>
        </div>
    </div>
    """)
    page_num += 1

    # 4. BRIEF ALIGNMENT COMPARISON MATRIX PAGE
    html_parts.append(f"""
    <div class="pdf-page">
        <div class="page-content">
            <div class="page-header">
                <span class="header-badge">SALOCATIONS // BRIEF ALIGNMENT MATRIX</span>
                <span class="header-sub">SIDE-BY-SIDE PRODUCTION EVALUATION</span>
            </div>

            <div style="margin-bottom: 4mm;">
                <h2 style="font-family: Georgia, serif; font-size: 17pt; color: #fff; margin-bottom: 1.5mm;">Brief Alignment Comparison Matrix</h2>
                <p style="font-size: 8.5pt; color: #9ba6a1;">
                    Side-by-side technical evaluation of all 6 curated properties against the client's creative brief
                    and March 2027 shooting schedule.
                </p>
            </div>

            <table class="matrix-tbl">
                <thead>
                    <tr>
                        <th style="width: 18%;">Option & Area</th>
                        <th style="width: 18%;">British Style / Character</th>
                        <th style="width: 20%;">Living Room Suitability</th>
                        <th style="width: 18%;">Garden Party Lawn</th>
                        <th style="width: 13%;">Day Rate (12h)</th>
                        <th style="width: 13%;">March 2027</th>
                    </tr>
                </thead>
                <tbody>
    """)

    for idx, loc in enumerate(locs):
        html_parts.append(f"""
                    <tr>
                        <td>
                            <strong style="color:#fff; font-size: 8.5pt;">{loc['name']}</strong><br>
                            <span style="color:#9ba6a1; font-size: 7.2pt;">Option 0{idx+1} · {loc['area']}</span>
                        </td>
                        <td><span class="badge badge-gold" style="font-size: 6.8pt;">{loc['style']}</span></td>
                        <td style="font-size: 7.8pt;">Warm timber, authentic fireplace, seating for friends group</td>
                        <td style="font-size: 7.8pt;">Mature deciduous trees, level lawn, established boundary</td>
                        <td>
                            <strong style="color:#dfb76c; font-size: 8.5pt;">{loc.get('gbp_shoot') or loc.get('rate_shoot')}</strong><br>
                            <span style="color:#9ba6a1; font-size: 6.8pt;">{loc.get('zar_shoot', '')}</span>
                        </td>
                        <td><span style="color:#6ee7b7; font-weight:600; font-size: 7.8pt;">✓ Confirmed Open</span></td>
                    </tr>
        """)

    html_parts.append(f"""
                </tbody>
            </table>

            <div class="cta-box">
                <h3>Ready to Confirm or Scout These Locations?</h3>
                <p>
                    We recommend placing a <strong>48-hour first option pencil</strong> on your preferred 2–3 options immediately
                    to secure priority holds for the March 2027 shooting window.
                </p>
                <div style="font-size: 9pt; color: #dfb76c; font-weight: 600; margin-bottom: 2mm;">
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

    print("Generating PDF via Microsoft Edge headless...")
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    edge = next((p for p in edge_paths if os.path.exists(p)), None)
    if not edge:
        print("Error: msedge.exe not found.")
        sys.exit(1)

    out_pdf_path = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\British_Homes\British_Residential_Homes_Location_Pitch.pdf"
    
    cmd = [
        edge,
        "--headless=new",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out_pdf_path}",
        out_html_path
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Edge execution finished with code {res.returncode}")

    if os.path.exists(out_pdf_path):
        size = os.path.getsize(out_pdf_path)
        print(f"Generated PDF: {out_pdf_path} ({size} bytes)")
        
        # Verify with PyMuPDF
        doc = fitz.open(out_pdf_path)
        print(f"Total Pages in generated PDF: {len(doc)}")
        loc_names = [l['name'] for l in locs]
        for name in loc_names:
            pages_found = [i+1 for i in range(len(doc)) if name.lower() in doc[i].get_text().lower()]
            print(f"  {name}: present on pages {pages_found}")

        # Also copy to artifacts and Pictures folder
        pictures_pdf = r"C:\Users\Jardin\OneDrive\Pictures\English\British_Residential_Homes_Location_Pitch.pdf"
        artifact_pdf = r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\British_Residential_Homes_Location_Pitch.pdf"

        import shutil
        shutil.copy2(out_pdf_path, pictures_pdf)
        shutil.copy2(out_pdf_path, artifact_pdf)
        print(f"Copied updated PDF to {pictures_pdf} and {artifact_pdf}")
    else:
        print("Error: PDF file was not created.")

if __name__ == "__main__":
    main()
