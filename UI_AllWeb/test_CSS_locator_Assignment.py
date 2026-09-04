from playwright.sync_api import Page, expect
import pytest 

def test_css_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(page).to_have_title("Demo Web Shop")