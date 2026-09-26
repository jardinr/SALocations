# Film Location Scouting & Photo Comparison Standards

This document establishes the mandatory protocol for analyzing, comparing, categorizing, and presenting location scouting photographs and director visual references for SA Locations & Zencrew film production decks.

---

## 1. EXIF & Orientation Integrity (Zero Rotation Errors)
- **Always transpose on ingestion**: Never load or view any photo without applying `ImageOps.exif_transpose(image)`. Many mobile and camera JPEGs store orientation flags (e.g. tag `0x0112 == 3` or `6`). Ignoring this causes images to display upside down or rotated 90°.
- **Visual verification**: Verify upright orientation for public plazas, waterfront amphitheaters, architectural facades, and road horizons prior to approving assets for client decks.

---

## 2. Landmark & Exact Geographic Matching (The "Identical Match" Rule)
- **Identify Cape Town landmarks immediately**: When given a director visual reference, first inspect the background and topography for real-world Cape Town landmarks:
  - **Mountain profiles**: Lion's Head, Table Mountain, Devil's Peak, Twelve Apostles, Chapman's Peak, Sentinel.
  - **Coastal roads**: Check road curves and angles against known coastal passes:
    - If a reference shows a winding coastal road hugging the ocean with Lion's Head / Camps Bay in the distance (e.g., `cast drive.jpeg`), it is **Victoria Road (M6)** taken from above.
    - Match it directly with ground-level **Victoria Road (`M6-to CB`)** as a **100% Exact Match**, supported by Chapman's Peak for cliffside tracking.
  - **Venues & Interiors**: Check wallpaper, millwork, booth seating, bar counter shapes, and lighting fixtures:
    - If a director reference is an actual Cape Town venue (e.g. `nightclub.jpeg` is **Harringtons Cocktail Lounge** in East City), identify it immediately as a **100% Exact Match**, not merely a stylistic similarity.
- **Hero Badge Designation**: When a 100% real-world match exists, always promote it to the **Hero Scouted Database Match** with the `100% Exact Match` badge.

---

## 3. Strict Typological & Environmental Categorization
Never cross-contaminate architectural typologies or functional environments:

| Category | Permitted Typologies & Venues | STRICTLY FORBIDDEN |
| :--- | :--- | :--- |
| **Hero House / Character Cottages** | Domestic Victorian/Edwardian suburban cottages, character facades, streetscapes (e.g. Vicki in Gardens, Culver St, Chatham St, Rosemount Ave). | Nightclub/bar interiors, commercial venues, remote rustic mountain cabins. |
| **Mountainside Shack / Nature Retreats** | Rustic log cabins, timber eco-lodges, stone chalets, secluded hillside wilderness retreats (e.g. Blackwood Cabin in Scarborough, Amara Moon in Red Hill, Monkey Valley in Noordhoek). | Suburban heritage houses, urban residences, nightclubs. |
| **Nightclub / Lounge / Beach Club** | Low-lit ambient venues, cocktail lounges, velvet banquettes, dancefloors, DJ booths, sunset beach clubs (e.g. Harringtons, Cafe Caprice, Club Destiny, Club Halo, Hexagon). | Residential living rooms, cafes without evening club setups. |
| **Live Music Cafe & Supper Club** | Differentiate interior cabaret/theatrical dining (Stardust) from outdoor cafe courtyards/wetland decks (Imhoff's Gift). | Standalone residential kitchens or sterile rehearsal lofts. |
| **Rehearsal & Soundstage Studios** | Daylight cycloramas, industrial lofts, acoustically treated ADR/music studios, soundstages (Roodebloem, Studio 107, Milestone, Plug, Suite Spot, UCT, Forest Studio). | Residential rooms or live music cafes. |

---

## 4. Curated Naming & Client Localization
- **"Scouted Images Database"**: Always use the exact terminology **"Scouted Images Database"** for badges, filters, column headers, and modal captions to distinguish verified location inventory from director references.
- **Client Currency & Rate Formatting**: Always format financial estimates and day rates in the client's home currency (e.g. Indian Rupees `₹` / INR alongside South African Rand `ZAR` for Indian production companies like Mirage Media).
- **Executive Contact Branding**: Ensure pitch presentations display Zencrew & SA Locations executive contacts (Laura Diana Macleod & Jardin Roestorff) with verified direct links, phone numbers, and company bios.
