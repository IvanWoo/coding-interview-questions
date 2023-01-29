import pytest

from puzzles.unique_paths_iii import unique_paths_iii


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4),
        ([[0, 1], [2, 0]], 0),
    ],
)
def test_unique_paths_iii(grid, expected):
    assert unique_paths_iii(grid) == expected
