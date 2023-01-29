import pytest

from puzzles.three_sum_closest import three_sum_closest


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([0, 1, 2], 3, 3),
        ([0, 2, 1, -3], 1, 0),
    ],
)
def test_three_sum_closest(nums, target, expected):
    assert three_sum_closest(nums, target) == expected
