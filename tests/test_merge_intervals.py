import pytest

from puzzles.merge_intervals import merge


def test_merge():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
