import pytest

from puzzles.jump_game_iv import min_jumps


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([100, -23, -23, 404, 100, 23, 23, 23, 3, 404], 3),
        ([7], 0),
        ([7, 6, 9, 6, 9, 6, 9, 7], 1),
        ([7, 7, 7, 7, 7, 7, 9], 2),
    ],
)
def test_min_jumps(arr, expected):
    assert min_jumps(arr) == expected
