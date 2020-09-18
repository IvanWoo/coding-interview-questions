import pytest
from puzzles.shortest_unsorted_continuous_subarray import find_unsorted_subarray


def test_find_unsorted_subarray():
    assert find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]) == 5