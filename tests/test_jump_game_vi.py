import pytest
from puzzles.jump_game_vi import max_result


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, -1, -2, 4, -7, 3], 2, 7),
        ([10, -5, -2, 4, 0, 3], 3, 17),
        ([1, -5, -20, 4, -1, 3, -6, -3], 2, 0),
    ],
)
def test_max_result(nums, k, expected):
    assert max_result(nums, k) == expected
