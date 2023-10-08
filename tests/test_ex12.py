from src.ex12 import *


def test_get_smallest():
    assert get_smallest([1, 2, 3]) == 1
    assert get_smallest([3, 2, 1]) == 1
    assert get_smallest([28, 25, 42, 2, 28]) == 2
    assert get_smallest([1]) == 1
    assert get_smallest([]) is None
