import pytest
from puzzles.delete_and_earn import delete_and_earn


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1], 1),
        ([3, 4, 2], 6),
        ([2, 2, 3, 3, 3, 4], 9),
    ],
)
def test_delete_and_earn(nums, expected):
    assert delete_and_earn(nums) == expected
