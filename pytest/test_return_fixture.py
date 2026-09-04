import pytest 

@pytest.fixture
def setup():
    print("Open Browser...")
    print("Setup executed....")
    yield
    print("Close Browser...")
    print("Teardown executed....")
    return "Chrome"

def test_one(setup):
    assert 2 + 2 == 4
    print("test_one executed....")  
    print("Browser name is {}".format(setup))

def test_two(setup):
    assert 3 + 3 == 6
    print("test_two executed")  
    print("Browser name is {}".format(setup))

def test_three( setup):
    assert 4 + 4 == 8   
    print("test_three executed")    
    print("Browser name is {}".format(setup))

