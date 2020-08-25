import pytest
from puzzles.merge_sort import sort, merge_sort


def test_sort():
    assert sort([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert sort([5, 2, 3, 1]) == [1, 2, 3, 5]


def test_merge_sort():
    assert merge_sort([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    assert merge_sort([5, 2, 3, 1]) == [1, 2, 3, 5]
