import pytest

from puzzles.number_of_ways_to_reorder_array_to_get_same_bst import num_of_ways


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 1, 3], 1),
        ([3, 4, 5, 1, 2], 5),
        ([1, 2, 3], 0),
    ],
)
def test_num_of_ways(nums, expected):
    assert num_of_ways(nums) == expected
