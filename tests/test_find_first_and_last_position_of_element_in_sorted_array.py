import pytest
from puzzles.find_first_and_last_position_of_element_in_sorted_array import search_range


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([2, 2], 2, [0, 1]),
        ([1, 3, 5, 7, 9], 1, [0, 0]),
    ],
)
def test_search_range(nums, target, expected):
    assert search_range(nums, target) == expected
