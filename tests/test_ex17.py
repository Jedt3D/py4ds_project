from src.ex17 import *


def test_roll_dice():
    assert roll_dice(0) == 0
    assert roll_dice(1000) != 1000
    for i in range(1000):
        assert 1 <= roll_dice(1) <= 6
        assert 2 <= roll_dice(2) <= 12
        assert 3 <= roll_dice(3) <= 18
        assert 100 <= roll_dice(100) <= 600
