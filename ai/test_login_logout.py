import pytest
from playwright.sync_api import Page, expect

from ai.login_page import LoginPage


def test_login_logout_flow(page: Page) -> None:
    login_page = LoginPage(page)

    login_page.open_home_page()
    expect(login_page.login_link).to_be_visible()

    login_page.open_login_modal()
    login_page.login("pavanol", "test@123")

    expect(login_page.logout_link).to_be_visible()
    expect(login_page.welcome_user).to_contain_text("Welcome pavanol")

    login_page.logout()

    expect(login_page.login_link).to_be_visible()
