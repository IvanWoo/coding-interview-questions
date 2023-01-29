import pytest

from puzzles.remove_stones_to_minimize_the_total import min_stone_sum


@pytest.mark.parametrize(
    "piles, k, expected",
    [
        ([5, 4, 9], 2, 12),
        ([4, 3, 6, 7], 3, 12),
    ],
)
def test_min_stone_sum(piles, k, expected):
    assert min_stone_sum(piles, k) == expected
