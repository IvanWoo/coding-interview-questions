import pytest

from puzzles.best_time_to_buy_and_sell_stock_iii import max_profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([1, 2, 3, 4, 5], 4),
        ([3, 3, 5, 0, 0, 3, 1, 4], 6),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
    ],
)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected
