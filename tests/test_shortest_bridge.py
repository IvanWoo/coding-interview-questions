import pytest

from puzzles.shortest_bridge import shortest_bridge


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[0, 1], [1, 0]], 1),
        ([[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2),
        (
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ],
            1,
        ),
    ],
)
def test_shortest_bridge(grid, expected):
    assert shortest_bridge(grid) == expected
