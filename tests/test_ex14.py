from src.ex14 import *


def test_average():
    assert average([1, 2, 3]) == 2
    assert average([1, 2, 8]) == 3.66666666666666652
    assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert average([12, 20, 37]) == 23
    assert average([0, 0, 0, 0, 0]) == 0
