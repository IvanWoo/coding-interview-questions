import pytest
from puzzles.jump_game_ii import jump_game


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([0], 0),
        ([1, 1, 1, 1], 3),
    ],
)
def test_jump_game(nums, expected):
    assert jump_game(nums) == expected
