from playwright.sync_api import Page, expect
import pytest

#tag is optional
#tag+id. tag#id
#tag+class  tag.class
#tag+attribute tag[attribute]
#tage+class+attribute. tag.class[attribute]

def test_verify_cs_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("input#small-searchterms").fill("Apple MacBook")
    page.wait_for_timeout(50)
    page.locator("#small-searchterms").fill("Apple MacBook")
    page.wait_for_timeout(50)
    

    page.locator("input.search-box-text").fill("T Shirts")
    page.wait_for_timeout(50)
    page.locator(".search-box-text").fill("T Shirts")

    page.locator("input[name=q]").fill("Women wear")
    page.wait_for_timeout(50)
    
    page.locator("input.search-box-text[name='q']").fill("kids wear")
    page.wait_for_timeout(100)
