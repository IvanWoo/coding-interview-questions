import pytest
from puzzles.degree_of_array import find_shortest_sub_array


def test_find_shortest_sub_array():
    assert find_shortest_sub_array([1, 2, 2, 3, 1, 4, 2]) == 6
    assert find_shortest_sub_array([1, 2, 2, 3, 1]) == 2
