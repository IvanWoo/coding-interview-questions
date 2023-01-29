import pytest

from puzzles.find_all_numbers_disappeared_in_an_array import find_disappeared_numbers


def test_find_disappeared_numbers():
    assert find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
