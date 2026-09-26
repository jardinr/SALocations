import os
import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})
        
        html_path = os.path.abspath('index.html')
        await page.goto(f'file:///{html_path}')
        await page.wait_for_timeout(1500)

        # Click Tab 6 (Nightclub)
        tab_club = await page.query_selector('#tab-nightclub-venue')
        if tab_club:
            await tab_club.click()
            await page.wait_for_timeout(500)
            
            # Scroll down to gallery
            gallery = await page.query_selector('#panel-nightclub-venue .gallery-grid')
            if gallery:
                await gallery.scroll_into_view_if_needed()
                await page.wait_for_timeout(500)
                await page.screenshot(path='C:/Users/Jardin/.gemini/antigravity/brain/7c530ea6-81c1-4bb5-b9b6-1e435280896c/zen_deck_club_gallery.jpg')
                print("Captured club gallery with Cafe Caprice!")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(capture())
