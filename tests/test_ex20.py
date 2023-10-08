from src.ex20 import *


def test_is_leap_year():
    assert is_leap_year(1999) is False
    assert is_leap_year(2000) is True
    assert is_leap_year(2001) is False
    assert is_leap_year(2004) is True
    assert is_leap_year(2100) is False
    assert is_leap_year(2400) is True
