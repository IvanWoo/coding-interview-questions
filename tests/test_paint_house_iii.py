import pytest
from puzzles.paint_house_iii import min_cost


@pytest.mark.parametrize(
    "houses, cost, m, n, target, expected",
    [
        ([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 9),
        ([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 11),
        ([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3, -1),
    ],
)
def test_min_cost(houses, cost, m, n, target, expected):
    assert min_cost(houses, cost, m, n, target) == expected
