from src.ex03 import *


def test_is_odd():
    assert is_odd(42) == False
    assert is_odd(9999) == True
    assert is_odd(-10) == False
    assert is_odd(-11) == True
    assert is_odd(3.1415) == False


def test_is_even():
    assert is_even(42) == True
    assert is_even(9999) == False
    assert is_even(-10) == True
    assert is_even(-11) == False
    assert is_even(3.1415) == False
