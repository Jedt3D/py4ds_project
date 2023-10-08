from src.ex19 import *


def test_gen_password():
    assert len(gen_password(8)) == 12
    pwd = gen_password(14)
    assert len(pwd) == 14
    has_lower_case = False
    has_upper_case = False
    has_number = False
    has_special_char = False
    for char in pwd:
        if char in LOWER_LETTERS:
            has_lower_case = True
        if char in UPPER_LETTERS:
            has_upper_case = True
        if char in NUMBERS:
            has_number = True
        if char in SPECIAL:
            has_special_char = True

    assert has_lower_case and has_upper_case and has_number and has_special_char
