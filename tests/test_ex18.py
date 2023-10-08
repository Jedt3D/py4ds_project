from src.ex18 import *


def test_get_cost_of_coffee():
    assert get_cost_of_coffee(7, 2.50) == 17.50
    assert get_cost_of_coffee(8, 2.50) == 20
    assert get_cost_of_coffee(9, 2.50) == 20
    assert get_cost_of_coffee(10, 2.50) == 22.50
    for i in range(1, 4):
        assert get_cost_of_coffee(0, i) == 0
        assert get_cost_of_coffee(8, i) == 8 * i
        assert get_cost_of_coffee(9, i) == 8 * i
        assert get_cost_of_coffee(18, i) == 16 * i
        assert get_cost_of_coffee(19, i) == 17 * i
        assert get_cost_of_coffee(30, i) == 27 * i


def test_get_cost_of_coffee_2():
    assert get_cost_of_coffee_2(7, 2.50) == 17.50
    assert get_cost_of_coffee_2(8, 2.50) == 20
    assert get_cost_of_coffee_2(9, 2.50) == 20
    assert get_cost_of_coffee_2(10, 2.50) == 22.50
    for i in range(1, 4):
        assert get_cost_of_coffee_2(0, i) == 0
        assert get_cost_of_coffee_2(8, i) == 8 * i
        assert get_cost_of_coffee_2(9, i) == 8 * i
        assert get_cost_of_coffee_2(18, i) == 16 * i
        assert get_cost_of_coffee_2(19, i) == 17 * i
        assert get_cost_of_coffee_2(30, i) == 27 * i
