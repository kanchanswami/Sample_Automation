from playwright.sync_api import Page, expect
import re
import pytest

@pytest.mark.skip(reason="Public site is blocked by Google in GitHub Actions")
def test_dynamic(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/", timeout=60000)

    for i in range(5):
        #button=page.locator("button[name^='st']")
        import re

        button = page.get_by_role("button", name=re.compile(r"ST.*"))
        button.click()
        page.wait_for_timeout(2000)

