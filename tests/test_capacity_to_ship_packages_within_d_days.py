import pytest
from puzzles.capacity_to_ship_packages_within_d_days import ship_within_days


def test_ship_within_days():
    assert ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert ship_within_days([3, 2, 2, 4, 1, 4], 3) == 6
    assert ship_within_days([1, 2, 3, 1, 1], 4) == 3
