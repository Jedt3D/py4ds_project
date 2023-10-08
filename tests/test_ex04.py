from src.ex04 import *

"""
The formulas for calculating area, perimeter, volume and surface area 
are based on the length(L), width(W) and height(H) of the shape

    1. area = L x W
    2. perimeter = L+W + L+W
    3. volume = L x W x H
    4. surface area = 2 x (L x W) + 2 x (W x H) + 2 x (L x H)
"""


def test_area():
    assert area(10, 10) == 100
    assert area(0, 9999) == 0
    assert area(5, 8) == 40


def test_perimeter():
    assert perimeter(10, 10) == 40
    assert perimeter(0, 9999) == 19998
    assert perimeter(5, 8) == 26


def test_volume():
    assert volume(10, 10, 10) == 1000
    assert volume(9999, 0, 9999) == 0
    assert volume(5, 8, 10) == 400


def test_surface_area():
    assert surface_area(10, 10, 10) == 600
    assert surface_area(9999, 0, 9999) == 199960002
    assert surface_area(5, 8, 10) == 340
