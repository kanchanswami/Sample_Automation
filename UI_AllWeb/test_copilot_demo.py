from playwright.sync_api import Page, expect

def test_copilot_demo(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Q
    # Login
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    # Open PIM page
    page.get_by_role("link", name="PIM").click()

    # Wait for page to load
    page.wait_for_load_state("networkidle")

    # Locate the dropdown
    element = page.locator(
        '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
    )

    expect(element).to_be_visible()
    print(element.text_content())       

    
