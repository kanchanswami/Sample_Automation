from datetime import datetime, timedelta

from faker import Faker
from playwright.sync_api import Playwright, expect


def test_create_booking_faker(playwright: Playwright):
    base_url="https://restful-booker.herokuapp.com"

    request_context = playwright.request.new_context()
    faker=Faker()

    first_name=faker.first_name()
    last_name=faker.last_name()
    total_price=faker.random_int(min=100, max=5000)
    deposit =faker.boolean()
    checkin_date = datetime.now().strftime("%Y-%m-%d")
    checkout_date = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
    additonal_needs=faker.word()

    request_body = {
"firstname": first_name,
"lastname": last_name,
"totalprice": total_price,
"depositpaid": deposit,
"bookingdates": {
"checkin": checkin_date,
"checkout": checkout_date
},
"additionalneeds": additonal_needs
}

    
    response = request_context.post(f"{base_url}/booking", data = request_body)

    #validation
    assert response.ok
    assert response.status==200
    response_body = response.json()
    print("response is:- ", response_body)
    #attribute validation
    assert "bookingid" in response_body
    assert "booking" in response_body
    #data validation
    booking = response_body["booking"]
    assert booking["firstname"]==first_name
    #nested data validation
    assert booking["bookingdates"]["checkin"] == checkin_date
    assert booking["bookingdates"]["checkout"] == checkout_date
    print("data validation is done")

    request_context.dispose()

