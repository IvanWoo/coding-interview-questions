import pytest
from puzzles.unique_paths_ii import unique_paths_with_obstacles


@pytest.mark.parametrize(
    "obstacle_grid, expected",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 6),
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 0]], 1),
        ([[0, 0], [1, 1], [0, 0]], 0),
        ([[1, 0]], 0),
    ],
)
def test_unique_paths_with_obstacles(obstacle_grid, expected):
    assert unique_paths_with_obstacles(obstacle_grid) == expected
