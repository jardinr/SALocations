import os
import json

web_dir = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\zen-mirage-media-web"
data_path = os.path.join(web_dir, "embedded_data.json")

with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

embedded_images = data["images"]
categories = data["categories"]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cape Town Location Scouting & Production Services Proposal | Zencrew & Mirage Media</title>
    <meta name="description" content="Feature Film Production Location Scouting & Fixer Proposal for Mirage Media (Pranav Pingle Reddy), presented by Zencrew (Laura Diana Macleod) & SA Locations. 9 curated location categories and premier studio soundstages.">

    <!-- Open Graph / WhatsApp / LinkedIn / iMessage -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Mirage Media Feature Film Proposal · Cape Town Locations & Studios">
    <meta property="og:description" content="Curated Cape Town locations, Blackwood Cabin, and premier studio soundstages matching director visual references. Presented by Zencrew (Laura Diana Macleod) & SA Locations.">
    <meta property="og:image" content="https://zen-mirage-media.vercel.app/og-preview.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800&family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --bg: #090d0b;
            --surface: #101614;
            --surface-card: #16201c;
            --surface-hover: #1e2c26;
            --border: rgba(255, 255, 255, 0.08);
            --border-highlight: rgba(212, 175, 55, 0.4);
            --text-main: #f5f6f4;
            --text-muted: #9ba7a1;
            --gold: #d4af37;
            --gold-bright: #f3ce63;
            --gold-glow: rgba(212, 175, 55, 0.15);
            --emerald: #1f4233;
            --emerald-accent: #2e664e;
            --cyan: #38ef7d;
            --font-serif: 'Cinzel', Georgia, serif;
            --font-sans: 'Inter', -apple-system, sans-serif;
            --font-tech: 'Space Grotesk', monospace, sans-serif;
            --radius: 12px;
            --shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            background-color: var(--bg);
            color: var(--text-main);
            font-family: var(--font-sans);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
        }

        /* Top Navigation */
        header.top-nav {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(9, 13, 11, 0.94);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            padding: 0.9rem 2.25rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1.5rem;
        }
        .nav-brand {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .brand-badge {
            font-family: var(--font-tech);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            padding: 0.35rem 0.75rem;
            background: var(--emerald);
            color: var(--gold-bright);
            border: 1px solid var(--gold);
            border-radius: 4px;
        }
        .brand-title {
            font-family: var(--font-tech);
            font-size: 0.95rem;
            font-weight: 700;
            letter-spacing: 1px;
            color: var(--text-main);
        }
        .brand-sub {
            font-size: 0.78rem;
            color: var(--text-muted);
        }
        .nav-actions {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-wrap: wrap;
        }
        .btn-nav {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.5rem 1rem;
            font-family: var(--font-sans);
            font-size: 0.82rem;
            font-weight: 600;
            text-decoration: none;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 1px solid var(--border);
            background: var(--surface-card);
            color: var(--text-main);
        }
        .btn-nav:hover {
            background: var(--surface-hover);
            border-color: var(--gold);
            color: var(--gold-bright);
        }
        .btn-nav.primary {
            background: var(--gold);
            color: #080c0b;
            border-color: var(--gold);
            font-weight: 700;
        }
        .btn-nav.primary:hover {
            background: var(--gold-bright);
            transform: translateY(-1px);
        }

        /* Container */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2.5rem 2rem;
        }

        /* Executive Hero Banner */
        .proposal-hero {
            background: linear-gradient(145deg, rgba(16, 22, 20, 0.98), rgba(31, 66, 51, 0.35));
            border: 1px solid var(--border);
            border-left: 4px solid var(--gold);
            border-radius: var(--radius);
            padding: 2.75rem;
            margin-bottom: 3rem;
            position: relative;
            box-shadow: var(--shadow);
        }
        .hero-tagline {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-family: var(--font-tech);
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: var(--gold);
            margin-bottom: 0.85rem;
        }
        .proposal-hero h1 {
            font-family: var(--font-serif);
            font-size: 2.85rem;
            font-weight: 800;
            line-height: 1.15;
            color: #ffffff;
            margin-bottom: 1rem;
            letter-spacing: 0.5px;
        }
        .hero-client {
            font-family: var(--font-tech);
            font-size: 1.05rem;
            color: var(--gold-bright);
            margin-bottom: 1.25rem;
            font-weight: 600;
        }
        .hero-desc {
            font-size: 1.1rem;
            color: var(--text-muted);
            max-width: 1040px;
            margin-bottom: 2rem;
            line-height: 1.7;
        }
        .hero-desc strong {
            color: var(--text-main);
        }

        /* Scope Pills */
        .scope-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 1rem;
            border-top: 1px solid var(--border);
            padding-top: 1.75rem;
        }
        .scope-item {
            background: rgba(0, 0, 0, 0.3);
            padding: 1rem 1.2rem;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .scope-label {
            font-family: var(--font-tech);
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--gold);
            margin-bottom: 0.35rem;
        }
        .scope-val {
            font-size: 0.95rem;
            font-weight: 600;
            color: #ffffff;
        }

        /* Location Tabs */
        .section-header {
            margin-bottom: 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            flex-wrap: wrap;
            gap: 1rem;
        }
        .section-title {
            font-family: var(--font-serif);
            font-size: 1.95rem;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        .section-subtitle {
            font-size: 0.95rem;
            color: var(--text-muted);
        }

        .category-tabs {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 0.75rem;
            margin-bottom: 2.5rem;
        }
        .tab-btn {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1rem 0.9rem;
            text-align: left;
            cursor: pointer;
            transition: all 0.25s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            gap: 0.3rem;
        }
        .tab-btn:hover {
            background: var(--surface-hover);
            border-color: var(--border-highlight);
            transform: translateY(-2px);
        }
        .tab-btn.active {
            background: var(--surface-card);
            border-color: var(--gold);
            box-shadow: 0 0 24px var(--gold-glow);
        }
        .tab-btn.active::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: var(--gold);
        }
        .tab-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .tab-num {
            font-family: var(--font-tech);
            font-size: 0.68rem;
            font-weight: 700;
            color: var(--gold);
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }
        .tab-icon {
            font-size: 1.15rem;
        }
        .tab-name {
            font-family: var(--font-serif);
            font-size: 0.95rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.25;
            margin-top: 0.2rem;
        }
        .tab-score {
            font-family: var(--font-tech);
            font-size: 0.65rem;
            font-weight: 700;
            padding: 0.2rem 0.45rem;
            border-radius: 3px;
            background: rgba(212, 175, 55, 0.15);
            color: var(--gold-bright);
            align-self: flex-start;
            margin-top: 0.25rem;
        }

        /* Detail Panel */
        .category-panel {
            display: none;
            animation: fadeIn 0.35s ease-out forwards;
        }
        .category-panel.active {
            display: block;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Category Hero Card */
        .cat-hero-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 2.25rem;
            margin-bottom: 2rem;
            box-shadow: var(--shadow);
        }
        .cat-hero-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 1.5rem;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid var(--border);
            padding-bottom: 1.25rem;
        }
        .cat-hero-title h2 {
            font-family: var(--font-serif);
            font-size: 2.2rem;
            color: #ffffff;
            line-height: 1.2;
            margin-bottom: 0.4rem;
        }
        .cat-meta-pills {
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            align-items: center;
        }
        .meta-pill {
            font-family: var(--font-tech);
            font-size: 0.78rem;
            padding: 0.3rem 0.75rem;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-main);
            border: 1px solid var(--border);
        }
        .meta-pill.gold {
            background: rgba(212, 175, 55, 0.12);
            color: var(--gold-bright);
            border-color: rgba(212, 175, 55, 0.35);
            font-weight: 700;
        }
        .meta-pill.green {
            background: rgba(46, 213, 115, 0.12);
            color: #2ed573;
            border-color: rgba(46, 213, 115, 0.3);
            font-weight: 600;
        }
        .cat-tagline {
            font-size: 1.15rem;
            color: #e5ece8;
            margin-bottom: 1rem;
            line-height: 1.6;
            font-weight: 400;
        }
        .cat-synopsis {
            font-size: 0.98rem;
            color: var(--text-muted);
            margin-bottom: 1.5rem;
            line-height: 1.7;
        }

        /* Side-by-Side Reference vs Match Section */
        .comparison-section {
            margin-bottom: 2rem;
        }
        .comparison-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.75rem;
        }
        .comparison-card {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: border-color 0.2s ease;
        }
        .comparison-card:hover {
            border-color: var(--border-highlight);
        }
        .comparison-card.ref-card {
            border-left: 4px solid #e06c75;
        }
        .comparison-card.match-card {
            border-left: 4px solid var(--gold);
        }
        .comp-header {
            padding: 1.25rem 1.5rem;
            background: rgba(0, 0, 0, 0.25);
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .comp-badge {
            font-family: var(--font-tech);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            padding: 0.25rem 0.6rem;
            border-radius: 4px;
        }
        .ref-card .comp-badge {
            background: rgba(224, 108, 117, 0.18);
            color: #ff7b86;
            border: 1px solid rgba(224, 108, 117, 0.35);
        }
        .match-card .comp-badge {
            background: rgba(212, 175, 55, 0.18);
            color: var(--gold-bright);
            border: 1px solid rgba(212, 175, 55, 0.35);
        }
        .comp-sub {
            font-size: 0.78rem;
            color: var(--text-muted);
        }
        .comp-img-wrap {
            position: relative;
            aspect-ratio: 16/10;
            background: #000;
            cursor: pointer;
            overflow: hidden;
        }
        .comp-img-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.35s ease;
        }
        .comp-img-wrap:hover img {
            transform: scale(1.03);
        }
        .comp-img-caption {
            padding: 1rem 1.5rem;
            font-size: 0.92rem;
            color: #dbe4df;
            line-height: 1.5;
            background: var(--surface-card);
            flex-grow: 1;
        }

        /* Features & Logistics Row */
        .details-grid {
            display: grid;
            grid-template-columns: 1.1fr 1fr;
            gap: 1.75rem;
            margin-bottom: 2.25rem;
        }
        .features-box, .specs-box {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 2rem;
        }
        .box-title {
            font-family: var(--font-serif);
            font-size: 1.3rem;
            color: #ffffff;
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }
        .feature-list {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }
        .feature-list li {
            font-size: 0.92rem;
            color: #dbe4df;
            display: flex;
            align-items: flex-start;
            gap: 0.65rem;
            line-height: 1.5;
        }
        .feature-list li::before {
            content: '✓';
            color: var(--gold);
            font-weight: bold;
            font-size: 0.9rem;
            margin-top: 0.1rem;
        }

        .specs-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
        }
        .specs-table tr {
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        .specs-table tr:last-child {
            border-bottom: none;
        }
        .specs-table th {
            text-align: left;
            padding: 0.85rem 1rem 0.85rem 0;
            color: var(--gold);
            font-family: var(--font-tech);
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            width: 32%;
            vertical-align: top;
        }
        .specs-table td {
            padding: 0.85rem 0;
            color: #dbe4df;
            line-height: 1.5;
        }

        /* Gallery Section */
        .gallery-section {
            margin-bottom: 3.5rem;
        }
        .gallery-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.25rem;
            flex-wrap: wrap;
            gap: 0.75rem;
        }
        .filter-pills {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        .filter-pill {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border);
            padding: 0.4rem 0.9rem;
            border-radius: 50px;
            font-size: 0.8rem;
            font-family: var(--font-tech);
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.2s;
        }
        .filter-pill:hover, .filter-pill.active {
            background: var(--gold);
            color: #080c0b;
            border-color: var(--gold);
            font-weight: 700;
        }
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.25rem;
        }
        .gallery-item {
            position: relative;
            aspect-ratio: 3/2;
            border-radius: 8px;
            overflow: hidden;
            background: #000;
            border: 1px solid var(--border);
            cursor: pointer;
            transition: transform 0.25s, border-color 0.25s;
        }
        .gallery-item:hover {
            transform: translateY(-3px);
            border-color: var(--gold);
            box-shadow: 0 10px 24px rgba(0,0,0,0.5);
        }
        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .item-caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.92) 0%, rgba(0,0,0,0.7) 70%, transparent 100%);
            padding: 1.5rem 1rem 0.75rem 1rem;
            font-size: 0.82rem;
            color: #fff;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            gap: 0.5rem;
        }
        .item-source-tag {
            font-family: var(--font-tech);
            font-size: 0.65rem;
            font-weight: 700;
            padding: 0.15rem 0.45rem;
            border-radius: 3px;
            text-transform: uppercase;
            flex-shrink: 0;
        }
        .tag-ref {
            background: rgba(224, 108, 117, 0.25);
            color: #ff9aa2;
            border: 1px solid rgba(224, 108, 117, 0.4);
        }
        .tag-scouted {
            background: rgba(46, 213, 115, 0.2);
            color: #5af09a;
            border: 1px solid rgba(46, 213, 115, 0.4);
        }

        /* Fixer & Services Rate Card */
        .services-card {
            background: linear-gradient(145deg, rgba(16, 22, 20, 0.98), rgba(24, 34, 30, 0.95));
            border: 1px solid var(--border-highlight);
            border-radius: var(--radius);
            padding: 2.5rem;
            margin-bottom: 3.5rem;
            box-shadow: var(--shadow);
        }
        .services-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 1.5rem;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--border);
            padding-bottom: 1.5rem;
        }
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-bottom: 1.75rem;
        }
        .service-box {
            background: rgba(0, 0, 0, 0.35);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.6rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .service-box.featured {
            background: rgba(212, 175, 55, 0.08);
            border-color: var(--gold);
            position: relative;
        }
        .service-badge {
            font-family: var(--font-tech);
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--gold);
            margin-bottom: 0.5rem;
        }
        .service-price {
            font-size: 1.75rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.75rem;
            display: flex;
            align-items: baseline;
            gap: 0.5rem;
        }
        .service-price span.sub {
            font-size: 0.95rem;
            color: var(--gold-bright);
            font-weight: 600;
        }
        .service-desc {
            font-size: 0.88rem;
            color: var(--text-muted);
            line-height: 1.55;
        }

        /* Footer Banner Section */
        .executive-footer {
            margin-top: 4rem;
            margin-bottom: 2rem;
            border-radius: var(--radius);
            overflow: hidden;
            border: 1px solid var(--border-highlight);
            box-shadow: 0 20px 50px rgba(0,0,0,0.8);
            background: #000;
        }
        .footer-banner-img {
            width: 100%;
            height: auto;
            display: block;
        }
        .footer-interactive-bar {
            background: #0c1210;
            border-top: 1px solid var(--border);
            padding: 1.75rem 2.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1.5rem;
        }
        .footer-contacts {
            display: flex;
            gap: 1.25rem;
            align-items: center;
            flex-wrap: wrap;
        }
        .footer-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-family: var(--font-sans);
            font-size: 0.88rem;
            color: var(--text-main);
            text-decoration: none;
            transition: color 0.2s;
        }
        .footer-link:hover {
            color: var(--gold-bright);
        }
        .footer-actions {
            display: flex;
            gap: 0.85rem;
            align-items: center;
            flex-wrap: wrap;
        }

        /* Lightbox */
        .lightbox {
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0, 0, 0, 0.94);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            padding: 2rem;
        }
        .lightbox.active {
            display: flex;
        }
        .lightbox-close {
            position: absolute;
            top: 1.5rem;
            right: 2rem;
            background: none;
            border: none;
            color: #fff;
            font-size: 2.2rem;
            cursor: pointer;
            z-index: 1001;
            transition: color 0.2s;
        }
        .lightbox-close:hover { color: var(--gold); }
        .lightbox-img-wrap {
            max-width: 90vw;
            max-height: 80vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .lightbox-img-wrap img {
            max-width: 100%;
            max-height: 80vh;
            object-fit: contain;
            border-radius: 6px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8);
        }
        .lightbox-nav {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            width: 52px;
            height: 52px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            font-size: 1.4rem;
            transition: all 0.2s;
        }
        .lightbox-nav:hover {
            background: var(--gold);
            color: #000;
        }
        .lightbox-nav.prev { left: 2rem; }
        .lightbox-nav.next { right: 2rem; }
        .lightbox-caption {
            margin-top: 1.25rem;
            font-family: var(--font-sans);
            color: #e5ece8;
            font-size: 1rem;
            text-align: center;
            max-width: 800px;
        }
        .lightbox-counter {
            font-family: var(--font-tech);
            font-size: 0.82rem;
            color: var(--gold);
            margin-top: 0.35rem;
        }

        @media (max-width: 900px) {
            header.top-nav { padding: 1rem; flex-direction: column; align-items: flex-start; }
            .proposal-hero { padding: 1.75rem; }
            .proposal-hero h1 { font-size: 2.1rem; }
            .comparison-grid { grid-template-columns: 1fr; }
            .details-grid { grid-template-columns: 1fr; }
            .lightbox-nav { display: none; }
            .footer-interactive-bar { flex-direction: column; align-items: flex-start; }
        }
    </style>
