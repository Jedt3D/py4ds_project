from src.ex08 import *

file = 'greeting.txt'


def test_write_to_file():
    msg = 'write to current file\n'
    write_to_file(file, msg)
    with open(file, 'r') as f:
        content = f.read()
        assert content == msg


def test_append_to_file():
    msg = 'append to current file\n'
    expected = 'write to current file\nappend to current file\n'
    append_to_file(file, msg)
    with open(file, 'r') as f:
        content = f.read()
        assert content == expected


def test_read_from_file():
    expected = 'write to current file\nappend to current file\n'
    with open(file, 'r') as f:
        content = f.read()
    assert read_from_file(file) == expected


def test_file_operations():
    write_to_file(file, 'Hello\n')
    append_to_file(file, 'World!\n')
    assert read_from_file(file) == 'Hello\nWorld!\n'
