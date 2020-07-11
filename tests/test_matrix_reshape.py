import pytest

from puzzles.matrix_reshape import matrix_reshape, matrix_reshape_2


def test_matrix_reshape():
    nums = [[1, 2], [3, 4]]
    assert matrix_reshape(nums, 2, 4) == nums
    assert matrix_reshape(nums, 1, 4) == [[1, 2, 3, 4]]
    assert matrix_reshape(nums, 4, 1) == [[x] for x in range(1, 5)]


def test_matrix_reshape_2():
    nums = [[1, 2], [3, 4]]
    assert matrix_reshape_2(nums, 2, 4) == nums
    assert matrix_reshape_2(nums, 1, 4) == [[1, 2, 3, 4]]
    assert matrix_reshape_2(nums, 4, 1) == [[x] for x in range(1, 5)]
