import pytest
from puzzles.split_array_into_consecutive_subsequences import is_possible


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 3, 4, 5], True),
        ([1, 2, 3, 3, 4, 4, 5, 5], True),
        ([1, 2, 3, 4, 4, 5], False),
        ([1, 2, 3, 3, 3, 4, 4, 5], False),
        ([1, 2, 3, 3, 4, 5, 9], False),
        ([4, 5, 6, 7, 7, 8, 8, 9, 10, 11], True),
    ],
)
def test_is_possible(nums, expected):
    assert is_possible(nums) == expected
