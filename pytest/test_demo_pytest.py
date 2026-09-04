import pytest

def test_one(setup):
    assert 1 == 1
    print("test_one executed....")

    
def test_two(setup):
    assert 2 == 2
    print("test_two executed")

def test_three():
    assert 3 == 3
    print("test_three executed")