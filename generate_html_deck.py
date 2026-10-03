import os
import json

deck_dir = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-global-locations-deck"
data_path = os.path.join(deck_dir, "embedded_data.json")

print("Reading embedded dataset...")
with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

categories = data["categories"]
images = data["images"]
hero_bg = data.get("hero_background", "")

print(f"Loaded {len(categories)} categories, {len(images)} encoded images, and hero background.")

# 7-Cluster Alphabetical Grouping Architecture (A-C, D-F, G-I, M-O, P-R, S-U, V-Z)
alpha_groups = [
    {
        "id": "a-c",
        "label": "A – C",
        "title": "Aviation, Civic, Coastal & Golf",
        "desc": "Modern airfields, championship links, skyline views, detention blocks & cliffside coastal passes.",
        "cat_ids": [
            "airports-aviation-transport-terminals",
            "golf-courses-country-club-estates",
            "city-views-rooftops-panoramas",
            "civic-institutions-corrections-jail",
            "coastal-passes-ocean-roads"
        ]
    },
    {
        "id": "d-f",
        "label": "D – F",
        "title": "Forest Cabins & Nature Retreats",
        "desc": "Pacific Northwest timber eco-cabins, lush canopy treehouses & forest retreats.",
        "cat_ids": [
            "forest-cabins-nature-retreats"
        ]
    },
    {
        "id": "g-i",
        "label": "G – I",
        "title": "Heritage Cottages & Character Streets",
        "desc": "London Victorian/Edwardian suburban cottages, period facades & heritage streetscapes.",
        "cat_ids": [
            "heritage-cottages-character-streets"
        ]
    },
    {
        "id": "m-o",
        "label": "M – O",
        "title": "Modern Luxury, Wilderness & Nightlife",
        "desc": "Hollywood Hills cantilevered villas, Nevada arid desert basins, rock formations & cocktail lounges.",
        "cat_ids": [
            "modern-luxury-villas",
            "natural-wilderness-geological",
            "nightclubs-lounges-beach-clubs"
        ]
    },
    {
        "id": "p-r",
        "label": "P – R",
        "title": "Pristine Beaches & Industrial Quarries",
        "desc": "Cannes-style white sand coves, granite boulders & deep-cut industrial rock quarries.",
        "cat_ids": [
            "pristine-beaches-coastal-coves",
            "quarries-industrial-excavations"
        ]
    },
    {
        "id": "s-u",
        "label": "S – U",
        "title": "Studios, Stadiums, Dining & Urban CBD",
        "desc": "Daylight cycloramas, soundstages, Olympic-grade arenas, Parisian cabaret & Manhattan CBD skyscrapers.",
        "cat_ids": [
            "soundstages-cycloramas-studios",
            "stadiums-arenas-athletics",
            "theatrical-dining-live-music",
            "urban-metropolis-cbd"
        ]
    },
    {
        "id": "v-z",
        "label": "V – Z",
        "title": "Wine Country & Maritime Harbours",
        "desc": "Tuscan-style vineyards, Cape Dutch farmlands & French Riviera-grade deep-water working harbours.",
        "cat_ids": [
            "wine-country-historic-estates",
            "working-harbours-maritime-basins"
        ]
    }
]


