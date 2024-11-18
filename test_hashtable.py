# test_hashtable.py

from calculator import add_two_numbers

def test_should_always_pass():
    assert 2 + 2 == 4, "This is just a dummy test"

def test_add_two_numbers():
    assert add_two_numbers(2,2) == 4