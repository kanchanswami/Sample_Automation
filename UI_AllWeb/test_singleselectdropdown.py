from playwright.sync_api import Page, expect


def test_singleselectdropdown(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    #3 ways to select dropdown
    #1: 
    page.locator("#country").select_option("Germany")
    page.wait_for_timeout(5000)
    page.locator("#country").select_option(label = "France")
    page.wait_for_timeout(5000)
    page.locator("#country").select_option(index = 9)

    page.wait_for_timeout(5000)

    dropdown_list=page.locator("#country>option")
    expect(dropdown_list).to_have_count(10)

    options_text = [text.strip() for text in dropdown_list.all_text_contents()]
    #print(options_text)
    for option in options_text:
        print(option)


    #page.locator("#colors").select_option(["Red", "Blue", "Green"])
    #page.locator("#colors").select_option(label = ["Red", "Blue", "Green"])
    #page.locator("#colors").select_option(value = ["Red", "Blue", "Green", "white"])

    page.locator("#colors").select_option(index = [1,2])

    page.wait_for_timeout(5000)


