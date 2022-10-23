import pytest
from puzzles.set_mismatch import find_error_nums


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 2, 4], [2, 3]),
        ([1, 1], [1, 2]),
    ],
)
def test_find_error_nums(nums, expected):
    assert find_error_nums(nums) == expected
