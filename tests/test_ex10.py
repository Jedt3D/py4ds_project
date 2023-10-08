from src.ex10 import *


def test_find_and_replace():
    assert find_and_replace('The fox', 'fox', 'dog') == 'The dog'
    assert find_and_replace('fox', 'fox', 'dog') == 'dog'
    assert find_and_replace('Firefox', 'fox', 'dog') == 'Firedog'
    assert find_and_replace('foxfox', 'fox', 'dog') == 'dogdog'
    assert find_and_replace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
