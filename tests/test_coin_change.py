import pytest

from puzzles.coin_change import coin_change


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ],
)
def test_coin_change(coins, amount, expected):
    assert coin_change(coins, amount) == expected
