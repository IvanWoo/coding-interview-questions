import pytest
from puzzles.longest_increasing_subsequence import length_of_LIS


def test_length_of_LIS():
    assert length_of_LIS([]) == 0
    assert length_of_LIS([10, 9, 2, 5, 3, 4]) == 3
    assert length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
