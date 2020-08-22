import pytest
from puzzles.two_sum import two_sum


def test_two_sum():
    assert two_sum([1, 2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([1], 2) == [0, 0]
