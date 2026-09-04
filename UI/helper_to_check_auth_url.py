from playwright.sync_api import sync_playwright
import time

def check_url(username='admin', password='admin'):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=100) # browser 
            page=browser.new_page() #window browser
            page.goto(f'https://{username}:{password}@the-internet.herokuapp.com/basic_auth')
            page.screenshot(path='sample2.png', full_page=True)
            print(page.url)
            if "basic_auth" in page.url:
                 return True
            else:
                 return False
            browser.close()
    except Exception as e:
            return False

# check_url()
#check_url(username='stepup', password='admin')
#check_url(username='admin', password='password@123')
#check_url(username='stepup', password='password@123')
