#create (POST)
#GetBooking (GET)
#Create Token (POST/Auth)
#Partial update (PATCH)
#Full update (PUT)
#Delete Booking (DELETE)
import json
from playwright.sync_api import Playwright, expect
import pytest

base_url="https://restful-booker.herokuapp.com"
url_token = "https://restful-booker.herokuapp.com/auth"


#function read
def read_json(file_path):
    file = open(file_path, "r")
    return json.load(file)


# playwright context
@pytest.fixture(scope="session")
def request_context(playwright:Playwright):
    context = playwright.request.new_context()
    yield context
    context.dispose()

def test_create_booking(request_context):
    data = read_json("testdata/POST_request_body.json")
    response = request_context.post(url= f"{base_url}/booking", data=data) # type: ignore
    assert response.ok, "POST request failed"
    assert response.status==200
    response_body= response.json()
    print("Create booking response:", response_body)

    assert "bookingid" in response_body
    assert "booking" in response_body

    booking=response_body["booking"]
    assert booking["firstname"]==data["firstname"]
    assert booking["lastname"]==data["lastname"]
    assert booking["totalprice"]==data["totalprice"]

    assert booking["depositpaid"]==data["depositpaid"]

    assert booking["bookingdates"]["checkin"]==data["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"]==data["bookingdates"]["checkout"]
    assert booking["firstname"]==data["firstname"]
    global booking_id,check_in, check_out
    booking_id =response_body["bookingid"]
    check_in =booking["bookingdates"]["checkin"]
    check_out =booking["bookingdates"]["checkout"]
   


def test_get_booking_by_id(request_context):
    response = request_context.get(url= f"{base_url}/booking/{booking_id}")

    assert response.ok
    assert response.status==200
    response_body= response.json()
    print(f"Listed details for {booking_id}", response_body)
    assert "firstname" in response_body
    assert "lastname" in response_body

def get_booking_by_name(request_context, firstname, lastname):
    return request_context.get(
        url=f"{base_url}/booking?firstname={firstname}&lastname={lastname}"
    )

def test_get_booking_by_name(request_context):
    response = get_booking_by_name(request_context, "kanchan", "s")

    print(response.status)
    #print(response.json())

    assert response.status == 200
    print("Booking IDs fetched by IDs", response.json())
    assert len(response.json()) > 0
    for item in response.json():
        assert "bookingid" in item


def get_booking_by_dates(request_context, check_in, check_out):
    return request_context.get(
        url=f"{base_url}/booking?checkin={check_in}&lastname={check_out}"
    )

def test_get_booking_by_dates(request_context):
    response = get_booking_by_dates(request_context,check_in, check_out)

    assert response.ok
    assert response.status==200
    response_body= response.json()
    print("Booking IDs fetched by dates", response.json())
    for item in response.json():
        assert "bookingid by dates" in item


def test_create_token(request_context):
    global token

    data = read_json("testdata/TOKEN_request_body.json")
    response = request_context.post(
        url=url_token,
        data=data
    )

    assert response.ok
    assert response.status == 200

    response_body = response.json()
    print(response_body)

    assert "token" in response_body

    token = response_body["token"]

def test_parital(request_context):
    data = read_json("testdata/PATCH_request_body.json")
    response = request_context.patch(url=f"{base_url}/booking/{booking_id}", data=data, headers={"Cookie": f"token={token}", "Content-Type": "application/json"})
    assert response.status==200
    response_body =response.json()
    
    for key in data.keys():
        assert key in response_body
        assert response_body[key]==data[key]
        print(key, response_body[key])

def test_full_update(request_context):
    data = read_json("testdata/PUT_request_body.json")
    response = request_context.put(url=f"{base_url}/booking/{booking_id}", data=data, headers={"Cookie": f"token={token}", "Content-Type": "application/json"})
    assert response.status==200
    response_body =response.json()
    
    for key in data.keys():
        assert key in response_body
        assert response_body[key]==data[key]
        print(key, response_body[key])

def test_delete_booking(request_context):
    response = request_context.delete(
        url=f"{base_url}/booking/{booking_id}",
         headers={"Cookie": f"token={token}", "Content-Type": "application/json"}
    )

    assert response.status == 201
    print(response.text())   # Prints: Created
    print("Booking id deleted successfully:", booking_id)





  
    
    






