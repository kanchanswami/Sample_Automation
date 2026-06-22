from playwright.sync_api import sync_playwright
import time 

def open_url(url):
    with sync_playwright() as p:
        driver=p.chromium.launch(headless=False, args=["--log-level=3"]) # open browser
        page=driver.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        print("URL:", page.url)
        print("Title:", page.title())
        time.sleep(5)
        driver.close()

#open_url("http://google.com")
#open_url("https://stepupandlearn.in")