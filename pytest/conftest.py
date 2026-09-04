import pytest


@pytest.fixture()   
def setup():
    print("Setup executed....")
    yield
    print("Teardown executed....")