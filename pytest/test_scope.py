#Fixture Reuable across multiple test files

#scope = 'function' - default scope, fixture is destroyed at the end of the test
#scope = 'class' - fixture is destroyed at the end of the last test in the class
#scope = 'module' - fixture is destroyed at the end of the last test in the module
#scope = 'package' - fixture is destroyed at the end of the last test in the package
#scope = 'session' - fixture is destroyed at the end of the test session
import pytest 

@pytest.fixture()
def setup():
    print("Setup executed....")
    yield
    print("Teardown executed....")

def test_one(setup):
    assert 1 == 1
    print("test_one executed....")  

def test_two(setup):
    assert 2 == 2
    print("test_two executed")  

def test_three(setup):
    assert 3 == 3
    print("test_three executed")    
    