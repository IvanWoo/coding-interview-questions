import pytest

from puzzles.trapping_rain_water import trap


def test_trap():
    assert trap([1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]) == 15
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([0] * 10) == 0
    assert trap(list(range(10))) == 0
    assert trap(list(range(10, 0, -1))) == 0

