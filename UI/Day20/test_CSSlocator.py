#cascading style sheet
# CSS work based on DOM(Document Object Module)

# tag with id  tagname#id
# tag with class tag.class
# tag with attribute tag[attribute=value]
# tag with id, class and attribute tag.class[attribute=value]
from playwright.sync_api import Page, expect
import pytest
import time

def test_csslocation(page: Page):
    page.goto("https://demowebshop.tricentis.com")
    # tag and id
    page.locator("input#small-searchterms").fill("computer")
    time.sleep(2)
    #page.locator("input.button-1.search-box-button").click()
    #page.wait_for_timeout(500)
    
    page.locator("input.button-1.search-box-button[value='Search']").click()
    page.wait_for_timeout(500)
                