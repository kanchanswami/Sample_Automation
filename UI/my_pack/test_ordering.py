import pytest 

#pip install pytest-order

@pytest.mark.order("first")
def test_login():
    print("This is test login")

@pytest.mark.order()
def test_add_item():
    print("This is test add item")

@pytest.mark.order("last")
def test_logout():
    print("This is test logout")


