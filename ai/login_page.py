from playwright.sync_api import Page

from ai.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_link = page.locator("#login2")
        self.username_input = page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.modal_login_button = page.locator("#logInModal button.btn.btn-primary")
        self.logout_link = page.locator("#logout2")
        self.welcome_user = page.locator("#nameofuser")

    def open_home_page(self) -> None:
        self.open("https://www.demoblaze.com/index.html")

    def open_login_modal(self) -> None:
        self.login_link.click()
        self.page.locator("#logInModal").wait_for(state="visible")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.modal_login_button.click()

    def logout(self) -> None:
        self.logout_link.click()

    def is_logged_in(self) -> bool:
        return self.logout_link.is_visible()

    def get_welcome_text(self) -> str:
        return self.welcome_user.text_content().strip()
