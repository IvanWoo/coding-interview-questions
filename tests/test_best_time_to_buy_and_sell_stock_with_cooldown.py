import pytest
from puzzles.best_time_to_buy_and_sell_stock_with_cooldown import max_profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([1, 2, 3, 0, 2], 3),
        ([1], 0),
    ],
)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected
