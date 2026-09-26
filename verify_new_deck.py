import asyncio
import os
from playwright.async_api import async_playwright

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        
        html_path = os.path.abspath('index.html')
        await page.goto(f'file:///{html_path}')
        await page.wait_for_timeout(1500)

        tabs = await page.query_selector_all('.tab-btn')
        print(f"Total categories/tabs: {len(tabs)}")

        # Check Category 1: Imhoff's Gift & Stardust
        tab1 = await page.query_selector('#tab-live-music-cafe')
        if tab1:
            await tab1.click()
            await page.wait_for_timeout(500)
            await page.screenshot(path='C:/Users/Jardin/.gemini/antigravity/brain/7c530ea6-81c1-4bb5-b9b6-1e435280896c/v2_cat1_imhoffs.jpg')

        # Check Category 3: House (Culver St & Amara Moon)
        tab3 = await page.query_selector('#tab-hero-house')
        if tab3:
            await tab3.click()
            await page.wait_for_timeout(500)
            await page.screenshot(path='C:/Users/Jardin/.gemini/antigravity/brain/7c530ea6-81c1-4bb5-b9b6-1e435280896c/v2_cat3_culver.jpg')

        # Check Category 6: Nightclub (Harringtons 100% match!)
        tab6 = await page.query_selector('#tab-nightclub-venue')
        if tab6:
            await tab6.click()
            await page.wait_for_timeout(500)
            # Scroll to comparison
            comp = await page.query_selector('#panel-nightclub-venue .comparison-grid')
            if comp:
                await comp.scroll_into_view_if_needed()
                await page.wait_for_timeout(500)
                await page.screenshot(path='C:/Users/Jardin/.gemini/antigravity/brain/7c530ea6-81c1-4bb5-b9b6-1e435280896c/v2_cat6_harringtons_comp.jpg')
            # Scroll to gallery
            gal = await page.query_selector('#panel-nightclub-venue .gallery-grid')
            if gal:
                await gal.scroll_into_view_if_needed()
                await page.wait_for_timeout(500)
                await page.screenshot(path='C:/Users/Jardin/.gemini/antigravity/brain/7c530ea6-81c1-4bb5-b9b6-1e435280896c/v2_cat6_harringtons_gallery.jpg')

        # Check Category 7: Merged Rehearsal & Studios
        tab7 = await page.query_selector('#tab-rehearsal-studio-spaces')
        if tab7:
            await tab7.click()
            await page.wait_for_timeout(500)
            await page.screenshot(path='C:/Users/Jardin/.gemini/antigravity/brain/7c530ea6-81c1-4bb5-b9b6-1e435280896c/v2_cat7_merged_studios.jpg')

        # Check Services section for INR
        services = await page.query_selector('#services')
        if services:
            await services.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await page.screenshot(path='C:/Users/Jardin/.gemini/antigravity/brain/7c530ea6-81c1-4bb5-b9b6-1e435280896c/v2_services_inr.jpg')

        await browser.close()
        print("All verification screenshots captured!")

if __name__ == '__main__':
    asyncio.run(verify())
