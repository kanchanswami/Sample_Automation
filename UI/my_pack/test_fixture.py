import pytest

@pytest.mark.skip
def test_loginbyemail():
    print("This is login by email")
    assert 1==1

def test_loginbyfacebook():
    print("This is login by facebook")
    assert 1==1

def test_loginbyphone():
    print("This is login by phone")
    assert 1==1

@pytest.mark.skip
def test_signbyemail():
    print("This is signup by email")
    assert 1==1

def test_signbyfacebook():
    print("This is signup by facebook")
    assert 1==1

def test_signbyphone():
    print("This is signup by phone")
    assert 1==1

