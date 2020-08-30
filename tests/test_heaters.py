import pytest
from puzzles.heaters import find_radius


def test_find_radius():
    assert find_radius([1, 2, 3], [2]) == 1
    assert find_radius([1, 2, 3, 4], [1, 4]) == 1
