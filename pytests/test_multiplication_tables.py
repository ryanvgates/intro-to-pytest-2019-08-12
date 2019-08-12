import pytest
from multiplication_tables import multiplication_tables

def test_two_by_two():
    assert multiplication_tables(2, 2) == [[1, 2], [2, 4]]


def test_three_by_four():
    assert multiplication_tables(3, 4) == [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]