from src.ex09 import *


def test_get_chess_square_color():
    assert get_chess_square_color(1, 1) == 'White'
    assert get_chess_square_color(2, 2) == 'White'
    assert get_chess_square_color(3, 3) == 'White'
    assert get_chess_square_color(4, 4) == 'White'
    assert get_chess_square_color(1, 2) == 'Black'
    assert get_chess_square_color(5, 4) == 'Black'
    assert get_chess_square_color(6, 7) == 'Black'
    assert get_chess_square_color(7, 2) == 'Black'
