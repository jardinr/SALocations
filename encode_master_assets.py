import os
import json
import base64
import io
from PIL import Image, ImageOps, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

base_dir = r"C:\Users\Jardin\OneDrive\Pictures"
output_dir = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-global-locations-deck"

os.makedirs(output_dir, exist_ok=True)

def encode_img(rel_path, max_size=(1200, 800), quality=80):
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Warning: Missing file: {full_path}")
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

print("Building Master Location Categories Dataset...")

categories = [
    {
        "id": "coastal-passes-ocean-roads",
        "num": "01",
        "title": "Coastal Passes, Ocean Roads & Arid Corridors",
        "icon": "🛣️",
        "doubles_as": "California Pacific Coast Highway (PCH) · Italian Amalfi Coast · French Riviera · Route 66 · Nevada Desert Corridor",
        "hero_badge": "100% Exact Match",
        "area": "Chapman's Peak Drive (M6), Victoria Road & R355 Karoo Highway",
        "tagline": "World-renowned coastal cliff highways carved into 500m ocean precipices, sweeping sea-level tarmac hugging the 12 Apostles, and uninterrupted horizon-to-horizon arid desert plains.",
        "creative_synopsis": "South Africa's coastal roadways offer the ultimate global doubling versatility. Chapman's Peak Drive (M6) provides 9km of cantilevered rock galleries and hairpin turns suspended 500m above the Atlantic, doubling seamlessly for the Italian Riviera or California's Big Sur. Below, Victoria Road (M6) stretches along turquoise Atlantic shores with direct lines-of-sight to Lion's Head and Camps Bay. Inland, the R355 in the Tankwa Karoo offers the longest uninterrupted straight dirt/gravel corridor on the continent for high-speed tracking and desert sequences.",
        "hero_image_file": r"Zen\Chapmans Peak (91).jpg",
        "hero_image_title": "Chapman's Peak Drive: Panoramic Cliff Pass Overlooking Hout Bay & The Sentinel (100% Exact Match)",
        "key_features": [
            "9km of vertical cliff highway with 114 curves, cantilevered rock canopy galleries, and half-tunnels",
            "Victoria Road sea-level tracking corridor connecting Clifton, Camps Bay, and Llandudno along the 12 Apostles",
            "R355 Arid Highway: 250km of uninterrupted desert plains, shimmering heat hazes, and zero light pollution",
            "Lookout Vantage: Chapman's Peak Lookout Over Monkey Valley & Long Beach Noordhoek",
            "Single-track cliff trails carved into red sandstone precipices for high-speed action tracking"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Permit Office & Entilini Concession (48–72 hr turnaround) · SANParks Commercial Permit",
            "power": "Self-contained mobile generator basecamps · 3-phase tie-ins available at Entilini depot & Hout Bay harbour",
            "parking": "4 designated heavy turnout bays on Chapman's Peak · Lower & upper parking lots accommodating full Motocrane/Russian Arm unit fleet",
            "sound_curfew": "No residential curfew on pass routes · Scheduled rolling road closures with local traffic police escorts"
        },
        "gallery": [
            {"file": r"Zen\Chapmans Peak (91).jpg", "title": "Chapman's Peak Pass: High Altitude Lookout Across Hout Bay Crescent Beach & The Sentinel", "tag": "Hero Pass"},
            {"file": r"Zen\Chapmans Peak (57).jpg", "title": "Chapman's Peak: Half-Tunnel Rock Gallery & Atlantic Horizon", "tag": "Rock Gallery"},
            {"file": r"Zen\Chapmans Peak (71).jpg", "title": "Chapman's Peak: Sweeping South Vista Towards Noordhoek & Ocean Horizon", "tag": "Coastal Curve"},
            {"file": r"Zen\Chapmans Peak (78).jpg", "title": "Chapman's Peak: Vertical Red Sandstone Cliff & Deep Turquoise Water", "tag": "Cliff Edge"},
            {"file": r"Zen\Chapmans Peak South Lookout (5).jpg", "title": "Chapman's Peak Lookout Over Monkey Valley & Long Beach Noordhoek", "tag": "Lookout Vista"},
            {"file": r"Zen\Chapmans Peak Trail (1).jpg", "title": "Chapman's Peak Trail: High Ridge Single-Track Above Ocean & Bay", "tag": "Cliff Trail"},
            {"file": r"Zen\Chapmans Peak Trail (2).jpg", "title": "Chapman's Peak Trail: Dramatic Sandstone Single-Track Cutting Into Cliff Face", "tag": "Action Trail"},
            {"file": r"Zen\M6-to CB (0).jpg", "title": "Victoria Road (M6): Sea-Level Coastal Drive Hugging Twelve Apostles Towards Lion's Head (100% Match)", "tag": "Victoria Rd"},
            {"file": r"Zen\M6-to CB (1).jpg", "title": "Victoria Road (M6): Golden Hour Tarmac & Atlantic Wave Horizon", "tag": "Coastal Highway"},
            {"file": r"Arid Road-R355\R355 (11).jpg", "title": "R355 Tankwa Karoo Highway: Uninterrupted Dirt Road & Vast Desert Basin", "tag": "Arid Highway"},
            {"file": r"Arid Road-R355\R355 (115).jpg", "title": "R355 Desert Horizon: Open Plain Tracking Corridor & Remote Mountain Backdrop", "tag": "Desert Highway"},
            {"file": r"Arid Road-R355\R355 (130).jpg", "title": "R355 Highway Corridor: Arid Scrubland & Endless Vanishing Point", "tag": "Desert Plain"}
        ]
    },
    {
        "id": "modern-luxury-villas",
        "num": "02",
        "title": "Modern Luxury Villas & Architectural Residences",
        "icon": "🏛️",
        "doubles_as": "Hollywood Hills · Malibu Oceanfront · Miami Waterfront Mansions · Modern Swiss/European Alpine Luxury",
        "hero_badge": "Scouted Database Match",
        "area": "Nettleton Road (Clifton), Clifton Rocks, Camps Bay & City Bowl",
        "tagline": "Multi-tier glass and concrete cantilevered architectural estates perched above turquoise ocean coves, rim-flow infinity pools, private funiculars, and skyline penthouses.",
        "creative_synopsis": "Cape Town's Atlantic Seaboard houses some of the world's most sought-after contemporary film villas. Nettleton Ridge in Clifton represents the pinnacle of cantilevered luxury—featuring double-volume glass walls, raw off-shutter concrete, and rim-flow infinity pools floating above the Atlantic. Cap d'Afrique offers curved whitewashed terraces with direct sea-edge rocks and private funicular access. Bella Ev on the Camps Bay slope provides seamless indoor-outdoor living framed against Lion's Head, while high-rise penthouses showcase 270-degree skyline vistas.",
        "hero_image_file": r"Houses\Nettleton\Photos-001\Nettleton (1).jpg",
        "hero_image_title": "Nettleton Ridge Architectural Villa: Cantilevered Concrete, Glass Horizons & Rim-Flow Pool (Clifton)",
        "key_features": [
            "Nettleton Road: Prestigious multi-level residence with floor-to-ceiling glass, floating timber stairs, and ocean terrace",
            "Cap d'Afrique (Clifton): Iconic white modernist curves, private funicular cliff lift, and direct ocean boulder access",
            "Bella Ev (Camps Bay): Polished marble terraces, frameless sliding glass pocket doors, and unobstructed sunset vistas",
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
            {"file": r"Houses\Nettleton\Photos-001\Nettleton (7).jpg", "title": "Nettleton Villa: Floating Timber Stairwell, Off-Shutter Concrete & Architectural Voids", "tag": "Architectural Interior"},
            {"file": r"Houses\Nettleton\Photos-001\Nettleton (8).jpg", "title": "Nettleton Villa: Minimalist Master Bathroom with Frameless Mountain Vista", "tag": "Luxury Bath"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (1).jpg", "title": "Cap d'Afrique: Curved Modernist Oceanfront Villa & Terrace on Clifton Rocks", "tag": "Cap d'Afrique"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (10).jpg", "title": "Cap d'Afrique: Double-Volume Living Lounge Overlooking Crashing Waves", "tag": "Ocean Living"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (11).jpg", "title": "Cap d'Afrique: Outdoor Dining Terrace & Private Funicular Track", "tag": "Cliff Terrace"},
            {"file": r"Houses\Clifton\GREAT ESCAPES CAP D'AFRIQUE CLIFTON (12).jpg", "title": "Cap d'Afrique: Sunken Lounge & Panoramic Atlantic Ocean Horizon", "tag": "Sunset Lounge"},
            {"file": r"Houses\Bella Ev\20260815_144853.jpg", "title": "Bella Ev: Modernist Open-Plan Lounge & Rim-Flow Pool Over Camps Bay", "tag": "Bella Ev"},
            {"file": r"Houses\Bella Ev\20260815_144924.jpg", "title": "Bella Ev: Floor-to-Ceiling Retractable Glass Terraces & Lion's Head Backdrop", "tag": "Indoor-Outdoor"},
            {"file": r"Apartments\Woodside\604\604\Woodside-604 (1).jpg", "title": "Woodside Skyline Penthouse: Modern Urban Living with Panoramic City Bowl & Mountain Views", "tag": "City Penthouse"},
            {"file": r"Apartments\Woodside\604\604\Woodside-604 (5).jpg", "title": "Woodside Penthouse: Wrap-Around Glass Balcony & Table Mountain Skyline", "tag": "Skyline Balcony"}
        ]
    },
    {
        "id": "heritage-cottages-character-streets",
        "num": "03",
        "title": "Heritage Cottages, Character Streets & Facades",
        "icon": "🏡",
        "doubles_as": "London Victorian Suburbs · San Francisco Painted Ladies · Historic Amsterdam · Colonial Caribbean Quarter",
        "hero_badge": "Scouted Database Match",
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
            {"file": r"Zen\House 2 Heritage Cottages (Culver & Chatham)\Culver St (3).jpg", "title": "Culver Street: Tree-Lined Residential Suburban Street Frontage", "tag": "Streetscape"},
            {"file": r"Zen\House 2 Heritage Cottages (Culver & Chatham)\Chatham St (2).jpg", "title": "Chatham Street: Heritage Cottage Entrance & Corrugated Iron Gabled Roof", "tag": "Chatham St"},
            {"file": r"Zen\Rosemount Ave-Gardens (4).jpg", "title": "Rosemount Avenue: Grand Double-Storey Victorian Facade with Cast-Iron Lace Balconies", "tag": "Victorian Grand"},
            {"file": r"CBD\Bo Kaap (1).jpg", "title": "Bo-Kaap: Vibrant Saturated Pastel Facades Along Steep Cobblestone Lane", "tag": "Bo-Kaap"},
            {"file": r"CBD\Bo Kaap (3).jpg", "title": "Bo-Kaap: Historic Heritage Street with Table Mountain Horizon", "tag": "Colour Quarter"},
            {"file": r"CBD\Bo Kaap (4).jpg", "title": "Bo-Kaap: Intimate Heritage Stoep & Traditional Sash Windows", "tag": "Street Detail"},
            {"file": r"De Waterkant\Fibre Designs (1).jpg", "title": "De Waterkant: European Cobblestone Alleyway & Wrought-Iron Exterior Balconies", "tag": "De Waterkant"},
            {"file": r"De Waterkant\Fibre Designs (2).jpg", "title": "De Waterkant: Quaint Sidewalk Stoep & Heritage Double-Storey Architecture", "tag": "Cobblestones"},
            {"file": r"De Waterkant\Fibre Designs (10).jpg", "title": "De Waterkant: Pedestrian Street with Cafe Terraces & Character Facades", "tag": "Cafe Lane"}
        ]
    },
    {
        "id": "wilderness-forest-cabins",
        "num": "04",
        "title": "Wilderness, Forest Cabins & Nature Retreats",
        "icon": "🌲",
        "doubles_as": "Pacific Northwest · Scandinavian Timber Retreats · Colorado Rockies · Extraterrestrial / Desert Planets",
        "hero_badge": "Scouted Database Match",
        "area": "Scarborough, Hout Bay Forest, Noordhoek & Cederberg Wilderness",
        "tagline": "Elevated dark timber stilt cabins with rock plunge pools, architectural glass treehouses in lush forest canopies, rustic milkwood chalets, and monumental desert sandstone rock arches.",
        "creative_synopsis": "When a screenplay calls for isolated wilderness or architectural nature sanctuaries, this category delivers uncompromised authenticity. Blackwood Cabin in Scarborough sits elevated on steel stilts above a coastal valley, complete with a natural rock plunge pool and winding wooden boardwalks through eucalyptus groves. In the lush canopy of Hout Bay forest, Amara Moon provides an architectural timber-and-glass stilt retreat. Vicki Residence captures artistic residential timber interiors, while the ancient Cederberg Stadsaal Caves provide monumental ochre rock arches and caves.",
        "hero_image_file": r"Zen\Blackwood Cabin\Blackwood Cabin (1).jpg",
        "hero_image_title": "Blackwood Cabin: Elevated Dark Timber Stilt Retreat & Rock Plunge Pool (Scarborough)",
        "key_features": [
            "Blackwood Cabin: Dark-stained timber cabin on stilts, wraparound deck, natural rock pool, and boardwalk",
            "Amara Moon: Architectural timber & glass stilt retreat situated in the lush canopy of Hout Bay forest (strictly forest canopy)",
            "Vicki Residence: Character mountainside retreat with warm exposed timber beams and rich daylight interiors",
            "Monkey Valley: Weathered log cabins nestled beneath ancient indigenous milkwood canopies overlooking the sea",
            "Stadsaal Caves (Cederberg): Monumental wind-carved sandstone arches and ancient San rock art"
        ],
        "specs": {
            "permitting": "Private Estate Filming Agreements (48 hr turnaround) · CapeNature Commercial Permits for Cederberg",
            "power": "On-site domestic single-phase + mobile silenced generator tie-in · Off-grid solar battery backup available",
            "parking": "Secure private property vehicle parking for 4–8 technical vans · 4x4 access staging for Cederberg",
            "sound_curfew": "Zero ambient city noise · Pristine acoustic environments for 24/7 synchronized dialogue and sound capture"
        },
        "gallery": [
            {"file": r"Zen\Blackwood Cabin\Blackwood Cabin (1).jpg", "title": "Blackwood Cabin: Elevated Timber Stilt Architecture & Natural Rock Plunge Pool", "tag": "Hero Cabin"},
            {"file": r"Zen\Blackwood Cabin\Blackwood Cabin (2).jpg", "title": "Blackwood Cabin: Wraparound Timber Deck, Plunge Pool & Indigenous Fynbos Garden", "tag": "Deck & Pool"},
            {"file": r"Zen\Blackwood Cabin\Blackwood Cabin (3).jpg", "title": "Blackwood Cabin: Architectural Timber Boardwalk Winding Through Eucalyptus Trees", "tag": "Forest Boardwalk"},
            {"file": r"Zen\Blackwood Cabin\Blackwood Cabin (4).jpg", "title": "Blackwood Cabin: Minimalist Timber Living Pavilion & Mountain Valley Vista", "tag": "Cabin Interior"},
            {"file": r"Zen\Amara Moon (2).jpg", "title": "Amara Moon: Architectural Timber Stilt Retreat Elevated in Lush Hout Bay Forest Canopy", "tag": "Forest Retreat"},
            {"file": r"Zen\Amara Moon (4).jpg", "title": "Amara Moon: Glass Living Pavilion Surrounded by Indigenous Forest Foliage", "tag": "Treehouse"},
            {"file": r"Zen\Vicki (22).JPG", "title": "Vicki Residence: Warm Exposed Timber Framing, Sunlight Voids & Artistic Character Interior", "tag": "Vicki Interior"},
            {"file": r"Trilogy\Crime series-Old\What Lies Beneath\Kommetjie\Imhoff's Gift\Vicki (1).JPG", "title": "Vicki Residence: Rustic Character Dining & Natural Timber Architecture", "tag": "Living Space"},
            {"file": r"Trilogy\Crime series-Old\What Lies Beneath\Kommetjie\Imhoff's Gift\Vicki (2).JPG", "title": "Vicki Residence: Sunlit Timber Kitchen & Studio Framing", "tag": "Timber Detail"},
            {"file": r"Zen\Monkey Valley.png", "title": "Monkey Valley: Rustic Log Chalet Canopy Nestled in Noordhoek Milkwood Trees", "tag": "Monkey Valley"},
            {"file": r"Stadsaal Cave-Cederberg\wetransfer_matjiesrivier-nr-stadsal_2023-05-26_0732\Matjiesrivier NR - Stadsal (10).jpg", "title": "Stadsaal Caves: Monumental Sandstone Rock Arches & Burnt-Orange Pillars (Cederberg)", "tag": "Stadsaal Arch"},
            {"file": r"Stadsaal Cave-Cederberg\wetransfer_matjiesrivier-nr-stadsal_2023-05-26_0732\Matjiesrivier NR - Stadsal (36).jpg", "title": "Stadsaal Caves: Wind-Carved Desert Sandstone Amphitheater & Otherworldly Formations", "tag": "Sandstone Cave"},
            {"file": r"Stadsaal Cave-Cederberg\wetransfer_matjiesrivier-nr-stadsal_2023-05-26_0732\Matjiesrivier NR - Stadsal (50).jpg", "title": "Stadsaal Caves: Ancient Weathered Rock Corridors & Dramatic Natural Light Shafts", "tag": "Rock Corridor"}
        ]
    },
    {
        "id": "beaches-coves-harbours",
        "num": "05",
        "title": "Pristine Beaches, Coastal Coves & Working Harbours",
        "icon": "🏖️",
        "doubles_as": "Mediterranean Coastline · Caribbean Sand Beaches · Brittany / Cornwall Fishing Ports · New England Quays",
        "hero_badge": "Scouted Database Match",
        "area": "Noordhoek Long Beach, Clifton 4th, V&A Waterfront & Tidal Pools",
        "tagline": "Endless 8km fine white sand beaches backed by coastal dunes, sheltered turquoise granite coves, operational historic maritime working basins, and nostalgic tidal bathing pools.",
        "creative_synopsis": "Cape Town's coastal portfolio encompasses both untamed wild coastlines and sheltered turquoise coves. Noordhoek Long Beach provides 8 uninterrupted kilometers of hard-packed white sand, Atlantic surf, and sand dunes. Clifton 4th Beach offers wind-sheltered turquoise water framed by massive granite boulders and palm trees. At the V&A Waterfront, active swing bridges, drydocks, tugboats, and the historic Victorian Clock Tower provide a fully functioning maritime hub. Historic tidal pools in Dalebrook and St. James add vintage coastal charm.",
        "hero_image_file": r"V&A Waterfront\V&A Waterfront (2).jpg",
        "hero_image_title": "V&A Waterfront Working Basin: Historic Red-Brick Clock Tower, Operational Tugboats & Table Mountain",
        "key_features": [
            "Long Beach Noordhoek: 8km wide flat sand corridor with horse-riding access, dunes, and Kakapo shipwreck",
            "Clifton 4th & Maiden's Cove: White quartz sand, turquoise water, and giant polished granite boulders",
            "V&A Waterfront Historic Basin: Working harbour with historic Clock Tower, luxury superyachts, and swing bridges",
            "Dalebrook & St. James Tidal Pools: Ocean-washed stone swimming walls and vibrant Victorian bathing boxes",
            "Direct beach vehicle ramp access and designated marine safety support"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Office & SANParks Coastal Permits (3–5 working days) · V&A Waterfront Film Office",
            "power": "V&A Waterfront: 3-phase 63A/125A shore power · Beaches: Mobile silenced generator trucks with beach matting",
            "parking": "V&A Waterfront: Dedicated subterranean staging for 25+ technical trucks · Noordhoek: Hardstand beach car park",
            "sound_curfew": "Golden hour sunrise call times recommended for pristine empty beaches · 24/7 harbour filming permissions"
        },
        "gallery": [
            {"file": r"V&A Waterfront\V&A Waterfront (2).jpg", "title": "V&A Waterfront Basin: Historic Clock Tower, Working Tugs & Unobstructed Table Mountain", "tag": "Hero Harbour"},
            {"file": r"V&A Waterfront\V&A Waterfront (3).jpg", "title": "V&A Waterfront: Swing Bridge, Modern Quayside & Maritime Ship Mooring", "tag": "Working Quayside"},
            {"file": r"V&A Waterfront\V&A Waterfront (31).jpg", "title": "V&A Waterfront: Historic Victoria & Alfred Working Harbour Basin & Maritime Wharves", "tag": "Harbour Basin"},
            {"file": r"V&A Waterfront\V&A Waterfront (32).jpg", "title": "V&A Waterfront: Operational Tugboats & Industrial Quayside Logistics", "tag": "Tugboats"},
            {"file": r"Beaches\Noordhoek\Noordhoek Beach (1).jpg", "title": "Noordhoek Long Beach: Wide 8km Untamed White Sand Corridor & Rolling Surf", "tag": "Long Beach"},
            {"file": r"Beaches\Noordhoek\Noordhoek Beach (2).jpg", "title": "Noordhoek Dunes: Fine Sand Dunes & Distant Chapman's Peak Mountain Headland", "tag": "Coastal Dunes"},
            {"file": r"Beaches\Noordhoek\Noordhoek Beach (3).jpg", "title": "Noordhoek Beach: Flat Wet-Sand Mirror Horizon Ideal for Vehicle & Stunt Tracking", "tag": "Beach Tracking"},
            {"file": r"Beaches\Clifton\Clifton 4th (1).jpg", "title": "Clifton 4th Beach: Sheltered Turquoise Water, Granite Boulders & Golden Sunset", "tag": "Clifton 4th"},
            {"file": r"Beaches\Clifton\Clifton-4th\Clifton 4th (10).jpg", "title": "Clifton Beach: Pristine White Sand Cove Framed by Dramatic Coastal Headlands", "tag": "Granite Cove"},
            {"file": r"Beaches\Dalebrook Tidal Pool\Dalebrook Tidal Pool (1).jpg", "title": "Dalebrook Tidal Pool: Historic Stone-Walled Ocean Swimming Pool & False Bay Horizon", "tag": "Tidal Pool"},
            {"file": r"Beaches\St. James Tidal Pool\Main Rd-St. James (1).jpg", "title": "St. James: Coastal Tarmac & Train Line Running Directly Along Ocean Wave Break", "tag": "Coastal Railway"},
            {"file": r"Beaches\St. James Tidal Pool\Main Rd-St. James (15).jpg", "title": "St. James Tidal Pool: Iconic Multi-Coloured Victorian Bathing Boxes & Beach", "tag": "Bathing Boxes"}
        ]
    },
    {
        "id": "urban-metropolis-cbd",
        "num": "06",
        "title": "Urban Metropolis, Commercial CBD & Civic Skylines",
        "icon": "🏙️",
        "doubles_as": "Chicago / New York Financial District · Modern Los Angeles Downtown · Tokyo Corporate Hub · European Modern Capitals",
        "hero_badge": "Scouted Database Match",
        "area": "Cape Town Financial District, Foreshore & CTICC Precinct",
        "tagline": "Sleek glass-curtain skyscrapers, brutalist concrete plazas, high-tech glass conference atriums, dramatic elevated freeway flyovers, and rooftop skyline vistas.",
        "creative_synopsis": "Cape Town's Central Business District is an established global production staple, frequently doubling for North American downtowns. Streets like Corporation, Darling, and Heerengracht present a mix of gleaming glass commercial towers, neoclassical civic architecture, and public plazas. The unfinished elevated freeway flyovers on the Foreshore offer an unparalleled location for high-speed car chases, stunt rigging, and post-apocalyptic urban scenes. The CTICC provides cavernous modern glass-and-steel atriums.",
        "hero_image_file": r"CBD\Corporation St (1).jpg",
        "hero_image_title": "Corporation Street Commercial Canyon: Glass Skyscrapers, Neoclassical Facades & Mountain Backdrop",
        "key_features": [
            "Financial District Canyons: Glass curtain-wall high-rises and busy multi-lane downtown corridors",
            "Elevated Foreshore Freeway Flyovers: Dramatic suspended concrete highways for vehicle chases and stunt rigging",
            "CTICC Precinct: Multi-storey glass atriums, architectural escalators, and polished stone concourses",
            "City Bowl Rooftops: Expansive commercial gravel/tar roofs with HVAC ducting and 360-degree mountain skylines",
            "Pre-cleared municipal road closure protocols for weekend street stunts and full block control"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Office CBD Street Permits (5 working days) · Weekend full-closure authorizations",
            "power": "Direct building tie-ins (3-phase 63A/100A) · Street-side generator truck parking bays",
            "parking": "Designated municipal hardstands, underground parking garages, and multi-vehicle technical basecamps",
            "sound_curfew": "Weekend filming allows high-SPL vehicle tracking and blank-firing stunt audio under police supervision"
        },
        "gallery": [
            {"file": r"CBD\Corporation St (1).jpg", "title": "Corporation Street: High-Rise Urban Canyon with Contemporary Commercial Towers", "tag": "Hero CBD"},
            {"file": r"CBD\Corporation St (2).jpg", "title": "Corporation Street: Clean Commercial Streetscape with Modernist Architectural Vistas", "tag": "Street Canyon"},
            {"file": r"CBD\Darling St (1).JPG", "title": "Darling Street: Grand Colonial Civic Hall & Broad Multi-Lane Downtown Corridor", "tag": "Civic Corridor"},
            {"file": r"CBD\Bo Kaap-Pan.jpg", "title": "Cape Town Skyline Panorama: Dense Urban High-Rise Core Framed Against Table Mountain", "tag": "Skyline Pano"},
            {"file": r"CTICC\CTICC 1 (1).jpg", "title": "CTICC Concourse: Monumental Multi-Level Glass Curtain Wall & Modernist Escalators", "tag": "CTICC Atrium"},
            {"file": r"CTICC\CTICC 1 (10).jpg", "title": "CTICC Interior: Cavernous Polished Granite Exhibition Gallery & High-Tech Ceiling Truss", "tag": "Convention Hall"},
            {"file": r"CTICC\CTICC 1 (11).jpg", "title": "CTICC Exterior: Sleek Curved Glass & Steel Facade Along Foreshore Boulevard", "tag": "Modern Facade"},
            {"file": r"Highway\Cut Off Highway (1).jpg", "title": "Foreshore Elevated Flyover: Dramatic Unfinished Concrete Highway Suspended in Urban Skyline", "tag": "Elevated Flyover"},
            {"file": r"Highway\Cut Off Highway (10).jpg", "title": "Elevated Freeway Ramp: High-Altitude Urban Tracking Deck with Harbor & Skyscraper Views", "tag": "Freeway Ramp"},
            {"file": r"Highway\Cut Off Highway (14).jpg", "title": "Elevated Highway Deck: Wide Multi-Lane Concrete Surface for High-Speed Stunt Filming", "tag": "Stunt Deck"},
            {"file": r"Rooftops\20231113_170008.jpg", "title": "CBD Commercial Rooftop: Industrial Ducting, Steel Vents & Table Mountain Backdrop", "tag": "Rooftop Vents"},
            {"file": r"Rooftops\20231113_172858.jpg", "title": "City Bowl Rooftop Sunset: Panoramic View Across Downtown Skyscrapers and Lion's Head", "tag": "Skyline Sunset"}
        ]
    },
    {
        "id": "nightlife-ambient-lounges",
        "num": "07",
        "title": "Nightlife, Ambient Lounges, Beach Clubs & Cabaret",
        "icon": "🍸",
        "doubles_as": "London Mayfair Cocktail Lounges · Ibiza / Mykonos Beach Clubs · Berlin Underground Clubs · Paris Cabaret Clubs",
        "hero_badge": "100% Exact Match",
        "area": "East City, Camps Bay Promenade, Woodstock & Granger Bay",
        "tagline": "Dark mahogany wood-paneled cocktail bars with crystal chandeliers, sunset beach lounges on palm-fringed promenades, authentic cabaret supper clubs, and heavy-production EDM nightclubs.",
        "creative_synopsis": "Cape Town's hospitality and nightlife scene features iconic world-class spaces ready for immediate filming. Harringtons Cocktail Lounge delivers opulent dark-mahogany bar paneling, glowing liquor backbars, and crystal chandeliers. Café Caprice on Camps Bay promenade offers the quintessence of beachfront luxury with fluted wood counters and sunset umbrella terraces. StarDust Theatrical Dining in Woodstock provides an authentic live performance supper club with an elevated stage, grand piano, and theatrical rigs.",
        "hero_image_file": r"Zen\Harringtons Cocktail Lounge\Harringtons (3).jpg",
        "hero_image_title": "Harringtons Cocktail Lounge: Dark Mahogany Bar Counter, Crystal Chandeliers & Glowing Bottle Displays (Hero Match)",
        "key_features": [
            "Harringtons (Hero): Dark mahogany wood-paneled bar counter, crystal chandeliers, and velvet booths",
            "Café Caprice: World-famous beachfront cocktail lounge fronting directly onto the Camps Bay palm promenade",
            "StarDust Theatrical Dining (100% Match): Raised stage, grand piano, illuminated StarDust emblem, and wide dining floor",
            "Grand Africa Café & Beach: Private oceanfront beach club with dining tables set directly into white sand",
            "Club Destiny, Club Halo & Hexagon: Pre-rigged DMX intelligent moving heads, LED walls, and VIP banquettes"
        ],
        "specs": {
            "permitting": "Private Commercial Venue Contracts (24–48 hr direct sign-off) · Late wrap alcohol licenses pre-cleared",
            "power": "3-Phase 63A/100A audio/lighting distribution on-site · Clean sound power feeds",
            "parking": "Dedicated alleyway or private lot staging for 6–10 technical vans and production catering",
            "sound_curfew": "Full acoustic interior isolation permitting 24/7 high-SPL playback and live tracking"
        },
        "gallery": [
            {"file": r"Zen\Harringtons Cocktail Lounge\Harringtons (3).jpg", "title": "Harringtons Cocktail Lounge: Hero Dark Mahogany Wood-Paneled Bar Counter & Crystal Chandeliers (Hero Match)", "tag": "Hero Bar"},
            {"file": r"Zen\Harringtons Cocktail Lounge\Harringtons (1).jpg", "title": "Harringtons: Ornate Wallpaper, Velvet Booth Seating & Disco Ball Glow", "tag": "Cocktail Lounge"},
            {"file": r"Zen\Harringtons Cocktail Lounge\Harringtons (2).jpg", "title": "Harringtons: Ambient Booth Seating & Chevron Hardwood Floors", "tag": "Velvet Booths"},
            {"file": r"Zen\Harringtons Cocktail Lounge\Harringtons (4).jpg", "title": "Harringtons: Intimate Mood Lighting, Brass Railings & Bar Stool Seating", "tag": "Bar Detail"},
            {"file": r"Zen\Cafe Caprice\Cafe Caprice (1).jpg", "title": "Café Caprice: Palm-Lined Camps Bay Beachfront Terrace & Sunset Umbrella Dining", "tag": "Beach Terrace"},
            {"file": r"Zen\Cafe Caprice\Cafe Caprice (2).jpg", "title": "Café Caprice: Curved Fluted-Wood Cocktail Bar, Veuve Clicquot Arch & Brass Gantry", "tag": "Curved Bar"},
            {"file": r"Zen\Stardust (12).jpg", "title": "StarDust Theatrical Dining: Wide Timber Dining Floor, Elevated Stage & Live Performance (100% Match)", "tag": "StarDust Hero"},
            {"file": r"Zen\Stardust (3).jpg", "title": "StarDust: Red Theatrical Stage Lighting, Seated Dining Audience & Piano", "tag": "Stage Lighting"},
            {"file": r"Zen\Stardust (6).jpg", "title": "StarDust: Live Acoustic Performance Corner & Cabaret Rigs", "tag": "Acoustic Corner"},
            {"file": r"Zen\Stardust (8).jpg", "title": "StarDust: Full Dining Room Vantage from Mezzanine Balcony", "tag": "Balcony View"},
            {"file": r"Zen\IMG_5253.JPG", "title": "Outdoor Cafe Courtyard: Multi-Pane Industrial Windows & Shaded Picnic Benches", "tag": "Cafe Courtyard"},
            {"file": r"Zen\Club Destiny (1).JPG", "title": "Club Destiny: High-Octane Nightclub Dancefloor with DMX Intelligent Moving Heads & Lasers", "tag": "Dancefloor"},
            {"file": r"Zen\Club Halo (8).jpg", "title": "Club Halo: LED Ceiling Array, VIP Mezzanine & Low-Lit Ambient Bar", "tag": "VIP Club"},
            {"file": r"Zen\Hexagon (4).jpg", "title": "Hexagon Lounge: Geometric Ambient Wall Lighting & Intimate Cocktail Tables", "tag": "Hexagon Lounge"},
            {"file": r"Bars & Clubs\Grand Cafe\Grand Africa Cafe & Beach Bar -11.jpg", "title": "Grand Africa Beach: Private Sand Dining Tables, Daybeds & Ocean Breakwater Views", "tag": "Grand Beach"}
        ]
    },
    {
        "id": "studios-soundstages",
        "num": "08",
        "title": "Industrial Infrastructure, Lofts, Studios & Soundstages",
        "icon": "🎬",
        "doubles_as": "Hollywood Soundstage Lot · London Abbey Road Studios · Berlin Converted Industrial Hall · Brooklyn Raw Lofts",
        "hero_badge": "Hero Database Match",
        "area": "Salt River, Epping Production Hub, Woodstock & Creative Precinct",
        "tagline": "Seamless white daylight cyclorama motion studios, fully acoustically treated soundstages with motorized lighting grids, converted historic church stages, and Dolby Atmos audio live rooms.",
        "creative_synopsis": "Cape Town provides turnkey world-class motion picture studio infrastructure. The Daylight Rehearsal Studio in Salt River features a seamless infinity cyclorama curve, polished screed floors, industrial cable trays, and rectangular daylight window bays. Studio 107 in Epping offers a heavy film soundstage with an overhead motorized lighting grid, mobile green screen, audio control booth, and acoustic ceiling baffles. Roodebloem Studios presents a converted historic church hall with 12m arched timber trusses, alongside Milestone and Suite Spot (Studio 1).",
        "hero_image_file": r"Zen\Daylight Rehearsal Studio (1).jpg",
        "hero_image_title": "Daylight Rehearsal Studio: Seamless White Infinity Cyclorama, Industrial Beams & Window Rays (Hero Match)",
        "key_features": [
            "Daylight Rehearsal Studio (Hero): Seamless white infinity cyclorama curve and polished floor with daylight control",
            "Studio 107: Soundproofed film soundstage with motorized lighting grid, mobile green screen, and acoustic baffles",
            "Roodebloem Studios (The Church): Converted historic 1800s church hall with 12m arched timber trusses and cyclorama",
            "Milestone Studios: Timber-paneled live tracking room, grand piano, drum booth, and Dolby Atmos control room",
            "Suite Spot Studios (Studio 1) & Plug Studio: Commercial photo & motion cyclorama stages with rapid turnaround"
        ],
        "specs": {
            "permitting": "Commercial Facility Hire · Pre-cleared studio bookings with 24-hr turnaround",
            "power": "Dedicated heavy 3-phase camlock distribution (100A–250A) · Uninterruptible clean sound power",
            "parking": "Direct drive-in loading docks for gear trucks · Secure on-site unit base and crew parking",
            "sound_curfew": "Full acoustic soundproofing · 24/7 round-the-clock filming, tracking, and live playback"
        },
        "gallery": [
            {"file": r"Zen\Daylight Rehearsal Studio (1).jpg", "title": "Daylight Rehearsal Studio: White Cyclorama Curve, Polished Concrete Floor & Natural Sunlit Window Bays", "tag": "Hero Cyclorama"},
            {"file": r"Zen\Daylight Rehearsal Studio (2).jpg", "title": "Daylight Rehearsal Studio: Industrial Concrete Ceiling Beams, Cable Trays & Window Framing", "tag": "Industrial Studio"},
            {"file": r"Zen\Studio 107 (Acoustic Studio & Green Screen).jpg", "title": "Studio 107: Film Soundstage with Overhead Grid, Mobile Green Screen & Acoustic Ceiling Baffles", "tag": "Studio 107 Grid"},
            {"file": r"Zen\Studio 107 (6).jpg", "title": "Studio 107: Acoustic Tracking Room, Wall Treatment Panels & Control Booth Window", "tag": "Studio 107 Acoustic"},
            {"file": r"Zen\Roodebloem Studios (2).jpg", "title": "Roodebloem Studios (The Church): 12m Arched Timber Trusses, Historic Church Windows & Cyclorama", "tag": "Church Studio"},
            {"file": r"Zen\Milstone Studios (3).jpg", "title": "Milestone Studios: Timber-Paneled Acoustic Live Room, Grand Piano & Isolated Booths", "tag": "Live Room"},
            {"file": r"Zen\studio1_02.jpg", "title": "Studio 1 at Suite Spot Studios: Commercial Motion & Photo Cyclorama Stage with Overhead Rigging", "tag": "Suite Spot Studio 1"},
            {"file": r"Zen\Plug Studio (12).jpg", "title": "Plug Studio: Commercial Audio Recording Suite, Mixing Console & Vocal Booth", "tag": "Audio Suite"},
            {"file": r"Zen\Suite Spot Studios (3).jpg", "title": "Suite Spot Studios: Turn-Key Studio Production Bay, Hair & Makeup Suites & Client Lounge", "tag": "Production Bay"}
        ]
    },
    {
        "id": "wine-country-historic-estates",
        "num": "09",
        "title": "Wine Country, Historic Estates & Farmland",
        "icon": "🍷",
        "doubles_as": "Tuscany / Italian Countryside · French Provence · Napa Valley · Historic English Countryside Manor",
        "hero_badge": "Scouted Database Match",
        "area": "Stellenbosch, Berg River Valley, Elgin & Banghoek Valley",
        "tagline": "Historic 18th-century Cape Dutch farmsteads with classic baroque gables, rolling hillside vineyards reflecting mountain lakes, oak-shaded cellar docks, and private forest amphitheaters.",
        "creative_synopsis": "The Cape Winelands deliver quintessential Old World European countryside within 45 minutes of Cape Town. Asara Wine Estate in Stellenbosch features rolling vineyard hills, tranquil private lakes reflecting jagged peaks, and traditional Cape Dutch hospitality buildings. Kersefontein Farmstead along the Berg River provides an intact 18th-century farm complex with whitewashed baroque gables, slave bell towers, and open wheat plains. Paul Cluver in Elgin offers cool-climate orchards and a forest amphitheater.",
        "hero_image_file": r"Farms\Wine Farms\Asara\Asara Wines (1).jpg",
        "hero_image_title": "Asara Wine Estate: Rolling Vineyards, Private Lake & Cape Dutch Cellar Architecture (Stellenbosch)",
        "key_features": [
            "Asara Wine Estate: Manicured vineyards, mountain-reflection lakes, barrel cellars, and boutique hotel rooms",
            "Kersefontein Historic Farmstead: 18th-century whitewashed manor, baroque gables, historic stables, and wheat plains",
            "Paul Cluver Wine Estate: Cool-climate apple orchards, pine forests, private dams, and an open-air forest amphitheater",
            "Zorgvliet Wine Estate: Dramatic location under the sheer rock precipices of the Simonsberg Mountains",
            "Extensive private agricultural land allowing pyrotechnics, drone tracking, and heavy unit base positioning"
        ],
        "specs": {
            "permitting": "Private Estate Filming Contracts (48 hr turnaround) · Local municipal drone clearance",
            "power": "3-Phase 63A/100A winery cellar docks · Mobile generator staging in farm courtyards",
            "parking": "Spacious paved hardstands and grass fields accommodating 30+ vehicle unit base fleets",
            "sound_curfew": "Quiet countryside setting · Zero residential noise restrictions on private acreage"
        },
        "gallery": [
            {"file": r"Farms\Wine Farms\Asara\Asara Wines (1).jpg", "title": "Asara Wine Estate: Manicured Vineyards, Calm Lake Reflection & Mountain Backdrop", "tag": "Hero Estate"},
            {"file": r"Farms\Wine Farms\Asara\Asara Wines (2).jpg", "title": "Asara Wine Estate: Classic Cape Dutch White Gabled Architecture & Waterfront Terrace", "tag": "Cape Dutch Manor"},
            {"file": r"Farms\Wine Farms\Asara\Asara Wines (11).jpg", "title": "Asara: Oak-Shaded Stone Courtyard & Boutique Hotel Hospitality Grounds", "tag": "Courtyard"},
            {"file": r"Farms\Wine Farms\Asara\Asara Wines (12).jpg", "title": "Asara: Rolling Hillside Vineyards & Panoramic Simonsberg Mountain Vista", "tag": "Vineyard Vista"},
            {"file": r"Farms\Kersefontein\WhatsApp Image 2026-08-06 at 13.50.13.jpeg", "title": "Kersefontein Farmstead: 18th-Century Cape Dutch Historic Manor House & Gables", "tag": "Kersefontein Manor"},
            {"file": r"Farms\Kersefontein\WhatsApp Image 2026-08-06 at 13.50.14.jpeg", "title": "Kersefontein: Historic White Stables, Farm Courtyard & Open Agricultural Plains", "tag": "Historic Stables"},
            {"file": r"Farms\Kersefontein\WhatsApp Image 2026-08-06 at 13.50.15 (1).jpeg", "title": "Kersefontein: Sprawling Berg River Farmland, Cattle Pastures & Countryside Horizons", "tag": "Open Farmland"},
            {"file": r"Farms\Paul Cluver\Paul Cluver (1).jpg", "title": "Paul Cluver Estate: Cool-Climate Vineyards, Pine Tree Belts & Mountain Dams", "tag": "Paul Cluver"},
            {"file": r"Farms\Paul Cluver\Paul Cluver (10).jpg", "title": "Paul Cluver: Timber Forest Amphitheater & Shaded Estate Lawns", "tag": "Forest Amphitheater"},
            {"file": r"Farms\Zorgvliet\Zorgvliet (1).jpg", "title": "Zorgvliet Wine Estate: Historic Cape Dutch Homestead Nestled Against Simonsberg Mountains", "tag": "Simonsberg Slopes"},
            {"file": r"Farms\Zorgvliet\Zorgvliet (5).jpg", "title": "Zorgvliet: Lush Vineyard Rows & Majestic Mountain Face", "tag": "Vineyard Rows"}
        ]
    },
    {
        "id": "civic-infrastructure-arenas",
        "num": "10",
        "title": "Civic Infrastructure, Institutional & Sports Arenas",
        "icon": "🏟️",
        "doubles_as": "International Olympic Training Facilities · Government Compounds · Private Airfields · Maximum Security Facilities",
        "hero_badge": "Scouted Database Match",
        "area": "Swartland Airfield, Green Point Stadium Precinct, Prisons & Paarl",
        "tagline": "Operational private tarmac runways with aircraft hangars, professional Olympic running tracks under stadium curves, heavy institutional prison corridors, and competition swimming pools.",
        "creative_synopsis": "Beyond scenic landscapes, South Africa offers large-scale institutional and civic infrastructure ready for major feature film productions. Diemerskraal Airfield provides a private operational tarmac runway and vintage hangars with total closure authority for vehicle tracking, stunt driving, and low-flying drone cinematography. The Green Point Track features an international running track situated right beneath Cape Town Stadium and Lion's Head. Disa Prison provides sterile, heavy security detention corridors and concrete towers.",
        "hero_image_file": r"Diemerskraal Airfield\Diemerskraal (1).jpg",
        "hero_image_title": "Diemerskraal Airfield: Operational Private Runway, Aircraft Hangars & Open Horizon Plains",
        "key_features": [
            "Diemerskraal Airfield: Private tarmac runway with vintage hangars, zero commercial flight delays, and stunt clearance",
            "Green Point Track: Professional synthetic running track with stadium bleachers beneath Cape Town Stadium",
            "Athlone Stadium: Multi-tiered civic sports stadium with spectator concourses and floodlighting",
            "Disa Prison: Heavy institutional architecture with watchtowers, razor wire perimeters, and secure interior corridors",
            "Olympic Municipal Pools: 50m outdoor competition pools in Paarl and Coetzenberg with starting blocks and grandstands"
        ],
        "specs": {
            "permitting": "Airfield: Private aviation contract · Sports/Prisons: Municipal and Department of Correctional Services clearance",
            "power": "Airfield: Mobile generator support · Stadiums/Prisons: Industrial 3-phase 100A–200A infrastructure",
            "parking": "Limitless airfield apron and stadium parking lots accommodating 50+ heavy support vehicles",
            "sound_curfew": "No noise restrictions at airfield · Controlled institutional filming schedules"
        },
        "gallery": [
            {"file": r"Diemerskraal Airfield\Diemerskraal (1).jpg", "title": "Diemerskraal Airfield: Private Tarmac Runway, Open Horizon & Aircraft Hangars", "tag": "Hero Runway"},
            {"file": r"Diemerskraal Airfield\Diemerskraal (6).jpg", "title": "Diemerskraal Airfield: Corrugated Aircraft Hangar & Maintenance Apron", "tag": "Hangar Apron"},
            {"file": r"Diemerskraal Airfield\Diemerskraal (10).jpg", "title": "Diemerskraal: Wide Runway Tracking Corridor with Zero Flight Obstructions", "tag": "Runway Corridor"},
            {"file": r"Stadia\Greenpoint Track\Greenpoint Track (1).jpg", "title": "Green Point Track: Olympic Running Track Beneath Iconic Curves of Cape Town Stadium & Lion's Head", "tag": "Running Track"},
            {"file": r"Stadia\Athlone Stadium\Athlone Stadium (1).jpg", "title": "Athlone Stadium: Grandstand Seating, Floodlight Towers & Professional Turf Pitch", "tag": "Sports Stadium"},
            {"file": r"Prisons\Disa Prison-Tygerberg (3).jpg", "title": "Disa Prison: Heavy Security Razor-Wire Perimeter Fence & Watchtower", "tag": "Prison Perimeter"},
            {"file": r"Prisons\Disa Prison-Tygerberg (4).jpg", "title": "Disa Prison: Institutional Concrete Guard Station & Barred Gate Security Access", "tag": "Security Checkpoint"},
            {"file": r"Prisons\Disa Prison-Tygerberg (5).jpg", "title": "Disa Prison: Institutional Corridors, Steel Gates & Sterile Facility Architecture", "tag": "Cell Block Corridor"},
            {"file": r"Municipal Pools\Coetzenberg\Coetzenberg (1).jpg", "title": "Coetzenberg Olympic Pool: 50m Competition Outdoor Pool & Spectator Grandstand", "tag": "Olympic Pool"},
            {"file": r"Municipal Pools\Forest Pool-Paarl\Forest Pool-Paarl (1).jpg", "title": "Forest Pool Paarl: Outdoor Public Swimming Arena Surrounded by Trees & Green Lawns", "tag": "Paarl Pool"},
            {"file": r"Municipal Pools\Paarl East\Paarl East (1).jpg", "title": "Paarl East Pool: Olympic Swimming Lanes, Diving Blocks & Bleacher Seating", "tag": "Competition Lanes"}
        ]
    }
]

# Process and encode all images
embedded_images = {}
total_images = sum(1 + len(cat["gallery"]) for cat in categories)
processed = 0

for cat in categories:
    # Encode hero
    hero_path = cat["hero_image_file"]
    if hero_path not in embedded_images:
        b64 = encode_img(hero_path, max_size=(1150, 750), quality=76)
        embedded_images[hero_path] = b64
        processed += 1
        print(f"[{processed}/{total_images}] Encoded Hero: {hero_path}")
    
    # Encode gallery
    for item in cat["gallery"]:
        gpath = item["file"]
        if gpath not in embedded_images:
            b64 = encode_img(gpath, max_size=(960, 640), quality=74)
            embedded_images[gpath] = b64
            processed += 1
            print(f"[{processed}/{total_images}] Encoded Gallery: {gpath}")

# Save to embedded_data.json
data = {
    "categories": categories,
    "images": embedded_images
}

data_path = os.path.join(output_dir, "embedded_data.json")
with open(data_path, "w", encoding="utf-8") as f:
    json.dump(data, f)

print(f"\nSuccessfully encoded {len(embedded_images)} master assets into {data_path}!")
print(f"JSON size: {os.path.getsize(data_path) / (1024*1024):.2f} MB")
