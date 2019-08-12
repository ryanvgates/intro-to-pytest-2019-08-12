import pytest

def divide_by_two(a):
    return a / 2


def divide_by(a, b):
    return a / b


def test_divide():
    assert divide_by_two(8) == 4
    assert divide_by_two(0) == 0


def test_error():
    assert divide_by(4, 2) == 2
    with pytest.rases(ZeroDivisionError):
        assert divide_by(9, 0) == 1
