import pytest

from puzzles.single_element_in_a_sorted_array import single_non_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
    ],
)
def test_single_non_duplicate(nums, expected):
    assert single_non_duplicate(nums) == expected
