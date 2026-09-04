import base64

from playwright.sync_api import Playwright

def test_api_auth(playwright:Playwright):
    request_context=playwright.request.new_context()
    #username password encode and decode
    credentials=base64.b64encode(b"user:pass").decode("utf-8")

    response = request_context.get(url="https://httpbin.org/basic-auth/user/pass", 
                                   headers={"Authorization": f"Basic {credentials}"
                                    })
    #assert response.status==200
    response_body =response.json()
    print("Response body..",response_body)

    request_context.dispose()



