import pytest

from puzzles.as_far_from_land_as_possible import max_distance


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 1], [1, 1]], -1),
        ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 2),
        ([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 4),
        ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], -1),
    ],
)
def test_max_distance(grid, expected):
    assert max_distance(grid) == expected
