from playwright.sync_api import Page, expect
import pytest 

def test_verifypage(page:Page):
    page.wait_for_timeout(10000)
    page.goto("https://www.google.com/?client=safari")
    my_url=page.url
    print("\n Url of the application:- ", my_url)
    expect(page).to_have_url("https://www.google.com/?client=safari")
    
    
def test_title(page:Page):
    page.wait_for_timeout(10000)
    page.goto("https://www.google.com/?client=safari")
    title_page=page.title()
    print("\n Title of the page is:- ", title_page)
    expect(page).to_have_title("Google")
    
    