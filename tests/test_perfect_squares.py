import pytest
from puzzles.perfect_squares import num_squares


def test_num_squares():
    assert num_squares(12) == 3
    assert num_squares(13) == 2
