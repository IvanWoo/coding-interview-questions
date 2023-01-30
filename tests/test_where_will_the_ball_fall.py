import pytest

from puzzles.where_will_the_ball_fall import find_ball


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                [1, 1, 1, -1, -1],
                [1, 1, 1, -1, -1],
                [-1, -1, -1, 1, 1],
                [1, 1, 1, 1, -1],
                [-1, -1, -1, -1, -1],
            ],
            [1, -1, -1, -1, -1],
        ),
        ([[-1]], [-1]),
        (
            [
                [1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1],
                [1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1],
            ],
            [0, 1, 2, 3, 4, -1],
        ),
    ],
)
def test_find_ball(grid, expected):
    assert find_ball(grid) == expected
