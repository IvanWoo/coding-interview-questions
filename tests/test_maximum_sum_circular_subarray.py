import pytest

from puzzles.maximum_sum_circular_subarray import max_subarray_sum_circular


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, -2, 3, -2], 3),
        ([5, -3, 5], 10),
        ([3, -1, 2, -1], 4),
        ([3, -2, 2, -3], 3),
        ([-2, -3, -1], -1),
    ],
)
def test_max_subarray_sum_circular(nums, expected):
    assert max_subarray_sum_circular(nums) == expected
