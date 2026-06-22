from helper_to_check_auth_url import *

#valid username and valid password
def test_url_vusername_vpassword():
    assert check_url(username='admin',password='admin'), "failed due to auth error"
