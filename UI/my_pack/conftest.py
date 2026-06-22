
import pytest

@pytest.fixture()
def setup():
    print("Setup envirnoment...")
    yield
    print("Tear Down..")


