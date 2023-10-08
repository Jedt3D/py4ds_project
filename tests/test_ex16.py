from src.ex16 import *


def test_mode():
    assert mode([]) is None
    assert mode([1, 2, 3, 4, 4]) == 4
    assert mode([1, 1, 2, 3, 4]) == 1
    assert mode([1, 2, 2, 2, 3]) == 2
