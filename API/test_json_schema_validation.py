# pip install jsonschema

from playwright.sync_api import Playwright

from jsonschema import ValidationError, validate

#helper function
def validate_json_schema(response_json, myschema):
    try:
        validate(instance=response_json, schema=myschema)
        print("schema validation success")
        return True 
    except ValidationError as e:
        print("Schema validation failed")
        return False
    

def test_json_schema_validation(playwright:Playwright):
    request_context = playwright.request.new_context()

    response = request_context.get("https://mocktarget.apigee.net/json")

    
  
    response_body = response.json()

    assert response.status==200
    assert response.status_text=='OK'
    print(response)

    schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "firstName": {
      "type": "string"
    },
    "lastName": {
      "type": "string"
    },
    "city": {
      "type": "string"
    },
    "state": {
      "type": "number"
    }
  },
  "required": [
    "firstName",
    "lastName",
    "city",
    "state"
  ]
}
    status = validate_json_schema(response_body, schema)
    assert status
    request_context.dispose()