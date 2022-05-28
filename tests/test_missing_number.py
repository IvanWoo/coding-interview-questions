import pytest
from puzzles.missing_number import missing_number


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ],
)
def test(nums, expected):
    assert missing_number(nums) == expected
