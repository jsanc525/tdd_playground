# test_hashtable.py

from calculator import add_two_nums

def test_should_always_pass():
    assert 2 + 2 == 4, "This is just a dummy test"

def test_add_two_nums():
    assert add_two_nums(2,2) == 4

def test_sub_two_nums():
    assert subtract_two_nums(2, 2) == 0