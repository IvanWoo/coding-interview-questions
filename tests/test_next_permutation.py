import pytest
from puzzles.next_permutation import next_permutation


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], [1, 3, 2]),
        ([1, 3, 2], [2, 1, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 5, 4]),
        ([1, 2, 5, 8, 7], [1, 2, 7, 5, 8]),
    ],
)
def test_next_permutation(nums, expected):
    next_permutation(nums)
    assert nums == expected
