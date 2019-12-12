import pytest
from puzzles.three_sum_closest import three_sum_closest


def test_three_sum_closest():
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2
    assert three_sum_closest([0, 1, 2], 3) == 3
    assert three_sum_closest([0, 2, 1, -3], 1) == 0
