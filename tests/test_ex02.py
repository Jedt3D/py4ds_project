from src.ex02 import *

"""
Use this two formulas for converting between Celsius and Fahrenheit
1. Fahrenheit = (9/5) * Celsius + 32
2. Celsius = (Fahrenheit - 32) * (5/9)
"""


def test_convert_to_celsius():
    assert convert_to_celsius(0) == -17.77777777777778
    assert convert_to_celsius(180) == 82.22222222222223


def test_convert_to_fahrenheit():
    assert convert_to_fahrenheit(0) == 32
    assert convert_to_fahrenheit(100) == 212


def test_convert_two_times():
    assert convert_to_celsius(convert_to_fahrenheit(15)) == 15
    # ทำไม?? ทำไมต้อง round() ??
    # TODO: answer this
    assert convert_to_celsius(convert_to_fahrenheit(42)) == round(42.00000000000001)
