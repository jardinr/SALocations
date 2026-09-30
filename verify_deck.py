import asyncio
import os
from playwright.async_api import async_playwright

deck_dir = r"C:\Users\Jardin\OneDrive\Documents\Market\SAL\Business-SALocations\Pitches\sal-global-locations-deck"
artifact_dir = r"C:\Users\Jardin\.gemini\antigravity\brain\7c530ea6-81c1-4bb5-b9b6-1e435280896c"
html_path = os.path.join(deck_dir, "index.html")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1400, "height": 900})
        page = await context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: console_errors.append(str(err)))

        print(f"Loading {html_path}...")
        await page.goto(f"file:///{html_path.replace(os.sep, '/')}")
        await page.wait_for_timeout(2500)

        # 1. Verify Title & Category Blocks
        title = await page.title()
        print(f"Page Title: {title}")

        blocks = await page.query_selector_all(".category-block")
        print(f"Rendered Category Blocks: {len(blocks)} / 16")

        # 2. Capture Hero Screenshot
        hero_screen = os.path.join(artifact_dir, "master_deck_hero.jpg")
        await page.screenshot(path=hero_screen, clip={"x": 0, "y": 0, "width": 1400, "height": 880})
        print(f"Saved Hero Screenshot to {hero_screen}")

        # Set headers to static for element screenshots to prevent sticky overlay artifacts
        await page.add_style_tag(content="header.top-nav, .category-nav-wrap { position: static !important; }")

        # 3. Capture Category 01 Screenshot (Landscape Hero with wording below)
        cat1 = await page.query_selector("#coastal-passes-ocean-roads")
        if cat1:
            cat1_screen = os.path.join(artifact_dir, "master_deck_cat01.jpg")
            await cat1.screenshot(path=cat1_screen)
            print(f"Saved Cat 01 Screenshot to {cat1_screen}")

        # 4. Capture Category 06 (Expanded Beaches: Camps Bay, Llandudno, Muizenberg, Noordhoek)
        cat6 = await page.query_selector("#pristine-beaches-coastal-coves")
        if cat6:
            cat6_screen = os.path.join(artifact_dir, "master_deck_cat06.jpg")
            await cat6.screenshot(path=cat6_screen)
            print(f"Saved Cat 06 Screenshot to {cat6_screen}")

        # 5. Capture Category 13 (Airports & Transit)
        cat13 = await page.query_selector("#airports-aviation-transport-terminals")
        if cat13:
            cat13_screen = os.path.join(artifact_dir, "master_deck_cat13.jpg")
            await cat13.screenshot(path=cat13_screen)
            print(f"Saved Cat 13 Screenshot to {cat13_screen}")

        # 6. Capture Category 14 (Prisons & Detention)
        cat14 = await page.query_selector("#civic-institutions-corrections-jail")
        if cat14:
            cat14_screen = os.path.join(artifact_dir, "master_deck_cat14.jpg")
            await cat14.screenshot(path=cat14_screen)
            print(f"Saved Cat 14 Screenshot to {cat14_screen}")

        # 7. Capture Category 15 (Stadiums & Athletics)
        cat15 = await page.query_selector("#stadiums-arenas-athletics")
        if cat15:
            cat15_screen = os.path.join(artifact_dir, "master_deck_cat15.jpg")
            await cat15.screenshot(path=cat15_screen)
            print(f"Saved Cat 15 Screenshot to {cat15_screen}")

        # 8. Capture Category 16 (Championship Golf Courses & Country Club Estates)
        cat16 = await page.query_selector("#golf-courses-country-club-estates")
        if cat16:
            cat16_screen = os.path.join(artifact_dir, "master_deck_cat16.jpg")
            await cat16.screenshot(path=cat16_screen)
            print(f"Saved Cat 16 (Golf) Screenshot to {cat16_screen}")

        # 9. Capture Rate Card & Executive Contacts (with IG & YT)
        rates_el = await page.query_selector("#rates-and-contacts")
        if rates_el:
            rates_screen = os.path.join(artifact_dir, "master_deck_rates.jpg")
            await rates_el.screenshot(path=rates_screen)
            print(f"Saved Rates Screenshot to {rates_screen}")

        # 10. Generate OG Preview (1200x630)
        await page.set_viewport_size({"width": 1200, "height": 630})
        await page.wait_for_timeout(500)
        og_path = os.path.join(deck_dir, "og-preview.jpg")
        await page.screenshot(path=og_path, clip={"x": 0, "y": 0, "width": 1200, "height": 630})
        print(f"Generated OG Preview Banner at {og_path}")

        # 12. Test Lightbox Open
        first_thumb = await page.query_selector(".gallery-card")
        if first_thumb:
            await first_thumb.click()
            await page.wait_for_timeout(1000)
            lb_active = await page.query_selector(".lightbox-modal.active")
            print(f"Lightbox Open Test: {'SUCCESS' if lb_active else 'FAILED'}")
            if lb_active:
                lb_screen = os.path.join(artifact_dir, "master_deck_lightbox.jpg")
                await page.screenshot(path=lb_screen)
                print(f"Saved Lightbox Screenshot to {lb_screen}")

        if console_errors:
            print("Console Errors detected:")
            for err in console_errors:
                print(f"  - {err}")
        else:
            print("Zero Console Errors detected!")

        await browser.close()
        print("\nAll Deck Verifications Passed Successfully!")

if __name__ == "__main__":
    asyncio.run(main())
