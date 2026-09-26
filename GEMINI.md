# Film Location Scouting & Photo Comparison Standards

This document establishes the mandatory protocol for analyzing, comparing, categorizing, and presenting location scouting photographs and director visual references for SA Locations & Zencrew film production decks.

---

## 1. EXIF & Orientation Integrity (Zero Rotation Errors)
- **Always transpose on ingestion**: Never load or view any photo without applying `ImageOps.exif_transpose(image)`. Many mobile and camera JPEGs store orientation flags (e.g. tag `0x0112 == 3` or `6`). Ignoring this causes images to display upside down or rotated 90°.
- **Visual verification**: Verify upright orientation for public plazas, waterfront amphitheaters, architectural facades, and road horizons prior to approving assets for client decks.

---

## 2. Landmark & Exact Geographic Matching (The "Identical Match" Rule)
- **Identify Cape Town landmarks and venue branding immediately**: When given a director visual reference, first inspect the background, topography, decor, and signage for real-world Cape Town landmarks and venues:
  - **StarDust Theatrical Dining (`cafe w live music.jpg`)**:
    - Inspect the stage backdrop wall: the "StarDust" logo is illuminated behind the singer.
    - Match it directly with `Stardust (12).jpg` as a **100% Exact Match** (wide timber dining floor, raised stage, grand piano, live performance).
  - **Victoria Road / M6 (`cast drive.jpeg`)**:
    - If a reference shows a winding coastal road hugging the ocean with Lion's Head / Camps Bay in the distance, it is **Victoria Road (M6)** taken from above.
    - Match it directly with ground-level **Victoria Road (`M6-to CB (0).jpg`)** as a **100% Exact Match**, supported by Chapman's Peak for cliffside tracking.
  - **Chapman's Peak Scenic Pass (`mountain bike trail2.jpeg`)**:
    - If a reference shows cyclists on a coastal mountain pass overlooking a curved bay, sandy beach, and Sentinel headland, it is **Chapman's Peak Drive** overlooking Hout Bay.
    - Match it directly with `Chapmans Peak (91).jpg` as a **100% Exact Match** pass vantage, accompanied by `Chapmans Peak Trail (1, 2)` for cliff single-track.
  - **Harringtons Cocktail Lounge (`nightclub.jpeg`)**:
    - Inspect wallpaper, crystal chandeliers, curved booth seating, and bar counter.
    - Match it directly with `Harringtons (2).jpg` as a **100% Exact Match**.
- **Hero Badge Designation**: When a 100% real-world match exists, always promote it to the **Hero Scouted Database Match** with the `100% Exact Match` badge.

---

## 3. Strict Typological & Environmental Categorization
Never cross-contaminate architectural typologies or functional environments:

| Category | Permitted Typologies & Venues | STRICTLY FORBIDDEN |
| :--- | :--- | :--- |
| **Hero House / Character Residences** | Domestic Victorian/Edwardian suburban cottages, character facades, streetscapes (Culver St 1–3, Chatham St 2, Rosemount Ave 4). | Nightclub/bar interiors, commercial venues, remote rustic mountain cabins, treehouses. |
| **Mountainside Shack / Nature Retreats** | Rustic log cabins, timber eco-lodges, architectural treehouses, character residential retreats (Blackwood Cabin in Scarborough, Amara Moon in Hout Bay forest, Vicki Residence, Monkey Valley in Noordhoek). | Suburban heritage street cottages, urban commercial nightlife venues. |
| **Nightclub / Lounge / Beach Club** | Low-lit ambient venues, cocktail lounges, velvet banquettes, dancefloors, DJ booths, sunset beach clubs (Harringtons, Cafe Caprice, Club Destiny, Club Halo, Hexagon). | Residential living rooms, cafes without evening club setups. |
| **Live Music Cafe & Supper Club** | Differentiate interior cabaret/theatrical dining (StarDust) from outdoor cafe courtyards/wetland decks (Imhoff's Gift). | Standalone residential kitchens or sterile rehearsal lofts. |
| **Rehearsal & Soundstage Studios** | Daylight cycloramas, industrial lofts, acoustically treated ADR/music studios, soundstages (Roodebloem, Studio 107, Milestone, Plug, Suite Spot, UCT, Forest Studio). | Residential rooms or live music cafes. |

---

## 4. Geographic & Factual Accuracy
- **Amara Moon**: Situated in the lush canopy of **Hout Bay forest**. It is an architectural timber and glass stilt retreat. **NEVER** claim Amara Moon is nestled against the 12 Apostles or that it has ocean views.
- **Vicki Residence**: Belongs under **Mountainside Shack / Character Retreats**, capturing artistic residential timber and daylight interiors.
- **StarDust Hero Framing**: The hero scouted photo for StarDust must always be `Stardust (12).jpg`, which captures the full wide dining floor, raised stage, grand piano, and live singer in view.

---

## 5. Curated Naming & Client Localization
- **"Scouted Images Database"**: Always use the exact terminology **"Scouted Images Database"** for badges, filters, column headers, and modal captions to distinguish verified location inventory from director references.
- **Client Currency & Rate Formatting**: Always format financial estimates and day rates in the client's home currency (e.g. Indian Rupees `₹` / INR alongside South African Rand `ZAR` for Indian production companies like Mirage Media).
- **Executive Contact Branding**: Ensure pitch presentations display Zencrew & SA Locations executive contacts (Laura Diana Macleod & Jardin Roestorff) with verified direct links, phone numbers, and company bios.
