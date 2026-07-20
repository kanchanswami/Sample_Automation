from playwright.sync_api import Playwright

def test_cookies_in_response(playwright:Playwright):
    request_context=playwright.request.new_context()
    response=request_context.get("https://google.com/")

    assert response.status_text=='OK'
    print(response.status_text)
    print(response.status)
    assert response.status==200
    headers=response.headers
    for key,value in headers.items():
        print(f"{key} ==> {value}" "\n" )

    print(headers.get("content-type"))
    assert "text/html" in headers.get("content-type")
    print(headers.get("content-encoding"))   
    assert "gzip" in headers.get("content-encoding")

    assert "server" in headers
    print(headers.get("server"))
    assert "set-cookie" in headers 
    print(headers.get("set-cookie"))

    #cookies -extract from request context
    print("This is cookies...\n ")
    cookies = request_context.storage_state()["cookies"]

    for c in cookies:
        print(f"{c['name']} ==> {c['value']} ==> {c['domain']}")

    aec_cookies=None
    for c in cookies:
        
        if c["name"]=="AEC":
            aec_cookies = c
            print("The name for aec_cookies is", aec_cookies['name'])
            print("The value for aec_cookies is", aec_cookies['value'])
            print("The domain for aec_cookies is", aec_cookies['domain'])
            print("The path for aec_cookies is", aec_cookies['path'])
            print("The expires for aec_cookies is", aec_cookies['expires'])

            break

    assert aec_cookies is not None, "cookies aec not found"