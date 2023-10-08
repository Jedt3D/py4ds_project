from src.ex22 import *


def test_rps_check():
    assert rps_check('rock', 'paper') == 'player two'
    assert rps_check('rock', 'scissors') == 'player one'
    assert rps_check('paper', 'scissors') == 'player two'
    assert rps_check('paper', 'rock') == 'player one'
    assert rps_check('scissors', 'rock') == 'player two'
    assert rps_check('scissors', 'paper') == 'player one'
    assert rps_check('rock', 'rock') == 'tie'
    assert rps_check('paper', 'paper') == 'tie'
    assert rps_check('scissors', 'scissors') == 'tie'
    