</head>
<body>

    <!-- Top Navigation -->
    <header class="top-nav">
        <div class="nav-brand">
            <span class="brand-badge">ZENCREW // LOCATIONS</span>
            <div>
                <div class="brand-title">Mirage Media Production Proposal</div>
                <div class="brand-sub">Cape Town Scouting & Production Services · 2026/2027</div>
            </div>
        </div>
        <div class="nav-actions">
            <a href="#categories" class="btn-nav">📍 Locations & Studios</a>
            <a href="#services" class="btn-nav">📋 Fixer & Services</a>
            <button class="btn-nav" onclick="window.print()">🖨️ Print / Save PDF</button>
            <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Location+Scouting+%26+Technical+Recce+-+Mirage+Media+%28Cape+Town%29&details=Location+Scouting+%26+Technical+Recce+with+Laura+Diana+Macleod+%28Zencrew%29+%26+Jardin+Roestorff+%28SA+Locations%29.%0A%0AClient%3A+Mirage+Media+%28Pranav+Pingle+Reddy%29%0AProject%3A+Feature+Film+Production+Locations+%26+Studios%0ACovering%3A+9+Curated+Categories+%28Live+Music+Cafe%2C+Chapman%27s+Peak+Drive%2C+Hero+House%2C+MTB+Trails%2C+Blackwood+Cabin%2C+Nightclubs%2C+Woodstock+Lofts%2C+V%26A+Waterfront%2C+Soundstages%29%0AWeb+Dossier%3A+https%3A%2F%2Fzen-mirage-media.vercel.app%0AContacts%3A+laura%40zencrew.co.za+%28%2B27+82+570+8818%29+%7C+jardin%40salocations.com&location=Cape+Town%2C+South+Africa&add=laura%40zencrew.co.za&add=jardinr%40gmail.com" target="_blank" rel="noopener noreferrer" class="btn-nav" style="border-color: var(--gold); color: var(--gold-bright); font-weight: 700;">📅 Book Recce (Cal)</a>
            <a href="mailto:laura@zencrew.co.za?cc=jardin@salocations.com&subject=Mirage%20Media%20Feature%20Film%20-%20Cape%20Town%20Locations%20Inquiry" class="btn-nav primary">✉️ Contact Laura</a>
        </div>
    </header>

    <div class="container">

        <!-- Executive Hero Banner -->
        <section class="proposal-hero">
            <div class="hero-tagline">🎬 Feature Film Production Proposal · Cape Town 2026/2027</div>
            <h1>Cape Town Location Scouting & Production Services</h1>
            <div class="hero-client">Prepared for Mirage Media · Attn: Pranav Pingle Reddy</div>
            <p class="hero-desc">
                Welcome Pranav and the Mirage Media creative team. Following review of your visual reference material (<strong>chinni loc refs</strong>), 
                <strong>Zencrew</strong>, led by Location Manager & Producer <strong>Laura Diana Macleod</strong> in technical collaboration with 
                <strong>Jardin Roestorff (SA Locations)</strong>, has curated Cape Town's premier matched locations, coastal drives, rustic forest cabins 
                (including the newly featured <strong>Blackwood Cabin</strong>), and world-class studio soundstages. Each category below directly pairs 
                your director references with real-world, camera-ready Cape Town production environments.
            </p>

            <div class="scope-grid">
                <div class="scope-item">
                    <div class="scope-label">Curated Scope</div>
                    <div class="scope-val">9 Categories (Refs + Matched Locations + Studios)</div>
                </div>
                <div class="scope-item">
                    <div class="scope-label">Visual Alignment</div>
                    <div class="scope-val">100% Match to Director Moodboard</div>
                </div>
                <div class="scope-item">
                    <div class="scope-label">Featured Locations</div>
                    <div class="scope-val">Stardust, Chapman's Peak, Blackwood Cabin, V&A</div>
                </div>
                <div class="scope-item">
                    <div class="scope-label">Studio Infrastructure</div>
                    <div class="scope-val">Roodebloem, Studio 107, Milestone ADR, CTFS</div>
                </div>
                <div class="scope-item">
                    <div class="scope-label">Production Support</div>
                    <div class="scope-val">Full Fixer, Permitting, Gear & Crew Sourcing</div>
                </div>
            </div>
        </section>

        <!-- Location Selector Section -->
        <div class="section-header" id="categories">
            <div>
                <h2 class="section-title">Curated Location & Studio Categories</h2>
                <div class="section-subtitle">Select a category to view the Director's Visual Reference side-by-side with Cape Town matched scouting photography</div>
            </div>
        </div>

        <!-- 9 Category Tabs -->
        <nav class="category-tabs" id="categoryTabs">
            <!-- Populated via script -->
        </nav>

        <!-- Category Detail Panels -->
        <div id="categoryPanels">
            <!-- Populated via script -->
        </div>

        <!-- Comprehensive Fixer & Services Rate Card -->
        <section class="services-card" id="services">
            <div class="services-header">
                <div>
                    <span class="brand-badge" style="margin-bottom: 0.5rem; display: inline-block;">ZENCREW // COMPREHENSIVE PRODUCTION SERVICES</span>
                    <h2 class="section-title" style="font-size: 1.85rem; margin-top: 0.35rem;">Cape Town Production Fixer & Location Management</h2>
                    <p style="color: var(--text-muted); font-size: 0.95rem; margin-top: 0.25rem;">End-to-end production support for international feature films, commercials, and high-end episodic productions</p>
                </div>
                <div style="text-align: right;">
                    <div style="font-family: var(--font-tech); font-size: 0.75rem; color: var(--gold); text-transform: uppercase; letter-spacing: 1px;">Direct Liaison</div>
                    <div style="font-weight: 700; color: #fff; font-size: 1.1rem;">Laura Diana Macleod</div>
                    <a href="mailto:laura@zencrew.co.za" style="color: var(--gold-bright); font-size: 0.85rem; text-decoration: none;">laura@zencrew.co.za</a>
                </div>
            </div>

            <div class="services-grid">
                <!-- Service 1 -->
                <div class="service-box">
                    <div>
                        <div class="service-badge">Location Scouting & Recces</div>
                        <div class="service-price">ZAR 6,000 <span class="sub">/ day (~£266)</span></div>
                        <p class="service-desc">
                            Full-day dedicated location scout / manager with 4x4 technical vehicle, fuel, drone capability (where permitted), GPS tagging, and high-resolution photo dossiers.
                        </p>
                    </div>
                </div>

                <!-- Service 2 -->
                <div class="service-box featured">
                    <div>
                        <div class="service-badge">Location Management & Permitting</div>
                        <div class="service-price">ZAR 7,500 <span class="sub">/ shoot day</span></div>
                        <p class="service-desc">
                            Complete City of Cape Town Film Permit Office liaison, SANParks environmental permits (Table Mountain, Chapman's Peak), road closures, police traffic escorts, and neighborhood notifications.
                        </p>
                    </div>
                </div>

                <!-- Service 3 -->
                <div class="service-box">
                    <div>
                        <div class="service-badge">Production Fixer & Unit Support</div>
                        <div class="service-price">Custom Tier <span class="sub">per production</span></div>
                        <p class="service-desc">
                            Comprehensive local fixing: department head sourcing (DP, Gaffer, Art Director, Wardrobe), camera/lighting gear hire (Panavision, Media Film Service), catering, and transport fleets.
                        </p>
                    </div>
                </div>

                <!-- Service 4 -->
                <div class="service-box">
                    <div>
                        <div class="service-badge">Studio & Soundstage Coordination</div>
                        <div class="service-price">Direct Rate <span class="sub">zero markup</span></div>
                        <p class="service-desc">
                            Preferential booking coordination for Cape Town Film Studios, Atlantic Studios, Roodebloem daylight cycloramas, and Milestone acoustic ADR/scoring facilities.
                        </p>
                    </div>
                </div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; background: rgba(0, 0, 0, 0.3); padding: 1.1rem 1.4rem; border-radius: 6px; font-size: 0.88rem;">
                <span style="color: var(--text-muted);">* All services tailored to Mirage Media's shooting block and episodic schedule in Cape Town.</span>
                <div style="display: flex; gap: 0.85rem; align-items: center; flex-wrap: wrap;">
                    <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Production+Planning+Meeting+-+Mirage+Media+%26+Zencrew&details=Production+Planning+%26+Scouting+Session+with+Laura+Diana+Macleod+%28Zencrew%29+and+Jardin+Roestorff+%28SA+Locations%29.%0A%0AClient%3A+Mirage+Media+%28Pranav+Pingle+Reddy%29%0AProject%3A+Feature+Film+Production+Locations+%26+Studios%0ACovering%3A+9+Curated+Categories%0AWeb+Dossier%3A+https%3A%2F%2Fzen-mirage-media.vercel.app&location=Cape+Town%2C+South+Africa&add=laura%40zencrew.co.za&add=jardinr%40gmail.com" target="_blank" rel="noopener noreferrer" class="btn-nav primary" style="background: var(--gold); color: #080c0b; font-weight: 700;">
                        📅 Schedule Production Call (Google Cal)
                    </a>
                    <a href="mailto:laura@zencrew.co.za?cc=jardin@salocations.com&subject=Mirage%20Media%20Production%20Support%20Inquiry" class="btn-nav">
                        ✉️ Email Inquiries
                    </a>
                </div>
            </div>
        </section>

        <!-- Executive Footer Banner -->
        <section class="executive-footer">
            <!-- Full Width Laura-Zen Banner Image -->
            <img class="footer-banner-img" id="footerBannerImg" src="" alt="Laura Diana Macleod - Zencrew Location Manager, Scouting, Producer, Fixer">

            <div class="footer-interactive-bar">
                <div class="footer-contacts">
                    <a href="tel:+27825708818" class="footer-link">
                        <span>📞</span> <strong>+27 82 570 8818</strong>
                    </a>
                    <a href="mailto:laura@zencrew.co.za" class="footer-link">
                        <span>✉️</span> <strong>laura@zencrew.co.za</strong>
                    </a>
                    <a href="https://www.zencrew.co.za/" target="_blank" rel="noopener noreferrer" class="footer-link">
                        <span>🌐</span> www.zencrew.co.za
                    </a>
                    <a href="https://www.linkedin.com/in/laura-diana-macleod-a217a525" target="_blank" rel="noopener noreferrer" class="footer-link">
                        <span>🔗</span> LinkedIn
                    </a>
                    <a href="https://www.imdb.com/name/nm2555501" target="_blank" rel="noopener noreferrer" class="footer-link">
                        <span>🎬</span> IMDb
                    </a>
                    <a href="https://itff.africa/meet-the-team-2/" target="_blank" rel="noopener noreferrer" class="footer-link">
                        <span>🏆</span> ITFF Africa
                    </a>
                </div>

                <div class="footer-actions">
                    <span style="font-size: 0.82rem; color: var(--text-muted);">Technical Scouting Partner: <strong style="color: var(--gold);">Jardin Roestorff (SA Locations)</strong></span>
                    <a href="mailto:jardin@salocations.com" style="color: var(--gold-bright); font-size: 0.82rem; text-decoration: none;">jardin@salocations.com</a>
                </div>
            </div>
        </section>

        <footer style="text-align: center; font-size: 0.75rem; color: #5a6660; margin: 2rem 0; font-family: var(--font-tech); letter-spacing: 1px;">
            CONFIDENTIAL FILM PRODUCTION PROPOSAL · PREPARED FOR MIRAGE MEDIA · ZENCREW & SALOCATIONS · CAPE TOWN 2026 / 2027
        </footer>

    </div>

    <!-- Lightbox Modal -->
    <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
        <button class="lightbox-close" onclick="closeLightboxDirect()">&times;</button>
        <button class="lightbox-nav prev" onclick="prevLightbox(event)">&#10094;</button>
        <div class="lightbox-img-wrap" onclick="event.stopPropagation()">
            <img id="lightboxImg" src="" alt="">
        </div>
        <button class="lightbox-nav next" onclick="nextLightbox(event)">&#10095;</button>
        <div class="lightbox-caption" id="lightboxCaption"></div>
        <div class="lightbox-counter" id="lightboxCounter"></div>
    </div>

    <script>
        const categories = __CATEGORIES_JSON__;
        const EMBEDDED_IMAGES = __IMAGES_JSON__;

        function getImgUrl(filename) {
            if (EMBEDDED_IMAGES[filename]) {
                return EMBEDDED_IMAGES[filename];
            }
            return filename;
        }

        let currentCatId = categories[0].id;
        let activeGallery = [];
        let currentLightboxIndex = 0;

        function initApp() {
            // Set footer banner
            if (EMBEDDED_IMAGES["footer_banner"]) {
                document.getElementById('footerBannerImg').src = EMBEDDED_IMAGES["footer_banner"];
            }

            renderTabs();
            renderPanels();
            switchCategory(categories[0].id);

            // Lightbox Keyboard Navigation
            document.addEventListener('keydown', (e) => {
                const lb = document.getElementById('lightbox');
                if (lb.classList.contains('active')) {
                    if (e.key === 'Escape') closeLightboxDirect();
                    if (e.key === 'ArrowLeft') prevLightbox();
                    if (e.key === 'ArrowRight') nextLightbox();
                }
            });
        }

        function renderTabs() {
            const container = document.getElementById('categoryTabs');
            container.innerHTML = categories.map((cat, idx) => `
                <button class="tab-btn ${idx === 0 ? 'active' : ''}" id="tab-${cat.id}" onclick="switchCategory('${cat.id}')">
                    <div class="tab-top">
                        <span class="tab-num">Option ${cat.num}</span>
                        <span class="tab-icon">${cat.icon}</span>
                    </div>
                    <div class="tab-name">${cat.title}</div>
                    <div class="tab-score">${cat.match_score}</div>
                </button>
            `).join('');
        }

        function renderPanels() {
            const container = document.getElementById('categoryPanels');
            container.innerHTML = categories.map((cat, idx) => `
                <div class="category-panel ${idx === 0 ? 'active' : ''}" id="panel-${cat.id}">
                    
                    <!-- Header Card -->
                    <div class="cat-hero-card">
                        <div class="cat-hero-header">
                            <div class="cat-hero-title">
                                <div class="cat-meta-pills" style="margin-bottom: 0.5rem;">
                                    <span class="meta-pill gold">${cat.icon} Option ${cat.num}</span>
                                    <span class="meta-pill">📍 ${cat.area}</span>
                                    <span class="meta-pill green">${cat.match_score}</span>
                                </div>
                                <h2>${cat.title}</h2>
                            </div>
                            <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
                                <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Location+Recce%3A+${encodeURIComponent(cat.title)}+%28Cape+Town%29&details=Technical+Recce+booking+for+Mirage+Media+Feature+Film.%0A%0ACategory%3A+${encodeURIComponent(cat.title)}%0AArea%3A+${encodeURIComponent(cat.area)}%0AMatch%3A+${encodeURIComponent(cat.match_heading)}%0AWeb+Dossier%3A+https%3A%2F%2Fzen-mirage-media.vercel.app&location=${encodeURIComponent(cat.area)}&add=laura%40zencrew.co.za&add=jardinr%40gmail.com" target="_blank" rel="noopener noreferrer" class="btn-nav primary" style="background: var(--gold); color: #080c0b; font-weight: 700;">
                                    📅 Schedule Recce (Google Cal)
                                </a>
                                <a href="mailto:laura@zencrew.co.za?cc=jardin@salocations.com&subject=Mirage%20Media%20Inquiry%20-%20${encodeURIComponent(cat.title)}" class="btn-nav">
                                    📩 Inquire on Category
                                </a>
                            </div>
                        </div>

                        <p class="cat-tagline">${cat.tagline}</p>
                        <p class="cat-synopsis">${cat.creative_synopsis}</p>

                        <!-- Side by Side Reference vs Scouted Match -->
                        <div class="comparison-section">
                            <div class="comparison-grid">
                                
                                <!-- Left: Director's Visual Reference -->
                                <div class="comparison-card ref-card">
                                    <div class="comp-header">
                                        <div>
                                            <span class="comp-badge">Director's Visual Reference</span>
                                            <div class="comp-sub" style="margin-top: 0.2rem;">From Project Reference Moodboard</div>
                                        </div>
                                        <span style="font-family: var(--font-tech); font-size: 0.75rem; color: #ff9aa2;">REFERENCE</span>
                                    </div>
                                    <div class="comp-img-wrap" onclick="openLightboxSingle('${cat.ref_hero}', '${cat.ref_hero_title}')">
                                        <img src="${getImgUrl(cat.ref_hero)}" alt="${cat.ref_hero_title}">
                                    </div>
                                    <div class="comp-img-caption">
                                        <strong>Creative Intent:</strong> ${cat.ref_hero_title}
                                    </div>
                                </div>

                                <!-- Right: Matched Cape Town Location -->
                                <div class="comparison-card match-card">
                                    <div class="comp-header">
                                        <div>
                                            <span class="comp-badge">Cape Town Scouted Match</span>
                                            <div class="comp-sub" style="margin-top: 0.2rem;">Pre-Screened Real-World Location</div>
                                        </div>
                                        <span style="font-family: var(--font-tech); font-size: 0.75rem; color: var(--gold-bright); font-weight: 700;">${cat.match_score}</span>
                                    </div>
                                    <div class="comp-img-wrap" onclick="openLightboxSingle('${cat.scouted_hero}', '${cat.scouted_hero_title}')">
                                        <img src="${getImgUrl(cat.scouted_hero)}" alt="${cat.scouted_hero_title}">
                                    </div>
                                    <div class="comp-img-caption">
                                        <strong>Scouted Environment:</strong> ${cat.scouted_hero_title}
                                    </div>
                                </div>

                            </div>
                        </div>

                        <!-- Details & Logistics Grid -->
                        <div class="details-grid">
                            <!-- Left: Key Scene Features -->
                            <div class="features-box">
                                <h3 class="box-title">🎬 Key Production & Scene Highlights</h3>
                                <ul class="feature-list">
                                    ${cat.key_features.map(f => `<li>${f}</li>`).join('')}
                                </ul>
                            </div>

                            <!-- Right: Filming Specs Table -->
                            <div class="specs-box">
                                <h3 class="box-title">📋 Production Logistics Specifications</h3>
                                <table class="specs-table">
                                    <tr>
                                        <th>Permit & Jurisdiction</th>
                                        <td>${cat.specs.permitting}</td>
                                    </tr>
                                    <tr>
                                        <th>Power Infrastructure</th>
                                        <td>${cat.specs.power}</td>
                                    </tr>
                                    <tr>
                                        <th>Crew Parking & Base</th>
                                        <td>${cat.specs.parking}</td>
                                    </tr>
                                    <tr>
                                        <th>Sound & Curfew</th>
                                        <td>${cat.specs.sound_curfew}</td>
                                    </tr>
                                </table>
                            </div>
                        </div>

                        <!-- Deep Photo Gallery -->
                        <div class="gallery-section">
                            <div class="gallery-header">
                                <div>
                                    <h3 class="section-title" style="font-size: 1.4rem;">Photo Gallery · ${cat.title}</h3>
                                    <span style="font-size: 0.85rem; color: var(--text-muted);">Click any photo to view full-screen high-resolution lightbox</span>
                                </div>
                                <div class="filter-pills" id="filters-${cat.id}">
                                    <button class="filter-pill active" onclick="filterGallery('${cat.id}', 'all', this)">All Photos (${cat.gallery.length})</button>
                                    <button class="filter-pill" onclick="filterGallery('${cat.id}', 'ref', this)">🎯 Director References</button>
                                    <button class="filter-pill" onclick="filterGallery('${cat.id}', 'scouted', this)">📍 Scouted Locations</button>
                                </div>
                            </div>

                            <div class="gallery-grid" id="grid-${cat.id}">
                                ${renderGalleryItems(cat, 'all')}
                            </div>
                        </div>

                    </div>

                </div>
            `).join('');
        }

        function renderGalleryItems(cat, filterCat = 'all') {
            const filtered = filterCat === 'all' ? cat.gallery : cat.gallery.filter(item => item.cat === filterCat);
            return filtered.map((item, idx) => {
                const originalIdx = cat.gallery.findIndex(g => g.file === item.file);
                const tagClass = item.source === 'ref' ? 'tag-ref' : 'tag-scouted';
                const tagLabel = item.source === 'ref' ? 'Reference' : 'Scouted';
                return `
                    <div class="gallery-item" onclick="openLightboxFor('${cat.id}', ${originalIdx})">
                        <img src="${getImgUrl(item.file)}" alt="${item.title}" loading="lazy">
                        <div class="item-caption">
                            <span>${item.title}</span>
                            <span class="item-source-tag ${tagClass}">${tagLabel}</span>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function filterGallery(catId, filterType, btnElement) {
            const cat = categories.find(c => c.id === catId);
            if (!cat) return;
            const grid = document.getElementById(`grid-${catId}`);
            grid.innerHTML = renderGalleryItems(cat, filterType);

            const pills = document.querySelectorAll(`#filters-${catId} .filter-pill`);
            pills.forEach(p => p.classList.remove('active'));
            btnElement.classList.add('active');
        }

        function switchCategory(id) {
            currentCatId = id;
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.category-panel').forEach(panel => panel.classList.remove('active'));

            const tab = document.getElementById(`tab-${id}`);
            const panel = document.getElementById(`panel-${id}`);
            if (tab) tab.classList.add('active');
            if (panel) panel.classList.add('active');
        }

        /* Lightbox Logic */
        function openLightboxFor(catId, photoIndex) {
            const cat = categories.find(c => c.id === catId);
            if (!cat) return;
            activeGallery = cat.gallery.map(item => ({
                url: getImgUrl(item.file),
                title: item.title,
                source: item.source
            }));
            currentLightboxIndex = photoIndex;
            showLightbox();
        }

        function openLightboxSingle(filename, title) {
            activeGallery = [{
                url: getImgUrl(filename),
                title: title,
                source: ''
            }];
            currentLightboxIndex = 0;
            showLightbox();
        }

        function showLightbox() {
            if (!activeGallery.length) return;
            const item = activeGallery[currentLightboxIndex];
            const lb = document.getElementById('lightbox');
            const img = document.getElementById('lightboxImg');
            const cap = document.getElementById('lightboxCaption');
            const count = document.getElementById('lightboxCounter');

            img.src = item.url;
            cap.innerText = item.title;
            count.innerText = `Photo ${currentLightboxIndex + 1} of ${activeGallery.length}`;
            lb.classList.add('active');
        }

        function closeLightbox(e) {
            if (e.target.id === 'lightbox') {
                closeLightboxDirect();
            }
        }

        function closeLightboxDirect() {
            document.getElementById('lightbox').classList.remove('active');
        }

        function prevLightbox(e) {
            if (e) e.stopPropagation();
            if (currentLightboxIndex > 0) {
                currentLightboxIndex--;
            } else {
                currentLightboxIndex = activeGallery.length - 1;
            }
            showLightbox();
        }

        function nextLightbox(e) {
            if (e) e.stopPropagation();
            if (currentLightboxIndex < activeGallery.length - 1) {
                currentLightboxIndex++;
            } else {
                currentLightboxIndex = 0;
            }
            showLightbox();
        }

        // Initialize application on DOM ready
        window.addEventListener('DOMContentLoaded', initApp);
    </script>
</body>
</html>
"""

# Replace placeholders
final_html = html_template.replace("__CATEGORIES_JSON__", json.dumps(categories))
final_html = final_html.replace("__IMAGES_JSON__", json.dumps(embedded_images))

out_html_path = os.path.join(web_dir, "index.html")
with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated index.html successfully at {out_html_path}! File size: {os.path.getsize(out_html_path)} bytes")

# Also write package.json for Vercel
pkg_json = {
    "name": "zen-mirage-media-proposal",
    "version": "1.0.0",
    "description": "Mirage Media Feature Film Production Proposal & Location Pitch Deck - Zencrew & SA Locations",
    "scripts": {
        "start": "npx serve ."
    }
}
with open(os.path.join(web_dir, "package.json"), "w", encoding="utf-8") as f:
    json.dump(pkg_json, f, indent=2)

# Also write .gitignore
with open(os.path.join(web_dir, ".gitignore"), "w", encoding="utf-8") as f:
    f.write(".vercel\nembedded_data.json\n")

print("Web project setup complete!")
