"""import pytest

def test_one():
    print("This is test one")


def test_two():
    print("This is test two")


def test_three():
    print("This is test three")
"""
"""import pytest


@pytest.fixture
def setup():
    print("Setup the browser")


def test_one(setup):
    print("This is test one")

def test_two(setup):
    print("This is test two")

def test_three(setup):
    print("This is test three")
"""

"""
import pytest

@pytest.fixture
def setup():
    print("Setup the browser")
    return "chrome"

def test_one(setup):
    print("This is test one")
    print(setup)

def test_two(setup):
    print("This is test two")
    print(setup)

def test_three(setup):
    print("This is test three")
    print(setup)
"""

import pytest

@pytest.fixture
def setup():
    print("\n Setup the browser..")
    yield 
    print("Close the browser..")

def test_one(setup):
    print("This is test 1...")

def test_two(setup):
    print("This is test 2...")

def test_three(setup):
    print("This is test 3...")




