import pytest

from puzzles.number_of_zero_filled_subarrays import zero_filled_subarray


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 0, 0, 2, 0, 0, 4], 6),
        ([0, 0, 0, 2, 0, 0], 9),
        ([2, 10, 2019], 0),
    ],
)
def test_zero_filled_subarray(nums, expected):
    assert zero_filled_subarray(nums) == expected
