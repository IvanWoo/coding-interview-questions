import pytest
from puzzles.non_decreasing_array import check_possibility


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 2], True),
        ([4, 2, 3], True),
        ([4, 2, 1], False),
        ([-1, 4, 2, 3], True),
        ([3, 4, 2, 3], False),
        ([5, 7, 1, 8], True),
        ([3, 4, 2, 3], False),
    ],
)
def test_check_possibility(nums, expected):
    assert check_possibility(nums) == expected
