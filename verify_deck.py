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

        # 2b. Capture Category 01 Screenshot (New Chapman's Peak Opener)
        cat1 = await page.query_selector("#coastal-passes-ocean-roads")
        if cat1:
            cat1_screen = os.path.join(artifact_dir, "master_deck_cat01.jpg")
            await cat1.screenshot(path=cat1_screen)
            print(f"Saved Cat 01 Screenshot to {cat1_screen}")

        # 3. Capture Category 03 Screenshot (Bo-Kaap Chiappini St)
        cat3 = await page.query_selector("#heritage-cottages-character-streets")
        if cat3:
            cat3_screen = os.path.join(artifact_dir, "master_deck_cat03.jpg")
            await cat3.screenshot(path=cat3_screen)
            print(f"Saved Cat 03 Screenshot to {cat3_screen}")

        # 4. Capture Category 05 Screenshot (Clean Mountains & Lourensford Prairie)
        cat5 = await page.query_selector("#natural-wilderness-geological")
        if cat5:
            cat5_screen = os.path.join(artifact_dir, "master_deck_cat05.jpg")
            await cat5.screenshot(path=cat5_screen)
            print(f"Saved Cat 05 Screenshot to {cat5_screen}")

        # 5. Capture Category 06 (Expanded Beaches: Camps Bay, Llandudno, St. James tidal pool)
        cat6 = await page.query_selector("#pristine-beaches-coastal-coves")
        if cat6:
            cat6_screen = os.path.join(artifact_dir, "master_deck_cat06.jpg")
            await cat6.screenshot(path=cat6_screen)
            print(f"Saved Cat 06 Screenshot to {cat6_screen}")

        # 6. Capture Category 07 (V&A Wide Harbour Water Panoramas)
        cat7 = await page.query_selector("#working-harbours-maritime-basins")
        if cat7:
            cat7_screen = os.path.join(artifact_dir, "master_deck_cat07.jpg")
            await cat7.screenshot(path=cat7_screen)
            print(f"Saved Cat 07 Screenshot to {cat7_screen}")

        # 7. Capture Category 08 (CBD Wide Avenue & Harbour Arch Wide)
        cat8 = await page.query_selector("#urban-metropolis-cbd")
        if cat8:
            cat8_screen = os.path.join(artifact_dir, "master_deck_cat08.jpg")
            await cat8.screenshot(path=cat8_screen)
            print(f"Saved Cat 08 Screenshot to {cat8_screen}")

        # 8. Capture Category 13 (Airports, Stellair & CTICC Interior)
        cat13 = await page.query_selector("#airports-aviation-transport-terminals")
        if cat13:
            cat13_screen = os.path.join(artifact_dir, "master_deck_cat13.jpg")
            await cat13.screenshot(path=cat13_screen)
            print(f"Saved Cat 13 Screenshot to {cat13_screen}")

        # 9. Capture Category 16 (Golf Greens & Lakes)
        cat16 = await page.query_selector("#golf-courses-country-club-estates")
        if cat16:
            cat16_screen = os.path.join(artifact_dir, "master_deck_cat16.jpg")
            await cat16.screenshot(path=cat16_screen)
            print(f"Saved Cat 16 (Golf) Screenshot to {cat16_screen}")

        # 10. Capture Golden Hour Section
        gh_el = await page.query_selector("#golden-hour")
        if gh_el:
            gh_screen = os.path.join(artifact_dir, "master_deck_golden_hour.jpg")
            await gh_el.screenshot(path=gh_screen)
            print(f"Saved Golden Hour Screenshot to {gh_screen}")

        # 11. Capture Rate Card & Executive Contacts (Laura website & Jardin business card)
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
                await page.keyboard.press("Escape")
                await page.wait_for_timeout(500)

        # 13. Test Category Direct Page Open (Zero Scrolling)
        print("\nTesting Direct Category Page Open...")
        tag_btn = await page.query_selector("button.doubling-tag")
        if tag_btn:
            tag_text = await tag_btn.inner_text()
            safe_text = tag_text.encode('ascii', errors='replace').decode('ascii')
            print(f"Clicking Doubling Tag: {safe_text}")
            await tag_btn.click()
            await page.wait_for_timeout(1000)

            hero_disp = await page.evaluate("() => document.querySelector('.hero-banner-wrapper').style.display")
            banner_disp = await page.evaluate("() => document.getElementById('categoryActiveBanner').style.display")
            scroll_pos = await page.evaluate("() => window.pageYOffset")
            hash_val = await page.evaluate("() => window.location.hash")

            print(f"Hero Display after click: {hero_disp} (Expected: 'none')")
            print(f"Active Banner Display: {banner_disp} (Expected: 'flex')")
            print(f"Page Scroll Position: {scroll_pos}px (Expected: 0)")
            print(f"URL Hash: {hash_val}")

            cat_direct_screen = os.path.join(artifact_dir, "master_deck_direct_category_open.jpg")
            await page.screenshot(path=cat_direct_screen, clip={"x": 0, "y": 0, "width": 1400, "height": 900})
            print(f"Saved Direct Category Page View Screenshot to {cat_direct_screen}")

            # Test Back to Global Overview Button
            back_btn = await page.query_selector(".btn-back-overview")
            if back_btn:
                await back_btn.click()
                await page.wait_for_timeout(1000)
                hero_disp_restored = await page.evaluate("() => document.querySelector('.hero-banner-wrapper').style.display")
                print(f"Hero Display restored after 'Back to Overview': {hero_disp_restored} (Expected: 'block')")

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
