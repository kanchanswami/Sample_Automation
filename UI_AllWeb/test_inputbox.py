from playwright.sync_api import Page, expect

def test_inputbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    name = page.get_by_role("textbox", name="Enter Name")
    name.fill("Kanchan123456789")
    page.wait_for_timeout(20000)

    text_box = page.locator("#name")
    text_box.fill("John Kenedy")
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()
    expect(text_box).to_have_attribute("maxlength", "15")

    

