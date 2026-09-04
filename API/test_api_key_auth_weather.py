from playwright.sync_api import Playwright

def test_api_key_auth_weather(playwright:Playwright):
    request_context=playwright.request.new_context()

    qparams = {
        "q":"sydney",
        "appid":"5a6ab7a5d3633255cb97dc69b7783af2"

    }
    response =request_context.get(url="http://api.openweathermap.org/data/2.5/weather",
                                  params=qparams)
    
    assert response.status==200
    response_body = response.json()

    print("weather info", response_body)