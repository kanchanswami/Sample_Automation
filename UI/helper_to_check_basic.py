from playwright.sync_api import sync_playwright


class HelperUI:
    def __init__(self, url):
        self.url = url

    def open_url(self, title=None, exurl=None):
        try:
            with sync_playwright() as p:
                driver = p.chromium.launch(headless=False, slow_mo=1000)
                page = driver.new_page()

                page.goto(self.url)
                page.screenshot(path="sample1.png", full_page=True)

                if title:
                    result = page.title()
                elif exurl:
                    result = page.url
                else:
                    result = None

                driver.close()
                return result

        except Exception as e:
            print(f"Error: {e}")
            raise

    @staticmethod
    

    def check_url(username="admin", password="admin"):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto(f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth")

            print("Current URL:", page.url)

            text = page.text_content("body")
            print("Page Text:", text)

            browser.close()

            return "Congratulations" in text

    def open_authenticated_url(self, title=None, exurl=None):
        try:
            with sync_playwright() as p:
                driver = p.chromium.launch(headless=False, slow_mo=1000)
                page = driver.new_page()

                page.goto(self.url)

                if title:
                    result = page.title()
                elif exurl:
                    result = page.url
                else:
                    result = None

                driver.close()
                return result

        except Exception as e:
            print(f"Error: {e}")
            raise