from src.ex01 import *


def test_greeting(capsys):
    greeting()
    captured = capsys.readouterr()
    assert captured.out == 'สวัสดีชาวลาดกระบัง\n'


def test_know_my_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Worajedt")
    result = know_my_name()
    assert result == 'Worajedt'


def test_say_hi(capsys):
    say_hi('เจษ')
    captured = capsys.readouterr()
    assert captured.out == 'สวัสดีคุณเจษ\n'

