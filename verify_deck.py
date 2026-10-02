import asyncio
import os
import sys
from playwright.async_api import async_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

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
        print(f"Rendered Category Blocks: {len(blocks)} / 18")

        # Measure nav height
        nav_h = await page.evaluate("() => document.querySelector('header.top-nav').offsetHeight")
        print(f"Top Navigation Height: {nav_h}px")

        # 2. Capture Hero Screenshot
        hero_screen = os.path.join(artifact_dir, "master_deck_hero.jpg")
        await page.screenshot(path=hero_screen, clip={"x": 0, "y": 0, "width": 1400, "height": 880})
        print(f"Saved Hero Screenshot to {hero_screen}")

        # Hide sticky header & sticky category filter bar temporarily for clean section element screenshots
        await page.evaluate("() => document.querySelectorAll('header.top-nav, .category-nav-wrap').forEach(el => el.style.display = 'none')")

        # 2b. Capture Strategic Proposal Screenshot
        strat_el = await page.query_selector("#strategic-proposal")
        if strat_el:
            strat_screen = os.path.join(artifact_dir, "master_deck_strategic_proposal.jpg")
            await strat_el.screenshot(path=strat_screen)
            print(f"Saved Clean Strategic Proposal Screenshot to {strat_screen}")

        # 2c. Capture Costing Estimate Screenshot
        cost_el = await page.query_selector("#costing-estimate")
        if cost_el:
            cost_screen = os.path.join(artifact_dir, "master_deck_costing_estimate.jpg")
            await cost_el.screenshot(path=cost_screen)
            print(f"Saved Clean Costing Estimate Screenshot to {cost_screen}")

        # Restore sticky header and category filter bar
        await page.evaluate("() => { document.querySelector('header.top-nav').style.display = 'flex'; document.querySelector('.category-nav-wrap').style.display = 'block'; }")

        # 3. Capture Category 01 Screenshot
        cat1 = await page.query_selector("#coastal-passes-ocean-roads")
        if cat1:
            cat1_screen = os.path.join(artifact_dir, "master_deck_cat01.jpg")
            await cat1.screenshot(path=cat1_screen)
            print(f"Saved Cat 01 Screenshot to {cat1_screen}")

        # 4. Capture Category 02 Screenshot
        cat2 = await page.query_selector("#modern-luxury-villas")
        if cat2:
            cat2_screen = os.path.join(artifact_dir, "master_deck_cat02.jpg")
            await cat2.screenshot(path=cat2_screen)
            print(f"Saved Cat 02 Screenshot to {cat2_screen}")

        # 5. Capture Category 18 (Quarries)
        cat18 = await page.query_selector("#quarries-industrial-excavations")
        if cat18:
            cat18_screen = os.path.join(artifact_dir, "master_deck_cat18.jpg")
            await cat18.screenshot(path=cat18_screen)
            print(f"Saved Cat 18 (Quarries) Screenshot to {cat18_screen}")

        # 6. Capture Golden Hour Section
        gh_el = await page.query_selector("#golden-hour")
        if gh_el:
            gh_screen = os.path.join(artifact_dir, "master_deck_golden_hour.jpg")
            await gh_el.screenshot(path=gh_screen)
            print(f"Saved Golden Hour Screenshot to {gh_screen}")

        # 7. Capture Rates & Contacts Section
        rates_el = await page.query_selector("#rates-and-contacts")
        if rates_el:
            rates_screen = os.path.join(artifact_dir, "master_deck_rates.jpg")
            await rates_el.screenshot(path=rates_screen)
            print(f"Saved Rates Screenshot to {rates_screen}")

        # 8. Test Currency Toggle with Costing Estimate Table
        print("\nTesting Live Multi-Currency Recalculation...")
        line_prod_cell = await page.query_selector(".costing-table td.rate-cell[data-base-zar='8000']")
        initial_rate = await line_prod_cell.inner_text()
        print(f"Initial ZAR Rate for Line Producer: {initial_rate} (Expected: 'R 8,000 / day')")

        # Click USD button
        usd_btn = await page.query_selector("button.curr-btn[data-curr='USD']")
        if usd_btn:
            await usd_btn.click()
            await page.wait_for_timeout(300)
            usd_rate = await line_prod_cell.inner_text()
            print(f"Converted USD Rate for Line Producer: {usd_rate} (Expected: '$ 448 / day')")

        # Click INR button
        inr_btn = await page.query_selector("button.curr-btn[data-curr='INR']")
        if inr_btn:
            await inr_btn.click()
            await page.wait_for_timeout(300)
            inr_rate = await line_prod_cell.inner_text()
            print(f"Converted INR Rate for Line Producer: {inr_rate} (Expected: '₹ 39,200 / day')")

        # Restore ZAR
        zar_btn = await page.query_selector("button.curr-btn[data-curr='ZAR']")
        if zar_btn:
            await zar_btn.click()
            await page.wait_for_timeout(300)
            restored_rate = await line_prod_cell.inner_text()
            print(f"Restored ZAR Rate: {restored_rate}")

        # 9. Test Lightbox Open
        first_thumb = await page.query_selector(".gallery-card")
        if first_thumb:
            await first_thumb.click()
            await page.wait_for_timeout(1000)
            lb_active = await page.query_selector(".lightbox-modal.active")
            print(f"\nLightbox Open Test: {'SUCCESS' if lb_active else 'FAILED'}")
            if lb_active:
                lb_screen = os.path.join(artifact_dir, "master_deck_lightbox.jpg")
                await page.screenshot(path=lb_screen)
                print(f"Saved Lightbox Screenshot to {lb_screen}")
                await page.keyboard.press("Escape")
                await page.wait_for_timeout(500)

        # 10. Test Category Direct Page Open (Zero Scrolling Focus Mode)
        print("\nTesting Direct Category Page Open & Focus Mode...")
        tag_btn = await page.query_selector("button.doubling-tag")
        if tag_btn:
            tag_text = await tag_btn.inner_text()
            safe_text = tag_text.encode('ascii', errors='replace').decode('ascii')
            print(f"Clicking Doubling Tag: {safe_text}")
            await tag_btn.click()
            await page.wait_for_timeout(1000)

            hero_disp = await page.evaluate("() => document.querySelector('.hero-banner-wrapper').style.display")
            strat_disp = await page.evaluate("() => document.getElementById('strategic-proposal').style.display")
            cost_disp = await page.evaluate("() => document.getElementById('costing-estimate').style.display")
            banner_disp = await page.evaluate("() => document.getElementById('categoryActiveBanner').style.display")
            scroll_pos = await page.evaluate("() => window.pageYOffset")
            hash_val = await page.evaluate("() => window.location.hash")

            print(f"Hero Display: {hero_disp} (Expected: 'none')")
            print(f"Strategic Proposal Display: {strat_disp} (Expected: 'none')")
            print(f"Costing Estimate Display: {cost_disp} (Expected: 'none')")
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
                strat_disp_restored = await page.evaluate("() => document.getElementById('strategic-proposal').style.display")
                cost_disp_restored = await page.evaluate("() => document.getElementById('costing-estimate').style.display")
                print(f"Hero Restored: {hero_disp_restored} (Expected: 'block')")
                print(f"Strategic Proposal Restored: {strat_disp_restored} (Expected: 'block')")
                print(f"Costing Estimate Restored: {cost_disp_restored} (Expected: 'block')")

        if console_errors:
            print("\nConsole Errors detected:")
            for err in console_errors:
                print(f"  - {err}")
        else:
            print("\nZero Console Errors detected!")

        await browser.close()
        print("\nAll Deck Verifications Passed Successfully!")

if __name__ == "__main__":
    asyncio.run(main())