# Build HTML Deck with 5-Pillar Strategic Proposal and Commercial Costing Estimate
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cape Town Master Location Scouting Database · International Film & Commercial Showcase</title>
    <meta name="description" content="Comprehensive master location database showcasing Cape Town and South Africa's film locations across 18 macro categories. Verified scouting inventory, international doubling power, technical filming specs, commercial costing estimate, and multi-currency rate cards. Presented by SA Locations & Zencrew.">

    <!-- Open Graph / Social Sharing -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Cape Town Master Location Scouting Database · Global Film & Commercial Showcase">
    <meta property="og:description" content="Curated 18-category location scouting inventory doubling South Africa for California, Mediterranean, London, New York, Nevada, European, Skyline Rooftop, Championship Golf & Industrial Quarry destinations. Verified hero assets, commercial costing estimate & multi-currency rates.">
    <meta property="og:image" content="https://sal-global-locations-deck.vercel.app/og-preview.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800;900&family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --bg: #070b0a;
            --bg-elevated: #0d1411;
            --surface: #121c17;
            --surface-card: #16241e;
            --surface-hover: #1e332a;
            --border: rgba(255, 255, 255, 0.08);
            --border-highlight: rgba(212, 175, 55, 0.35);
            --border-gold: #d4af37;
            --text-main: #f5f7f5;
            --text-muted: #9aa8a1;
            --text-dim: #64736c;
            --gold: #d4af37;
            --gold-bright: #f6d365;
            --gold-glow: rgba(212, 175, 55, 0.16);
            --emerald: #19382b;
            --emerald-bright: #256149;
            --cyan: #38ef7d;
            --font-serif: 'Cinzel', Georgia, serif;
            --font-heading: 'Cinzel', Georgia, serif;
            --font-sans: 'Inter', -apple-system, sans-serif;
            --font-tech: 'Space Grotesk', monospace, sans-serif;
            --radius-sm: 6px;
            --radius-md: 12px;
            --radius-lg: 18px;
            --shadow-subtle: 0 4px 20px rgba(0, 0, 0, 0.5);
            --shadow-elevated: 0 12px 40px rgba(0, 0, 0, 0.7);
            --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg);
            color: var(--text-main);
            font-family: var(--font-sans);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        /* Subtle Ambient Glow */
        .ambient-glow {
            position: fixed;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100vw;
            height: 600px;
            background: radial-gradient(circle at 50% 0%, rgba(25, 56, 43, 0.35) 0%, rgba(7, 11, 10, 0) 70%);
            pointer-events: none;
            z-index: 0;
        }

        /* Top Navigation Header */
        header.top-nav {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(7, 11, 10, 0.94);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            padding: 0.5rem 1.4rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.8rem;
            flex-wrap: nowrap;
            overflow-x: auto;
            scrollbar-width: none;
        }

        header.top-nav::-webkit-scrollbar {
            display: none;
        }

        .nav-brand {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            text-decoration: none;
            flex-shrink: 0;
        }

        .brand-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            background: rgba(212, 175, 55, 0.12);
            border: 1px solid var(--border-gold);
            color: var(--gold-bright);
            padding: 0.28rem 0.7rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            white-space: nowrap;
        }

        .pulse-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: var(--gold-bright);
            box-shadow: 0 0 10px var(--gold);
            animation: pulseGlow 2s infinite ease-in-out;
        }

        @keyframes pulseGlow {
            0%, 100% { opacity: 0.4; transform: scale(0.9); }
            50% { opacity: 1; transform: scale(1.2); }
        }

        .nav-title {
            font-family: var(--font-serif);
            font-size: 0.98rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            color: #ffffff;
            white-space: nowrap;
        }

        /* Main Navigation Links Menu */
        .nav-links-menu {
            display: flex;
            align-items: center;
            gap: 0.35rem;
            flex-shrink: 0;
        }

        .nav-link-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            padding: 0.32rem 0.65rem;
            border-radius: var(--radius-sm);
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border);
            color: var(--text-muted);
            text-decoration: none;
            font-family: var(--font-tech);
            font-size: 0.74rem;
            font-weight: 600;
            transition: var(--transition);
            white-space: nowrap;
        }

        .nav-link-pill:hover {
            border-color: var(--border-gold);
            color: var(--gold-bright);
            background: rgba(212, 175, 55, 0.08);
            transform: translateY(-1px);
        }

        .nav-link-pill.highlight {
            background: rgba(212, 175, 55, 0.12);
            border-color: var(--gold);
            color: var(--gold-bright);
        }

        .nav-controls {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            flex-shrink: 0;
        }

        .social-link-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.32rem 0.6rem;
            border-radius: var(--radius-sm);
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: var(--text-main);
            text-decoration: none;
            font-family: var(--font-tech);
            font-size: 0.73rem;
            font-weight: 600;
            transition: var(--transition);
            white-space: nowrap;
        }
        .social-link-btn:hover {
            border-color: var(--gold);
            color: var(--gold-bright);
            background: rgba(212, 175, 55, 0.08);
            transform: translateY(-1px);
        }

        .search-box {
            position: relative;
            display: flex;
            align-items: center;
        }

        .search-box input {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 0.36rem 0.85rem 0.36rem 2rem;
            color: #ffffff;
            font-size: 0.78rem;
            width: 145px;
            transition: var(--transition);
            outline: none;
            font-family: var(--font-sans);
        }

        .search-box input:focus {
            width: 200px;
            border-color: var(--border-gold);
            background: rgba(255, 255, 255, 0.08);
        }

        .search-box svg {
            position: absolute;
            left: 0.75rem;
            width: 14px;
            height: 14px;
            fill: var(--text-muted);
            pointer-events: none;
        }

        .currency-selector {
            display: flex;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 2px;
        }

        .curr-btn {
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 0.3rem 0.65rem;
            font-size: 0.75rem;
            font-weight: 600;
            border-radius: 999px;
            cursor: pointer;
            transition: var(--transition);
            font-family: var(--font-tech);
        }

        .curr-btn.active {
            background: var(--gold);
            color: #070b0a;
            font-weight: 700;
        }

        .shortlist-trigger {
            position: relative;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--emerald-bright);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #ffffff;
            padding: 0.42rem 0.95rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            font-family: var(--font-tech);
        }

        .shortlist-trigger:hover {
            background: #2f7a5d;
            box-shadow: 0 0 15px rgba(56, 239, 125, 0.25);
        }

        .shortlist-count {
            background: var(--gold-bright);
            color: #070b0a;
            border-radius: 50%;
            width: 18px;
            height: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.7rem;
            font-weight: 800;
        }

        /* Hero Banner Section with Table Mountain Background */
        .hero-banner-wrapper {
            position: relative;
            width: 100%;
            background-color: var(--bg);
            background-position: center 30%;
            background-size: cover;
            background-repeat: no-repeat;
            border-bottom: 1px solid var(--border);
            overflow: hidden;
        }

        .hero-banner-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(7, 11, 10, 0.46) 0%, rgba(7, 11, 10, 0.76) 55%, rgba(7, 11, 10, 0.95) 100%),
                        radial-gradient(ellipse at 50% 30%, rgba(25, 56, 43, 0.15) 0%, rgba(7, 11, 10, 0.5) 80%);
            pointer-events: none;
            z-index: 1;
        }

        .hero-section {
            position: relative;
            max-width: 1380px;
            margin: 0 auto;
            padding: 4.5rem 2rem 3rem 2rem;
            text-align: center;
            z-index: 2;
        }

        .hero-meta-badges {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }

        .badge-premium {
            background: rgba(212, 175, 55, 0.15);
            border: 1px solid var(--border-gold);
            color: var(--gold-bright);
            padding: 0.4rem 1rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.75rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            font-weight: 700;
        }

        .badge-sub {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 0.4rem 1rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-family: var(--font-tech);
            letter-spacing: 0.05em;
        }

        h1.hero-title {
            font-family: var(--font-serif);
            font-size: clamp(2.2rem, 4.5vw, 3.8rem);
            font-weight: 800;
            letter-spacing: -0.01em;
            line-height: 1.15;
            color: #ffffff;
            margin-bottom: 1.2rem;
            text-transform: uppercase;
        }

        h1.hero-title span.gold {
            background: linear-gradient(135deg, #f6d365 0%, #d4af37 60%, #aa820a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        p.hero-subtitle {
            font-size: 1.1rem;
            color: var(--text-muted);
            max-width: 860px;
            margin: 0 auto 2.5rem auto;
            line-height: 1.7;
            font-weight: 400;
        }

        /* KPI Stats Grid - 4 Balanced Focus Columns */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1rem;
            max-width: 1200px;
            margin: 0 auto 2.5rem auto;
        }

        @media (max-width: 900px) {
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .stat-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.25rem 1rem;
            text-align: center;
            transition: var(--transition);
        }

        .stat-card:hover {
            border-color: var(--border-highlight);
            transform: translateY(-2px);
        }

        .stat-number {
            font-family: var(--font-serif);
            font-size: 1.85rem;
            font-weight: 800;
            color: var(--gold-bright);
            line-height: 1.2;
            margin-bottom: 0.25rem;
        }

        .stat-label {
            font-size: 0.78rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-family: var(--font-tech);
        }

        /* Hero Action Button Cluster */
        .hero-action-buttons {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 3rem;
            flex-wrap: wrap;
        }

        /* Global Doubling Banner */
        .doubling-banner {
            max-width: 1200px;
            margin: 0 auto 1.5rem auto;
            background: linear-gradient(135deg, rgba(25, 56, 43, 0.45) 0%, rgba(18, 28, 23, 0.8) 100%);
            border: 1px solid var(--border-highlight);
            border-radius: var(--radius-lg);
            padding: 1.8rem 2.2rem;
            text-align: left;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 2rem;
            flex-wrap: wrap;
        }

        .doubling-title {
            font-family: var(--font-serif);
            font-size: 1.25rem;
            color: #ffffff;
            font-weight: 700;
            margin-bottom: 0.4rem;
        }

        .doubling-desc {
            font-size: 0.92rem;
            color: var(--text-muted);
            max-width: 780px;
            line-height: 1.55;
        }

        .doubling-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
            margin-top: 0.9rem;
        }

        .doubling-tag {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            background: rgba(25, 56, 43, 0.55);
            border: 1px solid rgba(212, 175, 55, 0.35);
            color: var(--gold-bright);
            font-family: var(--font-tech);
            font-size: 0.75rem;
            padding: 0.4rem 0.85rem;
            border-radius: 999px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
            text-decoration: none;
            outline: none;
        }

        .doubling-tag:hover {
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.3) 0%, rgba(25, 56, 43, 0.9) 100%);
            border-color: var(--gold-bright);
            color: #ffffff;
            transform: translateY(-2px);
            box-shadow: 0 4px 14px rgba(212, 175, 55, 0.3);
        }

        /* -------------------------------------------------------------
           STRATEGIC PRODUCER PROPOSAL: 5-PILLAR ARCHITECTURE
           ------------------------------------------------------------- */
        .proposal-section {
            position: relative;
            max-width: 1380px;
            margin: 3.5rem auto 4rem auto;
            padding: 0 2rem;
            z-index: 10;
        }

        .proposal-container {
            background: linear-gradient(135deg, rgba(22, 36, 30, 0.88) 0%, rgba(13, 20, 17, 0.96) 100%);
            border: 1px solid var(--border-gold);
            border-radius: var(--radius-lg);
            padding: 3.5rem 3rem;
            box-shadow: var(--shadow-elevated), 0 0 50px rgba(212, 175, 55, 0.08);
            position: relative;
            overflow: hidden;
        }

        .proposal-header {
            text-align: center;
            max-width: 960px;
            margin: 0 auto 3rem auto;
        }

        .proposal-header h2 {
            font-family: var(--font-serif);
            font-size: clamp(2rem, 3.5vw, 2.7rem);
            color: #ffffff;
            margin-top: 0.8rem;
            margin-bottom: 0.8rem;
        }

        .proposal-lead-quote {
            font-size: 1.1rem;
            color: var(--gold-bright);
            line-height: 1.7;
            font-style: italic;
            background: rgba(212, 175, 55, 0.08);
            border-left: 3px solid var(--gold);
            padding: 1.2rem 1.6rem;
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            margin: 1.5rem auto 0 auto;
            text-align: left;
            max-width: 920px;
        }

        /* 4-Pillars Matrix Table */
        .matrix-table-wrap {
            overflow-x: auto;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            background: var(--surface-card);
            margin-bottom: 3.5rem;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
        }

        .matrix-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
            text-align: left;
        }

        .matrix-table th {
            background: rgba(25, 56, 43, 0.6);
            color: var(--gold-bright);
            font-family: var(--font-tech);
            text-transform: uppercase;
            font-size: 0.78rem;
            letter-spacing: 0.08em;
            padding: 1.1rem 1.4rem;
            border-bottom: 1px solid var(--border-gold);
            white-space: nowrap;
        }

        .matrix-table td {
            padding: 1.3rem 1.5rem;
            border-bottom: 1px solid var(--border);
            vertical-align: top;
            line-height: 1.65;
        }

        .matrix-table tr:last-child td {
            border-bottom: none;
        }

        .matrix-table tr:hover td {
            background: rgba(255, 255, 255, 0.02);
        }

        .pillar-col-title {
            font-family: var(--font-serif);
            font-size: 1.1rem;
            font-weight: 700;
            color: #ffffff;
            white-space: nowrap;
        }

        .pillar-pos-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.35rem 0.8rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.75rem;
            font-weight: 700;
            white-space: nowrap;
        }

        .pillar-pos-badge.very-strong {
            background: rgba(56, 239, 125, 0.15);
            border: 1px solid #38ef7d;
            color: #38ef7d;
        }

        .pillar-pos-badge.strong {
            background: rgba(212, 175, 55, 0.18);
            border: 1px solid var(--gold);
            color: var(--gold-bright);
        }

        .pillar-pos-badge.caveat {
            background: rgba(255, 170, 0, 0.15);
            border: 1px solid #ffaa00;
            color: #ffc107;
        }

        /* TVC 4-Card Grid */
        .tvc-wrapper {
            margin-bottom: 3.5rem;
        }

        .tvc-section-title {
            font-family: var(--font-serif);
            font-size: 1.5rem;
            color: #ffffff;
            text-align: center;
            margin-bottom: 0.5rem;
        }

        .tvc-section-sub {
            font-size: 0.92rem;
            color: var(--text-muted);
            text-align: center;
            max-width: 750px;
            margin: 0 auto 2.2rem auto;
            line-height: 1.6;
        }

        .tvc-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.25rem;
        }

        @media (max-width: 1050px) {
            .tvc-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (max-width: 600px) {
            .tvc-grid {
                grid-template-columns: 1fr;
            }
        }

        .tvc-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.7rem;
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
            transition: var(--transition);
        }

        .tvc-card:hover {
            border-color: var(--border-gold);
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
        }

        .tvc-card-icon {
            font-size: 2rem;
            margin-bottom: 0.2rem;
        }

        .tvc-card-title {
            font-family: var(--font-tech);
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--gold-bright);
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        .tvc-card-desc {
            font-size: 0.86rem;
            color: var(--text-muted);
            line-height: 1.6;
        }

        /* Pillar 5: Facilitation & Workflow */
        .p5-banner {
            background: linear-gradient(135deg, rgba(25, 56, 43, 0.5) 0%, rgba(18, 28, 23, 0.85) 100%);
            border: 1px solid var(--border-gold);
            border-radius: var(--radius-md);
            padding: 2.2rem;
        }

        .p5-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            margin-bottom: 1.2rem;
            flex-wrap: wrap;
        }

        .p5-title {
            font-family: var(--font-serif);
            font-size: 1.45rem;
            color: #ffffff;
            font-weight: 700;
        }

        .p5-lead {
            font-size: 0.95rem;
            color: var(--text-muted);
            line-height: 1.65;
            max-width: 980px;
        }

        .workflow-steps-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 0.9rem;
            margin-top: 1.8rem;
        }

        @media (max-width: 950px) {
            .workflow-steps-grid {
                grid-template-columns: 1fr;
            }
        }

        .wf-step-card {
            background: rgba(7, 11, 10, 0.65);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 1.2rem;
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
            position: relative;
            transition: var(--transition);
        }

        .wf-step-card:hover {
            border-color: var(--gold);
            transform: translateY(-2px);
        }

        .wf-step-num {
            font-family: var(--font-tech);
            font-size: 0.72rem;
            font-weight: 800;
            color: var(--gold);
            letter-spacing: 0.12em;
        }

        .wf-step-title {
            font-size: 0.9rem;
            font-weight: 700;
            color: #ffffff;
        }

        .wf-step-desc {
            font-size: 0.78rem;
            color: var(--text-muted);
            line-height: 1.45;
        }

        /* -------------------------------------------------------------
           COMMERCIAL PRODUCTION COSTING ESTIMATE & DAY RATES
           ------------------------------------------------------------- */
        .costing-section {
            position: relative;
            max-width: 1380px;
            margin: 4.5rem auto 3rem auto;
            padding: 0 2rem;
            z-index: 10;
        }

        .costing-container {
            background: var(--surface);
            border: 1px solid var(--border-gold);
            border-radius: var(--radius-lg);
            padding: 3.5rem 3rem;
            box-shadow: var(--shadow-elevated), 0 0 50px rgba(212, 175, 55, 0.08);
        }

        .costing-header {
            text-align: center;
            max-width: 860px;
            margin: 0 auto 3rem auto;
        }

        .costing-header h2 {
            font-family: var(--font-serif);
            font-size: clamp(2rem, 3.2vw, 2.6rem);
            color: #ffffff;
            margin-top: 0.8rem;
            margin-bottom: 0.8rem;
        }

        .costing-lead {
            font-size: 1rem;
            color: var(--text-muted);
            line-height: 1.65;
        }

        .costing-table-card {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            margin-bottom: 2.5rem;
            overflow: hidden;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
        }

        .costing-card-header {
            padding: 1.3rem 1.8rem;
            background: linear-gradient(90deg, rgba(25, 56, 43, 0.45) 0%, rgba(18, 28, 23, 0.85) 100%);
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .costing-card-title {
            font-family: var(--font-serif);
            font-size: 1.25rem;
            font-weight: 700;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .costing-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
        }

        .costing-table th {
            background: rgba(0, 0, 0, 0.35);
            color: var(--gold);
            font-family: var(--font-tech);
            font-size: 0.74rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            padding: 0.95rem 1.4rem;
            border-bottom: 1px solid var(--border);
            text-align: left;
        }

        .costing-table td {
            padding: 0.95rem 1.4rem;
            border-bottom: 1px solid var(--border);
            color: var(--text-main);
            vertical-align: middle;
        }

        .costing-table tr:last-child td {
            border-bottom: none;
        }

        .costing-table tr:hover td {
            background: rgba(255, 255, 255, 0.025);
        }

        .role-title {
            font-weight: 600;
            color: #ffffff;
        }

        .dept-pill {
            display: inline-block;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border);
            color: var(--text-dim);
            font-family: var(--font-tech);
            font-size: 0.72rem;
            padding: 0.15rem 0.55rem;
            border-radius: 4px;
        }

        .rate-cell {
            font-family: var(--font-tech);
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--gold-bright);
            white-space: nowrap;
        }

        .scope-cell {
            font-size: 0.84rem;
            color: var(--text-muted);
            line-height: 1.5;
        }

        /* -------------------------------------------------------------
           dtic INCENTIVE DEEP DIVE SECTION
           ------------------------------------------------------------- */
        .incentive-section {
            position: relative;
            max-width: 1380px;
            margin: 4.5rem auto 3rem auto;
            padding: 0 2rem;
            z-index: 10;
        }

        .incentive-container {
            background: linear-gradient(135deg, rgba(13, 20, 17, 0.96) 0%, rgba(22, 36, 30, 0.85) 100%);
            border: 1px solid var(--border-gold);
            border-radius: var(--radius-lg);
            padding: 3.5rem 3rem;
            box-shadow: var(--shadow-elevated), 0 0 50px rgba(212, 175, 55, 0.08);
        }

        .incentive-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin-top: 2.5rem;
        }

        @media (max-width: 950px) {
            .incentive-grid {
                grid-template-columns: 1fr;
            }
        }

        .incentive-card {
            background: rgba(7, 11, 10, 0.65);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 2rem;
            display: flex;
            flex-direction: column;
            gap: 0.9rem;
            transition: var(--transition);
        }

        .incentive-card:hover {
            border-color: var(--border-gold);
            transform: translateY(-3px);
        }

        .incentive-card.highlight {
            border-color: var(--border-gold);
            background: linear-gradient(180deg, rgba(25, 56, 43, 0.45) 0%, rgba(7, 11, 10, 0.8) 100%);
        }

        .dtic-notice-box {
            background: rgba(255, 170, 0, 0.08);
            border: 1px solid rgba(255, 170, 0, 0.35);
            border-radius: var(--radius-md);
            padding: 1.6rem 2rem;
            margin-top: 2.5rem;
            display: flex;
            align-items: flex-start;
            gap: 1.2rem;
        }

        .notice-icon {
            font-size: 2rem;
            line-height: 1;
        }

        .notice-content h4 {
            font-family: var(--font-tech);
            font-size: 0.95rem;
            color: #ffc107;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin-bottom: 0.4rem;
        }

        .notice-content p {
            font-size: 0.88rem;
            color: var(--text-muted);
            line-height: 1.6;
        }

        /* Single Category View Banner */
        .category-active-banner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(135deg, rgba(22, 36, 30, 0.95) 0%, rgba(13, 20, 17, 0.98) 100%);
            border: 1px solid var(--border-gold);
            border-radius: var(--radius-md);
            padding: 0.85rem 1.4rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
            flex-wrap: wrap;
            gap: 1rem;
        }

        .btn-back-overview {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(212, 175, 55, 0.15);
            border: 1px solid var(--gold);
            color: var(--gold-bright);
            font-family: var(--font-tech);
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            padding: 0.55rem 1.1rem;
            border-radius: 999px;
            cursor: pointer;
            transition: all 0.25s ease;
        }

        .btn-back-overview:hover {
            background: var(--gold);
            color: #070b0a;
            transform: translateX(-3px);
            box-shadow: 0 4px 14px rgba(212, 175, 55, 0.35);
        }

        .active-category-title-display {
            font-family: var(--font-heading);
            font-size: 1rem;
            color: var(--text-main);
            font-weight: 600;
        }

        /* Sticky Category Filter Bar */
        .category-nav-wrap {
            position: sticky;
            top: 58px;
            z-index: 90;
            background: rgba(7, 11, 10, 0.95);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            padding: 0.6rem 1.5rem;
        }

        .category-nav {
            max-width: 1380px;
            margin: 0 auto;
            display: flex;
            gap: 0.5rem;
            overflow-x: auto;
            scrollbar-width: none;
            padding: 0.2rem 0;
        }

        .category-nav::-webkit-scrollbar {
            display: none;
        }

        .cat-pill {
            flex-shrink: 0;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 0.5rem 1rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: var(--transition);
            cursor: pointer;
            white-space: nowrap;
        }

        .cat-pill:hover {
            border-color: var(--border-highlight);
            color: #ffffff;
            background: rgba(255, 255, 255, 0.08);
        }

        .cat-pill.active {
            background: var(--gold);
            color: #070b0a;
            border-color: var(--gold);
            font-weight: 700;
        }

        /* Main Content Container */
        main.deck-container {
            max-width: 1380px;
            margin: 0 auto;
            padding: 2.5rem 2rem;
            position: relative;
            z-index: 10;
        }

        /* Category Section Block */
        .category-block {
            margin-bottom: 5rem;
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-elevated);
            transition: var(--transition);
        }

        .category-header {
            padding: 2.2rem 2.5rem 1.6rem 2.5rem;
            border-bottom: 1px solid var(--border);
            background: linear-gradient(180deg, rgba(25, 56, 43, 0.2) 0%, rgba(18, 28, 23, 0) 100%);
        }

        .cat-meta-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.8rem;
            flex-wrap: wrap;
            gap: 0.8rem;
        }

        .cat-num-badge {
            font-family: var(--font-tech);
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--gold);
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }

        .cat-doubling-banner {
            background: rgba(212, 175, 55, 0.1);
            border: 1px solid var(--border-gold);
            color: var(--gold-bright);
            padding: 0.3rem 0.85rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-family: var(--font-tech);
            font-weight: 600;
        }

        h2.category-title {
            font-family: var(--font-serif);
            font-size: clamp(1.6rem, 2.8vw, 2.2rem);
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .category-area {
            font-family: var(--font-tech);
            font-size: 0.88rem;
            color: var(--gold);
            font-weight: 500;
            margin-bottom: 1rem;
        }

        .category-synopsis {
            font-size: 0.95rem;
            color: var(--text-muted);
            line-height: 1.7;
            max-width: 1100px;
        }

        /* Hero Location Showcase - Strict Landscape with Wording Below */
        .hero-showcase {
            display: flex;
            flex-direction: column;
            border-bottom: 1px solid var(--border);
            background: var(--surface);
        }

        /* 3-Part Continuous Panorama Vista Styling */
        .panorama-triptych-wrap {
            background: linear-gradient(135deg, rgba(22, 36, 30, 0.7) 0%, rgba(13, 20, 17, 0.9) 100%);
            border: 1px solid var(--border-gold);
            border-radius: var(--radius-md);
            padding: 1.25rem;
            margin-bottom: 2rem;
        }

        .panorama-triptych-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }

        .panorama-triptych-title {
            font-family: var(--font-heading);
            font-size: 1.05rem;
            color: var(--text-main);
            font-weight: 600;
        }

        .panorama-triptych-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 6px;
            background: #000;
            padding: 4px;
            border-radius: var(--radius-sm);
        }

        @media (max-width: 900px) {
            .panorama-triptych-grid {
                grid-template-columns: 1fr;
            }
        }

        .panorama-pane {
            cursor: pointer;
            overflow: hidden;
            border-radius: 4px;
            background: var(--surface);
            display: flex;
            flex-direction: column;
            transition: transform 0.3s ease;
        }

        .panorama-pane:hover {
            transform: translateY(-2px);
        }

        .hero-image-wrap {
            position: relative;
            width: 100%;
            aspect-ratio: 16 / 9;
            max-height: 540px;
            background: #000;
            cursor: pointer;
            overflow: hidden;
        }

        .hero-image-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            display: block;
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .hero-image-wrap:hover img {
            transform: scale(1.025);
        }

        .hero-overlay-badge {
            position: absolute;
            top: 1.2rem;
            left: 1.2rem;
            background: rgba(7, 11, 10, 0.88);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-gold);
            color: var(--gold-bright);
            padding: 0.4rem 0.9rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.6);
        }

        .hero-overlay-heart {
            position: absolute;
            top: 1.2rem;
            right: 1.2rem;
            background: rgba(7, 11, 10, 0.75);
            backdrop-filter: blur(8px);
            border: 1px solid var(--border);
            width: 38px;
            height: 38px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: var(--transition);
        }

        .hero-overlay-heart:hover {
            border-color: #ff4757;
            transform: scale(1.1);
        }

        .hero-overlay-heart.active svg {
            fill: #ff4757;
        }

        .hero-overlay-heart svg {
            width: 18px;
            height: 18px;
            fill: #ffffff;
            transition: fill 0.2s;
        }

        /* Wording Below Landscape Hero */
        .hero-details-panel {
            padding: 2.2rem 2.5rem;
            display: flex;
            flex-direction: column;
            gap: 1.6rem;
            background: var(--surface);
        }

        .hero-details-top h3 {
            font-family: var(--font-serif);
            font-size: 1.4rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.5rem;
            line-height: 1.35;
        }

        .hero-details-top p.tagline {
            font-size: 0.92rem;
            color: var(--text-muted);
            line-height: 1.6;
        }

        .hero-content-grid {
            display: grid;
            grid-template-columns: 1.15fr 1fr;
            gap: 2.2rem;
        }

        @media (max-width: 900px) {
            .hero-content-grid {
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }
        }

        .section-sub-label {
            font-family: var(--font-tech);
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--gold-bright);
            font-weight: 700;
            margin-bottom: 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }

        .key-features-list {
            list-style: none;
        }

        .key-features-list li {
            position: relative;
            padding-left: 1.4rem;
            font-size: 0.88rem;
            color: var(--text-main);
            margin-bottom: 0.65rem;
            line-height: 1.5;
        }

        .key-features-list li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--gold);
            font-weight: 700;
        }

        /* Technical Filming Specs Grid */
        .specs-panel {
            background: rgba(0, 0, 0, 0.28);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.25rem 1.4rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.1rem;
        }

        @media (max-width: 600px) {
            .specs-panel {
                grid-template-columns: 1fr;
            }
        }

        .spec-item {
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }

        .spec-label {
            font-family: var(--font-tech);
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--gold);
            font-weight: 700;
        }

        .spec-value {
            font-size: 0.82rem;
            color: var(--text-muted);
            line-height: 1.45;
        }

        .hero-actions-row {
            display: flex;
            gap: 0.9rem;
            flex-wrap: wrap;
            padding-top: 0.5rem;
            border-top: 1px solid var(--border);
        }

        /* Scouted Images Database Gallery */
        .gallery-section {
            padding: 2.2rem 2.5rem 2.5rem 2.5rem;
            background: var(--surface-card);
        }

        .gallery-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
            gap: 0.8rem;
        }

        .gallery-title {
            font-family: var(--font-serif);
            font-size: 1.18rem;
            font-weight: 700;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .gallery-badge {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border);
            color: var(--text-muted);
            font-family: var(--font-tech);
            font-size: 0.72rem;
            padding: 0.2rem 0.65rem;
            border-radius: 999px;
        }

        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(270px, 1fr));
            gap: 1.25rem;
        }

        .gallery-card {
            position: relative;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            overflow: hidden;
            cursor: pointer;
            transition: var(--transition);
        }

        .gallery-card:hover {
            border-color: var(--border-highlight);
            transform: translateY(-4px);
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.6);
        }

        .gallery-thumb-wrap {
            position: relative;
            aspect-ratio: 16 / 10;
            background: #000;
            overflow: hidden;
        }

        .gallery-thumb-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.4s ease;
        }

        .gallery-card:hover .gallery-thumb-wrap img {
            transform: scale(1.05);
        }

        .gallery-thumb-tag {
            position: absolute;
            bottom: 0.6rem;
            left: 0.6rem;
            background: rgba(7, 11, 10, 0.85);
            backdrop-filter: blur(6px);
            border: 1px solid var(--border);
            color: var(--text-main);
            font-family: var(--font-tech);
            font-size: 0.68rem;
            font-weight: 600;
            padding: 0.2rem 0.55rem;
            border-radius: 4px;
        }

        .gallery-card-heart {
            position: absolute;
            top: 0.6rem;
            right: 0.6rem;
            background: rgba(7, 11, 10, 0.7);
            backdrop-filter: blur(6px);
            border: 1px solid var(--border);
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: var(--transition);
        }

        .gallery-card-heart:hover {
            border-color: #ff4757;
            transform: scale(1.1);
        }

        .gallery-card-heart.active svg {
            fill: #ff4757;
        }

        .gallery-card-heart svg {
            width: 14px;
            height: 14px;
            fill: #ffffff;
            transition: fill 0.2s;
        }

        .gallery-card-info {
            padding: 0.9rem 1rem;
        }

        .gallery-card-title {
            font-size: 0.84rem;
            font-weight: 600;
            color: #ffffff;
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        /* Buttons & Actions */
        .btn-nav {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border);
            color: var(--text-main);
            padding: 0.6rem 1.25rem;
            border-radius: var(--radius-sm);
            font-family: var(--font-tech);
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            text-decoration: none;
        }

        .btn-nav:hover {
            background: rgba(255, 255, 255, 0.12);
            border-color: var(--border-highlight);
            color: #ffffff;
            transform: translateY(-1px);
        }

        .btn-nav.primary {
            background: var(--gold);
            color: #070b0a;
            border-color: var(--gold);
            font-weight: 700;
        }

        .btn-nav.primary:hover {
            background: var(--gold-bright);
            box-shadow: 0 0 20px var(--gold-glow);
        }

        /* Rate Cards & Executive Strip */
        .rates-section {
            background: var(--surface);
            border: 1px solid var(--border-gold);
            border-radius: var(--radius-lg);
            padding: 3rem 2.5rem;
            margin: 4rem auto;
            max-width: 1200px;
        }

        .rates-header {
            text-align: center;
            max-width: 750px;
            margin: 0 auto 2.5rem auto;
        }

        .rates-header h2 {
            font-family: var(--font-serif);
            font-size: 2rem;
            color: #ffffff;
            margin-bottom: 0.6rem;
        }

        .rates-header p {
            font-size: 0.95rem;
            color: var(--text-muted);
        }

        .rates-cards-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin-bottom: 2.5rem;
        }

        @media (max-width: 850px) {
            .rates-cards-grid {
                grid-template-columns: 1fr;
            }
        }

        .rate-tier-card {
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 2rem 1.8rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: var(--transition);
        }

        .rate-tier-card.featured {
            border-color: var(--border-gold);
            box-shadow: 0 0 30px var(--gold-glow);
            position: relative;
        }

        .rate-badge {
            display: inline-block;
            background: var(--gold);
            color: #070b0a;
            font-family: var(--font-tech);
            font-size: 0.7rem;
            font-weight: 700;
            padding: 0.2rem 0.6rem;
            border-radius: 999px;
            margin-bottom: 1rem;
            align-self: flex-start;
            text-transform: uppercase;
        }

        .rate-tier-card h3 {
            font-family: var(--font-serif);
            font-size: 1.25rem;
            color: #ffffff;
            margin-bottom: 0.5rem;
        }

        .rate-tier-card p.tier-desc {
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 1.2rem;
            line-height: 1.5;
        }

        .rate-amount {
            font-family: var(--font-tech);
            font-size: 2rem;
            font-weight: 800;
            color: var(--gold-bright);
            margin-bottom: 1rem;
        }

        .rate-amount span.unit {
            font-size: 0.85rem;
            color: var(--text-muted);
            font-weight: 400;
        }

        .tier-features {
            list-style: none;
            margin-bottom: 1.8rem;
            flex-grow: 1;
        }

        .tier-features li {
            position: relative;
            padding-left: 1.3rem;
            font-size: 0.82rem;
            color: var(--text-main);
            margin-bottom: 0.5rem;
            line-height: 1.45;
        }

        .tier-features li::before {
            content: "•";
            position: absolute;
            left: 0;
            color: var(--gold);
            font-weight: 800;
        }

        /* Executive Contacts Card */
        .exec-contacts-card {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 2rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }

        @media (max-width: 750px) {
            .exec-contacts-card {
                grid-template-columns: 1fr;
            }
        }

        .contact-col {
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
        }

        .contact-role {
            font-family: var(--font-tech);
            font-size: 0.75rem;
            text-transform: uppercase;
            color: var(--gold);
            letter-spacing: 0.08em;
            font-weight: 700;
        }

        .contact-name {
            font-family: var(--font-serif);
            font-size: 1.3rem;
            color: #ffffff;
            font-weight: 700;
        }

        .contact-bio {
            font-size: 0.86rem;
            color: var(--text-muted);
            line-height: 1.55;
            margin-bottom: 0.5rem;
        }

        .contact-links {
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
        }

        .contact-link {
            font-family: var(--font-tech);
            font-size: 0.82rem;
            color: var(--text-main);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: var(--transition);
        }

        .contact-link.highlight {
            color: var(--gold-bright);
            font-weight: 600;
        }

        /* Business Card Box */
        .biz-card-box {
            background: rgba(7, 11, 10, 0.85);
            border: 1px solid rgba(212, 175, 55, 0.4);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5), 0 4px 15px rgba(0, 0, 0, 0.4);
            margin-top: 0.5rem;
        }

        .biz-card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 0.8rem;
        }

        .biz-card-company {
            font-family: var(--font-tech);
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--gold-bright);
            letter-spacing: 0.05em;
        }

        .biz-card-tagline {
            font-size: 0.8rem;
            color: var(--text-muted);
            letter-spacing: 0.03em;
        }

        .biz-card-flag {
            font-family: var(--font-tech);
            font-size: 0.75rem;
            color: var(--text-dim);
            background: rgba(255, 255, 255, 0.06);
            padding: 0.25rem 0.6rem;
            border-radius: 4px;
            border: 1px solid var(--border);
        }

        .biz-card-divider {
            height: 1px;
            background: linear-gradient(90deg, var(--gold) 0%, rgba(212, 175, 55, 0.15) 100%);
            margin-bottom: 0.8rem;
        }

        /* Golden Hour & Summer Daylight Section */
        .golden-hour-section {
            position: relative;
            max-width: 1380px;
            margin: 4.5rem auto 3rem auto;
            padding: 0 2rem;
            z-index: 10;
        }

        .gh-container {
            background: linear-gradient(135deg, rgba(22, 36, 30, 0.8) 0%, rgba(13, 20, 17, 0.9) 100%);
            border: 1px solid var(--border-gold);
            border-radius: var(--radius-lg);
            padding: 3rem 2.5rem;
            box-shadow: var(--shadow-elevated), 0 0 40px rgba(212, 175, 55, 0.08);
            position: relative;
            overflow: hidden;
        }

        .gh-container::before {
            content: '';
            position: absolute;
            top: -80px;
            right: -80px;
            width: 280px;
            height: 280px;
            background: radial-gradient(circle, rgba(246, 211, 101, 0.15) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
        }

        .gh-header {
            text-align: center;
            max-width: 860px;
            margin: 0 auto 2.5rem auto;
        }

        .gh-header h2 {
            font-family: var(--font-serif);
            font-size: clamp(1.8rem, 3.2vw, 2.5rem);
            color: #ffffff;
            margin-top: 0.8rem;
            margin-bottom: 0.8rem;
            letter-spacing: -0.01em;
        }

        .gh-subtitle {
            font-size: 1.05rem;
            color: var(--text-muted);
            line-height: 1.6;
        }

        .gh-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
        }

        .gh-card {
            background: rgba(7, 11, 10, 0.65);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.8rem;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            transition: var(--transition);
        }

        .gh-card:hover {
            border-color: rgba(212, 175, 55, 0.4);
            transform: translateY(-3px);
            background: rgba(7, 11, 10, 0.85);
        }

        .gh-card.featured {
            border-color: var(--border-gold);
            background: linear-gradient(180deg, rgba(25, 56, 43, 0.4) 0%, rgba(7, 11, 10, 0.75) 100%);
        }

        .gh-icon {
            font-size: 2.2rem;
            margin-bottom: 0.25rem;
        }

        .gh-stat {
            font-family: var(--font-serif);
            font-size: 1.8rem;
            font-weight: 800;
            color: var(--gold-bright);
            line-height: 1;
        }

        .gh-card-title {
            font-family: var(--font-tech);
            font-size: 0.95rem;
            font-weight: 700;
            color: #ffffff;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        .gh-desc {
            font-size: 0.88rem;
            color: var(--text-muted);
            line-height: 1.55;
        }

        /* Shortlist Drawer */
        .shortlist-drawer {
            position: fixed;
            top: 0;
            right: -420px;
            width: 400px;
            height: 100vh;
            background: rgba(13, 20, 17, 0.97);
            backdrop-filter: blur(20px);
            border-left: 1px solid var(--border-gold);
            z-index: 1000;
            display: flex;
            flex-direction: column;
            transition: right 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: -10px 0 30px rgba(0, 0, 0, 0.8);
        }

        .shortlist-drawer.open {
            right: 0;
        }

        .drawer-header {
            padding: 1.25rem 1.5rem;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .drawer-header h3 {
            font-family: var(--font-serif);
            font-size: 1.15rem;
            color: #ffffff;
        }

        .drawer-close {
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 1.4rem;
            cursor: pointer;
            transition: var(--transition);
        }

        .drawer-close:hover {
            color: #ffffff;
        }

        .drawer-body {
            padding: 1.5rem;
            flex-grow: 1;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .shortlist-item {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 0.8rem;
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }

        .shortlist-item img {
            width: 60px;
            height: 45px;
            object-fit: cover;
            border-radius: 4px;
        }

        .shortlist-item-info {
            flex-grow: 1;
        }

        .shortlist-item-title {
            font-size: 0.8rem;
            font-weight: 600;
            color: #ffffff;
            line-height: 1.3;
        }

        .shortlist-item-cat {
            font-size: 0.7rem;
            color: var(--gold);
            font-family: var(--font-tech);
        }

        .shortlist-remove {
            background: transparent;
            border: none;
            color: var(--text-dim);
            cursor: pointer;
            font-size: 1rem;
            transition: var(--transition);
            padding: 0.2rem;
        }

        .shortlist-remove:hover {
            color: #ff4757;
        }

        .drawer-footer {
            padding: 1.25rem 1.5rem;
            border-top: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .shortlist-empty {
            text-align: center;
            color: var(--text-dim);
            font-size: 0.9rem;
            margin: auto 0;
            line-height: 1.6;
        }

        /* Cinema Lightbox Modal */
        .lightbox-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(3, 6, 5, 0.96);
            backdrop-filter: blur(20px);
            z-index: 2000;
            display: none;
            flex-direction: column;
            opacity: 0;
            transition: opacity 0.25s ease;
        }

        .lightbox-modal.active {
            display: flex;
            opacity: 1;
        }

        .lb-top-bar {
            padding: 1rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        .lb-meta {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .lb-cat-badge {
            font-family: var(--font-tech);
            font-size: 0.75rem;
            color: var(--gold);
            background: rgba(212, 175, 55, 0.12);
            border: 1px solid var(--border-gold);
            padding: 0.3rem 0.8rem;
            border-radius: 999px;
            font-weight: 700;
        }

        .lb-counter {
            font-family: var(--font-tech);
            font-size: 0.8rem;
            color: var(--text-muted);
        }

        .lb-actions {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .lb-btn {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border);
            color: #ffffff;
            padding: 0.45rem 1rem;
            border-radius: var(--radius-sm);
            font-size: 0.8rem;
            font-family: var(--font-tech);
            cursor: pointer;
            transition: var(--transition);
        }

        .lb-btn:hover {
            border-color: var(--gold);
            color: var(--gold-bright);
        }

        .lb-close-btn {
            background: transparent;
            border: none;
            color: #ffffff;
            font-size: 1.5rem;
            cursor: pointer;
            padding: 0.3rem 0.6rem;
            transition: var(--transition);
        }

        .lb-close-btn:hover {
            color: var(--gold);
        }

        .lb-stage {
            flex-grow: 1;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 1rem 2rem;
            position: relative;
            overflow: hidden;
        }

        .lb-image-container {
            max-width: 90vw;
            max-height: 75vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: auto;
        }

        .lb-image-container img {
            max-width: 100%;
            max-height: 75vh;
            object-fit: contain;
            border-radius: 4px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.9);
        }

        .lb-nav-btn {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border);
            color: #ffffff;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            cursor: pointer;
            transition: var(--transition);
            z-index: 10;
        }

        .lb-nav-btn:hover {
            background: var(--gold);
            color: #070b0a;
            border-color: var(--gold);
        }

        .lb-caption-bar {
            padding: 1.25rem 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            text-align: center;
            background: rgba(7, 11, 10, 0.85);
        }

        .lb-caption-title {
            font-family: var(--font-serif);
            font-size: 1.15rem;
            color: #ffffff;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }

        .lb-caption-sub {
            font-size: 0.82rem;
            color: var(--text-muted);
            font-family: var(--font-tech);
        }

        /* Footer */
        footer.site-footer {
            border-top: 1px solid var(--border);
            background: #040706;
            padding: 3rem 2rem;
            text-align: center;
            position: relative;
            z-index: 10;
        }

        .footer-wrap {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1.5rem;
        }

        .footer-logo-row {
            display: flex;
            align-items: center;
            gap: 1.2rem;
            font-family: var(--font-serif);
            font-size: 1.1rem;
            font-weight: 700;
            color: #ffffff;
        }

        .footer-social-row {
            display: flex;
            align-items: center;
            gap: 1.5rem;
            flex-wrap: wrap;
            justify-content: center;
        }

        .footer-disclaimer {
            font-size: 0.82rem;
            color: var(--text-dim);
            max-width: 800px;
            line-height: 1.6;
        }


        /* Alphabetical Directory Grid & Spacious Categorization */
        .alpha-directory-section {
            background: rgba(18, 28, 23, 0.45);
            border: 1px solid rgba(212, 175, 55, 0.25);
            border-radius: var(--radius-lg);
            padding: 2.2rem 2.5rem;
            margin-top: 2rem;
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.45);
            backdrop-filter: blur(12px);
        }

        .alpha-dir-main-header {
            margin-bottom: 1.8rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 1.2rem;
        }

        .alpha-directory-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.35rem;
        }

        .alpha-dir-card {
            background: rgba(12, 20, 16, 0.7);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.3rem 1.45rem;
            transition: var(--transition);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .alpha-dir-card:hover {
            border-color: var(--border-gold);
            background: rgba(20, 32, 26, 0.85);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        }

        .alpha-dir-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 0.8rem;
            margin-bottom: 0.75rem;
            padding-bottom: 0.65rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        }

        .alpha-badge {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-tech);
            font-weight: 700;
            font-size: 0.82rem;
            letter-spacing: 0.1em;
            background: rgba(212, 175, 55, 0.18);
            color: var(--gold-bright);
            border: 1px solid var(--gold);
            padding: 0.25rem 0.65rem;
            border-radius: 6px;
            white-space: nowrap;
        }

        .alpha-dir-title {
            font-family: var(--font-serif);
            font-size: 0.96rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.3;
        }

        .alpha-dir-desc {
            font-size: 0.78rem;
            color: var(--text-dim);
            line-height: 1.45;
            margin-bottom: 0.85rem;
        }

        .btn-group-view {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: var(--text-main);
            font-family: var(--font-tech);
            font-size: 0.72rem;
            font-weight: 600;
            padding: 0.3rem 0.7rem;
            border-radius: 6px;
            cursor: pointer;
            transition: var(--transition);
            white-space: nowrap;
        }

        .btn-group-view:hover {
            background: var(--gold);
            color: #070b0a;
            border-color: var(--gold);
        }

        .alpha-dir-items {
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
        }

        /* Alphabetical Group Selector in Sticky Nav */
        .alpha-group-selector {
            display: flex;
            align-items: center;
            gap: 0.45rem;
            padding-bottom: 0.45rem;
            margin-bottom: 0.45rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            overflow-x: auto;
            scrollbar-width: none;
        }

        .alpha-group-selector::-webkit-scrollbar {
            display: none;
        }

        .alpha-selector-label {
            font-family: var(--font-tech);
            font-size: 0.72rem;
            color: var(--text-dim);
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            white-space: nowrap;
            margin-right: 0.25rem;
        }

        .alpha-tab-btn {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border);
            color: var(--text-muted);
            font-family: var(--font-tech);
            font-size: 0.74rem;
            font-weight: 600;
            padding: 0.25rem 0.7rem;
            border-radius: 6px;
            cursor: pointer;
            transition: var(--transition);
            white-space: nowrap;
        }

        .alpha-tab-btn:hover {
            border-color: var(--border-gold);
            color: var(--gold-bright);
            background: rgba(212, 175, 55, 0.08);
        }

        .alpha-tab-btn.active {
            background: var(--gold);
            color: #070b0a;
            border-color: var(--gold);
            font-weight: 700;
        }

        .nav-group-divider {
            display: inline-flex;
            align-items: center;
            color: var(--gold);
            font-family: var(--font-tech);
            font-size: 0.68rem;
            font-weight: 700;
            padding: 0 0.4rem;
            opacity: 0.85;
            letter-spacing: 0.05em;
            white-space: nowrap;
        }

        /* Main Content Cluster Sections */
        .alpha-cluster-wrapper {
            margin-bottom: 4.5rem;
        }

        .alpha-cluster-banner {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 1rem;
            background: linear-gradient(90deg, rgba(25, 56, 43, 0.75) 0%, rgba(18, 28, 23, 0.4) 100%);
            border-left: 4px solid var(--gold);
            border-top: 1px solid var(--border);
            border-right: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.25rem 2rem;
            margin-bottom: 2.2rem;
            margin-top: 1.5rem;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
        }

        .alpha-cluster-left {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .alpha-cluster-badge {
            font-family: var(--font-tech);
            font-weight: 700;
            font-size: 0.85rem;
            letter-spacing: 0.12em;
            background: rgba(212, 175, 55, 0.18);
            color: var(--gold-bright);
            border: 1px solid var(--gold);
            padding: 0.3rem 0.8rem;
            border-radius: 6px;
            white-space: nowrap;
        }

        .alpha-cluster-title {
            font-family: var(--font-serif);
            font-size: 1.28rem;
            font-weight: 700;
            color: #ffffff;
            margin: 0;
            letter-spacing: 0.03em;
        }

        .alpha-cluster-meta {
            font-family: var(--font-tech);
            font-size: 0.82rem;
            color: var(--text-muted);
        }

        /* Print Optimization */
        @media print {
            header.top-nav, .category-nav-wrap, .ambient-glow, .lb-nav-btn, .search-box, .currency-selector, .shortlist-trigger, .btn-nav, .hero-actions-row, .gallery-card-heart, .hero-overlay-heart {
                display: none !important;
            }
            body {
                background: #ffffff !important;
                color: #000000 !important;
            }
            .category-block {
                page-break-before: always;
                border: 1px solid #ccc !important;
                box-shadow: none !important;
                background: #ffffff !important;
                color: #000000 !important;
            }
            .category-header, .hero-details-panel, .gallery-section, .proposal-container, .costing-container {
                background: #ffffff !important;
                color: #000000 !important;
            }
            h1, h2, h3, h4 {
                color: #000000 !important;
            }
            p, li, .spec-value, .category-synopsis, .costing-lead {
                color: #333333 !important;
            }
        }
    </style>
</head>
<body>
"""

html_template += f"""
    <div class="ambient-glow"></div>

    <!-- Header Navigation -->
    <header class="top-nav">
        <div class="nav-brand">
            <div class="brand-pill">
                <span class="pulse-dot"></span>
                <span>Scouted Images Database</span>
            </div>
            <span class="nav-title">SA Locations & Zencrew</span>
        </div>

        <!-- Section Shortcuts -->
        <nav class="nav-links-menu">
            <a href="#strategic-proposal" class="nav-link-pill">📋 Strategic Proposal</a>
            <a href="#categories-showcase" class="nav-link-pill">🎬 Locations ({len(categories)})</a>
            <a href="#costing-estimate" class="nav-link-pill highlight">📊 Costing Estimate</a>
            <a href="#dtic-incentives" class="nav-link-pill">🏛️ dtic Incentives</a>
            <a href="#rates-and-contacts" class="nav-link-pill">👥 Team & Rates</a>
        </nav>

        <div class="nav-controls">
            <!-- Social Channels -->
            <a href="https://www.instagram.com/salocations" target="_blank" rel="noopener noreferrer" class="social-link-btn" title="SA Locations on Instagram">
                📸 Instagram
            </a>
            <a href="https://www.youtube.com/@salocations" target="_blank" rel="noopener noreferrer" class="social-link-btn" title="SA Locations on YouTube">
                🎬 YouTube
            </a>

            <!-- Global Search -->
            <div class="search-box">
                <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
                <input type="text" id="searchInput" placeholder="Search {len(images)} locations..." oninput="filterShowcase(this.value)">
            </div>

            <!-- Multi-Currency Selector -->
            <div class="currency-selector">
                <button class="curr-btn active" data-curr="ZAR" onclick="setCurrency('ZAR')">ZAR</button>
                <button class="curr-btn" data-curr="USD" onclick="setCurrency('USD')">USD</button>
                <button class="curr-btn" data-curr="EUR" onclick="setCurrency('EUR')">EUR</button>
                <button class="curr-btn" data-curr="GBP" onclick="setCurrency('GBP')">GBP</button>
                <button class="curr-btn" data-curr="INR" onclick="setCurrency('INR')">INR</button>
            </div>

            <!-- Shortlist Drawer Trigger -->
            <button class="shortlist-trigger" onclick="toggleShortlist()">
                <span>★ Shortlist</span>
                <span class="shortlist-count" id="shortlistBadge">0</span>
            </button>
        </div>
    </header>

    <!-- Hero Showcase Section with Table Mountain Backdrop -->
    <div class="hero-banner-wrapper" style="background-image: url('{hero_bg}');">
        <div class="hero-banner-overlay"></div>
        <section class="hero-section">
            <div class="hero-meta-badges">
                <span class="badge-premium">Verified Production Inventory · 2026/2027 Season</span>
                <span class="badge-sub">Turnkey Local Fixer & Location Management</span>
            </div>

            <h1 class="hero-title">
                CAPE TOWN & SOUTH AFRICA<br>
                <span class="gold">MASTER LOCATION SCOUTING DATABASE</span>
            </h1>

            <p class="hero-subtitle">
                An expansive cinematic portfolio curated for prospective international film, television, and commercial productions. Engineered for peerless global doubling versatility, rapid permitting, and world-class crew and studio infrastructure.
            </p>

            <!-- KPI Stats Grid - 4 Focused Macro Columns -->
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">{len(categories)}</div>
                    <div class="stat-label">Curated Macro Categories</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">{len(images)}</div>
                    <div class="stat-label">Verified Hero Assets</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">40-60%</div>
                    <div class="stat-label">Currency Budget Advantage</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">14.5h</div>
                    <div class="stat-label">Peak Summer Daylight</div>
                </div>
            </div>

            <!-- Hero Action Button Cluster -->
            <div class="hero-action-buttons">
                <a href="#categories-showcase" class="btn-nav primary" style="padding: 0.75rem 1.6rem; font-size: 0.88rem;">
                    🎬 Explore 18 Macro Categories
                </a>
                <a href="#costing-estimate" class="btn-nav" style="padding: 0.75rem 1.6rem; font-size: 0.88rem; border-color: var(--border-gold); color: var(--gold-bright); background: rgba(212, 175, 55, 0.12);">
                    📊 Commercial Costing Estimate (Live Multi-Currency)
                </a>
                <a href="#strategic-proposal" class="btn-nav" style="padding: 0.75rem 1.6rem; font-size: 0.88rem;">
                    📋 5-Pillar Strategic Proposal
                </a>
            </div>

            <!-- Alphabetical Category Directory & Global Doubling Catalog -->
            <div class="alpha-directory-section">
                <div class="alpha-dir-main-header">
                    <div class="doubling-title">The Global Doubling Catalog & Alphabetical Directory</div>
                    <div class="doubling-desc" style="max-width: 950px; margin-top: 0.4rem; color: var(--text-muted); font-size: 0.95rem; line-height: 1.6;">
                        Spaced out into distinct alphabetical regional clusters (<strong>A – C</strong>, <strong>D – F</strong>, <strong>G – I</strong>, <strong>M – O</strong>, <strong>P – R</strong>, <strong>S – U</strong>, <strong>V – Z</strong>). Within a 60-minute radius of Cape Town CBD, productions can access pristine Mediterranean coastlines, California highway passes, Hollywood villas, London streets, Nevada desert basins, Scandinavian timber lodges, Olympic arenas, and deep-cut industrial quarries. Select any cluster or category below to explore:
                    </div>
                </div>

                <div class="alpha-directory-grid">
"""

for grp in alpha_groups:
    html_template += f"""                    <div class="alpha-dir-card">
                        <div class="alpha-dir-header">
                            <div style="display: flex; align-items: center; gap: 0.65rem;">
                                <span class="alpha-badge">{grp['label']}</span>
                                <span class="alpha-dir-title">{grp['title']}</span>
                            </div>
                            <button type="button" class="btn-group-view" onclick="filterAlphaGroup('{grp['id']}')">View ({len(grp['cat_ids'])}) &rarr;</button>
                        </div>
                        <div class="alpha-dir-desc">{grp['desc']}</div>
                        <div class="alpha-dir-items">\n"""
    for cat_id in grp["cat_ids"]:
        cat = next((c for c in categories if c["id"] == cat_id), None)
        if not cat: continue
        html_template += f"""                            <button type="button" class="doubling-tag" onclick="filterCategory('{cat['id']}')">{cat['icon']} {cat['num']} {cat['doubles_as']}</button>\n"""
    html_template += """                        </div>\n                    </div>\n"""

html_template += """                </div>
                <div style="margin-top: 1.8rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 1.2rem;">
                    <div style="font-family: var(--font-tech); font-size: 0.82rem; color: var(--text-dim);">
                        All 18 macro categories mapped to verified Cape Town GPS coordinates with active municipal filming permits.
                    </div>
                    <a href="#costing-estimate" class="btn-nav primary" style="padding: 0.75rem 1.6rem; font-size: 0.88rem;">Review Commercial Costing Estimate</a>
                </div>
            </div>
        </section>
    </div>

    <!-- STRATEGIC PROPOSAL: WHY CAPE TOWN & THE 5-PILLAR ARCHITECTURE -->
    <section class="proposal-section" id="strategic-proposal">
        <div class="proposal-container">
            <div class="proposal-header">
                <span class="badge-premium">International Executive Pitch Framework</span>
                <h2>The Western Cape Production Proposition</h2>
                <p style="font-size: 1.05rem; color: var(--text-muted); max-width: 820px; margin: 0 auto; line-height: 1.65;">
                    A credible, evidence-based strategic framework evaluating Cape Town and the Western Cape against global film, television, and commercial production standards.
                </p>
                <div class="proposal-lead-quote">
                    "The Western Cape's pitch is not: 'Come here because we have a big rebate.' It is: 'The Western Cape combines an available national production incentive with a mature production ecosystem, exceptional location versatility, and relatively efficient logistics.'"
                </div>
            </div>

            <!-- Comparative Assessment Matrix Table -->
            <div class="matrix-table-wrap">
                <table class="matrix-table">
                    <thead>
                        <tr>
                            <th style="width: 22%;">Global Producer Criterion</th>
                            <th style="width: 23%;">Western Cape Position</th>
                            <th style="width: 55%;">What We Can Credibly Say (Verified Assessment)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="pillar-col-title">1. Production Incentives</td>
                            <td>
                                <span class="pillar-pos-badge caveat">Available National Incentive</span>
                                <div style="font-size: 0.78rem; color: var(--text-dim); margin-top: 0.4rem; font-family: var(--font-tech);">Subject to eligibility & approval</div>
                            </td>
                            <td>
                                <strong>South Africa operates a national incentive, not a separate simple "Western Cape rebate."</strong> Foreign productions currently qualify for <strong>25% of QSAPE</strong> (Qualifying South African Production Expenditure), capped at <strong>R25m</strong>, with a potential additional <strong>5%</strong> under specified conditions (e.g., qualifying post-production).<br><br>
                                <em style="color: var(--gold-bright);">Realistic Cash-Flow Note:</em> In August 2026, the <strong>dtic</strong> announced that it is comprehensively reviewing the Film and Television Incentive Programme. While applications proceed under current guidelines, processing cycles require planning. It should be presented as an attractive available incentive subject to formal approval, rather than guaranteed upfront cash.
                            </td>
                        </tr>
                        <tr>
                            <td class="pillar-col-title">2. Infrastructure & Crew</td>
                            <td>
                                <span class="pillar-pos-badge strong">Strong</span>
                                <div style="font-size: 0.78rem; color: var(--text-dim); margin-top: 0.4rem; font-family: var(--font-tech);">Established commercial & film ecosystem</div>
                            </td>
                            <td>
                                Cape Town hosts deeply established commercial production companies, world-class technical crews, premier equipment rental houses (Photo Hire, Panavision, Media Film Service), soundstages, and post-production facilities.<br><br>
                                <strong>Cape Town Film Studios (CTFS)</strong> provides purpose-built Hollywood-standard soundstage facilities, while facilities such as <strong>Photo Hire provide 220–405 m² studio options</strong> alongside comprehensive camera, lighting, and grip support.
                            </td>
                        </tr>
                        <tr>
                            <td class="pillar-col-title">3. Location Versatility</td>
                            <td>
                                <span class="pillar-pos-badge very-strong">Very Strong</span>
                                <div style="font-size: 0.78rem; color: var(--text-dim); margin-top: 0.4rem; font-family: var(--font-tech);">Primary regional differentiator globally</div>
                            </td>
                            <td>
                                <strong>This is the clearest Western Cape differentiator.</strong> Within relatively short travelling distances (under 60 minutes from Cape Town CBD), productions can access pristine beaches, ocean, mountain passes, vineyards, urban city streets, industrial excavation quarries, period architecture, modern cantilevered architecture, agricultural farms, and character residential environments.<br><br>
                                <strong>Film Cape Town</strong> specifically promotes the region's unmatched capability to double international locations (California, Mediterranean, London, New York, Nevada, and European alpine passes) from a single production hotel base.
                            </td>
                        </tr>
                        <tr>
                            <td class="pillar-col-title">4. Logistics & Stability</td>
                            <td>
                                <span class="pillar-pos-badge caveat">Strong, with Caveats</span>
                                <div style="font-size: 0.78rem; color: var(--text-dim); margin-top: 0.4rem; font-family: var(--font-tech);">Dedicated permit office & UTC+2 time zone</div>
                            </td>
                            <td>
                                Cape Town operates an established municipal <strong>Film Permit Office</strong>, online permitting, experienced local production support, advanced transport/ICT infrastructure, and a European-friendly time zone (UTC+2 / CAT with zero jetlag for UK and European agency clients).<br><br>
                                Public-location filming requires formal municipal permits, but the City has a dedicated coordination system for multi-department approvals (Metro Police road closures, SANParks nature reserves, and civic squares).
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- TVC 4-Pillar Grid -->
            <div class="tvc-wrapper">
                <h3 class="tvc-section-title">Where the Western Cape Excels for Commercials (TVCs)</h3>
                <p class="tvc-section-sub">
                    For commercial and brand producers, the Western Cape translates into an extraordinarily compelling, high-efficiency proposition:
                </p>
                <div class="tvc-grid">
                    <div class="tvc-card">
                        <div class="tvc-card-icon">💰</div>
                        <div class="tvc-card-title">1. Financials</div>
                        <p class="tvc-card-desc">
                            Highly competitive production day rates combined with a massive <strong>40% to 60% exchange-rate purchasing power advantage</strong> against USD, EUR, and GBP, plus the national incentive where the project meets QSAPE criteria.
                        </p>
                    </div>

                    <div class="tvc-card">
                        <div class="tvc-card-icon">🎥</div>
                        <div class="tvc-card-title">2. Production Capability</div>
                        <p class="tvc-card-desc">
                            Top-tier commercial directors of photography, gaffers, grips, art directors, and specialist camera operators (drones, Russian Arms, Phantom high-speed) deeply experienced in demanding international TVC turnarounds.
                        </p>
                    </div>

                    <div class="tvc-card">
                        <div class="tvc-card-icon">🗺️</div>
                        <div class="tvc-card-title">3. Creative Flexibility</div>
                        <p class="tvc-card-desc">
                            A single Cape Town base can provide dramatically different visual environments. A 3-day commercial schedule can shoot California coastal highways, a Tuscan vineyard estate, and a Manhattan rooftop without moving hotel bases.
                        </p>
                    </div>

                    <div class="tvc-card">
                        <div class="tvc-card-icon">⏱️</div>
                        <div class="tvc-card-title">4. Operational Practicality</div>
                        <p class="tvc-card-desc">
                            Fluent English-speaking crews, European-compatible time zone for seamless live client streaming, dedicated online film permitting, 14.5 hours of summer daylight, and compact travel distances between diverse locations.
                        </p>
                    </div>
                </div>
            </div>

            <!-- Pillar 5: Location Intelligence & Local Facilitation -->
            <div class="p5-banner">
                <div class="p5-header">
                    <div>
                        <span class="badge-premium">Pillar 5 · Turnkey Delivery</span>
                        <h3 class="p5-title" style="margin-top: 0.5rem;">Location Intelligence & Local Facilitation (SA Locations & Zencrew)</h3>
                    </div>
                    <a href="mailto:laura@zencrew.co.za?cc=jardin@salocations.com&subject=Production%20Inquiry%20-%20Cape%20Town%205-Pillar%20Pitch" class="btn-nav primary">
                        Inquire Production Brief
                    </a>
                </div>
                <p class="p5-lead">
                    International producers do not need to learn the Western Cape from scratch. <strong>SA Locations & Zencrew</strong> provide the specialized local location intelligence, scouting archives, private property access, council permit coordination, and on-the-ground management required to turn a creative brief into a flawless, shootable Cape Town production.
                </p>

                <!-- 5-Step Workflow -->
                <div class="workflow-steps-grid">
                    <div class="wf-step-card">
                        <div class="wf-step-num">STEP 01</div>
                        <div class="wf-step-title">Creative Briefing</div>
                        <div class="wf-step-desc">Detailed script breakdown, architectural doubling alignment, and director visual matching.</div>
                    </div>
                    <div class="wf-step-card">
                        <div class="wf-step-num">STEP 02</div>
                        <div class="wf-step-title">Database Scouting</div>
                        <div class="wf-step-desc">Curation from 8,000+ verified scouted assets with sun-path analysis and GPS coordinates.</div>
                    </div>
                    <div class="wf-step-card">
                        <div class="wf-step-num">STEP 03</div>
                        <div class="wf-step-title">Technical Recces</div>
                        <div class="wf-step-desc">Physical site inspections, drone previews, unit base parking staging, and power logistics checks.</div>
                    </div>
                    <div class="wf-step-card">
                        <div class="wf-step-num">STEP 04</div>
                        <div class="wf-step-title">Permitting & Legal</div>
                        <div class="wf-step-desc">Cape Town Film Permit Office, SANParks clearances, Metro Police escorts, and property contracts.</div>
                    </div>
                    <div class="wf-step-card">
                        <div class="wf-step-num">STEP 05</div>
                        <div class="wf-step-title">Shoot Management</div>
                        <div class="wf-step-desc">On-set location management, technical truck marshaling, environmental compliance, and site wrap.</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Sticky Category Filter Navigation with Alphabetical Tiering -->
    <nav class="category-nav-wrap" id="categories-showcase" style="top: 50px;">
        <!-- Tier 1: Alphabetical Group Tabs (A-C, D-F, etc.) -->
        <div class="alpha-group-selector">
            <span class="alpha-selector-label">Alphabetical Index:</span>
            <button class="alpha-tab-btn active" data-alpha-group="all" onclick="filterAlphaGroup('all', this)">All (18)</button>
"""
for grp in alpha_groups:
    html_template += f"""            <button class="alpha-tab-btn" data-alpha-group="{grp['id']}" onclick="filterAlphaGroup('{grp['id']}', this)">{grp['label']} ({len(grp['cat_ids'])})</button>\n"""

html_template += f"""        </div>

        <!-- Tier 2: Spaced Out Category Navigation Pills -->
        <div class="category-nav" id="categoryNav">
            <button class="cat-pill active" data-cat-id="all" onclick="filterCategory('all', this)">All Categories ({len(categories)})</button>
"""
for grp in alpha_groups:
    html_template += f"""            <span class="nav-group-divider" data-alpha-group="{grp['id']}">| {grp['label']} |</span>\n"""
    for cat_id in grp["cat_ids"]:
        cat = next((c for c in categories if c["id"] == cat_id), None)
        if not cat: continue
        pill_label = f"{cat['icon']} {cat['num']} {cat['title'].split(',')[0].split('&')[0].strip()}"
        html_template += f"""            <button class="cat-pill" data-cat-id="{cat['id']}" data-alpha-group="{grp['id']}" onclick="filterCategory('{cat['id']}', this)">{pill_label}</button>\n"""

html_template += """        </div>
    </nav>

    <!-- Main Location Showcase Content -->
    <main class="deck-container">
        <!-- Single Category View Breadcrumb Banner -->
        <div id="categoryActiveBanner" class="category-active-banner" style="display: none;">
            <button class="btn-back-overview" onclick="filterCategory('all')">
                ← Back to Global Overview (All {len(categories)} Categories)
            </button>
            <div class="active-category-title-display" id="activeCategoryTitleDisplay"></div>
        </div>
"""

# Render Category Blocks Grouped by Alphabetical Cluster (A-C, D-F, G-I, M-O, P-R, S-U, V-Z)
for grp in alpha_groups:
    html_template += f"""
        <!-- Alphabetical Group Cluster: {grp['label']} - {grp['title']} -->
        <section class="alpha-cluster-wrapper" id="group-{grp['id']}" data-alpha-group="{grp['id']}">
            <div class="alpha-cluster-banner">
                <div class="alpha-cluster-left">
                    <span class="alpha-cluster-badge">CATALOG GROUP {grp['label']}</span>
                    <h3 class="alpha-cluster-title">{grp['title']}</h3>
                </div>
                <div class="alpha-cluster-meta">{len(grp['cat_ids'])} Categories &middot; {grp['desc']}</div>
            </div>
"""
    for cat_id in grp["cat_ids"]:
        cat = next((c for c in categories if c["id"] == cat_id), None)
        if not cat: continue
        hero_b64 = images.get(cat["hero_image_file"], "")
        hero_img_file = cat["hero_image_file"].replace("\\", "\\\\")
        hero_title_clean = cat["hero_image_title"].replace("'", "\\'")
        cat_title_clean = cat["title"].replace("'", "\\'")

        search_text = f"{cat['title']} {cat['doubles_as']} {cat['area']} {cat['tagline']} {cat['hero_image_title']}".lower()

        html_template += f"""
            <!-- Category Block: {cat['num']} - {cat['title']} -->
            <article class="category-block" id="{cat['id']}" data-cat-id="{cat['id']}" data-alpha-group="{grp['id']}" data-search-text="{search_text}">
                <!-- Category Header -->
                <div class="category-header">
                    <div class="cat-meta-row">
                        <span class="cat-num-badge">GROUP {grp['label']} &middot; CATEGORY {cat['num']} OF {len(categories)}</span>
                        <span class="cat-doubling-banner">Doubles For: {cat['doubles_as']}</span>
                    </div>
                    <h2 class="category-title">{cat['icon']} {cat['title']}</h2>
                    <div class="category-area">Primary Locations: {cat['area']}</div>
                    <p class="category-synopsis">{cat['creative_synopsis']}</p>
                </div>

                <!-- Hero Location Showcase - Strict Landscape with Wording Below -->
                <div class="hero-showcase">
                    <div class="hero-image-wrap" data-cat-id="{cat['id']}" data-alpha-group="{grp['id']}" data-file="{hero_img_file}" onclick="openLightbox('{cat['id']}', 0)">
                        <img src="{hero_b64}" alt="{cat['hero_image_title']}" loading="lazy">
                        <span class="hero-overlay-badge">{cat['hero_badge']}</span>
                        <div class="hero-overlay-heart" onclick="event.stopPropagation(); toggleShortlistItem('{hero_img_file}', '{hero_title_clean}', '{cat_title_clean}', this)">
                            <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                        </div>
                    </div>

                    <!-- Wording Positioned Below the Landscape Hero Photo -->
                    <div class="hero-details-panel">
                        <div class="hero-details-top">
                            <h3>{cat['hero_image_title']}</h3>
                            <p class="tagline">{cat['tagline']}</p>
                        </div>

                        <div class="hero-content-grid">
                            <div>
                                <div class="section-sub-label">✦ Key Architectural & Filming Features</div>
                                <ul class="key-features-list">
    """
        for feat in cat["key_features"]:
            html_template += f"                                <li>{feat}</li>\n"

        cal_title = cat['title'].replace(' ', '+')
        cal_area = cat['area'].replace(' ', '+')
        html_template += f"""                            </ul>
                            </div>

                            <div>
                                <div class="section-sub-label">⚙ Technical Filming Specifications</div>
                                <div class="specs-panel">
                                    <div class="spec-item">
                                        <span class="spec-label">Permits & Authority</span>
                                        <span class="spec-value">{cat['specs']['permitting']}</span>
                                    </div>
                                    <div class="spec-item">
                                        <span class="spec-label">Power Logistics</span>
                                        <span class="spec-value">{cat['specs']['power']}</span>
                                    </div>
                                    <div class="spec-item">
                                        <span class="spec-label">Unit Base Parking</span>
                                        <span class="spec-value">{cat['specs']['parking']}</span>
                                    </div>
                                    <div class="spec-item">
                                        <span class="spec-label">Acoustics & Curfew</span>
                                        <span class="spec-value">{cat['specs']['sound_curfew']}</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="hero-actions-row">
                            <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Location+Scouting+Recce%3A+{cal_title}&details=Technical+Location+Recce+request+with+Zencrew+%28Laura+Diana+Macleod%29+and+SA+Locations+%28Jardin+Roestorff%29.%0A%0ACategory%3A+{cal_title}%0ARegion%3A+{cal_area}&location={cal_area}&add=laura@zencrew.co.za&add=jardin@salocations.com" target="_blank" rel="noopener noreferrer" class="btn-nav primary">
                                📅 Schedule Category Recce
                            </a>
                            <button class="btn-nav" onclick="copyCategoryLink('{cat['id']}')">🔗 Share Category</button>
                        </div>
                    </div>
                </div>

                <!-- Scouted Images Database Gallery -->
                <div class="gallery-section">
                    <div class="gallery-header-row">
                        <div class="gallery-title">
                            <span>Scouted Images Database Gallery</span>
                            <span class="gallery-badge">{len(cat['gallery'])} Verified Locations</span>
                        </div>
                        <div style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-tech);">
                            Click any image to view in fullscreen cinema lightbox
                        </div>
                    </div>
    """
        if cat["id"] == "golf-courses-country-club-estates":
            html_template += """
                    <div class="panorama-triptych-wrap">
                        <div class="panorama-triptych-header">
                            <span class="badge-premium">✦ Sequential 3-Shot Panoramic Vista</span>
                            <div class="panorama-triptych-title">Clovelly Country Club: 180° Valley Amphitheater Panorama (Left · Center · Right)</div>
                        </div>
                        <div class="panorama-triptych-grid">
    """
            for idx in range(3):
                item = cat["gallery"][idx]
                img_b64 = images.get(item["file"], "")
                item_img_file = item["file"].replace("\\", "\\\\")
                item_title_clean = item["title"].replace("'", "\\'")
                html_template += f"""
                            <div class="panorama-pane" data-cat-id="{cat['id']}" data-alpha-group="{grp['id']}" data-photo-idx="{idx}" data-file="{item_img_file}" onclick="openLightbox('{cat['id']}', {idx})">
                                <div class="gallery-thumb-wrap" style="aspect-ratio: 16/9;">
                                    <img src="{img_b64}" alt="{item['title']}" loading="lazy">
                                    <span class="gallery-thumb-tag">{item['tag']}</span>
                                    <div class="gallery-card-heart" onclick="event.stopPropagation(); toggleShortlistItem('{item_img_file}', '{item_title_clean}', '{cat_title_clean}', this)">
                                        <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                                    </div>
                                </div>
                                <div class="gallery-card-info">
                                    <div class="gallery-card-title">{item['title']}</div>
                                </div>
                            </div>"""

            html_template += """
                        </div>
                    </div>

                    <div class="gallery-grid">
    """
            gallery_items = cat["gallery"][3:]
            start_idx = 3
        else:
            html_template += """
                    <div class="gallery-grid">
    """
            gallery_items = cat["gallery"]
            start_idx = 0

        for idx_offset, item in enumerate(gallery_items):
            idx = start_idx + idx_offset
            img_b64 = images.get(item["file"], "")
            item_img_file = item["file"].replace("\\", "\\\\")
            item_title_clean = item["title"].replace("'", "\\'")
            html_template += f"""
                        <div class="gallery-card" data-cat-id="{cat['id']}" data-alpha-group="{grp['id']}" data-photo-idx="{idx}" data-file="{item_img_file}" onclick="openLightbox('{cat['id']}', {idx})">
                            <div class="gallery-thumb-wrap">
                                <img src="{img_b64}" alt="{item['title']}" loading="lazy">
                                <span class="gallery-thumb-tag">{item['tag']}</span>
                                <div class="gallery-card-heart" onclick="event.stopPropagation(); toggleShortlistItem('{item_img_file}', '{item_title_clean}', '{cat_title_clean}', this)">
                                    <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                                </div>
                            </div>
                            <div class="gallery-card-info">
                                <div class="gallery-card-title">{item['title']}</div>
                            </div>
                        </div>"""

        html_template += """
                    </div>
                </div>
            </article>
    """

    html_template += """        </section>\n"""

# Append Extended Daylight & Golden Hour Section
html_template += """
        <!-- Extended Summer Daylight & The Atlantic Golden Hour -->
        <section class="golden-hour-section" id="golden-hour">
            <div class="gh-container">
                <div class="gh-header">
                    <span class="badge-premium">Atlantic Seaboard Magic Hour Advantage</span>
                    <h2>Extended Summer Daylight & The Atlantic Golden Hour</h2>
                    <p class="gh-subtitle">
                        14.5 hours of daily filming light, a prolonged 90-minute west-facing Atlantic sunset magic hour, and opposite-hemisphere midsummer shooting when Europe and North America are frozen.
                    </p>
                </div>

                <div class="gh-grid">
                    <div class="gh-card">
                        <div class="gh-icon">☀️</div>
                        <div class="gh-stat">14.5 Hours</div>
                        <div class="gh-card-title">Peak Summer Daylight</div>
                        <p class="gh-desc">
                            During peak film season (November to March), Cape Town enjoys sunrise as early as 05:30 and dusk beyond 20:30. Production crews routinely schedule full 12-hour camera days with consistent, predictable sunlight.
                        </p>
                    </div>

                    <div class="gh-card featured">
                        <div class="gh-icon">🌅</div>
                        <div class="gh-stat">90 Minutes</div>
                        <div class="gh-card-title">The Atlantic Sunset Magic Hour</div>
                        <p class="gh-desc">
                            The iconic coastal corridor—Clifton, Camps Bay, Llandudno, and Chapman's Peak—faces unobstructed due west over the Atlantic Ocean. Golden hour bathes granite boulders, white sands, and ocean spray in rich amber light without early mountain shadows.
                        </p>
                    </div>

                    <div class="gh-card">
                        <div class="gh-icon">🔄</div>
                        <div class="gh-stat">Double-Call</div>
                        <div class="gh-card-title">Turnaround Shooting Flexibility</div>
                        <p class="gh-desc">
                            Directors can execute intensive daytime narrative dialogue scenes and transition seamlessly to sunset magic hour and blue-hour dusk ocean sequences within a single crew call, maximizing schedule efficiency.
                        </p>
                    </div>

                    <div class="gh-card">
                        <div class="gh-icon">🌍</div>
                        <div class="gh-stat">300+ Days</div>
                        <div class="gh-card-title">Reverse-Hemisphere Season</div>
                        <p class="gh-desc">
                            When North American and European production hubs enter overcast, cold winter conditions, Cape Town offers midsummer warmth, crystal-clear coastal skies, and 300+ days of annual sunshine.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- COMMERCIAL PRODUCTION COSTING ESTIMATE & DAY RATES (GENERIC) -->
        <section class="costing-section" id="costing-estimate">
            <div class="costing-container">
                <div class="costing-header">
                    <span class="badge-premium">Zencrew & SA Locations · Standard Commercial Costing Framework</span>
                    <h2>Commercial Production Costing Estimate</h2>
                    <p class="costing-lead">
                        Transparent commercial day rate schedule and verified location permitting benchmarks for international film, TVC, and stills productions in Cape Town and the Western Cape. All figures update dynamically in real time based on your selected currency.
                    </p>
                </div>

                <!-- TABLE 1: CREW & TECHNICAL OPERATIONS DAY RATES -->
                <div class="costing-table-card">
                    <div class="costing-card-header">
                        <div class="costing-card-title">
                            <span>👥 Key Crew & Technical Operations Day Rates</span>
                        </div>
                        <span class="badge-sub">Standard 10-12 Hour Camera Day Benchmark</span>
                    </div>
                    <div style="overflow-x: auto;">
                        <table class="costing-table">
                            <thead>
                                <tr>
                                    <th style="width: 25%;">Role / Operational Function</th>
                                    <th style="width: 15%;">Department</th>
                                    <th style="width: 40%;">Scope of Work & Production Responsibility</th>
                                    <th style="width: 20%;">Commercial Day Rate</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="role-title">Line Producer</td>
                                    <td><span class="dept-pill">Production</span></td>
                                    <td class="scope-cell">Master commercial line producing, production accounting, contract negotiation & local team oversight</td>
                                    <td class="rate-cell" data-base-zar="8000" data-rate-suffix="/ day">R 8,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Production Manager (PM)</td>
                                    <td><span class="dept-pill">Production</span></td>
                                    <td class="scope-cell">Day-to-day operational execution, transport coordination, shoot logistics & vendor management</td>
                                    <td class="rate-cell" data-base-zar="6000" data-rate-suffix="/ day">R 6,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">1st Assistant Director (1st AD)</td>
                                    <td><span class="dept-pill">Directing / Ops</span></td>
                                    <td class="scope-cell">On-set call sheet execution, shooting schedule pacing, safety enforcement & department coordination</td>
                                    <td class="rate-cell" data-base-zar="6000" data-rate-suffix="/ day">R 6,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Location Manager (LM)</td>
                                    <td><span class="dept-pill">Locations</span></td>
                                    <td class="scope-cell">Municipal film office liaison, private property contracts, council permits, police escorts & unit staging</td>
                                    <td class="rate-cell" data-base-zar="5000" data-rate-suffix="/ day">R 5,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Location Assistant / Unit Assistant</td>
                                    <td><span class="dept-pill">Locations / Unit</span></td>
                                    <td class="scope-cell">Unit base setup, parking coning, marquee staging, facility sanitation & environmental site cleanup</td>
                                    <td class="rate-cell" data-base-zar="3000" data-rate-suffix="/ day">R 3,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Focus Puller (1st AC)</td>
                                    <td><span class="dept-pill">Camera</span></td>
                                    <td class="scope-cell">Cine lens optical calibration, precision wireless follow-focus tracking, sensor care & camera package prep</td>
                                    <td class="rate-cell" data-base-zar="3800" data-rate-suffix="/ day">R 3,800 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Camera Assistant (2nd AC / Loader)</td>
                                    <td><span class="dept-pill">Camera</span></td>
                                    <td class="scope-cell">Clapper board slating, digital magazine logging, battery management, cable runs & camera support</td>
                                    <td class="rate-cell" data-base-zar="2400" data-rate-suffix="/ day">R 2,400 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Gaffer (Chief Lighting Technician)</td>
                                    <td><span class="dept-pill">Lighting</span></td>
                                    <td class="scope-cell">Lighting design execution, power distribution safety, generator synchronization & lighting crew direction</td>
                                    <td class="rate-cell" data-base-zar="4100" data-rate-suffix="/ day">R 4,100 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Best Boy Electric</td>
                                    <td><span class="dept-pill">Lighting</span></td>
                                    <td class="scope-cell">Lighting truck equipment inventory, cable distro runs, generator fueling & electrical safety oversight</td>
                                    <td class="rate-cell" data-base-zar="2800" data-rate-suffix="/ day">R 2,800 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Key Grip</td>
                                    <td><span class="dept-pill">Grips</span></td>
                                    <td class="scope-cell">Camera rigging, tracking dolly, cranes, jibs, vehicle camera mounts & structural set safety</td>
                                    <td class="rate-cell" data-base-zar="3900" data-rate-suffix="/ day">R 3,900 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Art Director</td>
                                    <td><span class="dept-pill">Art Dept</span></td>
                                    <td class="scope-cell">Production design implementation, spatial set dressing, property sourcing & practical set styling</td>
                                    <td class="rate-cell" data-base-zar="7000" data-rate-suffix="/ day">R 7,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Wardrobe Mistress / Stylist</td>
                                    <td><span class="dept-pill">Wardrobe</span></td>
                                    <td class="scope-cell">Costume continuity, fitting management, steamer stations, quick-change tents & talent wardrobe prep</td>
                                    <td class="rate-cell" data-base-zar="3500" data-rate-suffix="/ day">R 3,500 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Hair and Make-up Stylist (H&MU)</td>
                                    <td><span class="dept-pill">Make-up</span></td>
                                    <td class="scope-cell">Lead talent styling, skin continuity, sweat control under sunlight & on-set camera touch-ups</td>
                                    <td class="rate-cell" data-base-zar="3000" data-rate-suffix="/ day">R 3,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Chaperone & Vehicle (Seats 5 Pax)</td>
                                    <td><span class="dept-pill">Transport</span></td>
                                    <td class="scope-cell">Dedicated 5-passenger crew/talent air-conditioned shuttle vehicle including professional driver</td>
                                    <td class="rate-cell" data-base-zar="7000" data-rate-suffix="/ day">R 7,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">On-Location Unit Equipment Package</td>
                                    <td><span class="dept-pill">Logistics</span></td>
                                    <td class="scope-cell">Heavy-duty pop-up gazebos, folding tables, directors chairs, lighted mirror stations, bins & silent eco-power</td>
                                    <td class="rate-cell" data-base-zar="6500" data-rate-suffix="/ day">R 6,500 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Motorcycle with Sidecar (Action Prop Vehicle)</td>
                                    <td><span class="dept-pill">Specialty Props</span></td>
                                    <td class="scope-cell">Camera-ready vintage running motorcycle with sidecar for tracking scenes (fuel & transport quoted per distance)</td>
                                    <td class="rate-cell" data-base-zar="8625" data-rate-suffix="/ day">R 8,625 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Featured Extras</td>
                                    <td><span class="dept-pill">Cast</span></td>
                                    <td class="scope-cell">Screen-featured background talent with specific interaction or specialized wardrobe styling</td>
                                    <td class="rate-cell" data-base-zar="1350" data-rate-suffix="/ day">R 1,350 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Background Extras (Crowd / Atmosphere)</td>
                                    <td><span class="dept-pill">Cast</span></td>
                                    <td class="scope-cell">General atmospheric background talent for cafes, urban streets, markets, and venue scenes</td>
                                    <td class="rate-cell" data-base-zar="950" data-rate-suffix="/ day">R 950 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">FIVA Visas (Film Industry Visa Assistance)</td>
                                    <td><span class="dept-pill">Legal / Visas</span></td>
                                    <td class="scope-cell">Fast-track professional film industry work visa endorsement per international crew member</td>
                                    <td class="rate-cell" data-base-zar="800" data-rate-suffix="/ person">R 800 / person</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- TABLE 2: VERIFIED LOCATION PERMITTING & ACCESS BENCHMARKS -->
                <div class="costing-table-card">
                    <div class="costing-card-header">
                        <div class="costing-card-title">
                            <span>🏛️ Verified Location Permitting & Access Benchmarks</span>
                        </div>
                        <span class="badge-sub">Benchmark Daily Location Fees & Municipal Permits</span>
                    </div>
                    <div style="overflow-x: auto;">
                        <table class="costing-table">
                            <thead>
                                <tr>
                                    <th style="width: 25%;">Location Benchmark / Typology</th>
                                    <th style="width: 18%;">Authority / Sector</th>
                                    <th style="width: 37%;">Filming Scope, Access & Architectural Characteristics</th>
                                    <th style="width: 20%;">Daily Location Fee</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="role-title">V&A Waterfront Shopping Centre & Quays</td>
                                    <td><span class="dept-pill">Atlantic Seaboard (Private)</span></td>
                                    <td class="scope-cell">Working maritime quays, luxury boardwalks, retail plazas & yachts with Table Mountain backdrop</td>
                                    <td class="rate-cell" data-base-zar="45000" data-rate-suffix="/ day">R 45,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">StarDust Theatrical Dining & Live Cabaret</td>
                                    <td><span class="dept-pill">Woodstock (Private Commercial)</span></td>
                                    <td class="scope-cell">Full theatrical dining room, raised stage, grand piano, live acoustic lighting & sound rig</td>
                                    <td class="rate-cell" data-base-zar="6000" data-rate-suffix="/ day">R 60,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Luxury Residential Family Home</td>
                                    <td><span class="dept-pill">Atlantic / City Bowl (Private)</span></td>
                                    <td class="scope-cell">Contemporary luxury family home featuring open-plan living and panoramic Table Mountain views</td>
                                    <td class="rate-cell" data-base-zar="15825" data-rate-suffix="/ day">R 15,825 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Church Square Heritage Cafe / Coffee Shop</td>
                                    <td><span class="dept-pill">CBD (Private Commercial)</span></td>
                                    <td class="scope-cell">Historic cobbled courtyard cafe, European street-side seating & heritage colonial facades</td>
                                    <td class="rate-cell" data-base-zar="25000" data-rate-suffix="/ day">R 25,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Rehearsal Studio Stage (Suite Spot / Roodebloem)</td>
                                    <td><span class="dept-pill">City Bowl (Private Studio)</span></td>
                                    <td class="scope-cell">Daylight rehearsal studio, polished concrete floors, infinity cyclorama & production green rooms</td>
                                    <td class="rate-cell" data-base-zar="30000" data-rate-suffix="/ day">R 30,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Church Square Civic Plaza</td>
                                    <td><span class="dept-pill">Cape Town Film Permit Office</span></td>
                                    <td class="scope-cell">Municipal film permit for historic public cobbled square, civic monuments & surrounding colonnades</td>
                                    <td class="rate-cell" data-base-zar="5000" data-rate-suffix="/ day">R 5,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Cape Farmhouse Cabin & Rustic Retreat</td>
                                    <td><span class="dept-pill">Scarborough (Private Estate)</span></td>
                                    <td class="scope-cell">Rustic timber cabin, outdoor amphitheater stage, indigenous tree canopy & mountain fynbos</td>
                                    <td class="rate-cell" data-base-zar="30000" data-rate-suffix="/ day">R 30,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Lourensford Wine Estate & MTB Mountain Trails</td>
                                    <td><span class="dept-pill">Somerset West (Private Estate)</span></td>
                                    <td class="scope-cell">Expansive private vineyard estate, downhill mountain bike tracks, pine forests & historic cellar halls</td>
                                    <td class="rate-cell" data-base-zar="90000" data-rate-suffix="/ day">R 90,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">M62 Scenic Coastal Corridor (Kommetjie)</td>
                                    <td><span class="dept-pill">Provincial Road / CoCT</span></td>
                                    <td class="scope-cell">Ocean coastal driving passes, sweeping curves, Atlantic horizons & sunset vehicle tracking</td>
                                    <td class="rate-cell" data-base-zar="5000" data-rate-suffix="/ day">R 5,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Bantry Bay Ocean Tidal Pool & Granite Rocks</td>
                                    <td><span class="dept-pill">Cape Town Film Permit Office</span></td>
                                    <td class="scope-cell">Municipal permit for seaside tidal saltwater pool, natural Atlantic surf breakers & granite boulders</td>
                                    <td class="rate-cell" data-base-zar="5000" data-rate-suffix="/ day">R 5,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Mouille Point Oceanfront Promenade</td>
                                    <td><span class="dept-pill">Cape Town Film Permit Office</span></td>
                                    <td class="scope-cell">Public paved coastal walking promenade, green lawns, red-and-white lighthouse & ocean vistas</td>
                                    <td class="rate-cell" data-base-zar="5000" data-rate-suffix="/ day">R 5,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">CTICC Convention Centre (Airport Concourse Double)</td>
                                    <td><span class="dept-pill">Foreshore CBD (Municipal)</span></td>
                                    <td class="scope-cell">Monumental glass-and-steel modern architecture doubling for international airport terminals</td>
                                    <td class="rate-cell" data-base-zar="50000" data-rate-suffix="/ day">R 50,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Misty Cliffs Coastal Reserve & Shoreline</td>
                                    <td><span class="dept-pill">SANParks Permit Office</span></td>
                                    <td class="scope-cell">National park marine permit for dramatic white-sand beaches, Atlantic breakers & towering headlands</td>
                                    <td class="rate-cell" data-base-zar="30000" data-rate-suffix="/ day">R 30,000 / day</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Chapman's Peak Lookout Pass</td>
                                    <td><span class="dept-pill">SANParks / Entilini Concession</span></td>
                                    <td class="scope-cell">World-renowned precipice cliff road overlooking Hout Bay, Sentinel headland & monkey valley lookouts</td>
                                    <td class="rate-cell" data-base-zar="30000" data-rate-suffix="/ day">R 30,000 / day</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- TABLE 3: MANDATORY PRODUCTION INSURANCE & INDEMNITY BASELINE -->
                <div class="costing-table-card" style="margin-bottom: 1.5rem;">
                    <div class="costing-card-header">
                        <div class="costing-card-title">
                            <span>🛡️ Production Insurance & Statutory Indemnity Baseline</span>
                        </div>
                        <span class="badge-sub">Baseline Risk Coverage & Municipal Mandates</span>
                    </div>
                    <div style="overflow-x: auto;">
                        <table class="costing-table">
                            <thead>
                                <tr>
                                    <th style="width: 28%;">Insurance Policy / Coverage Line</th>
                                    <th style="width: 20%;">Underwriting Scope</th>
                                    <th style="width: 32%;">Regulatory & Commercial Requirement</th>
                                    <th style="width: 20%;">Baseline Premium</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="role-title">Film Producer's Indemnity Insurance</td>
                                    <td><span class="dept-pill">Production Interruption</span></td>
                                    <td class="scope-cell">Comprehensive coverage for cast non-appearance, media damage, and unforeseen filming delays</td>
                                    <td class="rate-cell" data-base-zar="8000" data-rate-suffix="once-off">R 8,000 once-off</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Third Party Property Damage</td>
                                    <td><span class="dept-pill">Property Indemnity</span></td>
                                    <td class="scope-cell">Comprehensive protection for private luxury villas, heritage structures & municipal facilities</td>
                                    <td class="rate-cell" data-base-zar="4000" data-rate-suffix="once-off">R 4,000 once-off</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Public Liability Insurance (R50M-R100M Cover)</td>
                                    <td><span class="dept-pill">Public Risk</span></td>
                                    <td class="scope-cell">Mandatory statutory requirement for all City of Cape Town & SANParks filming permits</td>
                                    <td class="rate-cell" data-base-zar="6000" data-rate-suffix="once-off">R 6,000 once-off</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Employers Liability</td>
                                    <td><span class="dept-pill">Workforce Protection</span></td>
                                    <td class="scope-cell">Statutory employer indemnification for local crew members, unit personnel & on-set workforce</td>
                                    <td class="rate-cell" data-base-zar="3000" data-rate-suffix="once-off">R 3,000 once-off</td>
                                </tr>
                                <tr>
                                    <td class="role-title">Crew and Cast Personal Accident</td>
                                    <td><span class="dept-pill">Medical & Accident</span></td>
                                    <td class="scope-cell">Emergency 24/7 medical evacuation, trauma care & accidental injury cover per crew/cast member</td>
                                    <td class="rate-cell" data-base-zar="35" data-rate-suffix="/ person / day">R 35 / person / day</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <div style="text-align: center; margin-top: 2rem;">
                    <a href="mailto:laura@zencrew.co.za?cc=jardin@salocations.com&subject=Costing%20Estimate%20%26%20Budget%20Inquiry%20-%20Cape%20Town" class="btn-nav primary" style="padding: 0.85rem 2rem; font-size: 0.95rem;">
                        ✉ Inquire Custom Commercial Budget & Production Estimate
                    </a>
                </div>
            </div>
        </section>

        <!-- dtic INCENTIVE DEEP DIVE -->
        <section class="incentive-section" id="dtic-incentives">
            <div class="incentive-container">
                <div class="proposal-header">
                    <span class="badge-premium">Financial Framework & Trade Incentives</span>
                    <h2>The South African Production Incentive (dtic)</h2>
                    <p style="font-size: 1.05rem; color: var(--text-muted); max-width: 840px; margin: 0 auto; line-height: 1.65;">
                        Clear guidance on the Foreign Film and Television Production Incentive administered by the Department of Trade, Industry and Competition (dtic).
                    </p>
                </div>

                <div class="incentive-grid">
                    <div class="incentive-card highlight">
                        <div class="tvc-card-icon">🏛️</div>
                        <div class="tvc-card-title">National Scheme (Not Regional)</div>
                        <p class="tvc-card-desc">
                            South Africa operates a single unified national film incentive programme. There is no separate "Western Cape rebate." The competitive advantage of the Western Cape lies in pairing this national incentive with world-class production infrastructure and location density.
                        </p>
                    </div>

                    <div class="incentive-card">
                        <div class="tvc-card-icon">📈</div>
                        <div class="tvc-card-title">25% QSAPE + 5% Potential Uplift</div>
                        <p class="tvc-card-desc">
                            Qualifying foreign productions shot in South Africa are eligible for a <strong>25% rebate</strong> on Qualifying South African Production Expenditure (QSAPE), capped at <strong>R25 million</strong>. A potential additional <strong>5%</strong> applies under specified conditions such as qualifying post-production.
                        </p>
                    </div>

                    <div class="incentive-card">
                        <div class="tvc-card-icon">💱</div>
                        <div class="tvc-card-title">Immediate 40–60% Currency Arbitrage</div>
                        <p class="tvc-card-desc">
                            Regardless of incentive timing, international producers realize an immediate, guaranteed <strong>40% to 60% hard-cost advantage</strong> against USD, EUR, and GBP across local crew day rates, studio rental, hotel accommodation, and location access fees.
                        </p>
                    </div>
                </div>

                <!-- dtic Strategic Review Context Notice -->
                <div class="dtic-notice-box">
                    <div class="notice-icon">⚠️</div>
                    <div class="notice-content">
                        <h4>Regulatory Transparency: August 2026 dtic Incentive Review Notice</h4>
                        <p>
                            In August 2026, the Department of Trade, Industry and Competition (dtic) announced that it is comprehensively reviewing the Film and Television Incentive Programme. While applications currently continue to be processed under existing regulations, updated guidelines are pending publication. Producers are advised to structure financial models around Cape Town's immediate baseline cost and exchange-rate advantages, factoring in realistic administrative timelines for incentive disbursement.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Rates, Turnkey Production & Executive Contacts -->
        <section class="rates-section" id="rates-and-contacts">
            <div class="rates-header">
                <span class="badge-premium">Transparent Commercial Framework</span>
                <h2 style="margin-top: 0.8rem;">Standard Daily Rates & Turnkey Management</h2>
                <p>
                    Full location scouting, permitting, logistics management, and local fixer facilitation for international film, television, streaming, and commercial productions.
                </p>
            </div>

            <!-- Rate Cards Grid -->
            <div class="rates-cards-grid">
                <!-- Location Scouting -->
                <div class="rate-tier-card">
                    <span class="rate-badge">Recce & Scouting</span>
                    <h3>Location Scouting</h3>
                    <p class="tier-desc">Dedicated technical scout, bespoke location scouting, custom contact sheets & GPS mapping.</p>
                    <div class="rate-amount" id="scoutRateDisplay">R 5,000 <span class="unit">/ day</span></div>
                    <ul class="tier-features">
                        <li>Custom location curation from 8,000+ photo archive</li>
                        <li>High-resolution contact sheets & GPS coordinate tagging</li>
                        <li>Sun tracking analysis & drone recce availability</li>
                        <li>Direct coordination with property owners & city authorities</li>
                    </ul>
                    <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Book+Location+Scouting+Day&details=Location+Scouting+booking+request+with+SA+Locations+%28Jardin+Roestorff%29+and+Zencrew+%28Laura+Diana+Macleod%29.&location=Cape+Town&add=jardin@salocations.com&add=laura@zencrew.co.za" target="_blank" rel="noopener noreferrer" class="btn-nav primary" style="text-align: center; justify-content: center;">
                        Book Location Scout
                    </a>
                </div>

                <!-- Location Management -->
                <div class="rate-tier-card featured">
                    <span class="rate-badge">Shoot Days</span>
                    <h3>Location Management</h3>
                    <p class="tier-desc">On-set management, council permitting, traffic department marshals & unit base logistics.</p>
                    <div class="rate-amount" id="manageRateDisplay">R 5,500 <span class="unit">/ shoot day</span></div>
                    <ul class="tier-features">
                        <li>City of Cape Town & SANParks permit submission</li>
                        <li>Metro Police road closure escorts & traffic plans</li>
                        <li>Unit base parking coning & technical truck staging</li>
                        <li>Community notifications & environmental eco-monitors</li>
                    </ul>
                    <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Book+Location+Management+Days&details=Location+Management+shoot+day+request+with+Zencrew+%28Laura+Diana+Macleod%29+and+SA+Locations+%28Jardin+Roestorff%29.&location=Cape+Town&add=laura@zencrew.co.za&add=jardin@salocations.com" target="_blank" rel="noopener noreferrer" class="btn-nav primary" style="text-align: center; justify-content: center;">
                        Book Shoot Management
                    </a>
                </div>

                <!-- Turnkey Fixer Package -->
                <div class="rate-tier-card">
                    <span class="rate-badge">Full Production Support</span>
                    <h3>Turnkey Production Services</h3>
                    <p class="tier-desc">End-to-end South African service production, equipment hire, crew booking & line producing.</p>
                    <div class="rate-amount">Custom <span class="unit">/ package</span></div>
                    <ul class="tier-features">
                        <li>Full line producing & production accounting</li>
                        <li>Camera, lighting, grip & crane gear coordination</li>
                        <li>Top-tier local crew booking (DOP, Gaffer, Grips, Art Dept)</li>
                        <li>Transport fleets, honeywagons & gourmet mobile catering</li>
                    </ul>
                    <a href="mailto:laura@zencrew.co.za?cc=jardin@salocations.com&subject=Turnkey%20Production%20Services%20Inquiry%20-%20Cape%20Town" class="btn-nav" style="text-align: center; justify-content: center;">
                        Inquire Turnkey Package
                    </a>
                </div>
            </div>

            <!-- Executive Contacts Strip (Zencrew & SA Locations) -->
            <div class="exec-contacts-card">
                <!-- Laura Diana Macleod (Zencrew) -->
                <div class="contact-col">
                    <span class="contact-role">Zencrew Production Services · Lead Fixer & Producer</span>
                    <h3 class="contact-name">Laura Diana Macleod</h3>
                    <p class="contact-bio">
                        Seasoned South African location manager, producer, and commercial fixer with 15+ years managing high-profile international feature films, commercials, and photographic campaigns across Cape Town, the Karoo, and Southern Africa.
                    </p>
                    <div class="contact-links">
                        <a href="https://www.zencrew.co.za" target="_blank" rel="noopener noreferrer" class="contact-link highlight">
                            🌐 Website: www.zencrew.co.za
                        </a>
                        <a href="https://wa.me/27825708818" target="_blank" rel="noopener noreferrer" class="contact-link">
                            📱 WhatsApp / Mobile: +27 82 570 8818
                        </a>
                        <a href="mailto:laura@zencrew.co.za" class="contact-link">
                            ✉ Email: laura@zencrew.co.za
                        </a>
                        <a href="https://www.linkedin.com/in/laura-diana-macleod-a217a525" target="_blank" rel="noopener noreferrer" class="contact-link">
                            💼 LinkedIn: Laura Diana Macleod
                        </a>
                        <a href="https://www.imdb.com/name/nm2555501/" target="_blank" rel="noopener noreferrer" class="contact-link">
                            ⭐ IMDb Profile & Film Credits
                        </a>
                        <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Production+Consultation+-+Zencrew&details=Production+Consultation+with+Laura+Diana+Macleod+%28Zencrew%29.&location=Cape+Town&add=laura@zencrew.co.za" target="_blank" rel="noopener noreferrer" class="contact-link">
                            📅 Book Consultation Call
                        </a>
                    </div>
                </div>

                <!-- Jardin Roestorff (SA Locations Business Card) -->
                <div class="contact-col">
                    <span class="contact-role">SA Locations · Official Business Card</span>
                    <div class="biz-card-box">
                        <div class="biz-card-header">
                            <div>
                                <div class="biz-card-company">SALocations</div>
                                <div class="biz-card-tagline">Location Scouting & Film Facilitation</div>
                            </div>
                            <div class="biz-card-flag">🇿🇦 Cape Town</div>
                        </div>
                        <div class="biz-card-divider"></div>
                        <h3 class="contact-name">Jardin Roestorff</h3>
                        <p class="contact-bio" style="margin-bottom: 0.8rem;">
                            Specialized technical location scout with an 8,000+ photo archive spanning the Western Cape. Dedicated to architectural precision, cinematic framing, crane clearances, and digital production decks.
                        </p>
                        <div class="contact-links">
                            <a href="tel:+27734921998" class="contact-link highlight">
                                📱 Mobile: +27 73 492 1998
                            </a>
                            <a href="mailto:jardin@salocations.com" class="contact-link">
                                ✉ Email: jardin@salocations.com
                            </a>
                            <a href="https://www.salocations.com" target="_blank" rel="noopener noreferrer" class="contact-link highlight">
                                🌐 Web: www.salocations.com
                            </a>
                            <a href="https://www.instagram.com/salocations" target="_blank" rel="noopener noreferrer" class="contact-link">
                                📸 Instagram: @salocations
                            </a>
                            <a href="https://www.youtube.com/@salocations" target="_blank" rel="noopener noreferrer" class="contact-link">
                                🎬 YouTube: @salocations
                            </a>
                            <a href="mailto:jardin@salocations.com?subject=Master%20Database%20Custom%20Scouting%20Request" class="contact-link">
                                📋 Custom Scout Request
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Client Shortlist Drawer -->
    <aside class="shortlist-drawer" id="shortlistDrawer">
        <div class="drawer-header">
            <h3>Saved Location Shortlist</h3>
            <button class="drawer-close" onclick="toggleShortlist()">✕</button>
        </div>
        <div class="drawer-body" id="shortlistBody">
            <div class="shortlist-empty">
                No locations saved yet.<br>Click the heart icon on any photo to add it to your custom production deck.
            </div>
        </div>
        <div class="drawer-footer">
            <button class="btn-nav primary" onclick="sendShortlistInquiry()" style="justify-content: center; text-align: center;">
                ✉ Submit Shortlist to Producers
            </button>
            <button class="btn-nav" onclick="clearShortlist()" style="justify-content: center; text-align: center;">
                Clear Shortlist
            </button>
        </div>
    </aside>

    <!-- Fullscreen Cinema Lightbox -->
    <div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox(event)">
        <div class="lb-top-bar" onclick="event.stopPropagation()">
            <div class="lb-meta">
                <span class="lb-cat-badge" id="lbCatBadge">Category</span>
                <span class="lb-counter" id="lbCounter">1 / 10</span>
            </div>
            <div class="lb-actions">
                <button class="lb-btn" onclick="saveCurrentLightboxPhoto()">★ Add to Shortlist</button>
                <button class="lb-close-btn" onclick="closeLightbox()">✕</button>
            </div>
        </div>

        <div class="lb-stage">
            <button class="lb-nav-btn lb-prev" onclick="prevLightbox(event)">‹</button>
            <div class="lb-image-container" onclick="event.stopPropagation()">
                <img id="lbMainImage" src="" alt="">
            </div>
            <button class="lb-nav-btn lb-next" onclick="nextLightbox(event)">›</button>
        </div>

        <div class="lb-caption-bar" onclick="event.stopPropagation()">
            <div class="lb-caption-title" id="lbCaptionTitle">Location Title</div>
            <div class="lb-caption-sub" id="lbCaptionSub">Technical Scouting Inventory · Cape Town, South Africa</div>
        </div>
    </div>

    <!-- Site Footer -->
    <footer class="site-footer">
        <div class="footer-wrap">
            <div class="footer-logo-row">
                <a href="https://www.salocations.com" target="_blank" rel="noopener noreferrer" style="color: #ffffff; text-decoration: none;">SA Locations</a>
                <span style="color: var(--gold);">✕</span>
                <a href="https://www.zencrew.co.za" target="_blank" rel="noopener noreferrer" style="color: #ffffff; text-decoration: none;">Zencrew Production Services</a>
            </div>
            <div class="footer-social-row">
                <a href="https://www.salocations.com" target="_blank" rel="noopener noreferrer" class="social-link-btn">
                    🌐 SA Locations (www.salocations.com)
                </a>
                <a href="https://www.zencrew.co.za" target="_blank" rel="noopener noreferrer" class="social-link-btn">
                    🌐 Zencrew (www.zencrew.co.za)
                </a>
                <a href="https://www.instagram.com/salocations" target="_blank" rel="noopener noreferrer" class="social-link-btn">
                    📸 Instagram @salocations
                </a>
                <a href="https://www.youtube.com/@salocations" target="_blank" rel="noopener noreferrer" class="social-link-btn">
                    🎬 YouTube @salocations
                </a>
                <a href="https://www.linkedin.com/in/laura-diana-macleod-a217a525" target="_blank" rel="noopener noreferrer" class="social-link-btn">
                    💼 LinkedIn (Laura)
                </a>
                <a href="https://www.imdb.com/name/nm2555501/" target="_blank" rel="noopener noreferrer" class="social-link-btn">
                    ⭐ IMDb (Laura)
                </a>
            </div>
            <div class="footer-disclaimer">
                © 2026/2027 SA Locations & Zencrew. All """ + str(len(images)) + """ photographs within the Scouted Images Database are proprietary assets photographed on location across the Western Cape, South Africa. Direct bookings subject to municipal permit authorization.
            </div>
        </div>
    </footer>

    <!-- Interactive Logic Script (Zero Redundant Base64 Duplication) -->
    <script>
        const categoriesData = """ + json.dumps(categories) + """;
        const alphaGroupsData = """ + json.dumps(alpha_groups) + """;

        // Exchange Rates relative to ZAR
        const rates = {
            ZAR: { symbol: 'R', rate: 1, scout: 5000, manage: 5500, format: (val) => `R ${val.toLocaleString()}` },
            USD: { symbol: '$', rate: 0.056, scout: 280, manage: 310, format: (val) => `$ ${Math.round(val * 0.056).toLocaleString()}` },
            EUR: { symbol: '€', rate: 0.051, scout: 255, manage: 280, format: (val) => `€ ${Math.round(val * 0.051).toLocaleString()}` },
            GBP: { symbol: '£', rate: 0.044, scout: 220, manage: 240, format: (val) => `£ ${Math.round(val * 0.044).toLocaleString()}` },
            INR: { symbol: '₹', rate: 4.9, scout: 24500, manage: 27000, format: (val) => `₹ ${Math.round(val * 4.9).toLocaleString()}` }
        };

        let currentCurrency = 'ZAR';
        let currentShortlist = [];
        let activeCategoryIndex = 0;
        let activePhotoIndex = 0;
        let activeGallery = [];

        // Dynamic Currency Switching Across All Rate Cards and Costing Tables
        function setCurrency(curr) {
            currentCurrency = curr;
            document.querySelectorAll('.curr-btn').forEach(b => {
                b.classList.toggle('active', b.dataset.curr === curr);
            });

            const info = rates[curr];
            const scoutEl = document.getElementById('scoutRateDisplay');
            const manageEl = document.getElementById('manageRateDisplay');
            if (scoutEl) scoutEl.innerHTML = `${info.format(info.scout)} <span class="unit">/ day</span>`;
            if (manageEl) manageEl.innerHTML = `${info.format(info.manage)} <span class="unit">/ shoot day</span>`;

            // Update all elements with data-base-zar
            document.querySelectorAll('[data-base-zar]').forEach(el => {
                const baseZar = parseFloat(el.getAttribute('data-base-zar'));
                if (!isNaN(baseZar)) {
                    const suffix = el.getAttribute('data-rate-suffix') || '';
                    const converted = curr === 'ZAR' ? baseZar : Math.round(baseZar * info.rate);
                    el.innerHTML = `${info.symbol} ${converted.toLocaleString()}${suffix ? ' ' + suffix : ''}`;
                }
            });
        }

        // Alphabetical Group Filter (A-C, D-F, G-I, M-O, P-R, S-U, V-Z)
        function filterAlphaGroup(groupId, btnElement) {
            const heroWrapper = document.querySelector('.hero-banner-wrapper');
            const proposalSec = document.getElementById('strategic-proposal');
            const goldenHour = document.getElementById('golden-hour');
            const costingSec = document.getElementById('costing-estimate');
            const incentiveSec = document.getElementById('dtic-incentives');
            const ratesSec = document.getElementById('rates-and-contacts');
            const activeBanner = document.getElementById('categoryActiveBanner');
            const activeTitleDisplay = document.getElementById('activeCategoryTitleDisplay');

            // Update Alpha Tab buttons
            document.querySelectorAll('.alpha-tab-btn').forEach(b => {
                b.classList.toggle('active', b.dataset.alphaGroup === groupId);
            });

            // Filter Category Nav Pills
            document.querySelectorAll('.cat-pill').forEach(p => {
                if (groupId === 'all') {
                    p.style.display = 'inline-flex';
                    p.classList.toggle('active', p.dataset.catId === 'all');
                } else {
                    const belongs = p.dataset.alphaGroup === groupId;
                    p.style.display = belongs ? 'inline-flex' : 'none';
                    p.classList.remove('active');
                }
            });

            // Filter Nav Group Dividers
            document.querySelectorAll('.nav-group-divider').forEach(d => {
                d.style.display = (groupId === 'all' || d.dataset.alphaGroup === groupId) ? 'inline' : 'none';
            });

            // Filter Alpha Cluster Wrappers & Category Blocks
            const clusters = document.querySelectorAll('.alpha-cluster-wrapper');
            const blocks = document.querySelectorAll('.category-block');

            if (groupId === 'all') {
                clusters.forEach(c => c.style.display = 'block');
                blocks.forEach(b => b.style.display = 'block');
                if (heroWrapper) heroWrapper.style.display = 'block';
                if (proposalSec) proposalSec.style.display = 'block';
                if (goldenHour) goldenHour.style.display = 'block';
                if (costingSec) costingSec.style.display = 'block';
                if (incentiveSec) incentiveSec.style.display = 'block';
                if (ratesSec) ratesSec.style.display = 'block';
                if (activeBanner) activeBanner.style.display = 'none';
                if (window.location.hash) {
                    history.pushState(null, '', window.location.pathname);
                }
                const catNav = document.getElementById('categories-showcase');
                if (catNav) catNav.scrollIntoView({ behavior: 'smooth' });
            } else {
                clusters.forEach(c => {
                    c.style.display = (c.dataset.alphaGroup === groupId) ? 'block' : 'none';
                });
                blocks.forEach(b => {
                    b.style.display = (b.dataset.alphaGroup === groupId) ? 'block' : 'none';
                });

                // Keep proposal/costing/rates visible or scroll to group
                if (heroWrapper) heroWrapper.style.display = 'block';
                if (proposalSec) proposalSec.style.display = 'block';
                if (goldenHour) goldenHour.style.display = 'block';
                if (costingSec) costingSec.style.display = 'block';
                if (incentiveSec) incentiveSec.style.display = 'block';
                if (ratesSec) ratesSec.style.display = 'block';

                const grp = alphaGroupsData.find(g => g.id === groupId);
                if (activeBanner) {
                    activeBanner.style.display = 'flex';
                    if (activeTitleDisplay && grp) {
                        activeTitleDisplay.innerHTML = `<span>Alphabetical Directory:</span> <strong>Group ${grp.label} &middot; ${grp.title} (${grp.cat_ids.length} Categories)</strong>`;
                    }
                }
                const targetCluster = document.getElementById('group-' + groupId);
                if (targetCluster) {
                    targetCluster.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }
        }

        // Category Filter Navigation & Direct Page Open (Zero Scrolling)
        function filterCategory(catId, btnElement) {
            if (catId === 'all') {
                filterAlphaGroup('all');
                return;
            }

            const heroWrapper = document.querySelector('.hero-banner-wrapper');
            const proposalSec = document.getElementById('strategic-proposal');
            const goldenHour = document.getElementById('golden-hour');
            const costingSec = document.getElementById('costing-estimate');
            const incentiveSec = document.getElementById('dtic-incentives');
            const ratesSec = document.getElementById('rates-and-contacts');
            const activeBanner = document.getElementById('categoryActiveBanner');
            const activeTitleDisplay = document.getElementById('activeCategoryTitleDisplay');

            // Update category pills active state
            document.querySelectorAll('.cat-pill').forEach(p => {
                p.style.display = 'inline-flex';
                p.classList.toggle('active', p.dataset.catId === catId);
            });
            document.querySelectorAll('.alpha-tab-btn').forEach(b => {
                b.classList.remove('active');
            });

            // Ensure all cluster wrappers are displayed so target category is visible
            document.querySelectorAll('.alpha-cluster-wrapper').forEach(c => {
                c.style.display = 'block';
            });

            const blocks = document.querySelectorAll('.category-block');
            let selectedCategory = null;

            blocks.forEach(b => {
                if (b.dataset.catId === catId) {
                    b.style.display = 'block';
                    selectedCategory = categoriesData.find(c => c.id === catId);
                } else {
                    b.style.display = 'none';
                }
            });

            // Hide other macro sections for direct focus
            if (heroWrapper) heroWrapper.style.display = 'none';
            if (proposalSec) proposalSec.style.display = 'none';
            if (goldenHour) goldenHour.style.display = 'none';
            if (costingSec) costingSec.style.display = 'none';
            if (incentiveSec) incentiveSec.style.display = 'none';
            if (ratesSec) ratesSec.style.display = 'none';

            if (activeBanner) {
                activeBanner.style.display = 'flex';
                if (selectedCategory && activeTitleDisplay) {
                    activeTitleDisplay.innerHTML = `<span>Active Category:</span> <strong>${selectedCategory.icon} ${selectedCategory.num} ${selectedCategory.title}</strong>`;
                }
            }
            history.pushState(null, '', '#' + catId);
            window.scrollTo({ top: 0, behavior: 'instant' });
        }

        // Global Search
        function filterShowcase(query) {
            const q = query.trim().toLowerCase();
            document.querySelectorAll('.category-block').forEach(b => {
                const text = b.dataset.searchText || '';
                if (!q || text.includes(q)) {
                    b.style.display = 'block';
                } else {
                    b.style.display = 'none';
                }
            });
        }

        // Copy Direct Category Link
        function copyCategoryLink(catId) {
            const url = window.location.origin + window.location.pathname + '#' + catId;
            navigator.clipboard.writeText(url).then(() => {
                alert('Direct category link copied to clipboard: ' + url);
            }).catch(() => {
                prompt('Copy category link:', url);
            });
        }

        // Lightbox Architecture
        function openLightbox(catId, photoIdx) {
            const cat = categoriesData.find(c => c.id === catId);
            if (!cat) return;

            activeGallery = cat.gallery;
            activeCategoryIndex = categoriesData.indexOf(cat);
            activePhotoIndex = photoIdx;

            updateLightboxContent();
            document.getElementById('lightboxModal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function updateLightboxContent() {
            const cat = categoriesData[activeCategoryIndex];
            let item = null;
            let cardImg = null;

            if (activePhotoIndex === -1 || activePhotoIndex >= activeGallery.length) {
                // Hero photo clicked
                cardImg = document.querySelector(`.category-block[data-cat-id="${cat.id}"] .hero-image-wrap img`);
                item = { title: cat.hero_image_title };
            } else {
                item = activeGallery[activePhotoIndex];
                cardImg = document.querySelector(`.category-block[data-cat-id="${cat.id}"] .gallery-card[data-photo-idx="${activePhotoIndex}"] img`);
                if (!cardImg) {
                    cardImg = document.querySelector(`.category-block[data-cat-id="${cat.id}"] .hero-image-wrap img`);
                }
            }

            const b64 = cardImg ? cardImg.src : '';

            document.getElementById('lbMainImage').src = b64;
            document.getElementById('lbCatBadge').innerText = `${cat.icon} Category ${cat.num}: ${cat.title}`;
            document.getElementById('lbCounter').innerText = `${Math.max(1, activePhotoIndex + 1)} / ${activeGallery.length}`;
            document.getElementById('lbCaptionTitle').innerText = item.title;
            document.getElementById('lbCaptionSub').innerText = `${cat.area} · Verified Scouted Database Asset`;
        }

        function closeLightbox(e) {
            if (e && e.target && e.target.closest('.lb-image-container')) return;
            document.getElementById('lightboxModal').classList.remove('active');
            document.body.style.overflow = 'auto';
        }

        function nextLightbox(e) {
            if (e) e.stopPropagation();
            activePhotoIndex = (activePhotoIndex + 1) % activeGallery.length;
            updateLightboxContent();
        }

        function prevLightbox(e) {
            if (e) e.stopPropagation();
            activePhotoIndex = (activePhotoIndex - 1 + activeGallery.length) % activeGallery.length;
            updateLightboxContent();
        }

        // Keyboard Controls
        window.addEventListener('keydown', (e) => {
            const modal = document.getElementById('lightboxModal');
            if (modal.classList.contains('active')) {
                if (e.key === 'Escape') closeLightbox();
                if (e.key === 'ArrowRight') nextLightbox();
                if (e.key === 'ArrowLeft') prevLightbox();
            }
        });

        // Shortlist Architecture
        function toggleShortlist() {
            const drawer = document.getElementById('shortlistDrawer');
            drawer.classList.toggle('open');
        }

        function toggleShortlistItem(filePath, title, categoryTitle, heartBtn) {
            const existingIdx = currentShortlist.findIndex(x => x.filePath === filePath);
            if (existingIdx > -1) {
                currentShortlist.splice(existingIdx, 1);
                if (heartBtn) heartBtn.classList.remove('active');
            } else {
                const parentCard = heartBtn.closest('.gallery-card, .hero-image-wrap, .panorama-pane');
                const img = parentCard ? parentCard.querySelector('img') : null;
                const b64 = img ? img.src : '';

                currentShortlist.push({
                    filePath: filePath,
                    title: title,
                    categoryTitle: categoryTitle,
                    thumbSrc: b64
                });
                if (heartBtn) heartBtn.classList.add('active');
            }
            renderShortlist();
        }

        function saveCurrentLightboxPhoto() {
            const cat = categoriesData[activeCategoryIndex];
            const item = activeGallery[activePhotoIndex];
            const cardImg = document.querySelector(`.category-block[data-cat-id="${cat.id}"] .gallery-card[data-photo-idx="${activePhotoIndex}"] img`) || document.querySelector(`.category-block[data-cat-id="${cat.id}"] .panorama-pane[data-photo-idx="${activePhotoIndex}"] img`);
            const b64 = cardImg ? cardImg.src : '';

            const existingIdx = currentShortlist.findIndex(x => x.filePath === item.file);
            if (existingIdx === -1) {
                currentShortlist.push({
                    filePath: item.file,
                    title: item.title,
                    categoryTitle: cat.title,
                    thumbSrc: b64
                });
                const heart = document.querySelector(`.category-block[data-cat-id="${cat.id}"] [data-photo-idx="${activePhotoIndex}"] .gallery-card-heart`);
                if (heart) heart.classList.add('active');
            }
            renderShortlist();
            alert('Location added to your custom shortlist!');
        }

        function removeShortlistItem(filePath) {
            const idx = currentShortlist.findIndex(x => x.filePath === filePath);
            if (idx > -1) {
                currentShortlist.splice(idx, 1);
                document.querySelectorAll(`[data-file="${filePath.replace(/\\\\/g, '\\\\\\\\')}"] .gallery-card-heart, [data-file="${filePath.replace(/\\\\/g, '\\\\\\\\')}"] .hero-overlay-heart`).forEach(h => {
                    h.classList.remove('active');
                });
                renderShortlist();
            }
        }

        function clearShortlist() {
            currentShortlist = [];
            document.querySelectorAll('.gallery-card-heart, .hero-overlay-heart').forEach(h => h.classList.remove('active'));
            renderShortlist();
        }

        function renderShortlist() {
            const badge = document.getElementById('shortlistBadge');
            badge.innerText = currentShortlist.length;

            const body = document.getElementById('shortlistBody');
            if (currentShortlist.length === 0) {
                body.innerHTML = `
                    <div class="shortlist-empty">
                        No locations saved yet.<br>Click the heart icon on any photo to add it to your custom production deck.
                    </div>`;
                return;
            }

            let html = '';
            currentShortlist.forEach(item => {
                const safeFile = item.filePath.replace(/'/g, "\\'");
                html += `
                    <div class="shortlist-item">
                        <img src="${item.thumbSrc}" alt="${item.title}">
                        <div class="shortlist-item-info">
                            <div class="shortlist-item-title">${item.title}</div>
                            <div class="shortlist-item-cat">${item.categoryTitle}</div>
                        </div>
                        <button class="shortlist-remove" onclick="removeShortlistItem('${safeFile}')" title="Remove">✕</button>
                    </div>`;
            });
            body.innerHTML = html;
        }

        function sendShortlistInquiry() {
            if (currentShortlist.length === 0) {
                alert('Please add at least one location to your shortlist before submitting.');
                return;
            }

            const listText = currentShortlist.map((it, idx) => `${idx + 1}. [${it.categoryTitle}] ${it.title}`).join('%0D%0A');
            const subject = encodeURIComponent('Production Location Shortlist Inquiry - Cape Town Master Database');
            const body = `Dear Laura and Jardin,%0D%0A%0D%0AI have reviewed the Cape Town Master Location Scouting Database and shortlisted the following ${currentShortlist.length} location(s) for our upcoming production:%0D%0A%0D%0A${listText}%0D%0A%0D%0APlease provide availability, permit turnaround timelines, and scout recce scheduling for these venues.%0D%0A%0D%0ABest regards,%0D%0A[Producer / Production Company Name]`;

            window.location.href = `mailto:laura@zencrew.co.za?cc=jardin@salocations.com&subject=${subject}&body=${body}`;
        }

        // Direct Deep Linking on page load (#category-id)
        window.addEventListener('DOMContentLoaded', () => {
            const hash = window.location.hash.replace('#', '');
            if (hash && categoriesData.some(c => c.id === hash)) {
                filterCategory(hash);
            }
        });

        // Browser Back / Forward History Support
        window.addEventListener('popstate', () => {
            const hash = window.location.hash.replace('#', '');
            if (hash && categoriesData.some(c => c.id === hash)) {
                filterCategory(hash);
            } else {
                filterCategory('all');
            }
        });
    </script>
</body>
</html>
"""

output_html_path = os.path.join(deck_dir, "index.html")
print("Generating self-contained HTML deck...")
with open(output_html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

size_mb = os.path.getsize(output_html_path) / (1024 * 1024)
print(f"Successfully generated {output_html_path} ({size_mb:.2f} MB)")
