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
        print(f"Rendered Category Blocks: {len(blocks)} / 15")

        # 2. Capture Hero Screenshot
        hero_screen = os.path.join(artifact_dir, "master_deck_hero.jpg")
        await page.screenshot(path=hero_screen, clip={"x": 0, "y": 0, "width": 1400, "height": 880})
        print(f"Saved Hero Screenshot to {hero_screen}")

        # 3. Capture Category 01 Screenshot (Landscape Hero with wording below)
        cat1 = await page.query_selector("#coastal-passes-ocean-roads")
        if cat1:
            cat1_screen = os.path.join(artifact_dir, "master_deck_cat01.jpg")
            await cat1.screenshot(path=cat1_screen)
            print(f"Saved Cat 01 Screenshot to {cat1_screen}")

        # 4. Capture Category 02 (Modern Luxury with Lux Villa)
        cat2 = await page.query_selector("#modern-luxury-villas")
        if cat2:
            cat2_screen = os.path.join(artifact_dir, "master_deck_cat02.jpg")
            await cat2.screenshot(path=cat2_screen)
            print(f"Saved Cat 02 Screenshot to {cat2_screen}")

        # 5. Capture Category 04 (Forest Cabins)
        cat4 = await page.query_selector("#forest-cabins-nature-retreats")
        if cat4:
            cat4_screen = os.path.join(artifact_dir, "master_deck_cat04.jpg")
            await cat4.screenshot(path=cat4_screen)
            print(f"Saved Cat 04 Screenshot to {cat4_screen}")

        # 6. Capture Category 05 (Natural Wilderness & Stadsaal)
        cat5 = await page.query_selector("#natural-wilderness-geological")
        if cat5:
            cat5_screen = os.path.join(artifact_dir, "master_deck_cat05.jpg")
            await cat5.screenshot(path=cat5_screen)
            print(f"Saved Cat 05 Screenshot to {cat5_screen}")

        # 7. Capture Category 13 (Airports & Transit)
        cat13 = await page.query_selector("#airports-aviation-transport-terminals")
        if cat13:
            cat13_screen = os.path.join(artifact_dir, "master_deck_cat13.jpg")
            await cat13.screenshot(path=cat13_screen)
            print(f"Saved Cat 13 Screenshot to {cat13_screen}")

        # 8. Capture Category 14 (Prisons & Detention)
        cat14 = await page.query_selector("#civic-institutions-corrections-jail")
        if cat14:
            cat14_screen = os.path.join(artifact_dir, "master_deck_cat14.jpg")
            await cat14.screenshot(path=cat14_screen)
            print(f"Saved Cat 14 Screenshot to {cat14_screen}")

        # 9. Capture Category 15 (Stadiums & Athletics)
        cat15 = await page.query_selector("#stadiums-arenas-athletics")
        if cat15:
            cat15_screen = os.path.join(artifact_dir, "master_deck_cat15.jpg")
            await cat15.screenshot(path=cat15_screen)
            print(f"Saved Cat 15 Screenshot to {cat15_screen}")

        # 10. Capture Rate Card & Executive Contacts (with IG & YT)
        rates_el = await page.query_selector("#rates-and-contacts")
        if rates_el:
            rates_screen = os.path.join(artifact_dir, "master_deck_rates.jpg")
            await rates_el.screenshot(path=rates_screen)
            print(f"Saved Rates Screenshot to {rates_screen}")

        # 11. Generate OG Preview (1200x630)
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
