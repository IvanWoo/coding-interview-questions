import pytest

from puzzles.maximum_value_of_k_coins_from_piles import max_value_of_coins


@pytest.mark.parametrize(
    "piles, k, expected",
    [
        ([[1, 100, 3], [7, 8, 9]], 2, 101),
        ([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7, 706),
    ],
)
def test_max_value_of_coins(piles, k, expected):
    assert max_value_of_coins(piles, k) == expected
