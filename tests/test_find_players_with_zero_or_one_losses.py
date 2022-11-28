import pytest
from puzzles.find_players_with_zero_or_one_losses import find_winners


@pytest.mark.parametrize(
    "matches, expected",
    [
        (
            [
                [1, 3],
                [2, 3],
                [3, 6],
                [5, 6],
                [5, 7],
                [4, 5],
                [4, 8],
                [4, 9],
                [10, 4],
                [10, 9],
            ],
            [[1, 2, 10], [4, 5, 7, 8]],
        ),
        ([[2, 3], [1, 3], [5, 4], [6, 4]], [[1, 2, 5, 6], []]),
    ],
)
def test_find_winners(matches, expected):
    assert find_winners(matches) == expected
