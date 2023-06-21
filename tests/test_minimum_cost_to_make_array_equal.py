import pytest

from puzzles.minimum_cost_to_make_array_equal import min_cost


@pytest.mark.parametrize(
    "nums, cost, expected",
    [
        ([1, 3, 5, 2], [2, 3, 1, 14], 8),
        ([2, 2, 2, 2, 2], [4, 2, 8, 1, 3], 0),
    ],
)
def test_min_cost(nums, cost, expected):
    assert min_cost(nums, cost) == expected
