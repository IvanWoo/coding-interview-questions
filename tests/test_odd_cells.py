import pytest

from puzzles.odd_cells import odd_cells


def test_odd_cells():
    assert odd_cells(2, 3, [[0, 1], [1, 1]]) == 6
    assert odd_cells(2, 2, [[1, 1], [0, 0]]) == 0
