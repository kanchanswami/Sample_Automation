#test create booking
#request type : POST
#hardcode data 
#from urllib import response
from playwright.sync_api import Playwright, expect
import json


def test_create_booking(playwright:Playwright):
    """import pdb
    pdb.set_trace()"""
    base_url="https://restful-booker.herokuapp.com"

    request_context = playwright.request.new_context()

    """file = open("testdata/payload.json", "r")
    request_body = json.load(file)"""

    with open("testdata/payload.json", "r") as file:
        request_body = json.load(file)
    
    response = request_context.post(f"{base_url}/booking", data=request_body)

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
    assert booking["firstname"]=="kanchan"
    #nested data validation
    assert booking["bookingdates"]["checkin"] == "2015-01-01"
    assert booking["bookingdates"]["checkout"] == "2015-03-01"
    print("data validation is done")

    file.close()

