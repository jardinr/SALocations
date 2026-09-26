import os
import json
import base64
import io
import re
from PIL import Image

ref_dir = r"C:\Users\Jardin\OneDrive\Pictures\Zen\chinni loc refs"
zen_dir = r"C:\Users\Jardin\OneDrive\Pictures\Zen"
web_dir = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\zen-mirage-media-web"

os.makedirs(web_dir, exist_ok=True)

def encode_img(path, max_size=(1200, 800), quality=80):
    if not os.path.exists(path):
        print(f"Warning: {path} not found!")
        return ""
    try:
        with Image.open(path) as im:
            im = im.convert("RGB")
            im.thumbnail(max_size, Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            im.save(buf, format="JPEG", quality=quality)
            return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")
    except Exception as e:
        print(f"Error encoding {path}: {e}")
        return ""

# Define the 9 categories
categories = [
    {
        "id": "live-music-cafe",
        "num": "01",
        "title": "Live Music Cafe & Supper Club",
        "icon": "☕",
        "ref_heading": "Director's Visual Reference · Live Music Venue & Dining Terrace",
        "match_heading": "Cape Town Match · Stardust Theatrical Dining (Woodstock)",
        "match_score": "98% Match",
        "area": "Woodstock / City Fringe, Cape Town",
        "tagline": "Atmospheric cabaret supper club pairing vibrant red theatrical stage lighting, piano & acoustic performance setups, and seated dinner tables with outdoor daytime dining options.",
        "creative_synopsis": "The director's reference calls for an authentic live performance venue with immersive red/amber stage lighting where patrons dine while an acoustic act or singer performs on an intimate stage. Stardust in Woodstock delivers an exact real-world match — complete with theatrical lighting rigs, cabaret tables, acoustic piano, and a vibrant artistic envelope.",
        "ref_hero": "cafe w live music.jpg",
        "ref_hero_title": "Director Reference: Intimate Red-Lit Cabaret Supper Club with Singer & Stage",
        "scouted_hero": "Stardust (8).jpg",
        "scouted_hero_title": "Stardust Theatrical Dining: Full Interior Perspective with Red Stage Rig & Cabaret Seating",
        "key_features": [
            "Raised performance stage with professional acoustic PA system & intelligent red/amber lighting rigs",
            "Atmospheric tiered dining floor accommodating an intimate seated audience of 60–120 patrons",
            "Grand piano, acoustic microphone setups, and warm theatrical ambient glow",
            "Dedicated bar counter and backstage green room area for cast and wardrobe staging",
            "Daytime outdoor cafe deck and courtyard options available within Woodstock creative precinct"
        ],
        "specs": {
            "permitting": "Private Commercial Contract · Direct Home/Venue Agreement (48-hr turnaround)",
            "power": "3-Phase 63A Power On-Site · Domestic 16A Distributed Distribution Tie-Ins",
            "parking": "Dedicated secure gated parking for 6 technical vans + side-street production truck staging",
            "sound_curfew": "Acoustically treated interior venue · Evening shoot permissions available with late wrap"
        },
        "gallery": [
            {"file": "cafe w live music.jpg", "source": "ref", "title": "Director Ref: Cabaret Stage, Live Singer & Seated Dining Audience", "cat": "ref"},
            {"file": "cafe w live music2.jpeg", "source": "ref", "title": "Director Ref: Sunny Outdoor Wooden Cafe Deck with Umbrellas", "cat": "ref"},
            {"file": "cafe w live music3.jpeg", "source": "ref", "title": "Director Ref: Bustling Public Plaza Cafe Terrace & Patio", "cat": "ref"},
            {"file": "Stardust (8).jpg", "source": "scouted", "title": "Stardust Theatrical Dining: Stage Perspective & Dining Floor", "cat": "scouted"},
            {"file": "Stardust (3).jpg", "source": "scouted", "title": "Stardust: Red Stage Lighting, Cabaret Tables & Theatrical Backdrop", "cat": "scouted"},
            {"file": "Stardust (6).jpg", "source": "scouted", "title": "Stardust: Live Acoustic Performance Corner & Stage Lighting", "cat": "scouted"},
            {"file": "Stardust (9).jpg", "source": "scouted", "title": "Stardust: Intimate Seating Perspective with Ambient Lighting Rig", "cat": "scouted"},
            {"file": "Stardust (12).jpg", "source": "scouted", "title": "Stardust: Wide Floor Architecture & Ceiling Lighting Truss", "cat": "scouted"}
        ]
    },
    {
        "id": "cast-drive",
        "num": "02",
        "title": "Cast Drive · Coastal Scenic Highway",
        "icon": "🚗",
        "ref_heading": "Director's Visual Reference · Winding Sea-Cliff Ocean Highway",
        "match_heading": "Cape Town Match · Chapman's Peak Drive (M6) & Victoria Road",
        "match_score": "99% Match",
        "area": "Hout Bay to Noordhoek / Atlantic Seaboard, Cape Town",
        "tagline": "World-renowned winding coastal highway carved into sheer vertical sea-cliffs, offering breathtaking panoramic Atlantic ocean views, cantilever passes, and scenic vehicle tracking corridors.",
        "creative_synopsis": "The visual reference features an iconic coastal road trip scene: a winding tarmac highway carved into sea cliffs with mountain headlands rising behind deep turquoise waters. Chapman's Peak Drive (M6) is widely recognized as one of the most cinematic coastal drives on the planet, offering full-day rolling road closures, camera tracking vehicle permits, and dedicated helicopter/drone clearance.",
        "ref_hero": "cast drive.jpeg",
        "ref_hero_title": "Director Reference: Winding Cliffside Ocean Highway with Mountain Headland",
        "scouted_hero": "Chapmans Peak (91).jpg",
        "scouted_hero_title": "Chapman's Peak Drive: Golden Hour Coastal Curve Hugging Atlantic Sea Cliffs",
        "key_features": [
            "Sweeping coastal turns directly cantilevered over the crashing Atlantic Ocean surf",
            "Long uninterrupted tarmac stretches perfect for Russian Arm and tracking vehicle runs",
            "Designated paved laybys and lookout points for camera cranes, tripod setups, and basecamp",
            "Sunset and sunrise golden hour directional lighting along the western mountain face",
            "City of Cape Town Film Permit Office & Entilini Concession official closure protocol support"
        ],
        "specs": {
            "permitting": "City of Cape Town Film Office + Entilini Road Concession + SANParks (5-day notice)",
            "power": "Mobile Generator Truck Staging required at designated scenic laybys",
            "parking": "Dedicated wide lookout laybys for 8+ tech vehicles; basecamp at Hout Bay or Noordhoek farm",
            "sound_curfew": "Natural oceanic soundscape · Intermittent road traffic control available during shoot blocks"
        },
        "gallery": [
            {"file": "cast drive.jpeg", "source": "ref", "title": "Director Ref: Winding Coastal Highway Hugging Ocean Sea Cliffs", "cat": "ref"},
            {"file": "Chapmans Peak (91).jpg", "source": "scouted", "title": "Chapman's Peak: Dramatic Sunset Coastal Tarmac Run", "cat": "scouted"},
            {"file": "Chapmans Peak (57).jpg", "source": "scouted", "title": "Chapman's Peak: Sweeping Cliff Curve Overlooking Hout Bay", "cat": "scouted"},
            {"file": "Chapmans Peak (71).jpg", "source": "scouted", "title": "Chapman's Peak: Half-Tunnel Cantilever Pass & Sheer Mountain Wall", "cat": "scouted"},
            {"file": "Chapmans Peak (78).jpg", "source": "scouted", "title": "Chapman's Peak: Elevated Lookout Vista over Horizon Ocean", "cat": "scouted"},
            {"file": "Chapmans Peak South Lookout (5).jpg", "source": "scouted", "title": "South Lookout: Paved Staging Platform for Crane & Tracking Vehicles", "cat": "scouted"},
            {"file": "M6-to CB (0).jpg", "source": "scouted", "title": "Victoria Road (M6): Coastal Approach Toward Twelve Apostles & Camps Bay", "cat": "scouted"},
            {"file": "M6-to CB (1).jpg", "source": "scouted", "title": "Victoria Road: Coastal Tarmac Hugging Rocky Atlantic Shoreline", "cat": "scouted"},
            {"file": "M6-to CB (7).jpg", "source": "scouted", "title": "Victoria Road: Open Ocean Highway Corridor for Camera Chase Vehicle", "cat": "scouted"}
        ]
    },
    {
        "id": "hero-house",
        "num": "03",
        "title": "Hero House & Character Residence",
        "icon": "🏡",
        "ref_heading": "Director's Visual Reference · Mountainside Coastal Timber Cabin & Heritage Cottage",
        "match_heading": "Cape Town Match · Amara Moon (Camps Bay) / Hexagon House / Vicki",
        "match_score": "96% Match",
        "area": "Camps Bay / Llandudno / Gardens, Cape Town",
        "tagline": "Two complementary residential aesthetics: an elevated coastal timber stilt-villa with expansive ocean-view wooden decks, alongside heritage character cottages framed by Table Mountain.",
        "creative_synopsis": "The director's references capture two distinct residential options: (A) an elevated timber-clad coastal beach house perched in mountainside fynbos with panoramic bay vistas, and (B) a charming urban character cottage with heritage gables and mountain backdrops. Zencrew has pre-screened both aesthetics in Cape Town's premier filming zones (Amara Moon in Camps Bay, Hexagon House in Llandudno, and Vicki in Gardens).",
        "ref_hero": "house.jpg",
        "ref_hero_title": "Director Reference: Elevated Mountainside Timber Beach House with Bay Views",
        "scouted_hero": "Amara Moon (2).jpg",
        "scouted_hero_title": "Amara Moon (Camps Bay): Coastal Architectural Residence with Panoramic Ocean Deck",
        "key_features": [
            "Expansive timber sun decks overlooking the Atlantic ocean and coastal mountain peaks",
            "Floor-to-ceiling glass doors creating seamless interior-to-exterior camera tracking",
            "Open-plan living rooms with rich natural daylight, timber floors, and contemporary character",
            "Urban heritage cottage alternatives in Gardens/Oranjezicht with decorative gables and mountain views",
            "Private paved forecourts and secure driveways for equipment and technical vehicles"
        ],
        "specs": {
            "permitting": "Residential Location Agreement · Film-friendly private homeowners",
            "power": "Domestic 63A Distribution Tie-Ins · Silent Generator parking on driveway",
            "parking": "Private driveway accommodates 4 technical vans; quiet residential street parking",
            "sound_curfew": "Standard residential curfew (22:00 wrap) · Exceptional acoustic privacy"
        },
        "gallery": [
            {"file": "house.jpg", "source": "ref", "title": "Director Ref: Mountainside Timber Stilt House with Panoramic Ocean Vista", "cat": "ref"},
            {"file": "house2.jpeg", "source": "ref", "title": "Director Ref: Urban Heritage Cottage with Gable Wall & Mountain Peak", "cat": "ref"},
            {"file": "Amara Moon (2).jpg", "source": "scouted", "title": "Amara Moon: Elevated Deck with Panoramic Atlantic Ocean Views", "cat": "scouted"},
            {"file": "Amara Moon (4).jpg", "source": "scouted", "title": "Amara Moon: Contemporary Exterior Architecture Nestled into Slope", "cat": "scouted"},
            {"file": "Hexagon (4).jpg", "source": "scouted", "title": "Hexagon House: Multi-Level Coastal Villa & Pool Terrace", "cat": "scouted"},
            {"file": "Hexagon (5).jpg", "source": "scouted", "title": "Hexagon House: Outdoor Entertainment Terrace Overlooking Bay", "cat": "scouted"},
            {"file": "Hexagon (6).jpg", "source": "scouted", "title": "Hexagon House: Light-Filled Living Room with Ocean Horizons", "cat": "scouted"},
            {"file": "Vicki (22).JPG", "source": "scouted", "title": "Vicki Residence: Character Living Lounge with Warm Directional Light", "cat": "scouted"},
            {"file": "Rosemount Ave-Gardens (4).jpg", "source": "scouted", "title": "Rosemount Ave: Heritage Cottage Facade with Mountain Backdrop in Gardens", "cat": "scouted"}
        ]
    },
    {
        "id": "mountain-bike-trail",
        "num": "04",
        "title": "Mountain Bike Trail & Scenic Passes",
        "icon": "🚵",
        "ref_heading": "Director's Visual Reference · Mountain Single-Track Ridge & Coastal Pass",
        "match_heading": "Cape Town Match · Deer Park (Table Mountain) & Lourensford Trails",
        "match_score": "97% Match",
        "area": "Table Mountain National Park / Somerset West, Cape Town",
        "tagline": "Pristine mountain biking single-track trails along coastal mountain contours, pine forest canopies, and elevated gravel passes overlooking the ocean.",
        "creative_synopsis": "The reference photos showcase high-energy mountain biking along scenic dirt single-tracks perched above the ocean, alongside road cycling curves overlooking coastal bays. Table Mountain's Deer Park network and the private Lourensford Estate offer premier flow trails, banked berms, gravel fire roads, and dramatic mountain backdrops with easy technical crew vehicle access.",
        "ref_hero": "mountain bike trail.jpeg",
        "ref_hero_title": "Director Reference: Dirt Mountain Bike Single-Track Overlooking Atlantic Ocean",
        "scouted_hero": "Deer Park (2).jpg",
        "scouted_hero_title": "Deer Park (Table Mountain): Scenic Forest Single-Track with City & Bay Panorama",
        "key_features": [
            "Pristine dirt single-track trails and gravel fire roads traversing mountain slopes",
            "Spectacular elevated camera vantage points overlooking Table Mountain and the Atlantic ocean",
            "Lourensford private estate provides controlled filming terrain without public hiker interference",
            "Diverse terrain: fast flowing single-tracks, rocky technical descents, and pine forest switchbacks",
            "Vehicle-accessible service roads allowing chase quads, e-bikes, and stabilized camera rigs"
        ],
        "specs": {
            "permitting": "SANParks Commercial Permit (Table Mountain) or Private Estate Film Agreement (Lourensford)",
            "power": "Mobile battery base and silent towable generator for remote trail sections",
            "parking": "Dedicated trailhead gravel parking lot accommodating 10+ production trucks",
            "sound_curfew": "100% natural acoustic environment · Zero urban or commercial sound intrusion"
        },
        "gallery": [
            {"file": "mountain bike trail.jpeg", "source": "ref", "title": "Director Ref: Mountain Bike Single-Track Ridge with Coastal View", "cat": "ref"},
            {"file": "mountain bike trail2.jpeg", "source": "ref", "title": "Director Ref: Road Cyclists on Mountain Pass Overlooking Deep Bay", "cat": "ref"},
            {"file": "Deer Park (2).jpg", "source": "scouted", "title": "Deer Park: Single-Track Trail under Pine Canopy Overlooking Cape Town", "cat": "scouted"},
            {"file": "Deer Park (24).jpg", "source": "scouted", "title": "Deer Park: Forest Mountain Contour Path & Dirt Berms", "cat": "scouted"},
            {"file": "Lourensford trails (5).jpg", "source": "scouted", "title": "Lourensford Trails: Wide Gravel Mountain Track with Mountain Peaks", "cat": "scouted"},
            {"file": "Lourensford trails (14).jpg", "source": "scouted", "title": "Lourensford Trails: Flowing Single-Track Berm with Expansive Vistas", "cat": "scouted"}
        ]
    },
    {
        "id": "mountainside-shack",
        "num": "05",
        "title": "Mountainside Shack · Off-Grid Cabin",
        "icon": "🛖",
        "ref_heading": "Director's Visual Reference · Isolated Rugged Cabin on Rocky Mountain Slope",
        "match_heading": "Cape Town Match · Monkey Valley Nature Resort & Imhoff's Gift",
        "match_score": "95% Match",
        "area": "Noordhoek / Kommetjie Coastal Belt, Cape Town",
        "tagline": "Off-grid, rustic timber and stone cabins tucked into wild mountain milkwood forests and coastal fynbos slopes with sweeping ocean and wetland vistas.",
        "creative_synopsis": "The director's references depict a remote, off-the-grid hideout — a weathered stone or wooden shack perched on a steep wild mountain slope beneath rocky crags. Monkey Valley in Noordhoek and private coastal cabins in Imhoff's Gift (Kommetjie) provide this exact cinematic isolation, offering log and stone architecture, organic timber decks, and dramatic natural backdrops.",
        "ref_hero": "mountainside shack.jpg",
        "ref_hero_title": "Director Reference: Isolated Off-Grid Stone Cabin on Wild Coastal Mountain Slope",
        "scouted_hero": "Monkey Valley.png",
        "scouted_hero_title": "Monkey Valley (Noordhoek): Wooden Treetop Cabins Embedded in Mountain Forest",
        "key_features": [
            "Authentic rustic timber, log cabin, and weathered stone architectural finishes",
            "Perched positions surrounded by indigenous coastal milkwood forest and fynbos slopes",
            "Remote, off-the-beaten-track atmosphere while remaining within 45 minutes of Cape Town CBD",
            "Panoramic views over Noordhoek Beach, Chapman's Peak, and coastal salt marshes",
            "Established hospitality infrastructure with cast lodging, catering, and unit base support on-site"
        ],
        "specs": {
            "permitting": "Private Property Commercial Agreement · Film-supportive management",
            "power": "On-site 3-phase grid power with heavy-duty extension capability to cabin perimeters",
            "parking": "Spacious paved and gravel parking area for unit base, technical trucks, and catering",
            "sound_curfew": "Quiet coastal nature reserve zone · Birdsong and ocean surf ambience"
        },
        "gallery": [
            {"file": "mountainside shack.jpg", "source": "ref", "title": "Director Ref: Isolated Cabin on Rocky Mountain Slope with Wind Turbine", "cat": "ref"},
            {"file": "mountainside shack2.jpg", "source": "ref", "title": "Director Ref: Weathered Timber Cabin Beneath Sheer Mountain Cliff", "cat": "ref"},
            {"file": "Monkey Valley.png", "source": "scouted", "title": "Monkey Valley: Rustic Wooden Mountain Cabins under Milkwood Canopy", "cat": "scouted"},
            {"file": "Imhoff's Gift (18).jpg", "source": "scouted", "title": "Imhoff's Gift: Secluded Coastal Wooden Retreat with Mountain Views", "cat": "scouted"},
            {"file": "Imhoff's Gift (20).jpg", "source": "scouted", "title": "Imhoff's Gift: Timber & Stone Cabin Exterior in Fynbos Setting", "cat": "scouted"},
            {"file": "Imhoff's Gift (21).jpg", "source": "scouted", "title": "Imhoff's Gift: Rustic Covered Deck Looking Over Wetlands & Mountains", "cat": "scouted"}
        ]
    },
    {
        "id": "nightclub-venue",
        "num": "06",
        "title": "Nightclub · Music Venue · Beach Lounge",
        "icon": "🍸",
        "ref_heading": "Director's Visual Reference · High-Energy Club Dancefloor & Neon Beach Lounge",
        "match_heading": "Cape Town Match · Club Destiny & Club Halo (CBD) / Café Caprice",
        "match_score": "98% Match",
        "area": "CBD Nightlife Strip & Camps Bay Promenade, Cape Town",
        "tagline": "Vibrant nightlife environments featuring immersive neon stage lighting, packed dancefloors, live DJ booths, intimate VIP booths, and Camps Bay beachfront cocktail culture.",
        "creative_synopsis": "The visual brief calls for a dual nightlife identity: an intense, crowded club dancefloor with red/blue intelligent laser and beam lighting, live DJ/stage performance, alongside a chic beachfront neon lounge. Club Destiny and Club Halo in Cape Town CBD provide high-end club infrastructure with full DMX lighting control, while Café Caprice on Camps Bay strip matches the sunset-to-night beachfront lounge vibe.",
        "ref_hero": "nightclub.jpeg",
        "ref_hero_title": "Director Reference: Mood-Lit Club Bar with Live Performance & Warm Seating",
        "scouted_hero": "Club Destiny (1).JPG",
        "scouted_hero_title": "Club Destiny: Main Dancefloor with Intelligent Stage Lighting & DJ Enclosure",
        "key_features": [
            "Fully programmed DMX club lighting rigs, laser beams, LED ceiling grids, and haze machines",
            "Raised DJ performance stage and acoustic PA systems ready for music video or drama playback",
            "Plush VIP leather banquette seating, private cocktail bar counters, and mood-lit corridors",
            "Beachfront lounge exterior option on Camps Bay strip (Café Caprice) with sunset terrace",
            "Dedicated day-for-night blackout capabilities and late-night shoot authorizations"
        ],
        "specs": {
            "permitting": "Private Commercial Contract · Direct Club Management Partner (Daytime & night access)",
            "power": "High-Capacity 3-Phase 100A+ Commercial Power Tie-Ins On-Site",
            "parking": "City of Cape Town street parking reserved for technical vehicles and gear trucks",
            "sound_curfew": "Full soundproof acoustic interior · 24/7 filming and high-volume playback permitted"
        },
        "gallery": [
            {"file": "nightclub.jpeg", "source": "ref", "title": "Director Ref: Intimate Club Bar with Live Performance & Amber Glow", "cat": "ref"},
            {"file": "nightclub2.jpeg", "source": "ref", "title": "Director Ref: Packed Nightclub Dancefloor with Red/Blue Laser Beams", "cat": "ref"},
            {"file": "nightclub3.jpeg", "source": "ref", "title": "Director Ref: Neon Beachfront Bar Exterior at Dusk (Café Caprice, Camps Bay)", "cat": "ref"},
            {"file": "Club Destiny (1).JPG", "source": "scouted", "title": "Club Destiny: Main Dancefloor & Intelligent Stage Lighting Grid", "cat": "scouted"},
            {"file": "Club Destiny (4).JPG", "source": "scouted", "title": "Club Destiny: VIP Banquette Lounge with Mood Lighting", "cat": "scouted"},
            {"file": "Club Destiny (7).JPG", "source": "scouted", "title": "Club Destiny: Back-Lit Cocktail Bar & Intimate Lounge", "cat": "scouted"},
            {"file": "Club Destiny (8).JPG", "source": "scouted", "title": "Club Destiny: Performance Stage with Concert Sound Rigs", "cat": "scouted"},
            {"file": "Club Halo (8).jpg", "source": "scouted", "title": "Club Halo: Immersive LED Ceiling Arrays & Underground Club Atmosphere", "cat": "scouted"},
            {"file": "Club Halo (20).jpg", "source": "scouted", "title": "Club Halo: Private Mezzanine VIP Bar & Banquettes", "cat": "scouted"},
            {"file": "Club Halo (37).jpg", "source": "scouted", "title": "Club Halo: Main Floor Crowd Perspective with Blue Strobe Lighting", "cat": "scouted"}
        ]
    },
    {
        "id": "rehearsal-space",
        "num": "07",
        "title": "Rehearsal Space · Industrial Creative Lofts",
        "icon": "🎸",
        "ref_heading": "Director's Visual Reference · High-Ceiling Warehouse Loft with Factory Grid Windows",
        "match_heading": "Cape Town Match · Woodstock & Salt River Creative Industrial Studios",
        "match_score": "97% Match",
        "area": "Woodstock / Salt River Heritage Creative Hub, Cape Town",
        "tagline": "Expansive industrial studio spaces with polished wooden parquet floors, high whitewashed walls, industrial multi-pane steel windows, and exposed ceiling beams.",
        "creative_synopsis": "The director's references specify a spacious, authentic artist loft or band rehearsal room — defined by high ceilings, natural daylight pouring through industrial steel-frame grid windows, and timber parquet or polished concrete flooring. The creative warehouse lofts of Woodstock and Salt River provide this exact raw artistic texture, with easy ground-floor load-in for production gear.",
        "ref_hero": "rehearsal space.jpeg",
        "ref_hero_title": "Director Reference: Industrial Studio with Parquet Floors, White Brick & Studio Rigging",
        "scouted_hero": "IMG_5256.JPG",
        "scouted_hero_title": "Woodstock Creative Loft: Open Wooden Floor Plan & High Whitewashed Industrial Walls",
        "key_features": [
            "Authentic industrial multi-pane steel sash windows delivering soft directional natural daylight",
            "Polished timber parquet and sealed concrete floors supporting dance, band gear, and camera tracks",
            "Exposed steel roof trusses and ceiling piping for hanging lighting rigs and acoustic baffles",
            "Surrounding heritage brick factory facades and cobblestone streets in Culver and Chatham Streets",
            "Dedicated 3-phase power, drive-in roller shutter access, and production staging areas"
        ],
        "specs": {
            "permitting": "Private Commercial Creative Studio Agreement + City Film Office for street parking",
            "power": "3-Phase 63A Distribution On-Site with multiple 16A single-phase drops",
            "parking": "Drive-in equipment access with private courtyard loading bays; street parking for unit base",
            "sound_curfew": "Creative industrial precinct · High tolerance for live music and rehearsal playback"
        },
        "gallery": [
            {"file": "rehearsal space.jpeg", "source": "ref", "title": "Director Ref: Industrial Loft Studio with Parquet Flooring & Pipe Rigs", "cat": "ref"},
            {"file": "rehearsal space2.webp", "source": "ref", "title": "Director Ref: High Warehouse Studio with Factory Grid Windows & Skylight", "cat": "ref"},
            {"file": "IMG_5256.JPG", "source": "scouted", "title": "Woodstock Studio: Open Creative Floor Plan with Natural Window Daylight", "cat": "scouted"},
            {"file": "IMG_5253.JPG", "source": "scouted", "title": "Woodstock Studio: High Industrial Walls & Structural Wooden Flooring", "cat": "scouted"},
            {"file": "IMG_5259.JPG", "source": "scouted", "title": "Woodstock Studio: Exposed Brickwork & Overhead Industrial Beams", "cat": "scouted"},
            {"file": "Culver St (1).jpg", "source": "scouted", "title": "Culver Street: Heritage Industrial Brick Factory Exterior in Salt River", "cat": "scouted"},
            {"file": "Culver St (2).jpg", "source": "scouted", "title": "Culver Street: Industrial Facade with Wide Loading Access Doors", "cat": "scouted"},
            {"file": "Culver St (3).jpg", "source": "scouted", "title": "Culver Street: Quiet Side-Street Staging for Unit Base & Trucks", "cat": "scouted"},
            {"file": "Chatham St (2).jpg", "source": "scouted", "title": "Chatham Street: Urban Character Streetscape in Woodstock Creative District", "cat": "scouted"}
        ]
    },
    {
        "id": "shopping-centre",
        "num": "08",
        "title": "Shopping Centre · Public Commercial Piazza",
        "icon": "🛍️",
        "ref_heading": "Director's Visual Reference · Neo-Classical Shopping Square with Clock Tower & Cafes",
        "match_heading": "Cape Town Match · V&A Waterfront (Clock Tower Precinct & Quayside)",
        "match_score": "96% Match",
        "area": "Victoria & Alfred Waterfront, Cape Town Harbor",
        "tagline": "Historic neo-classical waterfront shopping promenade, central Victorian clock tower, pedestrian piazzas, open-air cafe terraces, and bustling quayside backdrops.",
        "creative_synopsis": "The reference visual features an upscale commercial lifestyle destination with an ornate clock tower, stone colonnades, open-air cafe seating, and public pedestrian piazzas. The V&A Waterfront — South Africa's most visited cultural and retail destination — perfectly embodies this aesthetic through its iconic red Victorian Clock Tower, historic swing bridge, and bustling quayside promenades.",
        "ref_hero": "shopping centre.jpeg",
        "ref_hero_title": "Director Reference: Neo-Classical Commercial Piazza with Clock Tower & Outdoor Cafes",
        "scouted_hero": "V&A Waterfront (3).jpg",
        "scouted_hero_title": "V&A Waterfront: Pedestrian Shopping Promenade with Table Mountain Backdrop",
        "key_features": [
            "Iconic Victorian red Clock Tower (1882) and historic working dry-dock maritime backdrops",
            "Expansive pedestrian plazas and quayside shopping promenades lined with cafes and boutiques",
            "Sweeping unobstructed views of Table Mountain, Lion's Head, and the working Atlantic harbor",
            "Established filming infrastructure with 24/7 security, crowd management, and underground parking",
            "Controlled early morning and evening filming windows for high-production-value public scenes"
        ],
        "specs": {
            "permitting": "V&A Waterfront Filming Protocol + City Film Office (Coordinated by Zencrew)",
            "power": "Extensive commercial 3-phase and domestic shore-power hookups throughout precinct",
            "parking": "Multi-storey secure underground parking structures accommodating large crew fleets",
            "sound_curfew": "Active retail & harbor environment · Filming permitted during standard and off-peak trading"
        },
        "gallery": [
            {"file": "shopping centre.jpeg", "source": "ref", "title": "Director Ref: Commercial Shopping Piazza with Clock Tower & Outdoor Seating", "cat": "ref"},
            {"file": "V&A Waterfront (3).jpg", "source": "scouted", "title": "V&A Waterfront: Pedestrian Shopping Promenade with Table Mountain", "cat": "scouted"},
            {"file": "V&A Waterfront (2).jpg", "source": "scouted", "title": "V&A Waterfront: Historic Red Clock Tower & Harbor Quayside Walkway", "cat": "scouted"},
            {"file": "V&A Waterfront (31).jpg", "source": "scouted", "title": "V&A Waterfront: Bustling Commercial Amphitheatre & Pedestrian Plaza", "cat": "scouted"},
            {"file": "V&A Waterfront (32).jpg", "source": "scouted", "title": "V&A Waterfront: Open-Air Quayside Dining with Umbrella Seating", "cat": "scouted"},
            {"file": "V&A Waterfront (35).jpg", "source": "scouted", "title": "V&A Waterfront: Colonnaded Walkway Overlooking Working Harbor", "cat": "scouted"}
        ]
    },
    {
        "id": "film-studios",
        "num": "09",
        "title": "Film Studios · Soundstages & Recording Facilities",
        "icon": "🎬",
        "ref_heading": "Production Facility Brief · Soundstages, Cycloramas & Sound Recording Facilities",
        "match_heading": "Cape Town Facilities · Roodebloem, Studio 107, Milestone & Plug Studios",
        "match_score": "100% Match",
        "area": "Woodstock, CBD, Maitland & Somerset West, Cape Town",
        "tagline": "Comprehensive studio infrastructure spanning daylight photo/film studios, acoustic soundproof broadcast soundstages, infinity cycloramas, and multi-track music/ADR recording rooms.",
        "creative_synopsis": "To support full-scale feature film production, ADR, music scoring, and controlled interior set builds, Zencrew has assembled Cape Town's premier production facilities. This includes Roodebloem Studios (historic daylight cycloramas in converted church), Studio 107 (dedicated soundstage), Milestone Studios (premier orchestral & ADR recording with grand piano), Plug Studio & Suite Spot (audio tracking), Forest Studio (nature-inspired tracking), and large-scale studio soundstages (CTFS & Atlantic).",
        "ref_hero": "Roodebloem Studios (2).jpg",
        "ref_hero_title": "Roodebloem Studios: High-Ceilinged Infinity Cyclorama Film Stage",
        "scouted_hero": "Milstone Studios (3).jpg",
        "scouted_hero_title": "Milestone Studios: Main Live Recording Room & Grand Piano for Film Scoring & ADR",
        "key_features": [
            "Roodebloem Studios: World-renowned daylight and infinity curve cyclorama studios in Woodstock",
            "Studio 107: Soundproof broadcast soundstage with overhead lighting grids and drive-in access",
            "Milestone Studios (CBD): Cape Town's flagship film scoring, ADR, and multi-track audio suite",
            "Plug Studio & Suite Spot: Modern tracking, live rehearsal, and voiceover isolation booths",
            "UCT Recording Studio: Symphonic concert acoustics suitable for live orchestral and choir scoring",
            "Forest Studio: Peaceful wooden creative sanctuary in nature for artist development and rehearsals",
            "Full Soundstages: Direct partnerships with Cape Town Film Studios & Atlantic Film Studios for massive set builds"
        ],
        "specs": {
            "permitting": "Direct Studio Booking Contract (Preferential rates secured via Zencrew)",
            "power": "Industrial 3-Phase 125A–400A Soundstage Power Tie-Ins · Silent HVAC systems",
            "parking": "Secure on-site private production parking, makeup rooms, green rooms, and production offices",
            "sound_curfew": "Full acoustic soundproofing · 24-hour round-the-clock filming and live audio recording"
        },
        "gallery": [
            {"file": "Roodebloem Studios (2).jpg", "source": "scouted", "title": "Roodebloem Studios: Heritage Church Converted to High-End Daylight Film Studio", "cat": "scouted"},
            {"file": "Studio 107 (6).jpg", "source": "scouted", "title": "Studio 107: Soundproof Film Production Soundstage & Overhead Lighting Grid", "cat": "scouted"},
            {"file": "Milstone Studios (3).jpg", "source": "scouted", "title": "Milestone Studios: Flagship Acoustic Live Room with Grand Piano & ADR Suite", "cat": "scouted"},
            {"file": "Plug Studio (12).jpg", "source": "scouted", "title": "Plug Studio: Professional Band Rehearsal & Multi-Track Audio Suite", "cat": "scouted"},
            {"file": "Suite Spot Studios (3).jpg", "source": "scouted", "title": "Suite Spot Studios: Acoustic Mixing, Voiceover & Tracking Booth", "cat": "scouted"},
            {"file": "UCT-Rec Studio (8).jpg", "source": "scouted", "title": "UCT Recording Studio: Symphonic Concert Acoustic Hall for Film Orchestras", "cat": "scouted"},
            {"file": "Forest Studio (7).jpg", "source": "scouted", "title": "Forest Studio: Timber Acoustic Creative Studio in Natural Forest Setting", "cat": "scouted"},
            {"file": "Forest Studio (16).jpg", "source": "scouted", "title": "Forest Studio: Creative Workspace & Rehearsal Lounge in Nature", "cat": "scouted"},
            {"file": "studio1_02.jpg", "source": "scouted", "title": "Studio 1: White Infinity Cyclorama Soundstage for Controlled Set Builds", "cat": "scouted"}
        ]
    }
]

print("Category definitions ready. Total categories:", len(categories))
