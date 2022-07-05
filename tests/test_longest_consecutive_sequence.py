import pytest
from puzzles.longest_consecutive_sequence import longest_consecutive


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 2, 0, 1], 3),
        ([], 0),
        ([100, 4, 200, 1, 3, 2], 4),
    ],
)
def test_longest_consecutive(nums, expected):
    assert longest_consecutive(nums) == expected
