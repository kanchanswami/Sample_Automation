from playwright.sync_api import sync_playwright
import time 

class HelperUI:
    def __init__(self, url):
        self.url=url   
    def open_url(self, title=None, exurl=None):
        try:
            with sync_playwright() as p:
                driver=p.chromium.launch(headless=False, slow_mo=1000) # open browser
                page=driver.new_page()
                page.goto(self.url)
                page.screenshot(path="sample1.png", full_page=True)
                #page.wait_for_timeout(3000)
                if(title):
                    return(page.title())
                elif exurl:
                    return(page.url)
                    
                driver.close()
        except Exception as e:
            print(e)

    def check_url(self, title=None, exurl=None):
        try:
            with sync_playwright() as p:
                driver=p.chromium.launch(headless=False, slow_mo=1000) # open browser
                page=driver.new_page()
                page.goto(self.url)
                page.screenshot(path="sample1.png", full_page=True)
                #page.wait_for_timeout(3000)
                if(title):
                    return(page.title())
                elif exurl:
                    return(page.url)
                    
                driver.close()
        except Exception as e:
            print(e)



