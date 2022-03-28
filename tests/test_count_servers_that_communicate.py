import pytest
from puzzles.count_servers_that_communicate import count_servers


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 0], [0, 1]], 0),
        ([[1, 0], [1, 1]], 3),
        ([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4),
        (
            [
                [1, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
            ],
            8,
        ),
    ],
)
def test_count_servers(grid, expected):
    assert count_servers(grid) == expected
