from playwright.async_api import async_playwright,Page, expect
import pytest 

@pytest.mark.asyncio
async def test_verifypage():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=False)
        my_page=await browser.new_page()
        await my_page.goto("https://www.google.com/?client=safari")
        await expect(my_page).to_have_url("https://www.google.com/?client=safari")
    
    