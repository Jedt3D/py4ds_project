from src.ex05 import *

"""
FizzBuzz is a simple game to test if
the number is divisible by 3 or 5.
    1. Return Fizz if divisible by 3.
    2. Return Buzz if divisible by 5.
    3. Return FizzBuzz if divisible by both 3 and 5.
    4. Return the number if not divisible by 3 or 5.
"""


def test_fizz_buzz():
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(7) == 7
    assert fizz_buzz(2) == 2
