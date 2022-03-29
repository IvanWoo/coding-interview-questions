import pytest
from puzzles.find_the_duplicate_number import find_duplicate


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([2, 2, 2], 2),
    ],
)
def test_find_duplicate(nums, expected):
    assert find_duplicate(nums) == expected
