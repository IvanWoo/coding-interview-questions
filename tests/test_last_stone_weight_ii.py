import pytest

from puzzles.last_stone_weight_ii import last_stone_weight_ii


@pytest.mark.parametrize(
    "stones, expected",
    [([2, 7, 4, 1, 8, 1], 1), ([31, 26, 33, 21, 40], 5), ([1, 2], 1)],
)
def test_last_stone_weight_ii(stones, expected):
    assert last_stone_weight_ii(stones) == expected
