from src.ex11 import *


def test_get_hr_min_sec():
    assert get_hr_min_sec(30) == '30s'
    assert get_hr_min_sec(60) == '1m'
    assert get_hr_min_sec(90) == '1m 30s'
    assert get_hr_min_sec(3600) == '1h'
    assert get_hr_min_sec(3601) == '1h 1s'
    assert get_hr_min_sec(3661) == '1h 1m 1s'
    assert get_hr_min_sec(90042) == '25h 42s'
    assert get_hr_min_sec(0) == '0s'
