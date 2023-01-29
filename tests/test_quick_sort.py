import pytest

from puzzles.quick_sort import sort


def test_sort():
    assert sort([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert sort([5, 2, 3, 1]) == [1, 2, 3, 5]
