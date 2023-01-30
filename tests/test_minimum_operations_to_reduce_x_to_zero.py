import pytest

from puzzles.minimum_operations_to_reduce_x_to_zero import min_operations


@pytest.mark.parametrize(
    "nums, x, expected",
    [
        ([1, 1, 4, 2, 3], 5, 2),
        ([5, 6, 7, 8, 9], 4, -1),
        ([3, 2, 20, 1, 1, 3], 10, 5),
        ([1, 1], 3, -1),
    ],
)
def test_min_operations(nums, x, expected):
    assert min_operations(nums, x) == expected
