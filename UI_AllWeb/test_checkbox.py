from playwright.sync_api import expect, Page

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    checkbox_Sun = page.locator("#sunday")
    checkbox_Sun.check()
    expect(checkbox_Sun).to_be_checked()
    page.wait_for_timeout(2000)


    
    days = ["sunday", "monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday"]

    count = 0   # Initialize the counter

    for day in days:
        checkbox = page.locator(f"#{day}")
        checkbox.check()
        expect(checkbox).to_be_checked()
        print("Checkbox count for this locator:", checkbox.count())

        count = count + 1
        page.wait_for_timeout(2000)

    print("Total checkboxes processed:", count)

    for day in days[-3:]:
        checkbox = page.locator(f"#{day}")
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
        print("Checkbox count for this locator:", checkbox.count())
        count = count + 1
        page.wait_for_timeout(2000)

    print("Total checkboxes processed:", count)




    