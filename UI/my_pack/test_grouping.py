import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyemail():
    print("This is login by email")
    assert 1==1

@pytest.mark.sanity
def test_loginbyfacebook():
    print("This is login by facebook")
    assert 1==1

@pytest.mark.regression
def test_loginbyphone():
    print("This is login by phone")
    assert 1==1

@pytest.mark.sanity
@pytest.mark.regression
def test_signbyemail():
    print("This is signup by email")
    assert 1==1

@pytest.mark.regression
def test_signbyfacebook():
    print("This is signup by facebook")
    assert 1==1

@pytest.mark.sanity
def test_signbyphone():
    print("This is signup by phone")
    assert 1==1

@pytest.mark.sanity
@pytest.mark.regression
def test_payment_indollar():
    print("This is payment is dollar")
    assert True == True

@pytest.mark.regression
def test_payment_inrupees():
    print("This is payment is rupees")
    assert True == True


