from playwright.sync_api import Page, expect

def test_radiobutton(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    male_radio = page.locator("input#male")
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()
    #male radio button not to be checked
    expect(male_radio).not_to_be_checked()

    #select
    male_radio.check()
    page.wait_for_timeout(2000)
    #male radio button to be checked 
    expect(male_radio).to_be_checked()
   
    


