import pytest

from puzzles.minimize_deviation_in_array import minimum_deviation


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], 1),
        ([4, 1, 5, 20, 3], 3),
        ([2, 10, 8], 3),
        ([1, 13], 11),
        ([4, 9, 4, 5], 5),
    ],
)
def test_minimum_deviation(nums, expected):
    assert minimum_deviation(nums) == expected
