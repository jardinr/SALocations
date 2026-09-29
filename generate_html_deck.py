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
    <meta name="description" content="Comprehensive master location database showcasing Cape Town and South Africa's film locations across 10 macro categories. Verified scouting inventory, international doubling power, technical filming specs, and multi-currency rate cards. Presented by SA Locations & Zencrew.">

    <!-- Open Graph / Social Sharing -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Cape Town Master Location Scouting Database · Global Film & Commercial Showcase">
    <meta property="og:description" content="Curated 10-category location scouting inventory doubling South Africa for California, Mediterranean, London, New York, Nevada & European destinations. 117 verified hero assets, technical filming specs & multi-currency rates.">
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
            --shadow-subtle: 0 10px 30px rgba(0, 0, 0, 0.5);
            --shadow-dramatic: 0 20px 60px rgba(0, 0, 0, 0.85);
            --transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
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

        /* Ambient Glow Backdrop */
        .ambient-glow {
            position: fixed;
            top: -20vh;
            left: 50%;
            transform: translateX(-50%);
            width: 1200px;
            height: 600px;
            background: radial-gradient(circle, rgba(212, 175, 55, 0.08) 0%, rgba(25, 56, 43, 0.05) 50%, transparent 80%);
            pointer-events: none;
            z-index: 0;
        }

        /* Top Header Navigation */
        header.top-nav {
            position: sticky;
            top: 0;
            z-index: 200;
            background: rgba(7, 11, 10, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            padding: 0.85rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1.5rem;
        }

        .nav-brand {
            display: flex;
            align-items: center;
            gap: 1.2rem;
        }
        .brand-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            background: rgba(212, 175, 55, 0.1);
            border: 1px solid var(--border-highlight);
            padding: 0.4rem 0.9rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--gold-bright);
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }
        .brand-pill .pulse-dot {
            width: 7px;
            height: 7px;
            background: var(--cyan);
            border-radius: 50%;
            box-shadow: 0 0 8px var(--cyan);
        }
        .nav-title {
            font-family: var(--font-serif);
            font-size: 0.95rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            color: var(--text-main);
        }

        .nav-controls {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        /* Global Search Input */
        .search-box {
            position: relative;
            display: flex;
            align-items: center;
        }
        .search-box input {
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text-main);
            padding: 0.45rem 1rem 0.45rem 2.2rem;
            border-radius: 999px;
            font-family: var(--font-sans);
            font-size: 0.85rem;
            width: 220px;
            transition: var(--transition);
        }
        .search-box input:focus {
            outline: none;
            border-color: var(--gold);
            width: 300px;
            box-shadow: 0 0 16px var(--gold-glow);
        }
        .search-box svg {
            position: absolute;
            left: 0.8rem;
            width: 14px;
            height: 14px;
            fill: var(--text-muted);
        }

        /* Currency Selector */
        .currency-selector {
            display: flex;
            align-items: center;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 999px;
            padding: 0.2rem 0.3rem;
            gap: 0.15rem;
        }
        .curr-btn {
            background: transparent;
            border: none;
            color: var(--text-muted);
            padding: 0.25rem 0.55rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.72rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
        }
        .curr-btn.active {
            background: var(--gold);
            color: #070b0a;
            font-weight: 700;
        }
        .curr-btn:hover:not(.active) {
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.05);
        }

        /* Shortlist Trigger */
        .shortlist-trigger {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text-main);
            padding: 0.45rem 0.95rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
        }
        .shortlist-trigger:hover {
            border-color: var(--gold);
            background: var(--surface-card);
        }
        .shortlist-badge {
            background: var(--gold);
            color: #070b0a;
            font-size: 0.7rem;
            font-weight: 800;
            padding: 0.1rem 0.45rem;
            border-radius: 999px;
        }

        /* Header Buttons */
        .btn-nav {
            text-decoration: none;
            font-family: var(--font-tech);
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.45rem 1rem;
            border-radius: 999px;
            border: 1px solid var(--border);
            color: var(--text-main);
            background: var(--surface);
            transition: var(--transition);
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            cursor: pointer;
        }
        .btn-nav:hover {
            border-color: var(--gold);
            color: var(--gold-bright);
        }
        .btn-nav.primary {
            background: var(--gold);
            color: #070b0a;
            border-color: var(--gold);
            font-weight: 700;
        }
        .btn-nav.primary:hover {
            background: var(--gold-bright);
            box-shadow: 0 0 16px var(--gold-glow);
        }

        /* Hero Section */
        .hero {
            position: relative;
            padding: 4.5rem 2rem 3rem 2rem;
            max-width: 1400px;
            margin: 0 auto;
            text-align: center;
            z-index: 10;
        }
        .hero-badge-row {
            display: flex;
            justify-content: center;
            gap: 0.8rem;
            flex-wrap: wrap;
            margin-bottom: 1.5rem;
        }
        .badge-premium {
            background: rgba(212, 175, 55, 0.12);
            border: 1px solid var(--border-highlight);
            color: var(--gold-bright);
            font-family: var(--font-tech);
            font-size: 0.78rem;
            font-weight: 700;
            padding: 0.4rem 1.1rem;
            border-radius: 999px;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }
        .badge-sub {
            background: rgba(25, 56, 43, 0.5);
            border: 1px solid rgba(56, 239, 125, 0.3);
            color: var(--cyan);
            font-family: var(--font-tech);
            font-size: 0.78rem;
            font-weight: 600;
            padding: 0.4rem 1.1rem;
            border-radius: 999px;
            letter-spacing: 0.05em;
        }

        h1.hero-title {
            font-family: var(--font-serif);
            font-size: clamp(2.2rem, 5vw, 3.8rem);
            font-weight: 800;
            line-height: 1.15;
            letter-spacing: 0.02em;
            color: #ffffff;
            margin-bottom: 1rem;
            text-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
        }
        h1.hero-title span.gold {
            background: linear-gradient(135deg, #ffffff 0%, var(--gold-bright) 50%, var(--gold) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        p.hero-subtitle {
            font-size: clamp(1rem, 2vw, 1.25rem);
            color: var(--text-muted);
            max-width: 900px;
            margin: 0 auto 2.5rem auto;
            font-weight: 300;
            line-height: 1.7;
        }

        /* Stats Strip */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.2rem;
            max-width: 1200px;
            margin: 0 auto 3rem auto;
        }
        .stat-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.4rem 1rem;
            text-align: center;
            transition: var(--transition);
        }
        .stat-card:hover {
            border-color: var(--border-highlight);
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
        }
        .stat-number {
            font-family: var(--font-tech);
            font-size: 2rem;
            font-weight: 700;
            color: var(--gold-bright);
            margin-bottom: 0.2rem;
        }
        .stat-label {
            font-family: var(--font-sans);
            font-size: 0.78rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 600;
        }

        /* Doubling Advantage Matrix */
        .doubling-banner {
            background: linear-gradient(135deg, rgba(22, 36, 30, 0.9) 0%, rgba(14, 22, 18, 0.9) 100%);
            border: 1px solid var(--border-highlight);
            border-radius: var(--radius-lg);
            padding: 1.75rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
            text-align: left;
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 2rem;
            align-items: center;
        }
        .doubling-title {
            font-family: var(--font-serif);
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--gold-bright);
            margin-bottom: 0.4rem;
        }
        .doubling-desc {
            font-size: 0.88rem;
            color: var(--text-muted);
            line-height: 1.6;
        }
        .doubling-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 0.8rem;
        }
        .doubling-tag {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid var(--border);
            color: var(--text-main);
            font-family: var(--font-tech);
            font-size: 0.72rem;
            padding: 0.25rem 0.65rem;
            border-radius: 999px;
        }

        /* Category Filter Navigation Bar */
        .category-nav-wrap {
            position: sticky;
            top: 61px;
            z-index: 150;
            background: rgba(7, 11, 10, 0.92);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            padding: 0.85rem 2rem;
        }
        .category-pills-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            gap: 0.6rem;
            overflow-x: auto;
            padding-bottom: 0.3rem;
            scrollbar-width: thin;
            scrollbar-color: var(--border) transparent;
        }
        .category-pills-container::-webkit-scrollbar {
            height: 4px;
        }
        .category-pills-container::-webkit-scrollbar-thumb {
            background: var(--border);
            border-radius: 999px;
        }
        .cat-pill {
            white-space: nowrap;
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 0.45rem 1rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }
        .cat-pill:hover {
            border-color: var(--gold);
            color: var(--text-main);
            background: var(--surface-card);
        }
        .cat-pill.active {
            background: var(--gold);
            color: #070b0a;
            border-color: var(--gold);
            font-weight: 700;
        }

        /* Main Content Container */
        main.content-area {
            max-width: 1400px;
            margin: 2.5rem auto;
            padding: 0 2rem;
            position: relative;
            z-index: 10;
        }

        /* Category Card Section */
        .category-block {
            margin-bottom: 4.5rem;
            background: var(--surface-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-subtle);
            transition: var(--transition);
        }
        .category-block:hover {
            border-color: var(--border-highlight);
            box-shadow: var(--shadow-dramatic);
        }

        /* Category Card Header */
        .category-header {
            padding: 2.2rem 2.5rem 1.8rem 2.5rem;
            background: linear-gradient(180deg, rgba(25, 38, 32, 0.6) 0%, rgba(18, 28, 23, 0) 100%);
            border-bottom: 1px solid var(--border);
        }
        .cat-meta-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin-bottom: 0.8rem;
        }
        .cat-num-badge {
            font-family: var(--font-tech);
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--gold-bright);
            letter-spacing: 0.1em;
            background: rgba(212, 175, 55, 0.1);
            padding: 0.3rem 0.8rem;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-highlight);
        }
        .cat-doubling-banner {
            font-family: var(--font-tech);
            font-size: 0.76rem;
            color: var(--cyan);
            background: rgba(37, 97, 73, 0.3);
            border: 1px solid rgba(56, 239, 125, 0.3);
            padding: 0.3rem 0.9rem;
            border-radius: 999px;
            font-weight: 600;
        }

        h2.category-title {
            font-family: var(--font-serif);
            font-size: clamp(1.6rem, 3vw, 2.3rem);
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.5rem;
        }
        .category-area {
            font-family: var(--font-sans);
            font-size: 0.95rem;
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

        /* Hero Scouted Match Showcase */
        .hero-showcase {
            display: grid;
            grid-template-columns: 1.25fr 1fr;
            border-bottom: 1px solid var(--border);
        }
        @media (max-width: 1024px) {
            .hero-showcase {
                grid-template-columns: 1fr;
            }
        }
        .hero-image-wrap {
            position: relative;
            background: #000;
            cursor: pointer;
            overflow: hidden;
            min-height: 420px;
        }
        .hero-image-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .hero-image-wrap:hover img {
            transform: scale(1.03);
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

        .hero-details-panel {
            padding: 2.2rem 2.5rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background: var(--surface);
        }
        .hero-details-top h3 {
            font-family: var(--font-serif);
            font-size: 1.35rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.8rem;
            line-height: 1.35;
        }
        .hero-details-top p.tagline {
            font-size: 0.9rem;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 1.4rem;
        }
        .key-features-list {
            list-style: none;
            margin-bottom: 1.5rem;
        }
        .key-features-list li {
            position: relative;
            padding-left: 1.4rem;
            font-size: 0.86rem;
            color: var(--text-main);
            margin-bottom: 0.55rem;
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
            background: rgba(0, 0, 0, 0.25);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.2rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        @media (max-width: 600px) {
            .specs-panel {
                grid-template-columns: 1fr;
            }
        }
        .spec-item {
            display: flex;
            flex-direction: column;
            gap: 0.2rem;
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
            font-size: 0.8rem;
            color: var(--text-muted);
            line-height: 1.4;
        }

        .hero-actions-row {
            display: flex;
            gap: 0.8rem;
            flex-wrap: wrap;
        }

        /* Scouted Images Database Gallery */
        .gallery-section {
            padding: 2rem 2.5rem 2.5rem 2.5rem;
            background: var(--surface-card);
        }
        .gallery-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.4rem;
            flex-wrap: wrap;
            gap: 0.8rem;
        }
        .gallery-title {
            font-family: var(--font-serif);
            font-size: 1.15rem;
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
            font-size: 0.7rem;
            padding: 0.2rem 0.6rem;
            border-radius: 999px;
        }

        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 1.2rem;
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
            height: 180px;
            overflow: hidden;
            background: #000;
        }
        .gallery-thumb-wrap img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.5s ease;
        }
        .gallery-card:hover .gallery-thumb-wrap img {
            transform: scale(1.06);
        }
        .gallery-thumb-tag {
            position: absolute;
            bottom: 0.6rem;
            left: 0.6rem;
            background: rgba(7, 11, 10, 0.8);
            backdrop-filter: blur(8px);
            border: 1px solid var(--border);
            color: var(--gold-bright);
            font-family: var(--font-tech);
            font-size: 0.68rem;
            font-weight: 600;
            padding: 0.2rem 0.55rem;
            border-radius: 999px;
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
            z-index: 5;
        }
        .gallery-card-heart:hover {
            border-color: #ff4757;
            transform: scale(1.15);
        }
        .gallery-card-heart.active svg {
            fill: #ff4757;
        }
        .gallery-card-heart svg {
            width: 14px;
            height: 14px;
            fill: #ffffff;
        }
        .gallery-card-info {
            padding: 0.85rem 1rem;
        }
        .gallery-card-title {
            font-size: 0.82rem;
            font-weight: 500;
            color: var(--text-main);
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        /* Rate Card & Commercial Section */
        .rates-section {
            background: var(--surface-card);
            border: 1px solid var(--border-highlight);
            border-radius: var(--radius-lg);
            padding: 3rem;
            margin: 4.5rem 0;
            box-shadow: var(--shadow-dramatic);
            position: relative;
            overflow: hidden;
        }
        .rates-section::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--gold), var(--cyan), var(--gold));
        }
        .rates-header {
            text-align: center;
            max-width: 800px;
            margin: 0 auto 2.5rem auto;
        }
        .rates-header h2 {
            font-family: var(--font-serif);
            font-size: 2.2rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.6rem;
        }
        .rates-header p {
            font-size: 0.95rem;
            color: var(--text-muted);
        }

        .rates-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2.5rem;
        }
        .rate-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 2.2rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: var(--transition);
        }
        .rate-card:hover {
            border-color: var(--gold);
            transform: translateY(-4px);
        }
        .rate-card.featured {
            border-color: var(--gold);
            background: linear-gradient(180deg, rgba(212, 175, 55, 0.08) 0%, var(--surface) 100%);
        }
        .rate-tier {
            font-family: var(--font-tech);
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--gold-bright);
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }
        .rate-price {
            font-family: var(--font-tech);
            font-size: 2.4rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.3rem;
        }
        .rate-price span.unit {
            font-size: 0.95rem;
            font-weight: 500;
            color: var(--text-muted);
        }
        .rate-equiv {
            font-family: var(--font-tech);
            font-size: 0.8rem;
            color: var(--cyan);
            margin-bottom: 1.4rem;
            padding-bottom: 1.2rem;
            border-bottom: 1px solid var(--border);
        }
        .rate-includes {
            list-style: none;
            margin-bottom: 1.8rem;
        }
        .rate-includes li {
            position: relative;
            padding-left: 1.3rem;
            font-size: 0.86rem;
            color: var(--text-main);
            margin-bottom: 0.6rem;
            line-height: 1.45;
        }
        .rate-includes li::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: var(--gold);
            font-weight: 700;
        }

        /* Executive Contacts Strip */
        .exec-contacts-card {
            background: linear-gradient(135deg, rgba(25, 38, 32, 0.8) 0%, rgba(14, 22, 18, 0.9) 100%);
            border: 1px solid var(--border-highlight);
            border-radius: var(--radius-lg);
            padding: 2.5rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2.5rem;
        }
        @media (max-width: 900px) {
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
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--gold-bright);
        }
        .contact-name {
            font-family: var(--font-serif);
            font-size: 1.6rem;
            font-weight: 700;
            color: #ffffff;
        }
        .contact-bio {
            font-size: 0.88rem;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 0.8rem;
        }
        .contact-links {
            display: flex;
            gap: 0.8rem;
            flex-wrap: wrap;
        }
        .contact-link {
            text-decoration: none;
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text-main);
            padding: 0.4rem 0.9rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.78rem;
            font-weight: 600;
            transition: var(--transition);
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }
        .contact-link:hover {
            border-color: var(--gold);
            color: var(--gold-bright);
        }

        /* Client Shortlist Modal / Drawer */
        .shortlist-drawer {
            position: fixed;
            top: 0;
            right: -480px;
            width: 480px;
            max-width: 100vw;
            height: 100vh;
            background: var(--surface-card);
            border-left: 1px solid var(--border-highlight);
            box-shadow: -10px 0 40px rgba(0, 0, 0, 0.8);
            z-index: 500;
            transition: right 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
        }
        .shortlist-drawer.open {
            right: 0;
        }
        .drawer-header {
            padding: 1.5rem 1.8rem;
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .drawer-header h3 {
            font-family: var(--font-serif);
            font-size: 1.25rem;
            color: #ffffff;
        }
        .drawer-close {
            background: transparent;
            border: none;
            color: var(--text-muted);
            font-size: 1.4rem;
            cursor: pointer;
            padding: 0.2rem;
        }
        .drawer-body {
            padding: 1.5rem 1.8rem;
            flex: 1;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        .shortlist-empty {
            text-align: center;
            color: var(--text-dim);
            padding: 3rem 1rem;
            font-size: 0.95rem;
        }
        .shortlist-item {
            display: grid;
            grid-template-columns: 80px 1fr auto;
            gap: 1rem;
            align-items: center;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 0.6rem;
        }
        .shortlist-thumb {
            width: 80px;
            height: 60px;
            object-fit: cover;
            border-radius: 4px;
        }
        .shortlist-item-info {
            overflow: hidden;
        }
        .shortlist-item-title {
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--text-main);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .shortlist-item-cat {
            font-family: var(--font-tech);
            font-size: 0.72rem;
            color: var(--gold);
        }
        .shortlist-remove {
            background: transparent;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            padding: 0.4rem;
        }
        .shortlist-remove:hover {
            color: #ff4757;
        }
        .drawer-footer {
            padding: 1.5rem 1.8rem;
            border-top: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
        }

        /* Lightbox Modal */
        .lightbox-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(4, 7, 6, 0.97);
            backdrop-filter: blur(20px);
            z-index: 1000;
            display: none;
            flex-direction: column;
            justify-content: space-between;
        }
        .lightbox-modal.active {
            display: flex;
        }
        .lb-top-bar {
            padding: 1.2rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
        }
        .lb-meta {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .lb-cat-badge {
            font-family: var(--font-tech);
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--gold-bright);
            background: rgba(212, 175, 55, 0.12);
            padding: 0.25rem 0.8rem;
            border-radius: 999px;
            border: 1px solid var(--border-highlight);
        }
        .lb-counter {
            font-family: var(--font-tech);
            font-size: 0.82rem;
            color: var(--text-muted);
        }
        .lb-actions {
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }
        .lb-btn {
            background: var(--surface);
            border: 1px solid var(--border);
            color: var(--text-main);
            padding: 0.45rem 0.95rem;
            border-radius: 999px;
            font-family: var(--font-tech);
            font-size: 0.8rem;
            font-weight: 600;
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
            color: var(--text-main);
            font-size: 2rem;
            line-height: 1;
            cursor: pointer;
            margin-left: 0.8rem;
        }

        .lb-stage {
            position: relative;
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1rem 5rem;
            overflow: hidden;
        }
        .lb-image-container {
            max-width: 100%;
            max-height: 75vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .lb-image-container img {
            max-width: 100%;
            max-height: 75vh;
            object-fit: contain;
            border-radius: var(--radius-sm);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.9);
        }

        .lb-nav-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(18, 28, 23, 0.8);
            border: 1px solid var(--border);
            color: #ffffff;
            width: 52px;
            height: 52px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6rem;
            cursor: pointer;
            transition: var(--transition);
            user-select: none;
        }
        .lb-nav-btn:hover {
            background: var(--gold);
            color: #070b0a;
            border-color: var(--gold);
            box-shadow: 0 0 20px var(--gold-glow);
        }
        .lb-prev { left: 1.5rem; }
        .lb-next { right: 1.5rem; }

        .lb-caption-bar {
            padding: 1.2rem 2.5rem;
            background: var(--surface);
            border-top: 1px solid var(--border);
            text-align: center;
        }
        .lb-caption-title {
            font-family: var(--font-serif);
            font-size: 1.15rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 0.3rem;
        }
        .lb-caption-sub {
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        /* Footer */
        footer.site-footer {
            border-top: 1px solid var(--border);
            background: var(--bg-elevated);
            padding: 3rem 2rem 4rem 2rem;
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
            <!-- Global Search -->
            <div class="search-box">
                <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
                <input type="text" id="globalSearch" placeholder="Search locations, doubling..." onkeyup="filterShowcase(this.value)">
            </div>

            <!-- Currency Selector -->
            <div class="currency-selector">
                <button class="curr-btn" data-curr="USD" onclick="setCurrency('USD')">$ USD</button>
                <button class="curr-btn" data-curr="EUR" onclick="setCurrency('EUR')">€ EUR</button>
                <button class="curr-btn" data-curr="GBP" onclick="setCurrency('GBP')">£ GBP</button>
                <button class="curr-btn active" data-curr="ZAR" onclick="setCurrency('ZAR')">R ZAR</button>
                <button class="curr-btn" data-curr="INR" onclick="setCurrency('INR')">₹ INR</button>
            </div>

            <!-- Client Shortlist Drawer Trigger -->
            <button class="shortlist-trigger" onclick="toggleShortlist()">
                <span>★ Shortlist</span>
                <span class="shortlist-badge" id="shortlistCount">0</span>
            </button>

            <!-- Recce & Print Actions -->
            <button class="btn-nav" onclick="window.print()">⎙ PDF Export</button>
            <a href="#rates-and-contacts" class="btn-nav primary">Book Recce</a>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-badge-row">
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
                <div class="stat-number">10</div>
                <div class="stat-label">Curated Macro Categories</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">117</div>
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
                    Within a 60-minute radius of Cape Town CBD, productions can access pristine Mediterranean coastlines, California Pacific Coast Highways, Hollywood Hills cantilevered villas, historic London residential streets, Nevada arid desert basins, Scandinavian timber eco-lodges, and Olympic-grade civic infrastructure.
                </div>
                <div class="doubling-tags">
                    <span class="doubling-tag">California PCH (Chapman's Peak)</span>
                    <span class="doubling-tag">Amalfi Coast (Victoria Rd)</span>
                    <span class="doubling-tag">Hollywood Hills (Clifton Villas)</span>
                    <span class="doubling-tag">London Suburbs (Culver & Chatham)</span>
                    <span class="doubling-tag">Nevada Desert (R355 Karoo)</span>
                    <span class="doubling-tag">Pacific Northwest (Blackwood Cabin)</span>
                    <span class="doubling-tag">Tuscany Vineyards (Asara Estate)</span>
                </div>
            </div>
            <div>
                <a href="#rates-and-contacts" class="btn-nav primary" style="padding: 0.8rem 1.6rem; font-size: 0.9rem;">Review Rate Cards</a>
            </div>
        </div>
    </section>

    <!-- Sticky Category Filter Navigation -->
    <div class="category-nav-wrap">
        <div class="category-pills-container">
            <button class="cat-pill active" onclick="filterCategory('all', this)">
                <span>🌐 All 10 Categories</span>
            </button>
"""

# Render Category Pills
for cat in categories:
    html_template += f"""
            <button class="cat-pill" onclick="filterCategory('{cat['id']}', this)">
                <span>{cat['icon']} Cat {cat['num']}: {cat['title']}</span>
            </button>"""

html_template += """
        </div>
    </div>

    <!-- Main Content Area -->
    <main class="content-area">
"""

# Render Category Blocks
for cat in categories:
    hero_b64 = images.get(cat["hero_image_file"], "")
    hero_img_file = cat["hero_image_file"].replace("\\", "\\\\")
    hero_title_clean = cat["hero_image_title"].replace("'", "\\'")
    cat_title_clean = cat["title"].replace("'", "\\'")
    search_text = f"{cat['title']} {cat['doubles_as']} {cat['area']} {cat['tagline']}".lower().replace('"', '&quot;')
    
    html_template += f"""
        <!-- Category Block: {cat['num']} - {cat['title']} -->
        <article class="category-block" id="{cat['id']}" data-cat-id="{cat['id']}" data-search-text="{search_text}">
            <!-- Category Header -->
            <div class="category-header">
                <div class="cat-meta-row">
                    <span class="cat-num-badge">CATEGORY {cat['num']} OF 10</span>
                    <span class="cat-doubling-banner">Doubles For: {cat['doubles_as']}</span>
                </div>
                <h2 class="category-title">{cat['icon']} {cat['title']}</h2>
                <div class="category-area">Primary Locations: {cat['area']}</div>
                <p class="category-synopsis">{cat['creative_synopsis']}</p>
            </div>

            <!-- Hero Scouted Match Showcase -->
            <div class="hero-showcase">
                <div class="hero-image-wrap" data-cat-id="{cat['id']}" data-file="{hero_img_file}" onclick="openLightbox('{cat['id']}', 0)">
                    <img src="{hero_b64}" alt="{cat['hero_image_title']}" loading="lazy">
                    <span class="hero-overlay-badge">{cat['hero_badge']}</span>
                    <div class="hero-overlay-heart" onclick="event.stopPropagation(); toggleShortlistItem('{hero_img_file}', '{hero_title_clean}', '{cat_title_clean}', this)">
                        <svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
                    </div>
                </div>

                <div class="hero-details-panel">
                    <div class="hero-details-top">
                        <h3>{cat['hero_image_title']}</h3>
                        <p class="tagline">{cat['tagline']}</p>

                        <ul class="key-features-list">
"""
    for feat in cat["key_features"]:
        html_template += f"                            <li>{feat}</li>\n"

    cal_title = cat['title'].replace(' ', '+')
    cal_area = cat['area'].replace(' ', '+')
    html_template += f"""                        </ul>

                        <!-- Technical Filming Specifications -->
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
                        Click to view full-resolution cinema lightbox
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

# Render Commercial Rate Cards and Executive Contacts
html_template += """
        <!-- Commercial Rate Card Section -->
        <section class="rates-section" id="rates-and-contacts">
            <div class="rates-header">
                <span class="badge-premium">Transparent Commercial Framework</span>
                <h2>Standard Location Scouting & Management Rates</h2>
                <p>Standardized, professional union-compliant rates with direct multi-currency transparency for international production accounting.</p>
            </div>

            <div class="rates-grid">
                <!-- Location Scouting Card -->
                <div class="rate-card">
                    <div>
                        <div class="rate-tier">Tier 01 · Pre-Production</div>
                        <div class="rate-price" id="scoutRateDisplay">R 5,000 <span class="unit">/ day</span></div>
                        <div class="rate-equiv" id="scoutEquivDisplay">≈ USD $280 · EUR €255 · GBP £220 · INR ₹24,500</div>
                        <ul class="rate-includes">
                            <li>Comprehensive photographic location scouting & GPS metadata logging</li>
                            <li>Director reference matching and doubling feasibility analysis</li>
                            <li>Initial municipal permitting verification (City of Cape Town / SANParks)</li>
                            <li>Digital dossier generation with high-resolution contact sheets</li>
                            <li>Client liaison, itinerary routing, and scout vehicle logistics</li>
                        </ul>
                    </div>
                    <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Book+Location+Scouting+Days&details=Location+Scouting+inquiry+for+Cape+Town+production.+Day+rate%3A+ZAR+5%2C000%2Fday.&location=Cape+Town%2C+South+Africa&add=laura@zencrew.co.za&add=jardin@salocations.com" target="_blank" rel="noopener noreferrer" class="btn-nav primary" style="text-align: center; justify-content: center;">
                        Book Location Scout
                    </a>
                </div>

                <!-- Location Management Card -->
                <div class="rate-card featured">
                    <div>
                        <div class="rate-tier">Tier 02 · Principal Photography</div>
                        <div class="rate-price" id="manageRateDisplay">R 5,500 <span class="unit">/ shoot day</span></div>
                        <div class="rate-equiv" id="manageEquivDisplay">≈ USD $310 · EUR €280 · GBP £240 · INR ₹27,000</div>
                        <ul class="rate-includes">
                            <li>Full on-set location management and municipal liaison</li>
                            <li>Commercial filming permit execution & road closure police coordination</li>
                            <li>Unit base staging, honeywagon positioning, and generator clearance</li>
                            <li>Property owner contracts, damage waivers, and security protocols</li>
                            <li>Sound curfew enforcement, neighbour notifications & reinstatement</li>
                        </ul>
                    </div>
                    <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Book+Location+Management+Days&details=Location+Management+booking+for+shoot+days.+Rate%3A+ZAR+5%2C500%2Fshoot+day.&location=Cape+Town%2C+South+Africa&add=laura@zencrew.co.za&add=jardin@salocations.com" target="_blank" rel="noopener noreferrer" class="btn-nav primary" style="text-align: center; justify-content: center;">
                        Book Location Manager
                    </a>
                </div>

                <!-- Production Fixer & Unit Support -->
                <div class="rate-card">
                    <div>
                        <div class="rate-tier">Tier 03 · Full Production Services</div>
                        <div class="rate-price">Custom <span class="unit">/ scope</span></div>
                        <div class="rate-equiv">Turnkey Production Services Package</div>
                        <ul class="rate-includes">
                            <li>End-to-end local fixer services through Zencrew Production Services</li>
                            <li>Head-of-department crew sourcing (Cinematography, Art, Grips, Gaffer)</li>
                            <li>Tier-1 equipment rental coordination (Panavision, ARRI, Media Film Service)</li>
                            <li>Catering trucks, unit facilities, mobile production offices</li>
                            <li>Temporary work visas, equipment ATA Carnet, and tax rebate advice</li>
                        </ul>
                    </div>
                    <a href="mailto:laura@zencrew.co.za?cc=jardin@salocations.com&subject=Turnkey%20Production%20Services%20Inquiry%20-%20Cape%20Town" class="btn-nav" style="text-align: center; justify-content: center;">
                        Inquire Turnkey Package
                    </a>
                </div>
            </div>

            <!-- Executive Contacts Strip -->
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
                        <a href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=Production+Consultation+-+Zencrew&details=Production+Consultation+with+Laura+Diana+Macleod+%28Zencrew%29.&location=Cape+Town&add=laura@zencrew.co.za" target="_blank" rel="noopener noreferrer" class="contact-link">📅 Book Call</a>
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
                        <a href="https://github.com/jardinr/SALocations" target="_blank" rel="noopener noreferrer" class="contact-link">💻 GitHub Repository</a>
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
            <div class="footer-disclaimer">
                © 2026/2027 SA Locations & Zencrew. All photographs within the Scouted Images Database are proprietary assets photographed on location across the Western Cape, South Africa. Transposed under strict zero-rotation standards. Direct bookings subject to municipal permit authorization.
            </div>
        </div>
    </footer>

    <!-- Interactive Logic Script -->
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
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
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
            const item = activeGallery[activePhotoIndex];
            const cat = categoriesData[activeCategoryIndex];
            
            // Pull image src directly from corresponding card in DOM
            const cardImg = document.querySelector(`.category-block[data-cat-id="${cat.id}"] .gallery-card[data-photo-idx="${activePhotoIndex}"] img`);
            const b64 = cardImg ? cardImg.src : '';

            document.getElementById('lbMainImage').src = b64;
            document.getElementById('lbCatBadge').innerText = `${cat.icon} Category ${cat.num}: ${cat.title}`;
            document.getElementById('lbCounter').innerText = `${activePhotoIndex + 1} / ${activeGallery.length}`;
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
                const parent = heartBtn ? heartBtn.closest('.hero-image-wrap, .gallery-card') : document.querySelector(`[data-file="${CSS.escape(filePath)}"]`);
                const imgEl = parent ? parent.querySelector('img') : null;
                const thumbSrc = imgEl ? imgEl.src : '';
                currentShortlist.push({ filePath, title, categoryTitle, thumbSrc });
                if (heartBtn) heartBtn.classList.add('active');
            }
            updateShortlistUI();
        }

        function saveCurrentLightboxPhoto() {
            const item = activeGallery[activePhotoIndex];
            const cat = categoriesData[activeCategoryIndex];
            const card = document.querySelector(`.category-block[data-cat-id="${cat.id}"] .gallery-card[data-photo-idx="${activePhotoIndex}"]`);
            const heartBtn = card ? card.querySelector('.gallery-card-heart') : null;
            toggleShortlistItem(item.file, item.title, cat.title, heartBtn);
            alert('Saved "' + item.title + '" to your custom shortlist!');
        }

        function updateShortlistUI() {
            document.getElementById('shortlistCount').innerText = currentShortlist.length;
            const body = document.getElementById('shortlistBody');

            if (currentShortlist.length === 0) {
                body.innerHTML = `
                    <div class="shortlist-empty">
                        No locations saved yet.<br>Click the heart icon on any photo to add it to your custom production deck.
                    </div>`;
                return;
            }

            let html = '';
            currentShortlist.forEach((item, idx) => {
                html += `
                    <div class="shortlist-item">
                        <img class="shortlist-thumb" src="${item.thumbSrc}" alt="${item.title}">
                        <div class="shortlist-item-info">
                            <div class="shortlist-item-title">${item.title}</div>
                            <div class="shortlist-item-cat">${item.categoryTitle}</div>
                        </div>
                        <button class="shortlist-remove" onclick="removeShortlistItem(${idx})">✕</button>
                    </div>`;
            });
            body.innerHTML = html;
        }

        function removeShortlistItem(idx) {
            currentShortlist.splice(idx, 1);
            updateShortlistUI();
        }

        function clearShortlist() {
            currentShortlist = [];
            updateShortlistUI();
            document.querySelectorAll('.hero-overlay-heart, .gallery-card-heart').forEach(h => h.classList.remove('active'));
        }

        function sendShortlistInquiry() {
            if (currentShortlist.length === 0) {
                alert('Please add at least one location to your shortlist before submitting.');
                return;
            }
            let listText = "Selected Cape Town Locations for Production Inquiry:\\n\\n";
            currentShortlist.forEach((item, i) => {
                listText += `${i + 1}. [${item.categoryTitle}] ${item.title}\\n`;
            });
            const subject = encodeURIComponent("Cape Town Location Scouting Shortlist Inquiry");
            const body = encodeURIComponent(listText + "\\n\\nPlease provide availability, scouting recces, and permitting details.\\n\\nRegards,\\nProduction Client");
            window.location.href = `mailto:laura@zencrew.co.za?cc=jardin@salocations.com&subject=${subject}&body=${body}`;
        }
    </script>
</body>
</html>
"""

output_html_path = os.path.join(deck_dir, "index.html")
print(f"Writing complete index.html to {output_html_path}...")

with open(output_html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Successfully generated {output_html_path}!")
print(f"File size: {os.path.getsize(output_html_path) / (1024*1024):.2f} MB")

# Write package.json for static serve
pkg_path = os.path.join(deck_dir, "package.json")
pkg_json = {
    "name": "sal-global-locations-deck",
    "version": "1.0.0",
    "description": "Cape Town Master Location Scouting Database · International Film & Commercial Showcase - SA Locations & Zencrew",
    "scripts": {
        "start": "npx serve ."
    }
}
with open(pkg_path, "w", encoding="utf-8") as f:
    json.dump(pkg_json, f, indent=2)

# Write .gitignore
gitignore_path = os.path.join(deck_dir, ".gitignore")
with open(gitignore_path, "w", encoding="utf-8") as f:
    f.write(".vercel\nembedded_data.json\n")

print("All build assets written successfully!")
