import pytest
from puzzles.find132pattern import find132pattern


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 5, 0, 3, 4], True),
        ([3, 5, 0, 2, 1], True),
        ([1, 2, 3, 4], False),
        ([-1, 3, 2, 0], True),
        ([1, 0, 1, -4, -3], False),
        ([1, 1, 1, 1, 1], False),
    ],
)
def test_find132pattern(nums, expected):
    assert find132pattern(nums) == expected
