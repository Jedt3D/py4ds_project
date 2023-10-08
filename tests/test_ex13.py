from src.ex13 import *


def test_calc_sum():
    assert calc_sum([]) == 0
    assert calc_sum([2, 4, 6, 8, 10]) == 30


def test_calc_prod():
    assert calc_prod([]) == 1
    assert calc_prod([2, 4, 6, 8, 10]) == 3840
