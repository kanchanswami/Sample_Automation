from playwright.sync_api import Playwright

def test_bearer_token_auth(playwright:Playwright):
    token ="xxxxxxx"
    request_context=playwright.request.new_context()
    response = request_context.get(url="https://api.github.com/user", headers={"Authorization": f"Bearer {token}"
                                    })
    assert response.status==200
    response_body=response.json()
    print("Response Body..", response_body)
