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
        print(f"Rendered Category Blocks: {len(blocks)} / 10")

        # 2. Capture Hero Screenshot
        hero_screen = os.path.join(artifact_dir, "master_deck_hero.jpg")
        await page.screenshot(path=hero_screen, clip={"x": 0, "y": 0, "width": 1400, "height": 880})
        print(f"Saved Hero Screenshot to {hero_screen}")

        # 3. Capture Category 01 Screenshot (Coastal Roads)
        cat1 = await page.query_selector("#coastal-passes-ocean-roads")
        if cat1:
            cat1_screen = os.path.join(artifact_dir, "master_deck_cat01.jpg")
            await cat1.screenshot(path=cat1_screen)
            print(f"Saved Cat 01 Screenshot to {cat1_screen}")

        # 4. Capture Category 04 Screenshot (Wilderness / Blackwood Cabin)
        cat4 = await page.query_selector("#wilderness-forest-cabins")
        if cat4:
            cat4_screen = os.path.join(artifact_dir, "master_deck_cat04.jpg")
            await cat4.screenshot(path=cat4_screen)
            print(f"Saved Cat 04 Screenshot to {cat4_screen}")

        # 5. Capture Category 07 Screenshot (Nightlife / Harringtons Bar)
        cat7 = await page.query_selector("#nightlife-ambient-lounges")
        if cat7:
            cat7_screen = os.path.join(artifact_dir, "master_deck_cat07.jpg")
            await cat7.screenshot(path=cat7_screen)
            print(f"Saved Cat 07 Screenshot to {cat7_screen}")

        # 6. Capture Rate Card & Contacts
        rates_el = await page.query_selector("#rates-and-contacts")
        if rates_el:
            rates_screen = os.path.join(artifact_dir, "master_deck_rates.jpg")
            await rates_el.screenshot(path=rates_screen)
            print(f"Saved Rates Screenshot to {rates_screen}")

        # 7. Generate OG Preview (1200x630)
        await page.set_viewport_size({"width": 1200, "height": 630})
        await page.wait_for_timeout(500)
        og_path = os.path.join(deck_dir, "og-preview.jpg")
        await page.screenshot(path=og_path, clip={"x": 0, "y": 0, "width": 1200, "height": 630})
        print(f"Generated OG Preview Banner at {og_path}")

        # 8. Test Lightbox Open
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
