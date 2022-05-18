import pytest
from puzzles.shortest_path_in_binary_matrix import shortest_path_binary_matrix


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
        (
            [
                [0, 1, 1, 0, 0, 0],
                [0, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 0],
                [0, 0, 0, 1, 1, 0],
                [1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 0],
            ],
            14,
        ),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 1]], -1),
    ],
)
def test(grid, expected):
    assert shortest_path_binary_matrix(grid) == expected
