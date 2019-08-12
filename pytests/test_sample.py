import pytest
from functions import divide_by, divide_by_two, sum_all


def test_divide():
    assert divide_by_two(8) == 4
    assert divide_by_two(0) == 0


def test_error():
    assert divide_by(4, 2) == 2
    with pytest.raises(ZeroDivisionError):
        assert divide_by(9, 0) == 1


def test_sum():
    assert sum_all([1, 2, 3, 4]) == 10
    assert sum_all([1, 2, 3, 4, -10]) == 0
    with pytest.raises(ValueError):
        assert sum_all([]) == 0
    with pytest.raises(ValueError):
        assert sum_all(1) == 0


