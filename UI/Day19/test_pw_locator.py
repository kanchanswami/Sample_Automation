""""

page.get_by_alt_text() --> image text suppose logo
page.get_by_text()

"""
from playwright.sync_api import Page, expect
import time
import re

def test_logo(page: Page):
    page.goto("https://practicetestautomation.com/")

    #page.get_by_alt_text()
    logo = page.get_by_alt_text("Practice Test Automation")
    expect(logo).to_be_visible()

def test_text(page:Page):
    #page.get_by_text()
    page.goto("https://practicetestautomation.com/")
    text1 = page.get_by_text("Welcome to Practice Test Automation!")
    expect(text1).to_be_visible()
    #expect(page.get_by_text("Welcome to")).to_be_visible()
    #expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()

def test_role(page: Page):
    #page.get_by_role()
    page.goto("https://practicetestautomation.com/")
    role1 = page.get_by_role("heading", name = "Get a FREE XPath cheat sheet by Signing Up for our newsletter")
    expect(role1).to_be_visible()


def test_label(page: Page):
    #page.get_by_label()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    #time.sleep(500)
    page.get_by_role("button", name="Submit").click()
    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")

    
def test_orangeHRM(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()