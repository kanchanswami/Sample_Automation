import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests"
    )

@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup():
    print("Setup environment...")
    yield
    print("Tear Down..")