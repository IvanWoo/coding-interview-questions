import pytest

from puzzles.best_time_to_buy_and_sell_stock import max_profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected
