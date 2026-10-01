import os
import json
import base64
import io
from PIL import Image, ImageOps, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

pics_root = r"C:\Users\Jardin\OneDrive\Pictures"
output_json = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-global-locations-deck\embedded_data.json"

def encode_img(rel_path, max_size=(980, 650), quality=70):
    if os.path.isabs(rel_path):
        full_path = rel_path
    else:
        full_path = os.path.join(pics_root, rel_path)
    if not os.path.exists(full_path):
        print(f"Warning: File not found: {full_path}")
        return ""
    try:
        with Image.open(full_path) as im:
            # Strict GEMINI.md Rule 1: Always transpose on ingestion
            im = ImageOps.exif_transpose(im)
            im = im.convert("RGB")
            im.thumbnail(max_size, Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            im.save(buf, format="JPEG", quality=quality, optimize=True)
            return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")
    except Exception as e:
        print(f"Error encoding {full_path}: {e}")
        return ""

print("Encoding 16 Macro Categories Master Dataset...")

categories = [
    # 01
    {
        "id": "coastal-passes-ocean-roads",
        "num": "01",
        "title": "Coastal Passes, Ocean Roads & Arid Corridors",
        "icon": "🛣️",
        "doubles_as": "California Pacific Coast Highway (PCH) · Italian Amalfi Coast · French Riviera · Route 66 · Nevada Desert Corridor",
        "hero_badge": "Verified Location",
        "area": "Chapman's Peak Drive (M6), Victoria Road & R355 Karoo Highway",
        "tagline": "World-renowned coastal cliff highways carved into 500m ocean precipices, sweeping sea-level tarmac hugging the 12 Apostles, and uninterrupted horizon-to-horizon arid desert plains.",
        "creative_synopsis": "South Africa's coastal roadways offer the ultimate global doubling versatility. Chapman's Peak Drive (M6) provides 9km of cantilevered rock galleries and hairpin turns suspended 500m above the Atlantic, doubling seamlessly for the Italian Riviera or California's Big Sur. Below, Victoria Road (M6) stretches along turquoise Atlantic shores with direct lines-of-sight to Lion's Head and Camps Bay. Inland, the R355 in the Tankwa Karoo offers the longest uninterrupted straight dirt/gravel corridor on the continent for high-speed tracking and desert sequences.",
        "hero_image_file": r"08-Stadium\Mountain Pass-city\Chapmans Peak Drive\Chapmans Peak Drive (14).jpg",
        "hero_image_title": "Chapman's Peak Drive: Iconic Marine Drive Hugging Sheer Sandstone Cliffs Overlooking Hout Bay & The Sentinel",
        "key_features": [
            "9km of vertical cliff highway with 114 curves, cantilevered rock canopy galleries, and half-tunnels",
            "Victoria Road sea-level tracking corridor connecting Clifton, Camps Bay, and Llandudno along the 12 Apostles",
            "R355 Arid Highway & Tankwa Karoo: 250km uninterrupted gravel tracking corridor, Inverdoorn cactus curve, and Sadawa expedition basecamp",
            "Lookout Vantage: Chapman's Peak Lookout Over Monkey Valley & Long Beach Noordhoek",
            "Single-track cliff trails carved into red sandstone precipices for high-speed action tracking"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Permit Office & Entilini Concession (48–72 hr turnaround) · SANParks Commercial Permit",
            "power": "Self-contained mobile generator basecamps · 3-phase tie-ins available at Entilini depot & Hout Bay harbour",
            "parking": "4 designated heavy turnout bays on Chapman's Peak · Lower & upper parking lots accommodating full Motocrane fleet",
            "sound_curfew": "No residential curfew on pass routes · Scheduled rolling road closures with local traffic police escorts"
        },
        "gallery": [
            {"file": r"08-Stadium\Mountain Pass-city\Chapmans Peak Drive\Chapmans Peak Drive (14).jpg", "title": "Chapman's Peak Drive: Iconic Marine Pass Hugging Sheer Sandstone Cliffs Above Ocean Horizon", "tag": "Hero Chapman's"},
            {"file": r"Zen\Chapmans Peak (57).jpg", "title": "Chapman's Peak: Half-Tunnel Rock Gallery & Atlantic Horizon", "tag": "Rock Gallery"},
            {"file": r"Zen\Chapmans Peak (71).jpg", "title": "Chapman's Peak: Sweeping South Vista Towards Noordhoek & Ocean Horizon", "tag": "Coastal Curve"},
            {"file": r"Zen\Chapmans Peak (78).jpg", "title": "Chapman's Peak: Vertical Red Sandstone Cliff & Deep Turquoise Water", "tag": "Cliff Edge"},
            {"file": r"Zen\Chapmans Peak South Lookout (5).jpg", "title": "Chapman's Peak Lookout Over Monkey Valley & Long Beach Noordhoek", "tag": "Lookout Vista"},
            {"file": r"Zen\Chapmans Peak Trail (1).jpg", "title": "Chapman's Peak Trail: High Ridge Single-Track Above Ocean & Bay", "tag": "Cliff Trail"},
            {"file": r"Zen\Chapmans Peak Trail (2).jpg", "title": "Chapman's Peak Trail: Dramatic Sandstone Single-Track Cutting Into Cliff Face", "tag": "Action Trail"},
            {"file": r"Zen\M6-to CB (0).jpg", "title": "Victoria Road (M6): Sea-Level Coastal Drive Hugging Twelve Apostles Towards Lion's Head", "tag": "Victoria Rd"},
            {"file": r"Zen\M6-to CB (1).jpg", "title": "Victoria Road (M6): Golden Hour Tarmac & Atlantic Wave Horizon", "tag": "Coastal Highway"},
            {"file": r"Arid Road-R355\Silversea\20240326_184545.jpg", "title": "R355 Tankwa Karoo Highway: Vast Desert Basin & Endless Dirt Tracking Corridor Under Golden Sunset", "tag": "Sunset Corridor"},
            {"file": r"Arid Road-R355\Silversea\20240326_185451.jpg", "title": "Inverdoorn Big 5 Game Reserve Entrance (Tankwa Karoo): Prickly Pear Cactus Road & Fiery Sunset Sky", "tag": "Inverdoorn Curve"},
            {"file": r"Arid Road-R355\Silversea\20240326_164927.jpg", "title": "R355 Arid Highway: Uninterrupted Straight Gravel Tracking Corridor Vanishing Over Rolling Karoo Crests", "tag": "Straight Highway"},
            {"file": r"Arid Road-R355\Silversea\20240326_162423.jpg", "title": "Perdekraal East Wind Farm (R355 Corridor): Renewable Turbine Array Across Vast Karoo Plains", "tag": "Wind Farm"},
            {"file": r"Arid Road-R355\Silversea\Sadawa (20).jpg", "title": "Sadawa Game Reserve (Tankwa Karoo): Remote Production Expedition Basecamp Under Twilight Magenta Skies", "tag": "Desert Basecamp"},
            {"file": r"Arid Road-R355\Silversea\Sadawa (25).jpg", "title": "Tankwa Karoo Desert Wilderness: Rugged Scrub Plains & Distant Mountain Horizon at Dusk", "tag": "Karoo Wilderness"}
        ]
    },

    # 02
    {
        "id": "modern-luxury-villas",
        "num": "02",
        "title": "Modern Luxury Villas & Architectural Residences",
        "icon": "🏛️",
        "doubles_as": "Hollywood Hills · Malibu Oceanfront · Miami Waterfront Mansions · Modern Swiss/European Alpine Luxury",
        "hero_badge": "Verified Location",
        "area": "Nettleton Road (Clifton), Clifton Rocks & Lux Villa",
        "tagline": "Multi-tier glass and concrete cantilevered architectural estates perched above turquoise ocean coves, rim-flow infinity pools, private funiculars, and skyline penthouses.",
        "creative_synopsis": "Cape Town's Atlantic Seaboard houses some of the world's most sought-after contemporary film villas. Nettleton Ridge in Clifton represents the pinnacle of cantilevered luxury—featuring double-volume glass walls, raw off-shutter concrete, and rim-flow infinity pools floating above the Atlantic. Cap d'Afrique offers curved whitewashed terraces with direct sea-edge rocks and private funicular access. Lux Villa provides expansive multi-tiered ocean living pavilions, and high-rise penthouses showcase 270-degree skyline vistas.",
        "hero_image_file": r"Houses\Nettleton\Photos-001\Nettleton (1).jpg",
        "hero_image_title": "Nettleton Ridge Architectural Villa: Cantilevered Concrete, Glass Horizons & Rim-Flow Pool (Clifton)",
        "key_features": [
            "Nettleton Road: Prestigious multi-level residence with floor-to-ceiling glass, floating timber stairs, and ocean terrace",
            "Cap d'Afrique (Clifton): Iconic white modernist curves, private funicular cliff lift, and direct ocean boulder access",
            "Lux Villa: Multi-tiered contemporary architectural pavilions, expansive sun decks, and infinity horizon vistas",
            "Modern Skyline Penthouses: Curvilinear wrap-around windows, polished screed floors, and panoramic mountain panoramas",
            "Interior daylight design optimized for cinema lighting rigs, crane tracking, and soft ambient bounce"
        ],
        "specs": {
            "permitting": "Private Residential Filming Contract (24–48 hr direct sign-off) · City of Cape Town street parking reservation",
            "power": "3-Phase 63A/100A domestic tie-ins on-site · Dedicated subterranean parking for technical equipment vans",
            "parking": "Private multi-vehicle garages + driveway staging for camera tracking van and light generator trailer",
            "sound_curfew": "Standard 22:00 residential exterior sound curfew · 24/7 interior silent filming permitted"
        },
        "gallery": [
            {"file": r"Houses\Nettleton\Photos-001\Nettleton (1).jpg", "title": "Nettleton Villa: Cantilevered Master Suite & Glass Living Pavilion Above Clifton", "tag": "Nettleton Ridge"},
            {"file": r"Houses\Nettleton\Photos-001\Nettleton (7).jpg", "title": "Nettleton Villa: Open Living Lounge, Concrete Columns & Shaded Dining Pergola", "tag": "Architectural Interior"},
            {"file": r"Houses\Nettleton\Photos-001\Nettleton (8).jpg", "title": "Nettleton Villa: Minimalist Master Bathroom with Frameless Mountain Vista", "tag": "Luxury Bath"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (1).jpg", "title": "Cap d'Afrique: Oceanfront Living Lounge & Panoramic Glass Above Clifton Breakers", "tag": "Ocean Living"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (22).jpg", "title": "Cap d'Afrique: Panoramic Cliffside Vista Over Twelve Apostles & Camps Bay Coastline", "tag": "Twelve Apostles Vista"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (23).jpg", "title": "Cap d'Afrique: Oceanfront Swimming Pool & Sunbathing Lawn Perched on Clifton Rocks", "tag": "Cliffside Pool"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (32).jpg", "title": "Cap d'Afrique: Curvilinear Glass Salon & Curved White Sofa Facing Atlantic Ocean", "tag": "Curved Ocean Salon"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (37).jpg", "title": "Cap d'Afrique: Panoramic Sunset Lounge & Architectural Dining Pavilion", "tag": "Sunset Lounge"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (11).jpg", "title": "Cap d'Afrique: Outdoor Dining Terrace & Private Funicular Cliff Track", "tag": "Cliff Terrace"},
            {"file": r"Backup 2022-02\Trackers\Houses\SMH-Houses\Luxe\Luxe (Hero-Exterior-Cantilever).jpg", "title": "Lux Villa: Monumental Cantilevered Multi-Tier Architectural Facade & Driveway (Camps Bay)", "tag": "Architectural Facade"},
            {"file": r"Backup 2022-02\Trackers\Houses\SMH-Houses\Luxe\Luxe (Hero-Pool-Deck).jpg", "title": "Lux Villa: Oceanfront Infinity Lap Pool, Hardwood Sun Deck & Daybeds", "tag": "Infinity Pool Deck"},
            {"file": r"Backup 2022-02\Trackers\Houses\SMH-Houses\Luxe\Luxe (Hero-Twilight-Terrace).jpg", "title": "Lux Villa: Twilight Entertainment Terrace, Concrete Fireplace & Sunset Ocean Horizon", "tag": "Sunset Terrace"},
            {"file": r"Backup 2022-02\Trackers\Houses\SMH-Houses\Luxe\Luxe (5).jpg", "title": "Lux Villa: Floor-to-Ceiling Glass Living Pavilion with Panoramic Coastal Views", "tag": "Glass Pavilion"},
            {"file": r"Apartments\Woodside\604\604\Woodside-604 (1).jpg", "title": "Woodside Skyline Penthouse: Modern Urban Living with Panoramic City Bowl & Mountain Views", "tag": "City Penthouse"},
            {"file": r"Apartments\Woodside\604\604\Woodside-604 (5).jpg", "title": "Woodside Penthouse: Wrap-Around Glass Balcony & Table Mountain Skyline", "tag": "Skyline Balcony"}
        ]
    },

    # 03
    {
        "id": "heritage-cottages-character-streets",
        "num": "03",
        "title": "Heritage Cottages, Character Streets & Facades",
        "icon": "🏡",
        "doubles_as": "London Victorian Suburbs · San Francisco Painted Ladies · Historic Amsterdam · Colonial Caribbean Quarter",
        "hero_badge": "Verified Location",
        "area": "Salt River, Gardens, Bo-Kaap & De Waterkant, Cape Town",
        "tagline": "Charming Victorian worker cottages with decorative timber fretwork verandas, grand cast-iron broekie-lace facades, cobblestone alleyways, and vibrant historic quarter streetscapes.",
        "creative_synopsis": "For period drama, indie romance, or UK suburban doubling, Cape Town's architectural heritage is second to none. Culver and Chatham Streets feature single-storey Edwardian worker cottages with gabled roofs, picket fences, and leafy sidewalk canopies that easily double for London suburbs. Rosemount Avenue in Gardens offers grand two-storey Victorian mansions with ornate cast-iron lace balustrades. Bo-Kaap delivers cobblestone streets with brightly colored Cape Dutch facades, while De Waterkant provides intimate European pedestrian lanes.",
        "hero_image_file": r"Zen\House 2 Heritage Cottages (Culver & Chatham)\Culver St (1).jpg",
        "hero_image_title": "Culver Street Heritage Cottage: Edwardian Timber Fretwork Veranda & Picket Gate (Salt River)",
        "key_features": [
            "Culver & Chatham Streets: Authentic Victorian worker cottages with broekie lace verandas and iron roofs",
            "Rosemount Avenue (Gardens): Grand double-storey Victorian residence with cast-iron balconies and mountain framing",
            "Bo-Kaap: Steep historic cobblestone streets flanked by saturated pastel facades and 18th-century minarets",
            "De Waterkant: European-style pedestrian cobblestone alleyways, wrought-iron Juliet balconies, and cafe stoops",
            "Quiet residential streets with low traffic volumes ideal for period continuity and dialogue recording"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Office Street Permits (3–5 working days) · Community filming notifications",
            "power": "Domestic 16A/32A power supply + street tie-ins · Small quiet generator vehicle staging permitted",
            "parking": "Municipal street coning for 6–8 technical vans and lighting support trucks",
            "sound_curfew": "Suburban sound curfew 22:00 · Excellent acoustic properties on cul-de-sacs and side lanes"
        },
        "gallery": [
            {"file": r"Zen\House 2 Heritage Cottages (Culver & Chatham)\Culver St (1).jpg", "title": "Culver Street Cottage: Edwardian Facade with Ornate Timber Trim & Front Garden", "tag": "Hero Cottage"},
            {"file": r"Zen\House 2 Heritage Cottages (Culver & Chatham)\Culver St (2).jpg", "title": "Culver Street: Covered Wooden Veranda & Heritage Sash Windows", "tag": "Veranda"},
            {"file": r"Zen\House 2 Heritage Cottages (Culver & Chatham)\Culver St (3).jpg", "title": "Culver Street: Traditional Corrugated Iron Roof & Decorative Timber Fascia", "tag": "Heritage Trim"},
            {"file": r"Zen\House 2 Heritage Cottages (Culver & Chatham)\Chatham St (2).jpg", "title": "Chatham Street: Side-by-Side Victorian Worker Cottages with Cast-Iron Picket Gates", "tag": "Cottage Row"},
            {"file": r"Zen\Rosemount Ave-Gardens (4).jpg", "title": "Rosemount Avenue: Grand Two-Storey Victorian Mansion with Cast-Iron Balconies", "tag": "Victorian Villa"},
            {"file": r"CBD\Bo Kaap (1).jpg", "title": "Bo-Kaap Historic Terraces: Cobblestone Road & Vibrant Multicoloured Facades", "tag": "Cobblestones"},
            {"file": r"Takealot\Bo Kaap\Chiappini St (1).JPG", "title": "Bo-Kaap Chiappini Street: Wide Cobblestone Corridor with Vibrant Saturated Cape Malay Heritage Facades", "tag": "Chiappini St"},
            {"file": r"CBD\Bo Kaap-Pan.jpg", "title": "Bo-Kaap Panorama: Wide Historic District View Across Vibrant Historic Streets", "tag": "Panorama"},
            {"file": r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790836863220.jpg", "title": "De Waterkant: Historic Pastel Cottage Streetscape & Cobblestone Townhouse Curve", "tag": "Streetscape"},
            {"file": r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790836863224.jpg", "title": "De Waterkant: Private Timber Rooftop Deck Overlooking Heritage Cottages & Lodge", "tag": "Village Deck"},
            {"file": r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790836863228.jpg", "title": "De Waterkant: Mediterranean Blue Double-Storey Townhouse with Bougainvillea & Veranda", "tag": "Blue Townhouse"},
            {"file": r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790836863232.jpg", "title": "De Waterkant: Rooftop Terrace Cafe Pergola & Multi-Colored Village Facades", "tag": "Rooftop Terrace"}
        ]
    },

    # 04
    {
        "id": "forest-cabins-nature-retreats",
        "num": "04",
        "title": "Forest Cabins & Architectural Nature Retreats",
        "icon": "🌲",
        "doubles_as": "Pacific Northwest Timber Retreats · Scandinavian Eco-Lodges · Colorado Rockies Chalets · Forest Sanctuaries",
        "hero_badge": "Verified Location",
        "area": "Scarborough, Hout Bay Forest, Kommetjie & Noordhoek Canopies",
        "tagline": "Elevated dark timber stilt cabins with rock plunge pools, architectural glass treehouses in lush forest canopies, and rustic milkwood chalets.",
        "creative_synopsis": "When a screenplay calls for isolated architectural forest living or nature sanctuaries, this category delivers uncompromised authenticity. Blackwood Cabin in Scarborough sits elevated on steel stilts above a coastal valley, complete with a natural rock plunge pool and winding wooden boardwalks through eucalyptus groves. In the lush canopy of Hout Bay forest, Amara Moon provides an architectural timber-and-glass stilt retreat surrounded by indigenous foliage. Vicki Residence captures artistic mountainside timber architecture set against natural fynbos slopes, while Monkey Valley nestles weathered log cabins beneath ancient milkwood trees.",
        "hero_image_file": r"Zen\Blackwood Cabin\Blackwood Cabin (1).jpg",
        "hero_image_title": "Blackwood Cabin: Elevated Dark Timber Stilt Retreat & Rock Plunge Pool (Scarborough)",
        "key_features": [
            "Blackwood Cabin: Dark-stained timber cabin on stilts, wraparound deck, natural rock pool, and boardwalk",
            "Amara Moon: Architectural timber & glass stilt retreat situated in the lush canopy of Hout Bay forest (strictly forest canopy)",
            "Vicki Residence: Character mountainside retreat with warm natural timber architecture set against indigenous mountainside slopes",
            "Monkey Valley: Weathered log cabins nestled beneath ancient indigenous milkwood canopies in Noordhoek",
            "Boardwalk pathways, outdoor forest showers, and secluded nature sanctuary aesthetics"
        ],
        "specs": {
            "permitting": "Private Estate Filming Agreements (24–48 hr direct sign-off) · No municipal street red-tape",
            "power": "On-site domestic single-phase + mobile silenced generator tie-in · Off-grid solar battery backup available",
            "parking": "Secure private property vehicle parking for 4–8 technical vans and support trailers",
            "sound_curfew": "Zero ambient city noise · Pristine acoustic environments for 24/7 synchronized dialogue and sound capture"
        },
        "gallery": [
            {"file": r"Zen\Blackwood Cabin\Blackwood Cabin (1).jpg", "title": "Blackwood Cabin: Elevated Timber Stilt Architecture & Natural Rock Plunge Pool", "tag": "Hero Cabin"},
            {"file": r"Zen\Blackwood Cabin\Blackwood Cabin (2).jpg", "title": "Blackwood Cabin: Wraparound Timber Deck, Plunge Pool & Indigenous Fynbos Garden", "tag": "Deck & Pool"},
            {"file": r"Zen\Blackwood Cabin\Blackwood Cabin (3).jpg", "title": "Blackwood Cabin: Architectural Timber Boardwalk Winding Through Eucalyptus Trees", "tag": "Forest Boardwalk"},
            {"file": r"Zen\Blackwood Cabin\Blackwood Cabin (4).jpg", "title": "Blackwood Cabin: Minimalist Timber Living Pavilion & Mountain Valley Vista", "tag": "Cabin Interior"},
            {"file": r"Zen\Amara Moon (2).jpg", "title": "Amara Moon: Architectural Timber Stilt Retreat Elevated in Lush Hout Bay Forest Canopy", "tag": "Forest Retreat"},
            {"file": r"Zen\Amara Moon (4).jpg", "title": "Amara Moon: Glass Living Pavilion Surrounded by Indigenous Forest Foliage", "tag": "Treehouse"},
            {"file": r"Zen\Vicki (22).JPG", "title": "Vicki Residence: Architectural Timber Mountain Retreat & Natural Exterior Facade", "tag": "Mountain Retreat"},
            {"file": r"Zen\Monkey Valley.png", "title": "Monkey Valley: Rustic Log Chalet Canopy Nestled in Noordhoek Milkwood Trees", "tag": "Monkey Valley"}
        ]
    },

    # 05
    {
        "id": "natural-wilderness-geological",
        "num": "05",
        "title": "Natural Wilderness, Mountain Passes & Geological Formations",
        "icon": "⛰️",
        "doubles_as": "Sci-Fi Desert Alien Planets · Ancient Middle Eastern Canyons · Australian Outback · Alpine Rocky Ranges",
        "hero_badge": "Verified Location",
        "area": "Cederberg Wilderness, Drakenstein & Cape Mountain Passes",
        "tagline": "Monumental wind-carved sandstone arches, ancient rock corridors, soaring jagged mountain precipices, and pristine alpine wilderness.",
        "creative_synopsis": "The Western Cape wilderness provides otherworldly geological landscapes that double for sci-fi alien planets, ancient desert realms, or rugged frontiers. The Stadsaal Caves in the Matjiesrivier Nature Reserve feature colossal burnt-orange sandstone arches, honeycomb rock formations, and ancient corridors carved by wind over hundreds of millions of years. Nearby, Drakenstein and Cape mountain reserves offer sheer cliff faces, alpine passes, and indigenous fynbos wilderness.",
        "hero_image_file": r"Stadsaal Cave-Cederberg\wetransfer_matjiesrivier-nr-stadsal_2023-05-26_0732\Matjiesrivier NR - Stadsal (10).jpg",
        "hero_image_title": "Stadsaal Caves: Monumental Sandstone Rock Arches & Burnt-Orange Pillars (Cederberg)",
        "key_features": [
            "Stadsaal Caves: Colossal red/ochre sandstone arches, labyrinthine rock halls, and ancient caves",
            "Wind-carved amphitheaters with natural light shafts ideal for cinematic epic framing",
            "Sheer mountain escarpments and alpine passes with zero modern intrusions or telephone poles",
            "Drakenstein & Simonsberg sheer rock faces and sweeping valley panoramas",
            "360-degree horizon views with zero light pollution for celestial and night filming"
        ],
        "specs": {
            "permitting": "CapeNature Commercial Filming Permits (5–7 working days) · Environmental eco-monitor required",
            "power": "Off-grid location: Mobile silenced trailer generators and heavy-duty portable lithium power stations required",
            "parking": "Dedicated gravel staging areas for 4x4 vehicles, unit support bakkies, and camera grip trucks",
            "sound_curfew": "100% natural acoustic isolation · Zero commercial air traffic or road sound bleed"
        },
        "gallery": [
            {"file": r"Stadsaal Cave-Cederberg\wetransfer_matjiesrivier-nr-stadsal_2023-05-26_0732\Matjiesrivier NR - Stadsal (10).jpg", "title": "Stadsaal Caves: Monumental Sandstone Rock Arches & Burnt-Orange Pillars (Cederberg)", "tag": "Hero Arch"},
            {"file": r"Stadsaal Cave-Cederberg\wetransfer_matjiesrivier-nr-stadsal_2023-05-26_0732\Matjiesrivier NR - Stadsal (36).jpg", "title": "Stadsaal Caves: Wind-Carved Desert Sandstone Amphitheater & Otherworldly Formations", "tag": "Rock Amphitheater"},
            {"file": r"Stadsaal Cave-Cederberg\wetransfer_matjiesrivier-nr-stadsal_2023-05-26_0732\Matjiesrivier NR - Stadsal (50).jpg", "title": "Stadsaal Caves: Ancient Weathered Rock Corridors & Dramatic Natural Light Shafts", "tag": "Rock Corridor"},
            {"file": r"Mountains\Boschendal\Boschendal (10).jpg", "title": "Drakenstein Mountain Range: Monumental Sandstone Precipices & Pristine Valley Escarpment", "tag": "Mountain Face"},
            {"file": r"Mountains\Hottentots Holland-Stellenbosch\Hottentotts Holland (1).jpg", "title": "Simonsberg & Hottentots Holland: Monumental Alpine Ridge & Deep Valley Basin", "tag": "Alpine Skyline"},
            {"file": r"Mountains\MTO (8).jpg", "title": "MTO Mountain Reserve: High-Altitude Forestry Trail & Sweeping Valley Vista", "tag": "Mountain Trail"},
            {"file": r"08-Stadium\Lourensford\Lourensfor Prairie (2).jpg", "title": "Lourensford Estate Plains: Vast Prairie Grasslands Framed by Helderberg Mountain Amphitheater", "tag": "Lourensford Plains"},
            {"file": r"Mountains\20241218_151516.jpg", "title": "Rugged Mountain Corridor: Open Alpine Valley & Endless Natural Horizons", "tag": "Valley Basin"}
        ]
    },

    # 06
    {
        "id": "pristine-beaches-coastal-coves",
        "num": "06",
        "title": "Pristine Beaches & Coastal Coves",
        "icon": "🏖️",
        "doubles_as": "Mediterranean Coastline · Caribbean Sand Beaches · California Surf Breaks · Vintage Coastal Havens · Cannes & Malibu",
        "hero_badge": "Verified Location",
        "area": "Camps Bay, Llandudno, Noordhoek Long Beach, Clifton 4th, Muizenberg & St. James",
        "tagline": "Iconic palm-lined white sand crescents, secluded granite boulder coves, 8km untamed sand corridors, world-famous surf breaks, and historic tidal pools.",
        "creative_synopsis": "Cape Town's coastline provides legendary diversity for beach and ocean filming. Camps Bay Beach is the crown jewel of the Atlantic Seaboard—a wide white-sand crescent lined with palm trees and backed by the Twelve Apostles mountain peaks, doubling for Cannes, Miami, or Malibu. Nearby Llandudno is an exclusive, undeveloped sanctuary framed by colossal granite boulders and turquoise waters. Noordhoek Long Beach offers 8 uninterrupted kilometers of hard-packed sand and untamed surf. Muizenberg Beach delivers world-famous surf culture and historic brightly colored Victorian bathing boxes, while Clifton 4th provides sheltered blue waters and Dalebrook / St. James bring historic tidal sea pools.",
        "hero_image_file": r"Beaches\Camps Bay\Camps Bay Beach\Camps Bay Beach (1).jpg",
        "hero_image_title": "Camps Bay Beach: Wide Palm-Fringed White Sands Facing Twelve Apostles & Lion's Head",
        "key_features": [
            "Camps Bay Beach: Iconic white sand crescent, palm-lined promenade, and monumental Twelve Apostles backdrop",
            "Llandudno Beach: Exclusive secluded cove flanked by dramatic granite boulders and turquoise Atlantic swell",
            "Noordhoek Long Beach: 8km wide flat sand corridor with horse-riding access, coastal dunes, and Kakapo shipwreck",
            "Clifton 4th Beach: Sheltered turquoise water, giant polished granite boulders, and golden sunset horizons",
            "Muizenberg Beach & Surfers Corner: World-renowned gentle surf break and iconic Victorian bathing boxes",
            "Kogel Bay & Clarence Drive: Dramatic vertical mountain cliffs plunging into wild coastal surf",
            "Historic Tidal Pools: Dalebrook and St. James stone-walled sea pools with crashing surf spray"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Office & SANParks Coastal Permits (3–5 working days)",
            "power": "Mobile silenced generator trucks with beach matting · Portable battery quiet packs for water edge",
            "parking": "Hardstand beach car park staging for 15+ technical vehicles · 4x4 beach track access authorized",
            "sound_curfew": "Golden hour sunset calls recommended for Atlantic Seaboard filming · Natural ocean ambient sound"
        },
        "gallery": [
            {"file": r"Beaches\Camps Bay\Camps Bay Beach\Camps Bay Beach (1).jpg", "title": "Camps Bay Beach: Wide Palm-Fringed White Sands Facing Twelve Apostles & Lion's Head", "tag": "Hero Beach"},
            {"file": r"Beaches\Camps Bay\Camps Bay Beach\Camps Bay Beach (10).jpg", "title": "Camps Bay Beach: Golden Sunset Swell, Atlantic Surf Line & Beachfront Promenade", "tag": "Sunset Surf"},
            {"file": r"Beaches\Rocky Beaches\Beaches\Llandudno Beach\Llandudno (1).jpg", "title": "Llandudno Beach: Secluded Granite Boulder Cove & Turquoise Atlantic Waves", "tag": "Granite Cove"},
            {"file": r"Beaches\Rocky Beaches\Beaches\Llandudno Beach\Llandudno (10).jpg", "title": "Llandudno Beach: Sweeping Coastal Headland, Fine White Sand & Untamed Ocean Swell", "tag": "Atlantic Swell"},
            {"file": r"Beaches\Noordhoek\Noordhoek Beach (1).jpg", "title": "Noordhoek Long Beach: Wide 8km Untamed White Sand Corridor & Rolling Surf", "tag": "8km Sand Corridor"},
            {"file": r"Beaches\Noordhoek\Noordhoek Beach (2).jpg", "title": "Noordhoek Dunes: Fine Sand Dunes & Distant Chapman's Peak Mountain Headland", "tag": "Coastal Dunes"},
            {"file": r"Beaches\Clifton\Clifton 4th (1).jpg", "title": "Clifton 4th Beach: Sheltered Turquoise Water, Granite Boulders & Golden Sunset", "tag": "Clifton 4th"},
            {"file": r"Beaches\Clifton\Clifton-4th\Clifton 4th (10).jpg", "title": "Clifton Beach: Pristine White Sand Cove Framed by Dramatic Coastal Headlands", "tag": "Sheltered Cove"},
            {"file": r"Beaches\Muizenberg\Muizenberg (10).jpg", "title": "Muizenberg Beach: World-Famous Surfers Corner & Expansive False Bay Sandflat", "tag": "Surfers Corner"},
            {"file": r"Beaches\Muizenberg\Muizenberg (11).jpg", "title": "Muizenberg: Vibrant Iconic Multi-Coloured Victorian Bathing Boxes & Longboard Waves", "tag": "Bathing Boxes"},
            {"file": r"Beaches\Kogel Bay\Kogel Bay (10).jpg", "title": "Kogel Bay / Caves: Sheer Sandstone Mountain Precipices Plunging into Wild Surf", "tag": "Wild Mountain Coast"},
            {"file": r"Beaches\Dalebrook Tidal Pool\Dalebrook Tidal Pool (1).jpg", "title": "Dalebrook Tidal Pool: Historic Stone-Walled Ocean Swimming Pool & False Bay Horizon", "tag": "Tidal Pool"},
            {"file": r"Beaches\St. James Tidal Pool\St. James Beach (1).jpg", "title": "St. James Tidal Pool: Ocean Splashback, Natural Stone Swimming Wall & False Bay Horizon", "tag": "Historic Sea Pool"}
        ]
    },

    # 07
    {
        "id": "working-harbours-maritime-basins",
        "num": "07",
        "title": "Working Harbours, Maritime Basins & Waterfront Quays",
        "icon": "⚓",
        "doubles_as": "European Maritime Ports · New England Working Docks · Cornwall / Brittany Wharves · Mediterranean Yacht Basins",
        "hero_badge": "Verified Location",
        "area": "V&A Waterfront, Victoria & Alfred Basins & Industrial Wharves",
        "tagline": "Operational historic maritime working basins with red-brick Victorian clock towers, active swing bridges, drydocks, industrial tugboats, and superyacht quaysides.",
        "creative_synopsis": "The historic Victoria & Alfred Waterfront offers an operational working harbour basin set against the iconic backdrop of Table Mountain. With active drydocks, commercial fishing wharves, industrial tugboats, historic swing bridges, and the distinctive 1882 Victorian Clock Tower, it provides an authentic working port environment. State-of-the-art superyacht berths sit alongside heritage stone quays, allowing seamless doubling for maritime thrillers, luxury lifestyle, or industrial nautical dramas.",
        "hero_image_file": r"V&A Waterfront\V&A Waterfront (2).jpg",
        "hero_image_title": "V&A Waterfront Basin: Historic Red-Brick Clock Tower, Operational Tugboats & Table Mountain",
        "key_features": [
            "V&A Waterfront Historic Basin: Active commercial harbour with working tugs, drydocks, and Table Mountain framing",
            "1882 Victorian Clock Tower: Gothic-Victorian red-brick landmark overlooking swing bridge and quays",
            "Pedestrian Swing Bridge: Operational revolving steel swing bridge across the inner harbour channel",
            "Working Quaysides: Heavy bollards, industrial ship repair berths, and luxury superyacht marinas",
            "24/7 filming access with integrated maritime security and vessel coordination"
        ],
        "specs": {
            "permitting": "V&A Waterfront Film Office Direct Approval (3–5 working days) · Transnet National Ports Authority coordination",
            "power": "3-Phase 63A/125A industrial shore power tie-ins along all main quaysides",
            "parking": "Dedicated underground and hardstand staging accommodating 25+ technical vehicles and lighting cranes",
            "sound_curfew": "24/7 operational harbour permits · Controlled commercial noise environment"
        },
        "gallery": [
            {"file": r"V&A Waterfront\V&A Waterfront (2).jpg", "title": "V&A Waterfront Basin: Historic Clock Tower, Working Tugs & Unobstructed Table Mountain", "tag": "Hero Basin"},
            {"file": r"V&A Waterfront\V&A Waterfront (1).jpg", "title": "V&A Waterfront Basin: Wide Panoramic View Across Working Harbour Waters & Table Mountain", "tag": "Wide Basin"},
            {"file": r"V&A Waterfront\V&A Waterfront (4).jpg", "title": "V&A Waterfront: Expansive Water Basin, Working Docks & Mountain Skyline", "tag": "Waterfront Vista"},
            {"file": r"V&A Waterfront\V&A Waterfront (3).jpg", "title": "V&A Waterfront: Swing Bridge, Modern Quayside & Maritime Ship Mooring", "tag": "Working Quayside"},
            {"file": r"V&A Waterfront\V&A Waterfront (32).jpg", "title": "V&A Waterfront: Operational Tugboats & Industrial Quayside Logistics", "tag": "Tugboats"},
            {"file": r"V&A Waterfront\V&A Waterfront (14).jpg", "title": "V&A Waterfront: Maritime Boardwalk, Granite Quays & Table Mountain Vista", "tag": "Boardwalk"}
        ]
    },

    # 08
    {
        "id": "urban-metropolis-cbd",
        "num": "08",
        "title": "Urban Metropolis, Commercial CBD & Civic Skylines",
        "icon": "🏙️",
        "doubles_as": "Chicago / New York Financial District · Modern Los Angeles Downtown · Tokyo Corporate Hub · European Modern Capitals",
        "hero_badge": "Verified Location",
        "area": "Cape Town Financial District, Foreshore & Heerengracht",
        "tagline": "Sleek glass-curtain skyscrapers, brutalist concrete plazas, dramatic elevated freeway flyovers, and rooftop skyline vistas.",
        "creative_synopsis": "Cape Town's Central Business District is an established global production staple, frequently doubling for North American downtowns. Streets like Corporation, Darling, and Heerengracht present a mix of gleaming glass commercial towers, neoclassical civic architecture, and public plazas. The unfinished elevated freeway flyovers on the Foreshore offer an unparalleled location for high-speed car chases, stunt rigging, and post-apocalyptic urban scenes. Expansive commercial rooftops offer 360-degree mountain skylines.",
        "hero_image_file": r"CBD\Yours\Christiaan Barnard-FWDK BLVD (1).jpg",
        "hero_image_title": "Christiaan Barnard & FW de Klerk Boulevard: Wide Commercial Metropolis Avenue, Skyscrapers & Mountain Skyline",
        "key_features": [
            "Financial District Canyons: Glass curtain-wall high-rises and busy multi-lane downtown corridors",
            "Elevated Foreshore Freeway Flyovers: Dramatic suspended concrete highways for vehicle chases and stunt rigging",
            "City Bowl Commercial Plazas: Brutalist civic squares, polished granite steps, and architectural voids",
            "City Bowl Commercial Rooftops: Expansive tar roofs with HVAC ducting and 360-degree mountain skylines",
            "Pre-cleared municipal road closure protocols for weekend street stunts and full block control"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Office CBD Street Permits (5 working days) · Weekend full-closure authorizations",
            "power": "Direct building tie-ins (3-phase 63A/100A) · Street-side generator truck parking bays",
            "parking": "Designated municipal hardstands, underground parking garages, and multi-vehicle technical basecamps",
            "sound_curfew": "Weekend filming allows high-SPL vehicle tracking and blank-firing stunt audio under police supervision"
        },
        "gallery": [
            {"file": r"CBD\Yours\Christiaan Barnard-FWDK BLVD (1).jpg", "title": "Christiaan Barnard Boulevard: Wide High-Rise Commercial Avenue & Mountain Skyline", "tag": "Hero CBD Wide"},
            {"file": r"CBD\Yours\Lower Heerengraght (1).jpg", "title": "Lower Heerengracht: Wide Commercial Boulevard Flanked by High-Rise Glass Towers", "tag": "Heerengracht Wide"},
            {"file": r"CBD\Corporation St (2).jpg", "title": "Corporation Street: Clean Commercial Streetscape with Modernist Architectural Vistas", "tag": "Street Canyon"},
            {"file": r"CBD\Darling St (1).JPG", "title": "Darling Street: Neoclassical Commercial Facades & Metropolitan City Traffic", "tag": "Darling St"},
            {"file": r"Highway\Cut Off Highway (1).jpg", "title": "Foreshore Elevated Freeway: Dramatic Suspended Concrete Overpass for Stunt Driving", "tag": "Freeway Flyover"},
            {"file": r"Highway\Cut Off Highway (10).jpg", "title": "Foreshore Flyover: Unfinished Elevated Highway Suspended Above Downtown Skyline", "tag": "Stunt Overpass"},
            {"file": r"Highway\Cut Off Highway (14).jpg", "title": "Foreshore Flyover: Aerial Highway Curve with Panoramic City Bowl Backdrop", "tag": "Highway Curve"},
            {"file": r"Rooftops\20231113_170008.jpg", "title": "CBD Skyline Rooftop: 360-Degree Panorama of Skyscrapers & Table Mountain", "tag": "Skyline Rooftop"},
            {"file": r"08-Glencor\Foreshore\Harbour Arch (1).jpg", "title": "Harbour Arch Precinct: Wide Urban Skyline, Multi-Lane Gateway & Glass High-Rises", "tag": "Harbour Arch Wide"},
            {"file": r"08-Glencor\Foreshore\Harbour Arch (2).jpg", "title": "Harbour Arch: Panoramic Glass High-Rise Boulevard & Modernist Architecture", "tag": "Harbour Arch Panorama"}
        ]
    },

    # 09
    {
        "id": "soundstages-cycloramas-studios",
        "num": "09",
        "title": "Soundstages, Cycloramas & Scoring Studios",
        "icon": "🎬",
        "doubles_as": "Hollywood Soundstages · London Pinewood / Leavesden Stages · Abbey Road / Sunset Sound Scoring Environments",
        "hero_badge": "Verified Location",
        "area": "Paarden Eiland, Salt River, Woodstock & Hout Bay",
        "tagline": "Acoustically isolated film soundstages with overhead lighting grids, infinity curve cycloramas, multi-pane daylight rehearsal lofts, and world-class live recording rooms.",
        "creative_synopsis": "Cape Town's studio ecosystem supports high-end international features and commercials with first-tier studio infrastructure. Daylight Rehearsal Studio features polished concrete floors, daylight bays, and an infinity cyclorama. Studio 107 provides premier acoustic tracking and green-screen facilities with an overhead rigging grid. Studio 1 at Suite Spot Studios offers high-volume motion control cycloramas, while historic converted church halls and scoring studios provide pristine acoustic reverberation.",
        "hero_image_file": r"Zen\Daylight Rehearsal Studio (1).jpg",
        "hero_image_title": "Daylight Rehearsal Studio: White Cyclorama, Exposed Concrete Beams & Sunlit Window Bays",
        "key_features": [
            "Daylight Rehearsal Studio: Polished concrete floor, white cyclorama cove, exposed ceiling trusses, and sunlit bays",
            "Studio 107: Soundstage with acoustic ceiling baffles, overhead pipe grid, mobile green-screen wall, and control booth",
            "Studio 1 at Suite Spot Studios: High-volume commercial photo and motion cyclorama stage with roll-in vehicle access",
            "Milestone Studios: Dedicated multi-room acoustic scoring and live music facility with grand pianos",
            "Roodebloem Converted Church Hall: Historic vaulted timber ceilings, arched stained-glass windows, and wooden floors"
        ],
        "specs": {
            "permitting": "Private Studio Hire Agreements (Immediate booking sign-off) · Zero municipal red tape",
            "power": "3-Phase 125A/250A camlock power drops on-site · Dedicated sound-isolated generator connections",
            "parking": "Private secure studio lots for production trucks, grip trailers, catering, and honeywagons",
            "sound_curfew": "24/7 filming and high-volume sound recording · Fully acoustically treated facilities"
        },
        "gallery": [
            {"file": r"Zen\Daylight Rehearsal Studio (1).jpg", "title": "Daylight Rehearsal Studio: White Infinity Cyclorama, Industrial Beams & Sunlit Bays", "tag": "Hero Rehearsal"},
            {"file": r"Zen\Daylight Rehearsal Studio (2).jpg", "title": "Daylight Rehearsal Studio: Wide Polished Screed Floor & Large Multi-Pane Daylight Windows", "tag": "Daylight Studio"},
            {"file": r"Zen\Studio 107 (Acoustic Studio & Green Screen).jpg", "title": "Studio 107: Premier Film Soundstage, Overhead Rigging Grid & Mobile Green Screen Wall", "tag": "Soundstage & Green Screen"},
            {"file": r"Zen\Studio 107 (6).jpg", "title": "Studio 107: Acoustic Tracking Studio, Floating Timber Floors & Control Booth Glass", "tag": "Live Tracking Room"},
            {"file": r"Zen\Suite Spot Studios (3).jpg", "title": "Suite Spot Studios: High-Volume Commercial Photo & Motion Cyclorama Stage", "tag": "Suite Spot Studio"},
            {"file": r"Zen\studio1_02.jpg", "title": "Studio 1 at Suite Spot Studios: Commercial Cyclorama Stage & Drive-In Access", "tag": "Studio 1"},
            {"file": r"Zen\Milstone Studios (3).jpg", "title": "Milestone Studios: Dedicated Multi-Room Acoustic Scoring & Live Music Facility", "tag": "Scoring Studio"},
            {"file": r"Zen\Plug Studio (12).jpg", "title": "Plug Music Studio: Intimate Band Rehearsal & Live Tracking Space", "tag": "Rehearsal Space"},
            {"file": r"Zen\Roodebloem Studios (2).jpg", "title": "Roodebloem Historic Church Hall: Vaulted Timber Ceilings, Wooden Floors & Arched Windows", "tag": "Historic Studio"}
        ]
    },

    # 10
    {
        "id": "nightclubs-lounges-beach-clubs",
        "num": "10",
        "title": "Nightclubs, Cocktail Lounges & Beach Clubs",
        "icon": "🍸",
        "doubles_as": "Mayfair London Cocktail Lounges · Berlin Underground Clubs · Ibiza / Miami Sunset Beach Clubs · New York Speakeasies",
        "hero_badge": "Verified Location",
        "area": "Harringtons (East City), Camps Bay Strip & Waterfront",
        "tagline": "Opulent mahogany cocktail lounges with crystal chandeliers, curved velvet booths, underground techno dancefloors, and oceanfront sunset beach clubs.",
        "creative_synopsis": "Cape Town's nightlife scene offers exceptional variety. Harringtons Cocktail Lounge in the East City represents classic cocktail bar aesthetics, featuring a dark mahogany bar counter, illuminated bottle displays, velvet booths, and crystal chandeliers. Cafe Caprice on the Camps Bay promenade delivers world-famous Mediterranean beach club energy with palm trees and sunset vistas. Grand Africa Beach Bar and Club Destiny provide cavernous multi-level dancefloors and private beach club settings.",
        "hero_image_file": r"Zen\Harringtons Cocktail Lounge\Harringtons (3).jpg",
        "hero_image_title": "Harringtons Cocktail Lounge: Dark Mahogany Bar Counter, Glowing Bottle Displays & Crystal Chandeliers",
        "key_features": [
            "Harringtons (East City): Dark mahogany wood-paneled bar counter, glowing back-lit bottles, and crystal chandeliers",
            "Harringtons Lounge: Plush curved emerald velvet booths, brass cocktail tables, and vintage botanical wallpaper",
            "Cafe Caprice (Camps Bay): Premier oceanfront sunset beach club lounge with outdoor curbside seating",
            "Club Destiny & Halo: Multi-tier underground nightclub venues with high-power moving beam rigs and DJ booths",
            "Grand Africa Beach Bar: Private oceanfront sand terrace, wooden daybeds, and private harbour setting"
        ],
        "specs": {
            "permitting": "Private Commercial Venue Filming Agreements (24–48 hr direct sign-off)",
            "power": "3-Phase 63A/100A venue power drops · Dedicated stage power for heavy lighting rigs",
            "parking": "Reserved street parking bays and private off-street loading docks for grip trucks",
            "sound_curfew": "Full soundproofing allows high-SPL music playback and nighttime shoot schedules 24/7"
        },
        "gallery": [
            {"file": r"Zen\Harringtons Cocktail Lounge\Harringtons (3).jpg", "title": "Harringtons Bar: Dark Mahogany Counter, Backlit Bottle Display & Crystal Chandeliers", "tag": "Hero Bar Match"},
            {"file": r"Zen\Harringtons Cocktail Lounge\Harringtons (1).jpg", "title": "Harringtons: Curved Emerald Velvet Banquettes & Vintage Botanical Wallpaper", "tag": "Velvet Booths"},
            {"file": r"Zen\Harringtons Cocktail Lounge\Harringtons (2).jpg", "title": "Harringtons: Intimate Velvet Cocktail Lounge with Ornate Ceiling Cornicing", "tag": "Cocktail Lounge"},
            {"file": r"Zen\Harringtons Cocktail Lounge\Harringtons (4).jpg", "title": "Harringtons: Ambient Gold-Lit Dining Room & Architectural Cornicing", "tag": "Dining Room"},
            {"file": r"Zen\Cafe Caprice\Cafe Caprice (1).jpg", "title": "Cafe Caprice: Premier Sunset Beach Club Bar Facing Camps Bay Ocean Horizon", "tag": "Beach Club Bar"},
            {"file": r"Zen\Cafe Caprice\Cafe Caprice (2).jpg", "title": "Cafe Caprice: Outdoor Cocktail Terrace, Palm Trees & Atlantic Ocean Waves", "tag": "Sunset Terrace"},
            {"file": r"Zen\Club Destiny (1).JPG", "title": "Club Destiny: Expansive Multi-Level Nightclub Dancefloor & Ambient Blue Rigging", "tag": "Dancefloor"},
            {"file": r"Zen\Club Halo (8).jpg", "title": "Club Halo: High-Tech Underground Electronic Dance Music Venue & Stage", "tag": "Techno Club"},
            {"file": r"Zen\Hexagon (4).jpg", "title": "Hexagon: Futuristic Geometric Nightclub Lighting Array & Dancefloor", "tag": "Geometric Club"},
            {"file": r"Bars & Clubs\Grand Cafe\Grand Africa Cafe & Beach Bar -11.jpg", "title": "Grand Africa Beach Club: Private Oceanfront Sand Dining & Sunset Deck", "tag": "Private Beach Club"}
        ]
    },

    # 11
    {
        "id": "theatrical-dining-live-music",
        "num": "11",
        "title": "Theatrical Dining, Live Music & Courtyards",
        "icon": "🎭",
        "doubles_as": "West End Cabaret Theatres · Greenwich Village Jazz Clubs · Parisian Outdoor Bistro Courtyards",
        "hero_badge": "Verified Location",
        "area": "StarDust Theatrical Dining (Woodstock) & Historic Courtyards",
        "tagline": "Two-tier cabaret dining halls with illuminated stage backdrops, grand pianos, and historic brick courtyards with multi-pane factory windows.",
        "creative_synopsis": "This category captures the theatrical dining and live musical performance spaces of the Western Cape. StarDust Theatrical Dining in Woodstock features a wide timber dining floor, raised musical stage, grand piano, and illuminated 'StarDust' marquee. For daytime dining, shaded brick courtyards with industrial multi-pane factory windows (`IMG_5253.JPG`) offer warm natural light for cafe dialogue scenes.",
        "hero_image_file": r"Zen\Stardust (12).jpg",
        "hero_image_title": "StarDust Theatrical Dining: Raised Musical Stage, Grand Piano, Wide Timber Floor & Illuminated Emblem",
        "key_features": [
            "StarDust Theatrical Dining: Wide timber floor, raised stage, grand piano, and glowing illuminated backdrop",
            "StarDust Mezzanine: Two-tier dining gallery with brass railings, velvet dining chairs, and stage line-of-sight",
            "Factory Courtyard (`IMG_5253.JPG`): Multi-pane industrial steel windows, weathered brick walls, and shaded picnic dining",
            "Full theatrical stage lighting grid, DMX control, and live multi-track audio recording tie-ins",
            "Acoustically isolated interior for dialogue and musical synchronization"
        ],
        "specs": {
            "permitting": "Private Commercial Venue Contracts (24–48 hr direct sign-off)",
            "power": "3-Phase 63A/100A venue power drops + dedicated audio isolation circuits",
            "parking": "Private off-street vehicle loading docks + secure street staging for unit trucks",
            "sound_curfew": "Full sound isolation at StarDust allows high-volume live performance recording 24/7"
        },
        "gallery": [
            {"file": r"Zen\Stardust (12).jpg", "title": "StarDust Theatrical Dining: Wide Timber Dining Floor, Raised Stage & Grand Piano", "tag": "Hero StarDust"},
            {"file": r"Zen\Stardust (3).jpg", "title": "StarDust: Elevated Mezzanine Dining Gallery Overlooking Main Performance Floor", "tag": "Mezzanine"},
            {"file": r"Zen\Stardust (6).jpg", "title": "StarDust: Close Stage Framing with Velvet Drapes & Professional Stage Lighting", "tag": "Performance Stage"},
            {"file": r"Zen\Stardust (8).jpg", "title": "StarDust: Intimate Dining Booths Flanking the Central Timber Dancefloor", "tag": "Dining Booths"},
            {"file": r"Zen\IMG_5253.JPG", "title": "Courtyard Cafe: Weathered Red Brick Facade, Multi-Pane Windows & Shaded Benches", "tag": "Brick Courtyard"}
        ]
    },

    # 12
    {
        "id": "wine-country-historic-estates",
        "num": "12",
        "title": "Wine Country, Historic Estates & Farmland",
        "icon": "🍇",
        "doubles_as": "Tuscan Vineyards · French Bordeaux & Provence Châteaux · Napa Valley Wine Country · Old World European Orchards",
        "hero_badge": "Verified Location",
        "area": "Stellenbosch, Helshoogte Pass & Elgin Valley",
        "tagline": "Classic Cape Dutch gabled manors, rolling hillside vineyards reflecting mountain lakes, modernist glass winery architecture, and historic farmsteads.",
        "creative_synopsis": "The Cape Winelands deliver quintessential Old World European doubling within 45 minutes of Cape Town. Asara Wine Estate in Stellenbosch features rolling vineyard hills, tranquil private lakes reflecting the mountains, and historic Cape Dutch white gabled manor houses. Across the Helshoogte Pass, Tokara Wine Estate delivers world-renowned contemporary architecture—cantilevered glass and sandstone pavilions perched above dramatic terraced vineyards and olive groves overlooking the Simonsberg. Paul Cluver in Elgin and Kersefontein farmstead add historic farmsteads and countryside horizons.",
        "hero_image_file": r"Farms\Wine Farms\Asara\Asara Wines (1).jpg",
        "hero_image_title": "Asara Wine Estate: Rolling Vineyards, Private Lake Reflection & Cape Dutch Manor (Stellenbosch)",
        "key_features": [
            "Asara Wine Estate: Manicured vineyards, mountain-reflecting lakes, and 18th-century Cape Dutch architecture",
            "Tokara Wine Estate (Helshoogte Pass): Award-winning modern glass and stone architecture, terraced vineyards, and olive groves",
            "Paul Cluver Wine Estate: Cool-climate apple orchards, pine tree windbreaks, and rustic amphitheaters",
            "Kersefontein Historic Farmstead: 18th-century Cape Dutch stables, whitewashed gables, and sprawling pastures",
            "Expansive private estate lands allowing large-scale unit basecamps, drone flights, and crane rigs"
        ],
        "specs": {
            "permitting": "Private Estate Filming Contracts (24–48 hr direct sign-off) · Unrestricted private air-rights for drones",
            "power": "3-Phase 63A/100A winery cellar docks · Mobile generator staging in cellar service courtyards",
            "parking": "Extensive paved and gravel parking lots accommodating full feature film circus and honeywagons",
            "sound_curfew": "Zero municipal curfew on private agricultural land · 24/7 filming and night lighting permitted"
        },
        "gallery": [
            {"file": r"Farms\Wine Farms\Asara\Asara Wines (1).jpg", "title": "Asara Wine Estate: Manicured Vineyards, Calm Lake Reflection & Mountain Backdrop", "tag": "Hero Estate"},
            {"file": r"Farms\Wine Farms\Asara\Asara Wines (2).jpg", "title": "Asara Wine Estate: Classic Cape Dutch White Gabled Manor & Bell Tower", "tag": "Cape Dutch Manor"},
            {"file": r"Farms\Wine Farms\Asara\Asara Wines (11).jpg", "title": "Asara: Tranquil Private Dam Reflecting Simonsberg Mountain Peak", "tag": "Estate Lake"},
            {"file": r"Farms\Wine Farms\Asara\Asara Wines (12).jpg", "title": "Asara: Rolling Hillside Vineyards & Panoramic Simonsberg Mountain Vista", "tag": "Vineyard Vista"},
            {"file": r"Farms\Paul Cluver\Paul Cluver (1).jpg", "title": "Paul Cluver Estate: Cool-Climate Vineyards, Pine Tree Belts & Mountain Dams", "tag": "Elgin Orchards"},
            {"file": r"Farms\Paul Cluver\Paul Cluver (10).jpg", "title": "Paul Cluver: Timber Forest Amphitheater & Shaded Estate Lawns", "tag": "Forest Amphitheater"},
            {"file": r"Farms\Wine Farms\Thelema\Thelema\Tokara (1).jpg", "title": "Tokara Wine Estate: Contemporary Sandstone Winery & Terraced Helshoogte Vineyards", "tag": "Tokara Hero"},
            {"file": r"Farms\Wine Farms\Thelema\Thelema\Tokara (2).jpg", "title": "Tokara: Terraced Olive Groves & Panoramic Simonsberg Mountain Vista", "tag": "Olive Groves"},
            {"file": r"Farms\Wine Farms\Thelema\Thelema\Tokara (4).jpg", "title": "Tokara: Modernist Glass Pavilion Overlooking Geometric Vineyard Rows", "tag": "Glass Pavilion"},
            {"file": r"Farms\Wine Farms\Thelema\Thelema\Tokara (7).jpg", "title": "Tokara: Helshoogte Valley Sweeping Vineyard Horizon & Mountain Amphitheatre", "tag": "Helshoogte Pass"},
            {"file": r"Farms\Wine Farms\Thelema\Thelema\Tokara (10).jpg", "title": "Tokara: High-Altitude Vineyard Ridge Facing Simonsberg Peak", "tag": "Vineyard Ridge"},
            {"file": r"Farms\Wine Farms\Thelema\Thelema\Tokara (11).jpg", "title": "Tokara: Golden Hour Shadows Across Vineyard Slopes & Cellar Terraces", "tag": "Golden Hour"},
            {"file": r"Farms\Kersefontein\WhatsApp Image 2026-08-06 at 13.50.13.jpeg", "title": "Kersefontein Farmstead: 18th-Century Cape Dutch Historic Manor House & Gables", "tag": "Kersefontein Manor"},
            {"file": r"Farms\Kersefontein\WhatsApp Image 2026-08-06 at 13.50.14.jpeg", "title": "Kersefontein: Historic White Stables, Farm Courtyard & Open Agricultural Plains", "tag": "Historic Stables"}
        ]
    },

    # 13
    {
        "id": "airports-aviation-transport-terminals",
        "num": "13",
        "title": "Airports, Aviation & Major Transport Terminals",
        "icon": "✈️",
        "doubles_as": "International Commercial Airports · Private Rural Airfields & Smuggling Airstrips · Luxury Cruise Liner Terminals · Civic Transit Hubs",
        "hero_badge": "Verified Location",
        "area": "Arrieskraal Airport, Stellair Airfield, CTI Airport, Passenger Terminal & CTICC",
        "tagline": "Private rural mountain valley airstrips and aircraft hangars, country airfields, commercial airport concourses, architectural cruise terminals, and soaring convention atriums.",
        "creative_synopsis": "This dedicated aviation and major transit category offers remarkable operational diversity. Arrieskraal and Stellair (Stellenbosch Flying Club) feature private rural and country mountain valley airstrips complete with operational aircraft hangars, flight lines, and open runway corridors—ideal for espionage, action stunts, and private charter sequences. Cape Town International Airport (CTI) provides authentic commercial airline terminals, baggage concourses, and tarmac aprons. The Port of Cape Town Passenger Terminal offers architectural cruise departure halls and glass gangways, while the CTICC delivers multi-level interior transit atriums and modern exhibition concourses.",
        "hero_image_file": r"Husqvarna\Farms\Arrieskraal (11).jpg",
        "hero_image_title": "Arrieskraal Airport: Private Rural Valley Airstrip, Aircraft Hangars & Mountain Runway",
        "key_features": [
            "Arrieskraal Airport & Stellair Airfield: Private country runways, operational aircraft hangars, and unobstructed mountain valley approaches",
            "Cape Town International Airport (CTI): Commercial passenger departure halls, check-in concourses, and tarmac gates",
            "Cape Town Cruise Passenger Terminal: Modernist curved rooflines, multi-level curbside drop-offs, and boarding gangways",
            "CTICC Interior Transit Hub: Soaring multi-storey glass exhibition concourses, escalators, and subterranean logistics docks",
            "Full operational coordination with aviation authorities (SACAA) and airfield operators for runway vehicle tracking"
        ],
        "specs": {
            "permitting": "Airports Company SA (ACSA) Commercial Permits · Transnet National Ports Authority · Private Airfield Owner contracts",
            "power": "3-Phase 125A industrial tie-ins at CTICC & Passenger Terminal · Mobile generator sets for Arrieskraal & Stellair airfields",
            "parking": "Expansive aircraft apron staging, multi-deck terminal parking garages, and private runway hardstands",
            "sound_curfew": "24/7 filming protocols at Arrieskraal & Stellair private airfields · Scheduled night filming at terminals"
        },
        "gallery": [
            {"file": r"Husqvarna\Farms\Arrieskraal (11).jpg", "title": "Arrieskraal Airport: Private Rural Valley Airstrip, Hangars & Mountain Runway", "tag": "Hero Airstrip"},
            {"file": r"Husqvarna\Farms\Arrieskraal (13).jpg", "title": "Arrieskraal Airport: Mountain Valley Runway Corridor & Open Tarmac Approach", "tag": "Valley Runway"},
            {"file": r"Husqvarna\Farms\Arrieskraal (3).jpg", "title": "Arrieskraal: Operational Airfield Hangars & Aircraft Staging Apron", "tag": "Aircraft Hangars"},
            {"file": r"Husqvarna\Farms\Arrieskraal (14).jpg", "title": "Arrieskraal Airport: Mountain Valley Airstrip Approach & Country Aviation Infrastructure", "tag": "Runway Corridor"},
            {"file": r"Backup 2022-02\Allie's Journey\Franschoek\Barns\Kromme River\Arrieskraal (2).jpg", "title": "Arrieskraal: Airstrip Horizon Facing Majestic Mountain Backdrops", "tag": "Runway Vista"},
            {"file": r"Backup 2022-02\Love Island\Stellair (1).jpg", "title": "Stellair Airfield: Private Country Runway Tarmac & Stellenbosch Mountain Horizon", "tag": "Stellair Runway"},
            {"file": r"Backup 2022-02\Love Island\Stellair (2).jpg", "title": "Stellair Airfield: Country Airfield Aircraft Hangars & Grass Flight Line", "tag": "Stellair Hangars"},
            {"file": r"Film AD\Romcom\Bachelor Party Getaway\Airport\CT Airport (2).JPG", "title": "Cape Town International Airport: Commercial Jet Tarmac & Passenger Boarding Gates", "tag": "Commercial Tarmac"},
            {"file": r"Film AD\Romcom\Bachelor Party Getaway\Airport\CT Airport (3).JPG", "title": "CTI Airport: Modernist Terminal Exterior, Departure Concourse & Curbside Drop-Off", "tag": "Airport Terminal"},
            {"file": r"Film AD\Romcom\Bachelor Party Getaway\Airport\CT Airport (4).JPG", "title": "CTI Airport: High-Ceiling International Departures Hall & Security Gates", "tag": "Departures Concourse"},
            {"file": r"Backup 2022-02\Trackers\CT Passenger Terminal\CT Passenger Terminal (1).jpg", "title": "Cape Town Passenger Terminal: Modern Maritime Cruise Terminal & Table Mountain Backdrop", "tag": "Passenger Terminal"},
            {"file": r"Backup 2022-02\Trackers\CT Passenger Terminal\CT Passenger Terminal (10).jpg", "title": "Passenger Terminal: Multi-Level Passenger Drop-Off Concourse & Glass Curtain Walls", "tag": "Terminal Concourse"},
            {"file": r"Backup 2022-02\Trackers\CT Passenger Terminal\CT Passenger Terminal (11).jpg", "title": "Passenger Terminal: Elevated Boarding Gangways & Quayside Ship Berths", "tag": "Boarding Gangway"},
            {"file": r"CTICC\CTICC 1 (10).jpg", "title": "CTICC: Multi-Storey Escalator Atrium, Glass Skybridges & Modernist Stone Floors", "tag": "Skybridge Atrium"},
            {"file": r"08-Glencor\CTICC-2\CTICC-2 (1).jpg", "title": "CTICC 2: Contemporary Curved Glass Facade & Exhibition Hall Entrance", "tag": "CTICC 2 Entrance"},
            {"file": r"08-Glencor\CTICC-2\CTICC-2 (10).jpg", "title": "CTICC 2: High-Volume Interior Conference Concourse & Polished Granite Walkways", "tag": "Interior Concourse"}
        ]
    },

    # 14
    {
        "id": "civic-institutions-corrections-jail",
        "num": "14",
        "title": "Civic Institutions, Corrections & Detention Facilities",
        "icon": "⛓️",
        "doubles_as": "Maximum Security Prisons · Federal Penitentiaries · Police Holding Cells · Cold War Detention Blocks · Municipal Courthouses",
        "hero_badge": "Verified Location",
        "area": "Disa Prison & Tygerberg Correctional Complex",
        "tagline": "Reinforced steel cellblocks, multi-tier concrete catwalks, razor-wire security perimeters, heavy barred intake gates, and institutional visitation rooms.",
        "creative_synopsis": "This specialized institutional category provides high-security correctional environments for crime dramas, espionage thrillers, and legal procedurals. Disa Prison and the Tygerberg correctional facilities feature authentic multi-level concrete cellblocks, heavy barred steel sliding gates, central guard walkways, and individual cells with stainless steel fittings. Complete with institutional holding areas, secure partition visitation cubicles, and perimeter high-voltage fence lines, it enables total control without disturbing operational facilities.",
        "hero_image_file": r"Prisons\Disa Prison-Tygerberg (3).jpg",
        "hero_image_title": "Disa Institutional Prison: Reinforced Steel Cellblock Gates, Security Checkpoint & Concrete Corridor",
        "key_features": [
            "Disa Prison: Heavy mechanical sliding cell doors, steel security grilles, and central guard corridors",
            "Multi-tier industrial cellblock catwalks with overhead institutional fluorescent lighting",
            "Concrete interrogation and intake processing rooms with heavy steel furniture",
            "Secure visitation partition booths with reinforced dividing glass and intercom units",
            "Exterior perimeter security: High-voltage razor-wire fences, watchtowers, and gated vehicle sally ports"
        ],
        "specs": {
            "permitting": "Department of Correctional Services (DCS) / Provincial Public Works filming protocol (5–7 working days)",
            "power": "3-Phase 63A/100A institutional utility hook-ups + generator access in secure compound courtyard",
            "parking": "Enclosed, secure perimeter compound parking for 15+ technical vehicles, grip trucks, and crew trailers",
            "sound_curfew": "Enclosed concrete structure provides outstanding acoustic containment · 24/7 filming permissions"
        },
        "gallery": [
            {"file": r"Prisons\Disa Prison-Tygerberg (3).jpg", "title": "Disa Prison: Reinforced Steel Cellblock Gates & Concrete Security Corridor", "tag": "Hero Cellblock"},
            {"file": r"Prisons\Disa Prison-Tygerberg (4).jpg", "title": "Disa Prison: Institutional Concrete Guard Station & Barred Gate Security Access", "tag": "Security Checkpoint"},
            {"file": r"Prisons\Disa Prison-Tygerberg (5).jpg", "title": "Disa Prison: Institutional Corridors, Steel Gates & Sterile Facility Architecture", "tag": "Cell Block Corridor"},
            {"file": r"Prisons\Disa Prison-Tygerberg (6).jpg", "title": "Disa Prison: Heavy Steel Barred Doors & Industrial Prison Gallery", "tag": "Cell Gallery"},
            {"file": r"Prisons\Disa Prison-Tygerberg (7).jpg", "title": "Disa Prison: High-Security Exercise Yard & Concrete Perimeter Watch Walls", "tag": "Exercise Yard"},
            {"file": r"Prisons\Disa Prison-Tygerberg (8).jpg", "title": "Disa Prison: Secure Partition Visitation Cubicles & Reinforced Glass", "tag": "Visitation Room"}
        ]
    },

    # 15
    {
        "id": "stadiums-arenas-athletics",
        "num": "15",
        "title": "Stadiums, Arenas & World-Class Athletics",
        "icon": "🏟️",
        "doubles_as": "Olympic Stadiums · European Premier Football Arenas · International Cricket Grounds · Velodrome & Track Facilities",
        "hero_badge": "Verified Location",
        "area": "Cape Town Stadium (DHL), Green Point Track, Athlone & Newlands",
        "tagline": "Monumental 55,000-seat World Cup stadiums with PTFE architectural canopies, Olympic synthetic running tracks, historic cricket grounds, and indoor velodromes.",
        "creative_synopsis": "Cape Town possesses Olympic-grade sports infrastructure capable of hosting international tournament scenes, commercials, and arena spectacles. Cape Town Stadium (DHL Stadium) in Green Point is an iconic 55,000-seat FIFA World Cup arena featuring a translucent undulating roof framed by Table Mountain and the Atlantic Ocean. Adjacent, the Green Point Athletics Track offers an Olympic 8-lane red synthetic running track and grandstand. Athlone Stadium provides a 34,000-seat community arena, while Newlands Cricket Ground and the Bellville Velodrome offer classic heritage and indoor cycling tracks.",
        "hero_image_file": r"Stadia\CT Stadium (1).jpg",
        "hero_image_title": "Cape Town Stadium (DHL Stadium): 55,000-Seat FIFA World Cup Arena, Translucent Roof & Ocean Backdrop",
        "key_features": [
            "Cape Town Stadium (DHL Stadium): 55,000-seat bowl, translucent PTFE canopy, player tunnels, and media suites",
            "Green Point Athletics Track: World Athletics certified 8-lane synthetic track, hurdles, and floodlight towers",
            "Athlone Stadium: 34,000-seat multi-tier bowl with cantilevered rooflines and immaculate sports turf",
            "Newlands Cricket Ground: Iconic historic cricket stadium with grass embankments framed by Devil's Peak",
            "Bellville Velodrome: Indoor banked timber cycling track and arena floor for specialized sports choreography"
        ],
        "specs": {
            "permitting": "Cape Town Stadium Management / City of Cape Town Recreation & Parks (5–7 working days)",
            "power": "Dual redundant 3-phase 400A broadcast power tie-ins on-site + high-capacity broadcast compound",
            "parking": "Dedicated broadcast compound parking for 30+ OB trucks, technical vehicles, and mobile cranes",
            "sound_curfew": "Full stadium PA audio systems · Pre-cleared high-SPL crowd simulation and night lighting"
        },
        "gallery": [
            {"file": r"Stadia\CT Stadium (1).jpg", "title": "Cape Town Stadium (DHL Stadium): FIFA World Cup Arena & Architectural Translucent Canopy", "tag": "Hero Stadium"},
            {"file": r"Stadia\CT Stadium (2).jpg", "title": "Cape Town Stadium: Panoramic Grandstand Seating Bowl, Turf Pitch & Mountain Skyline", "tag": "Grandstand Bowl"},
            {"file": r"Stadia\Greenpoint Track\GP Athletics.jpg", "title": "Green Point Athletics Track: Olympic-Standard 8-Lane Red Synthetic Track & Grandstand", "tag": "Olympic Track"},
            {"file": r"Stadia\Greenpoint Track\Greenpoint Track (1).jpg", "title": "Green Point Track: 400m Sprint Straight, Hurdles Layout & Floodlight Towers", "tag": "Track Straight"},
            {"file": r"Stadia\Greenpoint Track\Greenpoint Track (2).JPG", "title": "Green Point Track: Spectator Grandstand Concourse & Trackside Staging", "tag": "Track Grandstand"},
            {"file": r"Stadia\Athlone Stadium\Athlone Stadium (0).jpg", "title": "Athlone Stadium: 34,000-Seat Multi-Tier Community Sports Arena & Athletic Pitch", "tag": "Athlone Stadium"},
            {"file": r"Stadia\Athlone Stadium\Athlone Stadium (1).jpg", "title": "Athlone Stadium: Grandstand Seating, Floodlight Towers & Professional Turf Pitch", "tag": "Sports Stadium"},
            {"file": r"Stadia\Athlone Stadium\Athlone Stadium (12).jpg", "title": "Athlone Stadium: Sweeping Grandstand Curves & Cantilevered Roof Architecture", "tag": "Cantilevered Stands"},
            {"file": r"Stadia\Newlands Cricket (1).jpg", "title": "Newlands Cricket Ground: Iconic Grass Embankment & Stadium Facing Devil's Peak", "tag": "Newlands Cricket"},
            {"file": r"Stadia\Newlands Cricket (2).jpg", "title": "Newlands: International Cricket Pavilion, Floodlights & Outfield Turf", "tag": "Pavilion Stands"},
            {"file": r"Stadia\14th - Bellville Stadium (1).jpg", "title": "Bellville Stadium: Multi-Purpose Municipal Athletics Grounds & Cycling Track", "tag": "Bellville Athletics"},
            {"file": r"Stadia\20191202_125421.jpg", "title": "Bellville Velodrome: Indoor Banked Timber Cycling Track & Sports Arena", "tag": "Velodrome"}
        ]
    },

    # 16
    {
        "id": "golf-courses-country-club-estates",
        "num": "16",
        "title": "Championship Golf Courses & Country Club Estates",
        "icon": "⛳",
        "doubles_as": "Monterey Peninsula / Carmel Valley · Augusta Georgia Woodlands · Scottish & Irish Coastal Links · Surrey & Berkshire Parkland Estates · Napa Valley Wine Country Golf",
        "hero_badge": "Verified Location",
        "area": "Clovelly Country Club, Sunset Links (Milnerton), Royal Cape (Est. 1885), Westlake, Mowbray, Durbanville, Bellville & Stellenbosch",
        "tagline": "Championship 18-hole valley fairways framed by rugged sandstone amphitheaters, Atlantic links along Sunset Beach, grand country club function venues, and historic heritage parkland greens.",
        "creative_synopsis": "South Africa's Western Cape offers world-class championship golf courses and private country club estates that double seamlessly for the world's most prestigious golfing destinations. Clovelly Country Club, nestled in the Silvermine Valley, features undulating manicured fairways lined with coastal pines against a dramatic mountain amphitheater (presented as an expansive 3-part panorama). Sunset Links in Milnerton provides an Atlantic links perimeter with coastal palm boulevards. Royal Cape Golf Club, established in 1885 as the oldest club in Africa, provides classic English parkland fairways with Table Mountain views. Mowbray and Durbanville golf clubs offer immaculate bentgrass putting surfaces and white sand bunkers, while Stellenbosch provides historic Cape Winelands golf estates, complemented by grand vaulted clubhouse function venues for banquets and interior scenes.",
        "hero_image_file": r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790773859734.jpg",
        "hero_image_title": "Clovelly Country Club: Championship Valley Fairway, Coastal Pine Canopies & Mountain Backdrop (Silvermine Valley)",
        "key_features": [
            "Clovelly Country Club: Championship 18-hole layout in Silvermine Valley captured in an expansive 3-part panoramic vista",
            "Mowbray Golf Club: Pristine bentgrass putting green and manicured rough framed by the grand clubhouse and Table Mountain skyline",
            "Durbanville Golf Club: Rolling parkland fairways, deep white sand bunkers, and mature Boland woodland borders",
            "Royal Cape Golf Club (Est. 1885): South Africa's oldest club, traditional English parkland layout, and Table Mountain vistas",
            "Sunset Links (Milnerton): Atlantic seaside links perimeter with palm boulevards and ocean breeze settings",
            "Stellenbosch Golf Club: Historic Cape Winelands golf estate surrounded by vineyards and the towering Helderberg mountains",
            "Bellville Golf Club: Panoramic Welgemoed valley fairways, water hazard reflections, and elevated tee boxes",
            "Country Club Function Venue: Grand vaulted hall, wrought-iron chandeliers, and hardwood floors for gala and banquet filming"
        ],
        "specs": {
            "permitting": "Private Club Filming License (48–72 hr sign-off) · Scheduled tee-time buyout & dawn/dusk filming blocks",
            "power": "3-Phase 63A/100A clubhouse utility tie-ins · Mobile quiet battery generator packs for fairway setups",
            "parking": "Clubhouse tarmac hardstand parking for 25+ technical vehicles, honeywagons, and crew shuttles",
            "sound_curfew": "Acoustically secluded valley basins with minimal traffic noise · Dawn sunrise tee-off filming permitted"
        },
        "gallery": [
            {"file": r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790773859790.jpg", "title": "Clovelly Country Club: Left Valley Vista, Putting Greens & Indigenous Mountain Ridges (Panorama 1/3)", "tag": "Clovelly Pan 1"},
            {"file": r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790773859734.jpg", "title": "Clovelly Country Club: Championship Valley Fairway, Pine Canopies & Mountain Backdrop (Panorama 2/3)", "tag": "Clovelly Pan 2"},
            {"file": r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790773859677.jpg", "title": "Clovelly Country Club: Clubhouse Terrace Overlook, Historic Cannon & Fairways (Panorama 3/3)", "tag": "Clovelly Pan 3"},
            {"file": r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790773859657.jpg", "title": "Grand Country Club Function Hall & Estate Ballroom: Vaulted Ceilings, Wrought-Iron Chandeliers & Hardwood Floors", "tag": "Function Venue"},
            {"file": r"Trilogy\Crime series-Old\AM\Last Season\Sunset Beach\Sunset Links-1 (1).jpg", "title": "Sunset Links Golf Estate (Milnerton): Atlantic Links Perimeter, Palm Boulevards & Coastal Setting", "tag": "Milnerton Links"},
            {"file": r"Outsurance-Let it Rain\Royal Cape Golf Club\Royal Cape Golf (1).jpg", "title": "Royal Cape Golf Club (Est. 1885): South Africa's Oldest Parkland Course & Table Mountain Backdrop", "tag": "Heritage Parkland"},
            {"file": r"Outsurance-Let it Rain\Royal Cape Golf Club\Royal Cape Golf (2).jpg", "title": "Royal Cape Golf Club: Historic Championship Fairway, Ancient Oak Trees & Manicured Green", "tag": "Parkland Fairway"},
            {"file": r"Backup 2022-02\Stelara\Golf Clubs\Mowbray\Mowbray Golf Club (8).jpg", "title": "Mowbray Golf Club: Championship Putting Green Framed by Grand Clubhouse & Table Mountain Skyline", "tag": "Mowbray Putting Green"},
            {"file": r"Backup 2022-02\Stelara\Golf Clubs\Durbanville\Durbanville Golf Club (6).jpg", "title": "Durbanville Golf Club: Manicured Rolling Greens, White Sand Bunkers & Boland Woodland Border", "tag": "Durbanville Greens"},
            {"file": r"Golf-Miami\Bellville Golf Club\Bellville Golf (5).jpg", "title": "Bellville Golf Club: Elevated Panoramic Vista Across Rolling Welgemoed Valley Fairways & Lakes", "tag": "Bellville Vista"},
            {"file": r"Golf-Miami\Bellville Golf Club\Bellville Golf (12).jpg", "title": "Bellville Golf Club: Manicured Bentgrass Tee Box Overlooking Wooded Parkland Course", "tag": "Bellville Parkland"},
            {"file": r"Backup 2022-02\Stelara\Golf Clubs\Stellenbosch\Stellenbosch Golf (28).jpg", "title": "Stellenbosch Golf Club: Historic Winelands Championship Course Beneath Helderberg Mountains", "tag": "Winelands Golf"},
            {"file": r"Golf-Miami\Westlake Golf Course\Westlake Golf (1).jpg", "title": "Westlake Golf Course: Towering Pine Canopies & Slopes of the Silvermine Mountains", "tag": "Pine Woodland"},
            {"file": r"Golf-Miami\Westlake Golf Course\Westlake Golf (11).jpg", "title": "Westlake Golf Course: Manicured Lake Hazard, Reed Waterways & Silvermine Mountain Face", "tag": "Lake Hazard"}
        ]
    },

    # 17
    {
        "id": "city-views-rooftops-panoramas",
        "num": "17",
        "title": "City Views, Rooftop Lounges & Panoramic Lookouts",
        "icon": "🌇",
        "doubles_as": "Manhattan Skyline Rooftops · Miami Penthouse Terraces · Mediterranean Harbor Lookouts · Los Angeles Griffith Observatory Overlooks · Hong Kong & Tokyo Skyline Lounges",
        "hero_badge": "Verified Location",
        "area": "113 Loop St CBD, Signal Hill Lookout, Long Street Rooftops, Cloud 9 & Table Mountain Summit",
        "tagline": "Panoramic 360° city bowl vistas from iconic mountain crests, luxury penthouse pools, and chic CBD rooftop cocktail decks overlooking Table Mountain and Table Bay.",
        "creative_synopsis": "Perched between the Atlantic Ocean and Table Mountain, Cape Town's elevated architecture and natural mountain viewpoints provide incomparable panoramic vistas. Signal Hill delivers sweeping 360-degree lookouts over the Atlantic Seaboard, Cape Town Stadium, the working harbor, and the illuminated CBD skyline, doubling for Los Angeles lookouts or Mediterranean coastal cities. Within the central city, private architectural rooftop terraces like 113 Loop Street offer lush urban oasis decks with palm planters and daybeds, private plunge pools, and glass-wrapped penthouse lounges. Complemented by the famous Grand Daddy rooftop airstream trailer park in Long Street, Tokyo rooftop pool, and Cloud 9 Mountain Club overlooking Table Mountain.",
        "hero_image_file": r"SALocations\Rooftops\113 Loop (1).jpg",
        "hero_image_title": "113 Loop St Penthouse Rooftop: Hardwood Sun Deck, Palm Planters & Daybeds Overlooking Cape Town CBD Skyline",
        "key_features": [
            "113 Loop St Penthouse: Private hardwood sun deck, lush palm planters, daybeds, and panoramic CBD skyline views",
            "113 Loop St Rooftop Plunge Pool: Elevated infinity-style pool deck with sun loungers framed by Table Mountain",
            "113 Loop St Penthouse Lounge: Floor-to-ceiling glass enclosure, designer dining suite, and 360° urban views",
            "113 Loop St Terrace: Cocktail sundeck facing the gentle contours of Signal Hill and Lion's Head",
            "Signal Hill Atlantic Vantage: Monumental ocean lookouts over Green Point Common, Robben Island, and Cape Town Stadium",
            "Signal Hill Overlook: Elevated perspective over Table Bay Harbour, container docks, and skyscraper grid",
            "Signal Hill City Bowl & Table Mountain Face: High-altitude angle on Bo-Kaap, the city amphitheater, and Devil's Peak",
            "Grand Daddy Rooftop Sky Bar (Long St): Historic vintage Airstream trailer park and timber cocktail deck",
            "Cloud 9 Mountain Club & Tokyo Rooftop: Glass-balustraded rooftop pool decks with direct Table Mountain views",
            "Table Mountain Summit Vantage: High-altitude aerial perspective over Lion's Head and the Atlantic coastline"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Office & SANParks permits for Signal Hill (3–5 working days) · Private rooftop commercial location agreements (24–48 hrs)",
            "power": "Building 3-phase tie-ins available at 113 Loop & Grand Daddy · Mobile battery packs / quiet generators for Signal Hill lookouts",
            "parking": "CBD basement loading bays & street curb metering · Wide tarmac coach & unit parking loops at Signal Hill summit",
            "sound_curfew": "CBD rooftop filming permits through 23:00 · Zero sound curfew on Signal Hill mountain lookouts"
        },
        "gallery": [
            {"file": r"SALocations\Rooftops\113 Loop (1).jpg", "title": "113 Loop St: Hardwood Rooftop Sun Deck with Palm Planters & CBD Skyline Views", "tag": "Hero Rooftop"},
            {"file": r"SALocations\Rooftops\113 Loop (8).jpg", "title": "113 Loop St: Rooftop Plunge Pool & Lounger Deck Overlooking High-Rise Towers", "tag": "Rooftop Pool"},
            {"file": r"SALocations\Rooftops\113 Loop (3).jpg", "title": "113 Loop St: Glass-Enclosed Penthouse Lounge & Dining Suite with 360° Views", "tag": "Penthouse Lounge"},
            {"file": r"SALocations\Rooftops\113 Loop (11).jpg", "title": "113 Loop St: Rooftop Cocktail Terrace Facing Signal Hill & Lion's Head Ridge", "tag": "Mountain View Deck"},
            {"file": r"SALocations\Views\Signal Hill Rd (1).jpg", "title": "Signal Hill Summit: Panoramic Ocean Vista Over Green Point, Cape Town Stadium & Table Bay", "tag": "Atlantic Panorama"},
            {"file": r"SALocations\Views\Signal Hill Rd (3).jpg", "title": "Signal Hill Overlook: Elevated View Over Table Bay Harbour Quays & Waterfront Basins", "tag": "Harbour Overlook"},
            {"file": r"SALocations\Views\Signal Hill Rd (60).jpg", "title": "Signal Hill Lookout: Complete City Bowl Panorama Facing North Face of Table Mountain & Devil's Peak", "tag": "City Bowl Panorama"},
            {"file": r"SALocations\Views\Signal Hill Rd (61).jpg", "title": "Signal Hill East View: Urban CBD Grid, High-Rise Skyline & Table Mountain Backdrop", "tag": "Skyline Vista"},
            {"file": r"SALocations\Rooftops\Grand Daddy (1).jpg", "title": "Grand Daddy Rooftop (Long St): Vintage Airstream Trailer Park & Sky Bar Deck", "tag": "Airstream Rooftop"},
            {"file": r"SALocations\Rooftops\Mountain Club (2).jpg", "title": "Cloud 9 Mountain Club: Chic Rooftop Cocktail Banquettes with Table Mountain Views", "tag": "Rooftop Bar"},
            {"file": r"SALocations\Rooftops\Tokyo (6).jpg", "title": "The Tokyo Rooftop: Elevated Swimming Pool & Sun Deck Facing Table Mountain Crest", "tag": "Sky Pool"},
            {"file": r"SALocations\Views\Table Mountain (2).jpg", "title": "Table Mountain Summit Look: High-Altitude Aerial Vantage Over Lion's Head & Atlantic Coastline", "tag": "Summit Aerial"}
        ]
    }
]

print(f"Total Categories: {len(categories)}")

# Collect all files to encode
all_files = set()
for cat in categories:
    all_files.add(cat["hero_image_file"])
    for item in cat["gallery"]:
        all_files.add(item["file"])

print(f"Total Unique Assets to Encode: {len(all_files)}")

encoded_images = {}
for idx, f in enumerate(all_files):
    b64 = encode_img(f)
    if b64:
        encoded_images[f] = b64
    if (idx + 1) % 15 == 0 or (idx + 1) == len(all_files):
        print(f"Encoded {idx + 1}/{len(all_files)} images...")

hero_bg_path = r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c\.user_uploaded\media_1790773315582.jpg"
hero_bg_b64 = encode_img(hero_bg_path, max_size=(1600, 900), quality=75)
if hero_bg_b64:
    print("Encoded Table Mountain Hero Background successfully!")
else:
    print("Warning: Failed to encode Table Mountain Hero Background.")

payload = {
    "categories": categories,
    "images": encoded_images,
    "hero_background": hero_bg_b64
}

with open(output_json, "w", encoding="utf-8") as out:
    json.dump(payload, out)

file_size_mb = os.path.getsize(output_json) / (1024 * 1024)
print(f"\nSuccessfully wrote {output_json} ({file_size_mb:.2f} MB, {len(encoded_images)}/{len(all_files)} encoded)!")
