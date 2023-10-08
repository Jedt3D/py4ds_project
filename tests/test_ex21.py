from src.ex21 import *


def test_is_valid_date():
    assert is_valid_date(1999, 12, 31) is True
    assert is_valid_date(2000, 2, 29) is True
    assert is_valid_date(2001, 2, 29) is False
    assert is_valid_date(2029, 13, 1) is False
    assert is_valid_date(1000000, 1, 1) is True
    assert is_valid_date(2015, 4, 31) is False
    assert is_valid_date(1970, 5, 99) is False
    assert is_valid_date(1981, 0, 3) is False
    assert is_valid_date(1666, 4, 0) is False

    import datetime

    d = datetime.datetime(1970, 1, 1)
    one_day = datetime.timedelta(days=1)
    for i in range(1000000):
        assert is_valid_date(d.year, d.month, d.day) is True
        d += one_day
