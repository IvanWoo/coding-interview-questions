import pytest

from puzzles.increasing_triplet_subsequence import increasing_triplet


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([2, 2, 2], False),
        ([2, 1, 5, 0, 4, 6], True),
        ([1, 2, 5, 4, 0, 6], True),
    ],
)
def test_increasing_triplet(nums, expected):
    assert increasing_triplet(nums) == expected
