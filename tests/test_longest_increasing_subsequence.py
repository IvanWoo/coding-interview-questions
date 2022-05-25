import pytest
from puzzles.longest_increasing_subsequence import length_of_LIS


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], 0),
        ([10, 9, 2, 5, 3, 4], 3),
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ],
)
def test_length_of_LIS(nums, expected):
    assert length_of_LIS(nums) == expected
