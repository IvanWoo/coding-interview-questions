import pytest
from puzzles.letter_tile_possibilities import num_tile_possibilities


def test_num_tile_possibilities():
    assert num_tile_possibilities("AAB") == 8
    assert num_tile_possibilities("AAABBC") == 188
