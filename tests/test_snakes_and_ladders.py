import pytest
from puzzles.snakes_and_ladders import snakes_and_ladders


@pytest.mark.parametrize(
    "board, expected",
    [
        (
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ],
            4,
        ),
        ([[-1, -1], [-1, 3]], 1),
        ([[1, 1, -1], [1, 1, 1], [-1, 1, 1]], -1),
        (
            [
                [-1, -1, 19, 10, -1],
                [2, -1, -1, 6, -1],
                [-1, 17, -1, 19, -1],
                [25, -1, 20, -1, -1],
                [-1, -1, -1, -1, 15],
            ],
            2,
        ),
    ],
)
def test_snakes_and_ladders(board, expected):
    assert snakes_and_ladders(board) == expected
