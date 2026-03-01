import asyncio
from playwright.async_api import async_playwright

SEEDS = [38,39,40,41,42,43,44,45,46,47]

BASE_URL = "https://sanand0.github.io/tdsdata/js_table/?seed="

async def main():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)

        context = await browser.new_context()

        grand_total = 0

        for seed in SEEDS:

            page = await context.new_page()

            url = f"{BASE_URL}{seed}"

            await page.goto(url, wait_until="networkidle")

            await page.wait_for_selector("table")

            cells = await page.query_selector_all("td")

            page_sum = 0

            for cell in cells:

                text = await cell.inner_text()

                try:
                    page_sum += float(text.strip())
                except:
                    pass

            print(f"Seed {seed} sum = {page_sum}")

            grand_total += page_sum

            await page.close()

        print(f"FINAL TOTAL = {grand_total}")

        await browser.close()

asyncio.run(main())
