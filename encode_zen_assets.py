import os
import json
import base64
import io
from PIL import Image, ImageOps

ref_dir = r"C:\Users\Jardin\OneDrive\Pictures\Zen\chinni loc refs"
zen_dir = r"C:\Users\Jardin\OneDrive\Pictures\Zen"
blackwood_dir = r"C:\Users\Jardin\OneDrive\Pictures\Zen\Blackwood Cabin"
harringtons_dir = r"C:\Users\Jardin\OneDrive\Pictures\Zen\Harringtons Cocktail Lounge"
house2_dir = r"C:\Users\Jardin\OneDrive\Pictures\Zen\House 2 Heritage Cottages (Culver & Chatham)"
web_dir = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\zen-mirage-media-web"

os.makedirs(web_dir, exist_ok=True)

def encode_img(path, max_size=(1200, 800), quality=80):
    if not os.path.exists(path):
        print(f"Warning: {path} not found!")
        return ""
    try:
        with Image.open(path) as im:
            im = ImageOps.exif_transpose(im)
            im = im.convert("RGB")
            im.thumbnail(max_size, Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            im.save(buf, format="JPEG", quality=quality)
            return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")
    except Exception as e:
        print(f"Error encoding {path}: {e}")
        return ""

embedded_images = {}

def get_file_path(filename, source_type):
    if source_type == "ref":
        return os.path.join(ref_dir, filename)
    elif source_type == "blackwood":
        return os.path.join(blackwood_dir, filename)
    elif source_type == "harringtons":
        return os.path.join(harringtons_dir, filename)
    elif source_type == "house2":
        return os.path.join(house2_dir, filename)
    else:
        return os.path.join(zen_dir, filename)

categories = [
    {
        "id": "live-music-cafe",
        "num": "01",
        "title": "Live Music Cafe & Supper Club",
        "icon": "☕",
        "ref_heading": "Director's Visual Reference · Live Music Venue & Dining Terrace",
        "match_heading": "Scouted Database · StarDust Theatrical Dining [100% Exact Match] & Imhoff's Gift",
        "match_score": "100% Exact Match",
        "area": "Woodstock & Noordhoek Coastal Valley, Cape Town",
        "tagline": "100% exact real-world match to Director Reference: StarDust Theatrical Dining in Woodstock with elevated stage, grand piano, and wide dining floor, paired with Imhoff's Gift sunny outdoor wetland cafe deck.",
        "creative_synopsis": "The director's visual reference (cafe w live music.jpg) is an exact photograph of StarDust Theatrical Dining in Woodstock! Look closely at the illuminated 'StarDust' emblem behind the stage. Our scouted hero photo (Stardust 12) captures the exact same venue from an elevated vantage, showcasing the full wide dining floor, cabaret tables, raised stage, grand piano, and live singer under stage lights. For daytime outdoor scenes, Imhoff's Gift in Noordhoek provides the sunny courtyard cafe and wooden wetland deck.",
        "ref_hero": "cafe w live music.jpg",
        "ref_hero_source": "ref",
        "ref_hero_title": "Director Reference: Intimate Cabaret Supper Club with Live Singer & Stage (StarDust Theatrical Dining)",
        "scouted_hero": "Stardust (12).jpg",
        "scouted_hero_source": "zen",
        "scouted_hero_title": "StarDust Theatrical Dining: Exact Venue Match with Wide Dining Floor, Elevated Stage & Live Performance",
        "key_features": [
            "100% Exact Venue Match: StarDust Theatrical Dining (Sir Lowry Rd, Woodstock)",
            "Elevated performance stage with grand piano, professional PA, and theatrical lighting rig",
            "Spacious wide timber dining floor accommodating tiered cabaret seating for 60–120 patrons",
            "Imhoff's Gift Exterior: Timber & stone courtyard cafe, sunny pergolas, and covered wooden deck over wetlands",
            "Outdoor Cafe Courtyards: Brick-paved terraces with wooden bench seating, umbrellas, and character multi-pane factory windows (IMG 5253)"
        ],
        "specs": {
            "permitting": "Private Commercial Contract · Direct Venue Agreements (48-hr turnaround)",
            "power": "3-Phase 63A Power On-Site · Domestic 16A Distributed Distribution Tie-Ins",
            "parking": "Dedicated secure gated parking for 6 technical vans + side-street production truck staging",
            "sound_curfew": "Acoustically treated interior venue · Evening shoot permissions available with late wrap"
        },
        "gallery": [
            {"file": "cafe w live music.jpg", "source": "ref", "title": "Director Ref: Cabaret Stage, Live Singer & Seated Dining Audience (StarDust)", "cat": "ref"},
            {"file": "cafe w live music2.jpeg", "source": "ref", "title": "Director Ref: Sunny Outdoor Wooden Cafe Deck with Umbrellas", "cat": "ref"},
            {"file": "cafe w live music3.jpeg", "source": "ref", "title": "Director Ref: Bustling Public Plaza Cafe Terrace & Patio", "cat": "ref"},
            {"file": "Stardust (12).jpg", "source": "zen", "title": "StarDust Theatrical Dining: Wide Floor Architecture, Elevated Stage & Live Singer (100% Match)", "cat": "scouted"},
            {"file": "Stardust (8).jpg", "source": "zen", "title": "StarDust Theatrical Dining: Dining Floor & Balcony Mezzanine", "cat": "scouted"},
            {"file": "Stardust (3).jpg", "source": "zen", "title": "StarDust: Red Stage Lighting, Cabaret Tables & Theatrical Backdrop", "cat": "scouted"},
            {"file": "Stardust (6).jpg", "source": "zen", "title": "StarDust: Live Acoustic Performance Corner & Stage Lighting", "cat": "scouted"},
            {"file": "Stardust (9).jpg", "source": "zen", "title": "StarDust: Intimate Seating Perspective with Ambient Lighting Rig", "cat": "scouted"},
            {"file": "IMG_5253.JPG", "source": "zen", "title": "Outdoor Cafe Courtyard & Terrace: Multi-Pane Windows & Shaded Picnic Seating", "cat": "scouted"},
            {"file": "Imhoff's Gift (20).jpg", "source": "zen", "title": "Imhoff's Gift: Timber & Stone Courtyard Cafe Exterior in Fynbos Setting", "cat": "scouted"},
            {"file": "Imhoff's Gift (21).jpg", "source": "zen", "title": "Imhoff's Gift: Rustic Covered Wooden Deck Looking Over Wetlands & Mountains", "cat": "scouted"},
            {"file": "Imhoff's Gift (18).jpg", "source": "zen", "title": "Imhoff's Gift: Secluded Coastal Wooden Dining Retreat with Mountain Views", "cat": "scouted"}
        ]
    },
    {
        "id": "cast-drive",
        "num": "02",
        "title": "Cast Drive · Coastal Scenic Highway",
        "icon": "🚗",
        "ref_heading": "Director's Visual Reference · Winding Ocean Highway Towards Mountain Headland",
        "match_heading": "Scouted Database · Victoria Road (M6) [100% Exact Match] & Chapman's Peak",
        "match_score": "100% Exact Match",
        "area": "Victoria Road (Atlantic Seaboard) & Chapman's Peak, Cape Town",
        "tagline": "100% exact real-world match to Director Reference: Victoria Road (M6) curving between the Atlantic Ocean and the 12 Apostles towards Lion's Head, paired with Chapman's Peak Drive.",
        "creative_synopsis": "The director's visual reference (cast drive.jpeg) is an aerial perspective of Victoria Road (M6) curving along the Atlantic coast towards Lion's Head and Camps Bay! Our scouted database pairs this directly with Victoria Road from ground level (M6-to CB 0) — the identical stretch of coastal tarmac hugging the 12 Apostles with Lion's Head on the horizon. Supported by Chapman's Peak Drive for high-altitude vertical rock cliff sequences.",
        "ref_hero": "cast drive.jpeg",
        "ref_hero_source": "ref",
        "ref_hero_title": "Director Reference: Winding Coastal Highway Approaching Lion's Head & Camps Bay (Victoria Road from Above)",
        "scouted_hero": "M6-to CB (0).jpg",
        "scouted_hero_source": "zen",
        "scouted_hero_title": "Victoria Road (M6): Exact Ground-Level Match to Ref Hugging 12 Apostles with Lion's Head Vista",
        "key_features": [
            "100% Exact Road Match: Victoria Road (M6) between Oudekraal and Camps Bay facing Lion's Head",
            "9 km of winding coastal highway with 12 Apostles mountain ramparts on one side and crashing Atlantic surf on the other",
            "Dedicated low-loader tracking vehicle (Russian Arm / Motocrane) filming clearance",
            "Full rolling road closure protocols managed via City of Cape Town Film Office",
            "Chapman's Peak Drive coastal extension for high-altitude cantilevered rock galleries and sheer 500m sea cliffs"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Permit Office & Entilini Concession (Standard 5-day lead time)",
            "power": "Mobile Generator Truck (Whisper-Watt 40kVA/60kVA) required for roadside basecamps",
            "parking": "Dedicated coastal turnout bays accommodate technical tracking vehicles and unit base",
            "sound_curfew": "Daylight filming preferred; sunset tracking closures and police escorts arranged"
        },
        "gallery": [
            {"file": "cast drive.jpeg", "source": "ref", "title": "Director Ref: Winding Coastal Highway Approaching Lion's Head (Victoria Road from Above)", "cat": "ref"},
            {"file": "M6-to CB (0).jpg", "source": "zen", "title": "Victoria Road (M6): Exact Ground-Level Match Hugging 12 Apostles with Lion's Head (100% Match)", "cat": "scouted"},
            {"file": "M6-to CB (1).jpg", "source": "zen", "title": "Victoria Road: Oceanfront Tarmac Run with Blue Atlantic Horizons", "cat": "scouted"},
            {"file": "M6-to CB (7).jpg", "source": "zen", "title": "Victoria Road: Sunset Curve Approaching Camps Bay", "cat": "scouted"},
            {"file": "Chapmans Peak (91).jpg", "source": "zen", "title": "Chapman's Peak: Dramatic Cliff Hugging S-Bend Looking Towards Hout Bay", "cat": "scouted"},
            {"file": "Chapmans Peak (57).jpg", "source": "zen", "title": "Chapman's Peak: Half-Tunnel Rock Gallery & Ocean Horizon", "cat": "scouted"},
            {"file": "Chapmans Peak (71).jpg", "source": "zen", "title": "Chapman's Peak: Sweeping South Vista Towards Noordhoek Beach", "cat": "scouted"},
            {"file": "Chapmans Peak (78).jpg", "source": "zen", "title": "Chapman's Peak: High Altitude Curve & Deep Turquoise Ocean", "cat": "scouted"},
            {"file": "Chapmans Peak South Lookout (5).jpg", "source": "zen", "title": "Chapman's Peak Lookout Over Monkey Valley & Long Beach Noordhoek", "cat": "scouted"}
        ]
    },
    {
        "id": "hero-house",
        "num": "03",
        "title": "Hero House & Heritage Character Residences",
        "icon": "🏡",
        "ref_heading": "Director's Visual Reference · Heritage Suburban Cottage with Mountain Backdrop",
        "match_heading": "Scouted Database · Culver & Chatham Cottages (Salt River) & Rosemount Avenue (Gardens)",
        "match_score": "99% Match",
        "area": "Salt River & Gardens, Cape Town",
        "tagline": "Authentic suburban heritage character residences featuring gabled rooflines, white boundary walls, picket gates, leafy pavement trees, and Table Mountain vistas, paired with atmospheric residential streetscapes.",
        "creative_synopsis": "The visual brief (house2.jpeg) captures an iconic suburban heritage cottage with a gabled front, picket gate, front veranda, and Table Mountain rising in the background. Our scouted database pairs this directly with the Culver Street & Chatham Street cottages in Salt River and Rosemount Avenue in Gardens, offering complete architectural fidelity, historic veranda detailing, and character residential streetscapes.",
        "ref_hero": "house2.jpeg",
        "ref_hero_source": "ref",
        "ref_hero_title": "Director Reference: Heritage Suburban Cottage with Gabled Front, Picket Gate & Mountain Peak",
        "scouted_hero": "Culver St (1).jpg",
        "scouted_hero_source": "zen",
        "scouted_hero_title": "Culver Street Heritage Cottage: Gabled Facade, Picket Gate, Front Veranda & Quiet Residential Street",
        "key_features": [
            "Culver & Chatham Cottages: Authentic Cape suburban architecture, gabled rooflines, white boundary walls & picket gates",
            "Direct architectural match to Director Reference (house2.jpeg) with tree-lined street frontage",
            "Rosemount Avenue: Classic Victorian street facade framed beneath Table Mountain and Lion's Head skyline",
            "Quiet suburban street corridors with easy unit parking and minimal traffic flow",
            "Full cast, crew, and technical turnaround access with pre-cleared residential filming agreements"
        ],
        "specs": {
            "permitting": "Private Residential Agreement + City of Cape Town Film Office Street Staging",
            "power": "Domestic 60A Single Phase + Exterior 3-Phase Tie-in / Silent Genny Staging",
            "parking": "On-site driveway for 3 lead vehicles + dedicated street coning for 6 technical vans",
            "sound_curfew": "Quiet residential neighborhood · Evening filming until 22:00 with community waiver"
        },
        "gallery": [
            {"file": "house2.jpeg", "source": "ref", "title": "Director Ref: Heritage Suburban Cottage with Gabled Front & Table Mountain Backdrop", "cat": "ref"},
            {"file": "Culver St (1).jpg", "source": "zen", "title": "Culver St Cottage: Gabled Heritage Facade, Picket Gate & Veranda (Direct Match to Ref 2)", "cat": "scouted"},
            {"file": "Culver St (2).jpg", "source": "zen", "title": "Culver St: Suburban Street Approach & Surrounding Heritage Homes", "cat": "scouted"},
            {"file": "Culver St (3).jpg", "source": "zen", "title": "Culver St: Architectural Detail of Heritage Porch & Picket Fence", "cat": "scouted"},
            {"file": "Chatham St (2).jpg", "source": "zen", "title": "Chatham St: Heritage Residential Street Corridor Framing Mountain Backdrop", "cat": "scouted"},
            {"file": "Rosemount Ave-Gardens (4).jpg", "source": "zen", "title": "Rosemount Avenue: Classic Victorian Street Facade Beneath Table Mountain", "cat": "scouted"}
        ]
    },
    {
        "id": "mountain-bike-trail",
        "num": "04",
        "title": "Mountain Bike Trail & Scenic Passes",
        "icon": "🚵",
        "ref_heading": "Director's Visual Reference · Scenic Coastal Pass with Cyclists & Mountain Single-Track",
        "match_heading": "Scouted Database · Chapman's Peak Scenic Pass [100% Match], Cliff Trails & Forest Tracks",
        "match_score": "100% Exact Match",
        "area": "Chapman's Peak Drive, Table Mountain National Park & Somerset West",
        "tagline": "Almost exact 1:1 real-world match to Director Reference: Chapman's Peak Drive coastal pass overlooking Hout Bay, paired with Chapman's Peak single-track cliff trails, Deer Park pine forest, and Lourensford flow tracks.",
        "creative_synopsis": "The director's reference (mountain bike trail2.jpeg) captures cyclists on Chapman's Peak Drive with the breathtaking vista of Hout Bay, the crescent beach, and Karbonkelberg/Sentinel! Our scouted database pairs this directly with Chapman's Peak (91) — the exact same panoramic curve and lookout. To provide dynamic off-road action, Chapman's Peak Trail adds narrow single-track paths carved into sheer red sandstone cliffs, while Deer Park and Lourensford Estate deliver high-speed forest descents.",
        "ref_hero": "mountain bike trail2.jpeg",
        "ref_hero_source": "ref",
        "ref_hero_title": "Director Reference: Scenic Coastal Mountain Pass with Cyclists Hugging Ocean Cliff (Chapman's Peak Vista)",
        "scouted_hero": "Chapmans Peak (91).jpg",
        "scouted_hero_source": "zen",
        "scouted_hero_title": "Chapman's Peak Pass: Exact Geographic Match to Director Ref Looking Across Hout Bay & Sentinel Headland",
        "key_features": [
            "100% Exact Pass Match: Chapman's Peak Drive lookout overlooking Hout Bay, sandy beach & Sentinel headland",
            "Chapman's Peak Trail: Dramatic single-track path carved into vertical red sandstone cliffs overlooking the ocean",
            "Deer Park (Table Mountain): Graded forest tracks and switchbacks winding beneath indigenous pine canopies",
            "Lourensford Estate Trails: Manicured flow tracks with sweeping mountain and vineyard backdrops",
            "Accessible camera tracking vehicle corridors running parallel to pass and trail sections"
        ],
        "specs": {
            "permitting": "SANParks Commercial Filming Permit (Table Mountain & Chapmans Peak) / Lourensford Estate",
            "power": "Battery-powered camera packages & portable whisper petrol inverter generators (2kVA)",
            "parking": "Chapman's Peak lookout parking / Deer Park lower car park accommodates full unit fleet",
            "sound_curfew": "Full natural daylight window; quiet electric quad bike tracking rigs permitted"
        },
        "gallery": [
            {"file": "mountain bike trail2.jpeg", "source": "ref", "title": "Director Ref: Scenic Coastal Pass with Cyclists Hugging Cliff Overlooking Hout Bay", "cat": "ref"},
            {"file": "mountain bike trail.jpeg", "source": "ref", "title": "Director Ref: Rider Navigating Forest Dirt Trail Along Mountain Flank", "cat": "ref"},
            {"file": "Chapmans Peak (91).jpg", "source": "zen", "title": "Chapman's Peak Pass: Exact Match Lookout Looking Towards Hout Bay & Sentinel (100% Match)", "cat": "scouted"},
            {"file": "Chapmans Peak Trail (2).jpg", "source": "zen", "title": "Chapman's Peak Trail: Red Sandstone Cliff Single-Track Path Carved Above Ocean", "cat": "scouted"},
            {"file": "Chapmans Peak Trail (1).jpg", "source": "zen", "title": "Chapman's Peak Trail: High Ridge Path Overlooking Hout Bay & The Sentinel Peak", "cat": "scouted"},
            {"file": "Deer Park (2).jpg", "source": "zen", "title": "Deer Park: Single-Track Trail Winding Through Table Mountain Pine Forest", "cat": "scouted"},
            {"file": "Deer Park (24).jpg", "source": "zen", "title": "Deer Park: Elevated Ridge Corridor Looking Out Over Cape Town", "cat": "scouted"},
            {"file": "Lourensford trails (5).jpg", "source": "zen", "title": "Lourensford Trails: Manicured Flow Track with Dramatic Mountain Backdrop", "cat": "scouted"},
            {"file": "Lourensford trails (14).jpg", "source": "zen", "title": "Lourensford Trails: Forest Descent with Sunlit Clearing", "cat": "scouted"}
        ]
    },
    {
        "id": "mountainside-shack",
        "num": "05",
        "title": "Mountainside Shack · Blackwood Cabin, Amara Moon & Retreats",
        "icon": "🛖",
        "ref_heading": "Director's Visual Reference · Off-Grid Cabin & Mountainside Stilt Villa",
        "match_heading": "Scouted Database · Blackwood Cabin, Amara Moon (Hout Bay Forest), Vicki Residence & Monkey Valley",
        "match_score": "99% Match",
        "area": "Hout Bay Forest, Scarborough & Noordhoek Coastal Valley, Cape Town",
        "tagline": "Secluded contemporary dark timber stilt cabins, architectural treehouse retreats nestled in the Hout Bay forest canopy (Amara Moon), character residential living (Vicki), and rustic mountain chalets.",
        "creative_synopsis": "The director's reference features isolated weathered timber cabins and secluded architectural stilt retreats. This category pairs Blackwood Cabin (contemporary dark timber stilt cabin in forest canopy with plunge pool) and Amara Moon (secluded architectural stilt villa nestled deep within the indigenous Hout Bay forest canopy), alongside the character-filled Vicki Residence and Monkey Valley Nature Resort.",
        "ref_hero": "mountainside shack.jpg",
        "ref_hero_source": "ref",
        "ref_hero_title": "Director Reference: Isolated Cabin on Rocky Mountain Slope with Wind Turbine",
        "scouted_hero": "Blackwood Cabin (1).jpg",
        "scouted_hero_source": "blackwood",
        "scouted_hero_title": "Blackwood Cabin: Contemporary Dark Timber Stilt Cabin with Elevated Boardwalk in Forest",
        "key_features": [
            "Blackwood Cabin: Elevated contemporary dark timber architecture on steel stilts with wraparound forest deck",
            "Amara Moon: Secluded modern architectural stilt retreat nestled within the private indigenous tree canopy of Hout Bay forest",
            "Vicki Residence: Character residential mountain retreat featuring authentic timber finishes, artistic interior living & natural daylighting",
            "Natural rock plunge pool with timber sun deck surrounded by giant strelitzias and ferns (Blackwood)",
            "Monkey Valley Nature Resort: Weathered log and thatch mountain chalets set beneath ancient milkwood trees"
        ],
        "specs": {
            "permitting": "Private Property Commercial Agreement · Film-supportive management (48-hr turnaround)",
            "power": "On-site domestic supply + dedicated 32A exterior socket for mobile distribution boards",
            "parking": "Gated private property parking for 6 technical vehicles + nearby overflow unit base",
            "sound_curfew": "Ultra-quiet secluded acoustic environment · Zero ambient traffic noise · 24/7 filming capability"
        },
        "gallery": [
            {"file": "mountainside shack.jpg", "source": "ref", "title": "Director Ref: Isolated Cabin on Rocky Mountain Slope with Wind Turbine", "cat": "ref"},
            {"file": "mountainside shack2.jpg", "source": "ref", "title": "Director Ref: Weathered Timber Cabin Beneath Sheer Mountain Cliff", "cat": "ref"},
            {"file": "house.jpg", "source": "ref", "title": "Director Ref: Elevated Wooden Villa on Mountain Slope Overlooking Ocean Bay", "cat": "ref"},
            {"file": "Blackwood Cabin (1).jpg", "source": "blackwood", "title": "Blackwood Cabin: Elevated Dark Timber Stilt Cabin & Winding Boardwalk Staircase", "cat": "scouted"},
            {"file": "Blackwood Cabin (2).jpg", "source": "blackwood", "title": "Blackwood Cabin: Natural Rock Plunge Pool, Timber Sun Deck & Strelitzia Garden", "cat": "scouted"},
            {"file": "Blackwood Cabin (3).jpg", "source": "blackwood", "title": "Blackwood Cabin: Double-Storey Timber Deck & Golden Hour Eucalyptus Canopy", "cat": "scouted"},
            {"file": "Blackwood Cabin (4).jpg", "source": "blackwood", "title": "Blackwood Cabin: Elevated Balcony Vista Overlooking Forest Deck & Mountain Slopes", "cat": "scouted"},
            {"file": "Amara Moon (2).jpg", "source": "zen", "title": "Amara Moon: Secluded Architectural Stilt Villa in Hout Bay Forest", "cat": "scouted"},
            {"file": "Amara Moon (4).jpg", "source": "zen", "title": "Amara Moon: Elevated Timber Deck Nestled in Indigenous Hout Bay Forest Canopy", "cat": "scouted"},
            {"file": "Vicki (22).JPG", "source": "zen", "title": "Vicki Residence: Character Living Interior & Natural Daylighting", "cat": "scouted"},
            {"file": "Monkey Valley.png", "source": "zen", "title": "Monkey Valley: Rustic Wooden Mountain Cabins under Milkwood Canopy (Noordhoek)", "cat": "scouted"}
        ]
    },
    {
        "id": "nightclub-venue",
        "num": "06",
        "title": "Nightclub · Music Venue · Beach Lounge",
        "icon": "🍸",
        "ref_heading": "Director's Visual Reference · Harringtons Live Bar, Club Dancefloor & Neon Beach Lounge",
        "match_heading": "Scouted Database · Harringtons Cocktail Lounge (100% Match), Café Caprice & Club Destiny",
        "match_score": "100% Exact Match",
        "area": "East City (Harrington St), CBD Nightlife Strip & Camps Bay Promenade, Cape Town",
        "tagline": "100% exact real-world match to Director Reference: Harringtons Cocktail Lounge with vintage chandeliers, velvet banquettes, wood-paneled bar counter, paired with Café Caprice beachfront lounge and high-energy club dancefloors.",
        "creative_synopsis": "The director's visual reference (nightclub.jpeg) is an exact photograph taken inside Harringtons Cocktail Lounge in Cape Town! We have secured Harringtons as a 100% direct location match, featuring amber-lit velvet booth seating, ornate crystal chandeliers, vintage disco balls, and a classic wooden paneled bar. To complement this, Café Caprice delivers the beachfront cocktail lounge, while Club Destiny, Club Halo, and Hexagon provide high-energy dancefloors with full DMX laser lighting.",
        "ref_hero": "nightclub.jpeg",
        "ref_hero_source": "ref",
        "ref_hero_title": "Director Reference: Intimate Amber-Lit Club Bar with Live Performance & Chandeliers (Harringtons)",
        "scouted_hero": "Harringtons (3).jpg",
        "scouted_hero_source": "harringtons",
        "scouted_hero_title": "Harringtons Cocktail Lounge: Classic Dark Mahogany Bar Counter, Backlit Glassware & Crystal Chandeliers (100% Match)",
        "key_features": [
            "100% Exact Location Match: Harringtons Cocktail Lounge (61B Harrington St, East City)",
            "Classic dark mahogany wood-paneled cocktail bar counter with backlit spirit displays (Direct Ref Match)",
            "Vintage crystal chandeliers, sparkling disco balls, exposed wooden roof trusses, and chevron timber flooring",
            "Plush curved velvet banquettes, tufted amber booth seating with arched windows and draped velvet curtains",
            "Café Caprice (Camps Bay Strip): Beachfront terrace with outdoor Corona umbrellas & curved fluted wood Veuve Clicquot bar",
            "Club Destiny, Club Halo & Hexagon: Heavy DMX intelligent stage lighting grids, laser arrays, and private VIP lounges"
        ],
        "specs": {
            "permitting": "Private Commercial Contract · Direct Venue Management Partner (Daytime & night access)",
            "power": "High-Capacity 3-Phase 100A+ Commercial Power Tie-Ins On-Site",
            "parking": "City of Cape Town street parking reserved for technical vehicles and gear trucks",
            "sound_curfew": "Full soundproof acoustic interior · 24/7 filming and high-volume playback permitted"
        },
        "gallery": [
            {"file": "nightclub.jpeg", "source": "ref", "title": "Director Ref: Harringtons Live Performance Stage, Amber Glow & Chandelier (100% Match)", "cat": "ref"},
            {"file": "nightclub2.jpeg", "source": "ref", "title": "Director Ref: Packed Nightclub Dancefloor with Red/Blue Laser Beams", "cat": "ref"},
            {"file": "nightclub3.jpeg", "source": "ref", "title": "Director Ref: Neon Beachfront Bar Exterior at Dusk (Café Caprice, Camps Bay)", "cat": "ref"},
            {"file": "Harringtons (3).jpg", "source": "harringtons", "title": "Harringtons: Classic Dark Mahogany Bar Counter & Backlit Glassware (Direct 100% Match to Ref Bar)", "cat": "scouted"},
            {"file": "Harringtons (2).jpg", "source": "harringtons", "title": "Harringtons: Main Dance Floor with Crystal Chandeliers, Disco Balls & Velvet Seating", "cat": "scouted"},
            {"file": "Harringtons (1).jpg", "source": "harringtons", "title": "Harringtons: Amber Velvet Booth Seating with Arched Windows & Blue Curtains", "cat": "scouted"},
            {"file": "Harringtons (4).jpg", "source": "harringtons", "title": "Harringtons: Wide Lounge Floor Perspective Facing Bar & Booths", "cat": "scouted"},
            {"file": "Harringtons (5).jpg", "source": "harringtons", "title": "Harringtons: Tufted Chesterfield Leather Couches & Rustic Wood Trusses", "cat": "scouted"},
            {"file": "Cafe Caprice (1).jpg", "source": "zen", "title": "Café Caprice: Camps Bay Beachfront Promenade Exterior & Outdoor Terrace", "cat": "scouted"},
            {"file": "Cafe Caprice (2).jpg", "source": "zen", "title": "Café Caprice: Curved Fluted Wood Cocktail Bar & Veuve Clicquot Lounge", "cat": "scouted"},
            {"file": "Club Destiny (1).JPG", "source": "zen", "title": "Club Destiny: Main Dancefloor & Intelligent Stage Lighting Grid", "cat": "scouted"},
            {"file": "Club Destiny (4).JPG", "source": "zen", "title": "Club Destiny: VIP Banquette Lounge with Mood Lighting", "cat": "scouted"},
            {"file": "Club Destiny (7).JPG", "source": "zen", "title": "Club Destiny: Back-Lit Cocktail Bar & Intimate Lounge", "cat": "scouted"},
            {"file": "Club Destiny (8).JPG", "source": "zen", "title": "Club Destiny: Performance Stage with Concert Sound Rigs", "cat": "scouted"},
            {"file": "Club Halo (8).jpg", "source": "zen", "title": "Club Halo: Immersive LED Ceiling Arrays & Underground Club Atmosphere", "cat": "scouted"},
            {"file": "Club Halo (20).jpg", "source": "zen", "title": "Club Halo: Private Mezzanine VIP Bar & Banquettes", "cat": "scouted"},
            {"file": "Club Halo (37).jpg", "source": "zen", "title": "Club Halo: Main Floor Crowd Perspective with Blue Strobe Lighting", "cat": "scouted"},
            {"file": "Hexagon (4).jpg", "source": "zen", "title": "Hexagon Lounge: Swapped Club Seating with Leather Banquettes & Red Velvet Stage", "cat": "scouted"},
            {"file": "Hexagon (5).jpg", "source": "zen", "title": "Hexagon Lounge: Intimate Cocktail Seating Corner with Mood Lighting", "cat": "scouted"},
            {"file": "Hexagon (6).jpg", "source": "zen", "title": "Hexagon Lounge: Elevated VIP Area with Velvet Curtains", "cat": "scouted"}
        ]
    },
    {
        "id": "rehearsal-studio-spaces",
        "num": "07",
        "title": "Rehearsal Spaces, Industrial Lofts & Film Soundstages",
        "icon": "🎸",
        "ref_heading": "Director's Visual Reference · High-Ceiling Warehouse Lofts & Creative Soundstages",
        "match_heading": "Scouted Database · Daylight Infinity Cyclorama Studio [Best Match], Roodebloem & Milestone Studios",
        "match_score": "100% Direct Match",
        "area": "Woodstock, Salt River & Epping Production Hubs, Cape Town",
        "tagline": "Best real-world match to Director Reference: Daylight infinity cyclorama rehearsal studio with side window light and concrete beams, combined with Roodebloem Studios, Milestone acoustic rooms, and soundstages.",
        "creative_synopsis": "The director's reference (rehearsal space.jpeg) calls for an expansive daylight rehearsal studio with white cyclorama, industrial concrete ceiling beams, and natural window light streaming across the floor. Our scouted Daylight Rehearsal Studio is the premier direct match: featuring a seamless white infinity curve, polished concrete floor, overhead industrial beams with cable trays, and expansive sunlit window bays. Paired with Roodebloem Studios (historic church daylight cycloramas), Studio 107 soundstages, Milestone acoustic rooms, and precision scoring suites.",
        "ref_hero": "rehearsal space.jpeg",
        "ref_hero_source": "ref",
        "ref_hero_title": "Director Reference: Sunlit Industrial Loft Rehearsal Space with Multi-Pane Windows & White Cyclorama",
        "scouted_hero": "Daylight Rehearsal Studio (1).jpg",
        "scouted_hero_source": "zen",
        "scouted_hero_title": "Daylight Infinity Cyclorama Studio: Sunlit Windows, Concrete Beams & Polished Rehearsal Floor (Best Match)",
        "key_features": [
            "Daylight Infinity Cyclorama Studio: Seamless white curve, natural window light beams, and smooth polished rehearsal floor",
            "Industrial overhead concrete beams and high-capacity electrical cable management for lighting grids",
            "Direct typological match to Director Reference (rehearsal space.jpeg) with full daylight control",
            "Roodebloem Studios (Studio 1): Converted heritage church with massive daylight arched windows and infinite cyclorama",
            "Studio 107: Broadcast soundstage with overhead lighting grid, mobile green screen, control booth & acoustic baffles",
            "Milestone Studios: Acoustic isolation tracking rooms, grand piano, drum booth, and 5.1/Dolby Atmos ADR suites",
            "Suite Spot Studios & Studio 1: Motion cyclorama stage, green screen, multi-track scoring, and precision sound isolation booths",
            "Plug Studio, UCT & Forest Studios: Multi-track scoring, vocal tracking, and musical instrument staging"
        ],
        "specs": {
            "permitting": "Private Commercial Contract · Film Studio & Creative Property Management (Immediate clearance)",
            "power": "3-Phase 100A to 400A Studio Power Distribution with camlock and 63A CEE form tie-ins",
            "parking": "Secure access-controlled studio premises accommodating 20+ support trucks and unit trailers",
            "sound_curfew": "Full acoustic soundproofing on studio soundstages · 24/7 filming and high-SPL tracking authorized"
        },
        "gallery": [
            {"file": "rehearsal space.jpeg", "source": "ref", "title": "Director Ref: Creative Rehearsal Warehouse Loft with Factory Windows", "cat": "ref"},
            {"file": "rehearsal space2.webp", "source": "ref", "title": "Director Ref: Acoustic Rehearsal Room with Wooden Ceiling & Instruments", "cat": "ref"},
            {"file": "Daylight Rehearsal Studio (1).jpg", "source": "zen", "title": "Daylight Rehearsal Studio: White Cyclorama Cove, Concrete Beams & Side Window Light (Best Match)", "cat": "scouted"},
            {"file": "Daylight Rehearsal Studio (2).jpg", "source": "zen", "title": "Daylight Rehearsal Studio: Expansive Polished Floor & Ceiling Skylight Architecture", "cat": "scouted"},
            {"file": "Roodebloem Studios (2).jpg", "source": "zen", "title": "Roodebloem Studios: Daylight Cyclorama & Historic Converted Church Hall", "cat": "scouted"},
            {"file": "Studio 107 (Acoustic Studio & Green Screen).jpg", "source": "zen", "title": "Studio 107: Soundstage Live Room with Acoustic Baffles, Green Screen & Control Booth", "cat": "scouted"},
            {"file": "Studio 107 (6).jpg", "source": "zen", "title": "Studio 107: Soundproof Film Soundstage with Overhead Grid & Control Booth", "cat": "scouted"},
            {"file": "Milstone Studios (3).jpg", "source": "zen", "title": "Milestone Studios: Acoustic Live Tracking Room with Drum Kit & Sound Baffles", "cat": "scouted"},
            {"file": "Plug Studio (12).jpg", "source": "zen", "title": "Plug Studio: Professional Audio Tracking Room & Mixing Console", "cat": "scouted"},
            {"file": "Suite Spot Studios (3).jpg", "source": "zen", "title": "Suite Spot Studios: Multi-Track Control Room & Sound Isolation Booth", "cat": "scouted"},
            {"file": "studio1_02.jpg", "source": "zen", "title": "Suite Spot (Studio 1): Motion Cyclorama & Green Screen Stage", "cat": "scouted"},
            {"file": "UCT-Rec Studio (8).jpg", "source": "zen", "title": "UCT Recording Studio: Precision Acoustically Treated Live Scoring Room", "cat": "scouted"},
            {"file": "Forest Studio (7).jpg", "source": "zen", "title": "Forest Studio: Nature-Surrounded Acoustic Live Tracking Space", "cat": "scouted"},
            {"file": "Forest Studio (16).jpg", "source": "zen", "title": "Forest Studio: Recording Booth & Monitoring Environment", "cat": "scouted"}
        ]
    },
    {
        "id": "shopping-centre",
        "num": "08",
        "title": "Shopping Centre & Public Commercial Piazza",
        "icon": "🛍️",
        "ref_heading": "Director's Visual Reference · Multi-Storey Retail Mall & Waterfront Plaza",
        "match_heading": "Scouted Database · V&A Waterfront Clock Tower Precinct & Quayside",
        "match_score": "98% Match",
        "area": "V&A Waterfront & Foreshore, Cape Town",
        "tagline": "Dynamic commercial waterfront shopping precinct combining multi-level glass atrium shopping, historic quaysides, Victorian clock towers, and scenic harbor backdrops.",
        "creative_synopsis": "The director's reference depicts a vibrant commercial shopping centre and outdoor public pedestrian plaza. The Victoria & Alfred (V&A) Waterfront provides an extraordinary cinematic match: high-end retail mall interiors, expansive multi-level glass atriums, bustling pedestrian promenades, swing bridges, and iconic maritime vistas framed by Table Mountain.",
        "ref_hero": "shopping centre.jpeg",
        "ref_hero_source": "ref",
        "ref_hero_title": "Director Reference: Multi-Level Commercial Shopping Centre with Glass Walkways",
        "scouted_hero": "V&A Waterfront (3).jpg",
        "scouted_hero_source": "zen",
        "scouted_hero_title": "V&A Waterfront: Historic Red Clock Tower, Public Quayside Piazza & Table Mountain Skyline",
        "key_features": [
            "Victoria Wharf & Clock Tower: Modern multi-tiered glass shopping mall with soaring skylights and escalators",
            "Historic red Victorian Gothic Clock Tower (1882) presiding over open public pedestrian square",
            "Working harbor quayside with historic tugboats, yachts, swing bridges, and seals",
            "Unrivalled direct line-of-sight views of Table Mountain, Lion's Head, and the Atlantic Ocean",
            "Extensive underground parking, dedicated logistics service docks, and 24/7 private security"
        ],
        "specs": {
            "permitting": "V&A Waterfront Film Office Permit (Well-established production protocol, 5-day lead time)",
            "power": "Dedicated 3-Phase 63A/125A shore-power tie-ins located across quayside pedestals",
            "parking": "Secure subterranean and access-controlled open-air parking for 15+ heavy production vehicles",
            "sound_curfew": "Interior shoots after retail hours (21:00–08:00); exterior quayside shoots all day with pedestrian marshals"
        },
        "gallery": [
            {"file": "shopping centre.jpeg", "source": "ref", "title": "Director Ref: Modern Shopping Mall Atrium & Pedestrian Escalators", "cat": "ref"},
            {"file": "V&A Waterfront (3).jpg", "source": "zen", "title": "V&A Waterfront: Historic Clock Tower & Waterfront Promenade with Table Mountain", "cat": "scouted"},
            {"file": "V&A Waterfront (2).jpg", "source": "zen", "title": "V&A Waterfront: Working Harbor Basin, Quayside Architecture & Cranes", "cat": "scouted"},
            {"file": "V&A Waterfront (31).jpg", "source": "zen", "title": "V&A Waterfront: Vibrant Pedestrian Piazza with Outdoor Dining & Retail", "cat": "scouted"},
            {"file": "V&A Waterfront (32).jpg", "source": "zen", "title": "V&A Waterfront: Maritime Basin with Classic Vessels & Historic Warehouses", "cat": "scouted"},
            {"file": "V&A Waterfront (35).jpg", "source": "zen", "title": "V&A Waterfront: Modern Commercial Building & Harbor Walkway", "cat": "scouted"}
        ]
    }
]

print("Encoding images...")

# 1. Laura banner
banner_path = os.path.join(zen_dir, "Laura-Zen sign.png")
if os.path.exists(banner_path):
    embedded_images["footer_banner"] = encode_img(banner_path, max_size=(1600, 700), quality=88)
    print("Encoded footer banner (Laura-Zen sign.png)")

# 2. Categories
for cat in categories:
    print(f"Encoding category {cat['num']} - {cat['title']}...")
    
    # Hero ref
    ref_hero_path = get_file_path(cat["ref_hero"], cat["ref_hero_source"])
    if cat["ref_hero"] not in embedded_images:
        b64 = encode_img(ref_hero_path)
        if b64:
            embedded_images[cat["ref_hero"]] = b64
            print(f"  Encoded {cat['ref_hero']} ({len(b64)} chars)")

    # Hero scouted
    scouted_hero_path = get_file_path(cat["scouted_hero"], cat["scouted_hero_source"])
    if cat["scouted_hero"] not in embedded_images:
        b64 = encode_img(scouted_hero_path)
        if b64:
            embedded_images[cat["scouted_hero"]] = b64
            print(f"  Encoded {cat['scouted_hero']} ({len(b64)} chars)")

    # Gallery items
    for item in cat["gallery"]:
        fname = item["file"]
        if fname not in embedded_images:
            fpath = get_file_path(fname, item["source"])
            b64 = encode_img(fpath)
            if b64:
                embedded_images[fname] = b64
                print(f"  Encoded {fname} ({len(b64)} chars)")

print(f"Total embedded images encoded: {len(embedded_images)}")

data_to_save = {
    "categories": categories,
    "images": embedded_images
}

out_json = os.path.join(web_dir, "embedded_data.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(data_to_save, f)

print(f"Saved {out_json} successfully!")
