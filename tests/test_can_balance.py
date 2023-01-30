import pytest

from puzzles.can_balance import can_balance


def test_can_balance():
    assert can_balance([1, 1, 1, 2, 1]) == True
    assert can_balance([2, 1, 1, 2, 1]) == False
    assert can_balance([10, 10]) == True
