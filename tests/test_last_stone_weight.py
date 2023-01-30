import pytest

from puzzles.last_stone_weight import last_stone_weight


@pytest.mark.parametrize(
    "stones, expected", [([2, 7, 4, 1, 8, 1], 1), ([2, 2], 0), ([1], 1)]
)
def test_last_stone_weight(stones, expected):
    assert last_stone_weight(stones) == expected
