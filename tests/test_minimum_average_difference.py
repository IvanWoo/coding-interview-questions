import pytest

from puzzles.minimum_average_difference import minimum_average_difference


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 5, 3, 9, 5, 3], 3),
        ([0], 0),
    ],
)
def test_minimum_average_difference(nums, expected):
    assert minimum_average_difference(nums) == expected
