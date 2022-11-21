import pytest
from puzzles.nearest_exit_from_entrance_in_maze import nearest_exit


@pytest.mark.parametrize(
    "maze, entrance, expected",
    [
        ([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2], 1),
        ([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0], 2),
        ([[".", "+"]], [0, 0], -1),
        (
            [
                ["+", ".", "+", "+", "+", "+", "+"],
                ["+", ".", "+", ".", ".", ".", "+"],
                ["+", ".", "+", ".", "+", ".", "+"],
                ["+", ".", ".", ".", "+", ".", "+"],
                ["+", "+", "+", "+", "+", ".", "+"],
            ],
            [0, 1],
            12,
        ),
    ],
)
def test_nearest_exit(maze, entrance, expected):
    assert nearest_exit(maze, entrance) == expected
