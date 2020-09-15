import pytest
from puzzles.score_after_flipping_matrix import matrix_score


def test_matrix_score():
    assert matrix_score([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]) == 39
