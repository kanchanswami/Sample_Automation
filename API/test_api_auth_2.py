import base64

from playwright.sync_api import Playwright

def test_api_auth(playwright:Playwright):
    request_context=playwright.request.new_context()
    #username password encode and decode
    credentials=base64.b64encode(b"admin:admin").decode("utf-8")

    response = request_context.get(url="http://the-internet.herokuapp.com/basic_auth", 
                                   headers={"Authorization": f"Basic {credentials}"
                                    })
    #assert response.status==200
    response_body =response.text()
    print("Response body..",response_body)

    response_body = response.text()

    assert "Basic Auth" in response_body
    assert "Congratulations! You must have the proper credentials." in response_body

    print("Authentication successful")


    request_context.dispose()




