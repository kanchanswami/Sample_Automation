from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def wait_for_page_ready(self) -> None:
        self.page.wait_for_load_state("domcontentloaded")
