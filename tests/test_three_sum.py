import pytest
from puzzles.three_sum import three_sum


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0], []),
        ([1, 2, -2, -1], []),
        ([], []),
    ],
)
def test_three_sum(nums, expected):
    assert three_sum(nums) == expected
