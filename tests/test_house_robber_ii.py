import pytest

from puzzles.house_robber_ii import rob


@pytest.mark.parametrize(
    "nums, expected",
    [([1], 1), ([2, 3, 2], 3), ([1, 2, 3, 1], 4), ([1, 2, 3], 3)],
)
def test_rob(nums, expected):
    assert rob(nums) == expected
