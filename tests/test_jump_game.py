import pytest

from puzzles.jump_game import jump_game


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([2, 0, 0], True),
        ([2, 5, 0, 0], True),
    ],
)
def test_jump_game(nums, expected):
    assert jump_game(nums) == expected
