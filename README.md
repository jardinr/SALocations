# British Residential Homes & Gardens · Location Pitch Dossier

**Production Client Presentation · March 2027 Production Window**  
**Curated by Jardin Roestorff · SA Locations (SAL)**  
🌐 **Live Interactive Deck:** [sal-british-homes.vercel.app](https://sal-british-homes.vercel.app)

---

## Overview

This repository contains the interactive location presentation portfolio created for an international commercial/film production client. The brief requires residential properties located in Cape Town's premier heritage belts that convincingly replicate authentic **British / English domestic architecture and established country gardens**.

All 6 properties in this collection have been pre-screened and curated strictly against the director's two core creative worlds:
* **World 1 (Living Room / Lounge & Kitchen):** Characterful, textured, lived-in living spaces for a group of 6–8 friends, featuring working stone/brick fireplace hearths, library shelving, and country shaker kitchens with central prep islands.
* **World 2 (Garden & Boundary):** Expansive, flat party lawns with mature deciduous shade trees, deep covered dining verandas, swimming pools, and established boundary fences/hedges for tracking shots.
* **Strict Curation Standard:** 100% of bedrooms and bathrooms have been excluded from the active deck to preserve creative focus.
* **Hero Establishing Shots:** The primary photograph for every property is a wide-angle establishing landscape shot showing the residence from a distance within its grounds.

---

## Curated Properties (Option 01 – Option 06)

| # | Property Name | Location / Area | Architectural Style | Hero Exterior Shot | 12h Shoot Rate |
|---|---|---|---|---|---|
| **01** | **Enchanted** | Bishopscourt / Constantia | English Country Manor & Estate Lawn | `Enchanted_31.jpg` (Wide Rear Lawn & Trees) | £2,100 / day |
| **02** | **English Elegance** | Constantia / Bishopscourt | Farmhouse & Sunken Turf Court | `English Elegance_5.jpg` (Terrace & Steps Across Lawn) | £2,100 / day |
| **03** | **Solace House** | Newlands / Rondebosch | Tudor / Arts & Crafts Cottage | `Solace House_8.jpg` (Pitched Roof & Trees Across Lawn) | £2,150 / day |
| **04** | **Villa Ten (#10)** | Upper Constantia | Painted Brick English Country Manor | `#10 (43).jpg` (White Manor Across Lawn & Drive) | £2,250 / day |
| **05** | **Arumbrook Estate** | Constantia Valley / Hout Bay | Cape-English Manor & Orchard Grounds | `Arumbrook_facade.jpg` (Double-Storey Manor & Grounds) | £2,000 / day |
| **06** | **Ariana** | Constantia Valley / Bergvliet | English Country Cottage & Grounds | `Ariana (2).jpg` (Gravel Drive, Tree Swing & Lawn) | £2,050 / day |

---

## Key Features

1. **Self-Contained Single-Page Architecture (`index.html`)**
   * Zero external image hosting dependencies. All 96 high-resolution curated photographs (16 per property) are base64-encoded and embedded directly in the application, ensuring instantaneous loading and 100% uptime.
   * Responsive layout with dark-luxury British green/gold palette (`Cinzel` serif, `Space Grotesk`, `Inter`).
   * Category-filtered photo galleries (Living Room, Garden & Grounds, Facade & Details) with interactive full-screen lightbox modal and keyboard navigation.

2. **Google Calendar Recce Integration**
   * Top navigation and every property card features a one-click **"📅 Book Recce (Google Cal)"** button.
   * Dynamically pre-populates event title (`Location Recce: [Property Name] (Cape Town)`), production details, commercial scouting rates, web dossier link, location coordinates, and automatically invites `jardinr@gmail.com`.

3. **Open Graph Social Preview Cards**
   * Dynamically generated 1200x630 social preview card (`og-preview.jpg`) with dark-luxury gradient overlay, brand pills, and property match badges for rich link previews across WhatsApp, iMessage, Slack, LinkedIn, and X.

4. **Production Logistics & Matrix**
   * Side-by-side production matrix comparing style, living room features, garden party depth, boundary security, day rates (GBP/ZAR), and March 2027 availability.
   * Dedicated Location Scouting & Management rate card (ZAR 5,000 scout + ZAR 1,000 4x4 vehicle/fuel = ZAR 6,000/day combined package).

---

## Repository Structure

```
├── index.html                 # Complete self-contained web app (6 properties, 96 embedded photos)
├── og-preview.jpg             # High-res 1200x630 Open Graph social preview thumbnail
├── package.json               # Node metadata for Vercel deployment
├── README.md                  # Project documentation & technical guide
├── add_ariana_to_deck.py      # Python script to encode photos and add property to deck
├── create_og_thumbnail.py     # Playwright script to render social preview card
├── expand_portfolio.py        # Automation pipeline for bulk image encoding and portfolio updates
└── verify_deck.py             # Integrity check script validating all 96 images and metadata
```

---

## Development & Maintenance

### Adding a New Location
1. Place source photos in a folder under `Pictures/English/<Property_Name>`.
2. Curate 16 photos matching World 1 and World 2 (exclude bedrooms/bathrooms).
3. Select an establishing shot from a distance as `hero`.
4. Run `add_ariana_to_deck.py` (or update `expand_portfolio.py`) to encode images at max `1200x800` quality `82` and update the `locations` array.
5. Run `python verify_deck.py` to confirm zero missing image keys.

### Regenerating the Social Card
```bash
python create_og_thumbnail.py
```

### Deploying to Vercel
```bash
npx vercel --scope sal19 --prod --yes
npx vercel alias set <deployment-url> sal-british-homes.vercel.app --scope sal19
```

---

**Confidential Scouting Dossier · SALocations / SMAIDM · 2026 / 2027**
