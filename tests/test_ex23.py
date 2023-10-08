from src.ex23 import *


def test_bottles_of_beer():
    assert bottles_of_beer(99) == """99 bottles of beer on the wall,
99 bottles of beer.
Take one down, pass it around,
98 bottles of beer on the wall.
"""
    assert bottles_of_beer(25) == """25 bottles of beer on the wall,
25 bottles of beer.
Take one down, pass it around,
24 bottles of beer on the wall.
"""
    assert bottles_of_beer(9) == """9 bottles of beer on the wall,
9 bottles of beer.
Take one down, pass it around,
8 bottles of beer on the wall.
"""
    assert bottles_of_beer(1) == """1 bottle of beer on the wall,
1 bottle of beer.
Take one down, pass it around,
No more bottles of beer on the wall!
"""
