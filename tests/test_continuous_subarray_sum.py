import pytest

from puzzles.continuous_subarray_sum import check_subarray_sum


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([23, 2, 6], 6, False),
        ([23, 2, 6, 4, 7], 6, True),
        ([23, 2, 6, 4, 7], 13, False),
        ([23, 2, 4, 6, 6], 7, True),
    ],
)
def test_check_subarray_sum(nums, k, expected):
    assert check_subarray_sum(nums, k) == expected
