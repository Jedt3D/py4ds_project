from src.ex03 import *


def test_is_odd():
    assert is_odd(42) is False
    assert is_odd(9999) is True
    assert is_odd(-10) is False
    assert is_odd(-11) is True
    assert is_odd(3.1415) is False


def test_is_even():
    assert is_even(42) is True
    assert is_even(9999) is False
    assert is_even(-10) is True
    assert is_even(-11) is False
    assert is_even(3.1415) is False
