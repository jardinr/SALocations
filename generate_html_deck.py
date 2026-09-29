import os
import json

deck_dir = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-global-locations-deck"
data_path = os.path.join(deck_dir, "embedded_data.json")

print("Reading embedded dataset...")
with open(data_path, "r", encoding="utf-8") as f:
    data = json.load(f)

categories = data["categories"]
images = data["images"]

print(f"Loaded {len(categories)} categories and {len(images)} encoded images.")

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cape Town Master Location Scouting Database · International Film & Commercial Showcase</title>
    <meta name="description" content="Comprehensive master location database showcasing Cape Town and South Africa's film locations across 15 macro categories. Verified scouting inventory, international doubling power, technical filming specs, and multi-currency rate cards. Presented by SA Locations & Zencrew.">

    <!-- Open Graph / Social Sharing -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Cape Town Master Location Scouting Database · Global Film & Commercial Showcase">
    <meta property="og:description" content="Curated 15-category location scouting inventory doubling South Africa for California, Mediterranean, London, New York, Nevada & European destinations. 150 verified hero assets, technical filming specs & multi-currency rates.">
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
            background: rgba(7, 11, 10, 0.88);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            padding: 0.75rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
        }

        .nav-brand {
            display: flex;
            align-items: center;
            gap: 1rem;
            text-decoration: none;
        }

        .brand-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(212, 175, 55, 0.12);
            border: 1px solid var(--border-gold);
            color: var(--gold-bright);
            padding: 0.35rem 0.85rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
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
            font-size: 1.05rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            color: #ffffff;
        }

        .nav-controls {
            display: flex;
            align-items: center;
            gap: 0.9rem;
            flex-wrap: wrap;
        }

        .social-link-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.4rem 0.8rem;
            border-radius: var(--radius-sm);
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border);
            color: var(--text-main);
            text-decoration: none;
            font-family: var(--font-tech);
            font-size: 0.75rem;
            font-weight: 600;
            transition: var(--transition);
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
            padding: 0.45rem 1rem 0.45rem 2.2rem;
            color: #ffffff;
            font-size: 0.85rem;
            width: 200px;
            transition: var(--transition);
            outline: none;
            font-family: var(--font-sans);
        }

        .search-box input:focus {
            width: 260px;
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
            padding: 0.45rem 1rem;
            border-radius: 999px;
            font-size: 0.8rem;
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

        /* Hero Banner */
        .hero-section {
            position: relative;
            max-width: 1380px;
            margin: 0 auto;
            padding: 3.5rem 2rem 2rem 2rem;
            text-align: center;
            z-index: 10;
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

        /* KPI Stats Grid */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 1rem;
            max-width: 1200px;
            margin: 0 auto 3rem auto;
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

        /* Global Doubling Banner */
        .doubling-banner {
            max-width: 1200px;
            margin: 0 auto 2.5rem auto;
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
            gap: 0.5rem;
            margin-top: 0.8rem;
        }

        .doubling-tag {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border);
            color: var(--gold);
            font-family: var(--font-tech);
            font-size: 0.72rem;
            padding: 0.25rem 0.65rem;
            border-radius: 999px;
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

        /* Hero Scouted Match Showcase - Strict Landscape with Wording Below */
        .hero-showcase {
            display: flex;
            flex-direction: column;
            border-bottom: 1px solid var(--border);
            background: var(--surface);
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

        .contact-link:hover {
            color: var(--gold-bright);
            transform: translateX(3px);
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
        }

        .footer-disclaimer {
            font-size: 0.82rem;
            color: var(--text-dim);
            max-width: 800px;
            line-height: 1.6;
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
            .category-header, .hero-details-panel, .gallery-section {
                background: #ffffff !important;
                color: #000000 !important;
            }
            h1, h2, h3, h4 {
                color: #000000 !important;
            }
            p, li, .spec-value, .category-synopsis {
                color: #333333 !important;
            }
        }
    </style>
</head>
<body>

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
                <input type="text" id="searchInput" placeholder="Search 150 locations..." oninput="filterShowcase(this.value)">
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

    <!-- Hero Showcase Section -->
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

        <!-- KPI Stats Grid -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">15</div>
                <div class="stat-label">Curated Macro Categories</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">150</div>
                <div class="stat-label">Verified Hero Assets</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">40-60%</div>
                <div class="stat-label">Currency Budget Advantage</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">300+</div>
                <div class="stat-label">Annual Filming Sunlight Days</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">0°</div>
                <div class="stat-label">Zero Rotation Errors (EXIF Verified)</div>
            </div>
        </div>

        <!-- Global Doubling Advantage Banner -->
        <div class="doubling-banner">
            <div>
                <div class="doubling-title">The Global Doubling Power of the Western Cape</div>
                <div class="doubling-desc">
                    Within a 60-minute radius of Cape Town CBD, productions can access pristine Mediterranean coastlines, California Pacific Coast Highways, Hollywood Hills cantilevered villas, historic London residential streets, Nevada arid desert basins, Scandinavian timber eco-lodges, ancient desert planets, maximum-security correctional blocks, and Olympic-grade sports stadiums.
                </div>
                <div class="doubling-tags">
                    <span class="doubling-tag">California PCH (Chapman's Peak)</span>
                    <span class="doubling-tag">Amalfi Coast (Victoria Rd)</span>
                    <span class="doubling-tag">Hollywood Hills (Clifton & Lux)</span>
                    <span class="doubling-tag">London Suburbs (Culver & Chatham)</span>
                    <span class="doubling-tag">Nevada Desert (R355 Karoo)</span>
                    <span class="doubling-tag">Pacific Northwest (Blackwood Cabin)</span>
                    <span class="doubling-tag">Cederberg Alien Planet (Stadsaal Caves)</span>
                    <span class="doubling-tag">French Riviera (V&A Basin)</span>
                    <span class="doubling-tag">Tuscan Vineyards (Asara & Tokara)</span>
                    <span class="doubling-tag">Maximum Security Prison (Disa Tygerberg)</span>
                    <span class="doubling-tag">Olympic Arena (Cape Town DHL Stadium)</span>
                    <span class="doubling-tag">Private Airfield (Arrieskraal Airport)</span>
                </div>
            </div>
            <div>
                <a href="#rates-and-contacts" class="btn-nav primary" style="padding: 0.8rem 1.6rem; font-size: 0.9rem;">Review Rate Cards</a>
            </div>
        </div>
    </section>

    <!-- Sticky Category Filter Navigation -->
    <nav class="category-nav-wrap">
        <div class="category-nav" id="categoryNav">
            <button class="cat-pill active" onclick="filterCategory('all', this)">All Categories (15)</button>
"""

# Append category pills
for cat in categories:
    html_template += f"""            <button class="cat-pill" onclick="filterCategory('{cat['id']}', this)">{cat['icon']} {cat['num']} {cat['title'].split(',')[0].split('&')[0].strip()}</button>\n"""

html_template += """        </div>
    </nav>

    <!-- Main Location Showcase Content -->
    <main class="deck-container">
"""

# Render Category Blocks
for cat in categories:
    hero_b64 = images.get(cat["hero_image_file"], "")
    hero_img_file = cat["hero_image_file"].replace("\\", "\\\\")
    hero_title_clean = cat["hero_image_title"].replace("'", "\\'")
    cat_title_clean = cat["title"].replace("'", "\\'")

    search_text = f"{cat['title']} {cat['doubles_as']} {cat['area']} {cat['tagline']} {cat['hero_image_title']}".lower()

    html_template += f"""
        <!-- Category Block: {cat['num']} - {cat['title']} -->
        <article class="category-block" id="{cat['id']}" data-cat-id="{cat['id']}" data-search-text="{search_text}">
            <!-- Category Header -->
            <div class="category-header">
                <div class="cat-meta-row">
                    <span class="cat-num-badge">CATEGORY {cat['num']} OF 15</span>
                    <span class="cat-doubling-banner">Doubles For: {cat['doubles_as']}</span>
                </div>
                <h2 class="category-title">{cat['icon']} {cat['title']}</h2>
                <div class="category-area">Primary Locations: {cat['area']}</div>
                <p class="category-synopsis">{cat['creative_synopsis']}</p>
            </div>

            <!-- Hero Scouted Match Showcase - Strict Landscape with Wording Below -->
            <div class="hero-showcase">
                <div class="hero-image-wrap" data-cat-id="{cat['id']}" data-file="{hero_img_file}" onclick="openLightbox('{cat['id']}', 0)">
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

                <div class="gallery-grid">
"""
    for idx, item in enumerate(cat["gallery"]):
        img_b64 = images.get(item["file"], "")
        item_img_file = item["file"].replace("\\", "\\\\")
        item_title_clean = item["title"].replace("'", "\\'")
        html_template += f"""
                    <div class="gallery-card" data-cat-id="{cat['id']}" data-photo-idx="{idx}" data-file="{item_img_file}" onclick="openLightbox('{cat['id']}', {idx})">
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

# Append Rate Cards & Executive Strip
html_template += """
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
                    <p class="tier-desc">Dedicated technical scout, director visual matching, custom contact sheets & GPS mapping.</p>
                    <div class="rate-amount" id="scoutRateDisplay">R 5,000 <span class="unit">/ day</span></div>
                    <ul class="tier-features">
                        <li>Visual reference matching from 8,000+ photo archive</li>
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

            <!-- Executive Contacts Strip (Git Replaced with Instagram & YouTube) -->
            <div class="exec-contacts-card">
                <div class="contact-col">
                    <span class="contact-role">Zencrew Production Services · Lead Fixer & Producer</span>
                    <h3 class="contact-name">Laura Diana Macleod</h3>
                    <p class="contact-bio">
                        Seasoned South African location manager, producer, and commercial fixer with 15+ years managing high-profile international feature films, commercials, and photographic campaigns across Cape Town, the Karoo, and Southern Africa.
                    </p>
                    <div class="contact-links">
                        <a href="mailto:laura@zencrew.co.za" class="contact-link">✉ laura@zencrew.co.za</a>
                        <a href="https://wa.me/27825708818" target="_blank" rel="noopener noreferrer" class="contact-link">📱 +27 82 570 8818 (WhatsApp)</a>
                        <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Production+Consultation+-+Zencrew&details=Production+Consultation+with+Laura+Diana+Macleod+%28Zencrew%29.&location=Cape+Town&add=laura@zencrew.co.za" target="_blank" rel="noopener noreferrer" class="contact-link">📅 Book Consultation Call</a>
                    </div>
                </div>

                <div class="contact-col">
                    <span class="contact-role">SA Locations · Technical Location Scout & Partner</span>
                    <h3 class="contact-name">Jardin Roestorff</h3>
                    <p class="contact-bio">
                        Specialized technical location scout with an 8,000+ photo database spanning the entire Western Cape. Dedicated to director visual reference matching, architectural precision, camera crane clearances, and digital production decks.
                    </p>
                    <div class="contact-links">
                        <a href="mailto:jardin@salocations.com" class="contact-link">✉ jardin@salocations.com</a>
                        <a href="https://www.instagram.com/salocations" target="_blank" rel="noopener noreferrer" class="contact-link">📸 Instagram: @salocations</a>
                        <a href="https://www.youtube.com/@salocations" target="_blank" rel="noopener noreferrer" class="contact-link">🎬 YouTube: @salocations</a>
                        <a href="mailto:jardin@salocations.com?subject=Master%20Database%20Custom%20Scouting%20Request" class="contact-link">📋 Custom Scout Request</a>
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
                <span>SA Locations</span>
                <span style="color: var(--gold);">✕</span>
                <span>Zencrew Production Services</span>
            </div>
            <div class="footer-social-row">
                <a href="https://www.instagram.com/salocations" target="_blank" rel="noopener noreferrer" class="social-link-btn">
                    📸 Instagram @salocations
                </a>
                <a href="https://www.youtube.com/@salocations" target="_blank" rel="noopener noreferrer" class="social-link-btn">
                    🎬 YouTube @salocations
                </a>
            </div>
            <div class="footer-disclaimer">
                © 2026/2027 SA Locations & Zencrew. All 150 photographs within the Scouted Images Database are proprietary assets photographed on location across the Western Cape, South Africa. Transposed under strict zero-rotation standards. Direct bookings subject to municipal permit authorization.
            </div>
        </div>
    </footer>

    <!-- Interactive Logic Script (Zero Redundant Base64 Duplication) -->
    <script>
        const categoriesData = """ + json.dumps(categories) + """;

        // Exchange Rates relative to ZAR
        const rates = {
            ZAR: { symbol: 'R', scout: 5000, manage: 5500, format: (val) => `R ${val.toLocaleString()}` },
            USD: { symbol: '$', scout: 280, manage: 310, format: (val) => `$ ${val.toLocaleString()}` },
            EUR: { symbol: '€', scout: 255, manage: 280, format: (val) => `€ ${val.toLocaleString()}` },
            GBP: { symbol: '£', scout: 220, manage: 240, format: (val) => `£ ${val.toLocaleString()}` },
            INR: { symbol: '₹', scout: 24500, manage: 27000, format: (val) => `₹ ${val.toLocaleString()}` }
        };

        let currentCurrency = 'ZAR';
        let currentShortlist = [];
        let activeCategoryIndex = 0;
        let activePhotoIndex = 0;
        let activeGallery = [];

        // Currency Switching
        function setCurrency(curr) {
            currentCurrency = curr;
            document.querySelectorAll('.curr-btn').forEach(b => {
                b.classList.toggle('active', b.dataset.curr === curr);
            });
            const info = rates[curr];
            document.getElementById('scoutRateDisplay').innerHTML = `${info.format(info.scout)} <span class="unit">/ day</span>`;
            document.getElementById('manageRateDisplay').innerHTML = `${info.format(info.manage)} <span class="unit">/ shoot day</span>`;
        }

        // Category Filter Navigation
        function filterCategory(catId, btnElement) {
            document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
            if (btnElement) btnElement.classList.add('active');

            const blocks = document.querySelectorAll('.category-block');
            blocks.forEach(b => {
                if (catId === 'all' || b.dataset.catId === catId) {
                    b.style.display = 'block';
                } else {
                    b.style.display = 'none';
                }
            });

            if (catId !== 'all') {
                const target = document.getElementById(catId);
                if (target) {
                    const y = target.getBoundingClientRect().top + window.pageYOffset - 120;
                    window.scrollTo({ top: y, behavior: 'smooth' });
                }
            }
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
                // Find image src in DOM
                const parentCard = heartBtn.closest('.gallery-card, .hero-image-wrap');
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
            const cardImg = document.querySelector(`.category-block[data-cat-id="${cat.id}"] .gallery-card[data-photo-idx="${activePhotoIndex}"] img`);
            const b64 = cardImg ? cardImg.src : '';

            const existingIdx = currentShortlist.findIndex(x => x.filePath === item.file);
            if (existingIdx === -1) {
                currentShortlist.push({
                    filePath: item.file,
                    title: item.title,
                    categoryTitle: cat.title,
                    thumbSrc: b64
                });
                // Highlight heart on card
                const heart = document.querySelector(`.category-block[data-cat-id="${cat.id}"] .gallery-card[data-photo-idx="${activePhotoIndex}"] .gallery-card-heart`);
                if (heart) heart.classList.add('active');
            }
            renderShortlist();
            alert('Location added to your custom shortlist!');
        }

        function removeShortlistItem(filePath) {
            const idx = currentShortlist.findIndex(x => x.filePath === filePath);
            if (idx > -1) {
                currentShortlist.splice(idx, 1);
                // Unhighlight any heart matching file
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
