import pytest
from puzzles.maximum_xor_of_two_numbers_in_an_array import find_maximum_XOR


def test_find_maximum_XOR():
    # assert find_maximum_XOR([3, 10, 5, 25, 2, 8]) == 28
    assert find_maximum_XOR([0]) == 0
    assert find_maximum_XOR([8, 10, 2]) == 10
    assert find_maximum_XOR([2, 4]) == 6
    assert find_maximum_XOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127
