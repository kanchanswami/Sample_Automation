from playwright.sync_api import Page, expect
import time

def test_url(page:Page):
    page.goto("https://www.google.com/")
    my_url=page.url
    print(my_url)
    expect(page).to_have_url("https://www.google.com/")

def test_title(page:Page):
    page.goto("https://www.google.com/")
    my_title=page.title()
    print(my_title)
    expect(page).to_have_title("Google")

