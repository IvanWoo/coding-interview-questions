import pytest

from puzzles.shortest_path_in_a_grid_with_obstacles_elimination import shortest_path


@pytest.mark.parametrize(
    "grid, k, expected",
    [
        ([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1, 6),
        ([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1, -1),
    ],
)
def test_shortest_path(grid, k, expected):
    assert shortest_path(grid, k) == expected
