import pytest

from puzzles.detonate_the_maximum_bombs import maximum_detonation


@pytest.mark.parametrize(
    "bombs, expected",
    [
        ([[2, 1, 3], [6, 1, 4]], 2),
        ([[1, 1, 5], [10, 10, 5]], 1),
        ([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], 5),
        (
            [
                [54, 95, 4],
                [99, 46, 3],
                [29, 21, 3],
                [96, 72, 8],
                [49, 43, 3],
                [11, 20, 3],
                [2, 57, 1],
                [69, 51, 7],
                [97, 1, 10],
                [85, 45, 2],
                [38, 47, 1],
                [83, 75, 3],
                [65, 59, 3],
                [33, 4, 1],
                [32, 10, 2],
                [20, 97, 8],
                [35, 37, 3],
            ],
            1,
        ),
    ],
)
def test_maximum_detonation(bombs, expected):
    assert maximum_detonation(bombs) == expected
