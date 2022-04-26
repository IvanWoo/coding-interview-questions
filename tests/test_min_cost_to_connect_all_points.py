import pytest
from puzzles.min_cost_to_connect_all_points import min_cost_connect_points


@pytest.mark.parametrize(
    "points, expected",
    [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
        ([[0, 0], [1, 1], [1, 0], [-1, 1]], 4),
        ([[-1000000, -1000000], [1000000, 1000000]], 4000000),
        ([[0, 0]], 0),
    ],
)
def test_min_cost_connect_points(points, expected):
    assert min_cost_connect_points(points) == expected
