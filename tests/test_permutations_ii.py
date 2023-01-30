import pytest

from puzzles.permutations_ii import permute_unique


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ],
)
def test_permute_unique(nums, expected):
    assert sorted(permute_unique(nums)) == sorted(expected)
