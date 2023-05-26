import pytest

from puzzles.stone_game_ii import stone_game_ii


@pytest.mark.parametrize(
    "piles, expected",
    [
        ([2, 7, 9, 4, 4], 10),
        ([1, 2, 3, 4, 5, 100], 104),
    ],
)
def test_stone_game_ii(piles, expected):
    assert stone_game_ii(piles) == expected
