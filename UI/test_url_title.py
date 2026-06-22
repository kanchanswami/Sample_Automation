from helper_to_check_basic  import *
import pytest


def test_title_url():
   obj = HelperUI(url="https://stepupandlearn.in")
   result = obj.open_url(title=True, exurl=None)
   assert "STEP UP " in result, "Failed, due to title miss match"


def test_current_url():
   obj = HelperUI(url="https://stepupandlearn.in")
   result = obj.open_url(title=None, exurl=True)
   assert "https://stepupandlearn.in" == "https://stepupandlearn.in" in result, "Failed, due to url miss match"

def test_authenticate_url():
   obj = HelperUI(url="https://admin:admin@the-internet.herokuapp.com/basic_auth")
   result = obj.open_authenticated_url(title=None, exurl=True)
   assert "the-internet" in result, "Failed, due to url miss match"