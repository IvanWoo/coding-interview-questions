import pytest
from puzzles.path_with_minimum_effort import minimum_effort_path


@pytest.mark.parametrize(
    "maze, expected",
    [
        ([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2),
        ([[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1),
        (
            [
                [1, 2, 1, 1, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 1, 1, 2, 1],
            ],
            0,
        ),
        (
            [
                [1, 2, 1, 9, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 1, 1, 2, 1],
            ],
            1,
        ),
    ],
)
def test_minimum_effort_path(maze, expected):
    assert minimum_effort_path(maze) == expected
