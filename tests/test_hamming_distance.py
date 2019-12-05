import pytest
from puzzles.hamming_distance import hamming_distance


def test_hamming_distance():
    assert hamming_distance(1, 4) == 2
