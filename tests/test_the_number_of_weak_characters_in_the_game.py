import pytest

from puzzles.the_number_of_weak_characters_in_the_game import number_of_weak_characters


@pytest.mark.parametrize(
    "properties, expected",
    [
        ([[5, 5], [6, 3], [3, 6]], 0),
        ([[2, 2], [3, 3]], 1),
        ([[1, 5], [10, 4], [4, 3]], 1),
        ([[1, 1], [2, 1], [2, 2], [1, 2]], 1),
        ([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]], 2),
        (
            [
                [7, 7],
                [1, 2],
                [9, 7],
                [7, 3],
                [3, 10],
                [9, 8],
                [8, 10],
                [4, 3],
                [1, 5],
                [1, 5],
            ],
            6,
        ),
    ],
)
def test_number_of_weak_characters(properties, expected):
    assert number_of_weak_characters(properties) == expected
