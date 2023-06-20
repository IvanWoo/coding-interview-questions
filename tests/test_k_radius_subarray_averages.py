import pytest

from puzzles.k_radius_subarray_averages import get_averages


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([7, 4, 3, 9, 1, 8, 5, 2, 6], 3, [-1, -1, -1, 5, 4, 4, -1, -1, -1]),
        ([100000], 0, [100000]),
        ([8], 100000, [-1]),
    ],
)
def test_get_averages(nums, k, expected):
    assert get_averages(nums, k) == expected
