import pytest
from puzzles.best_time_to_buy_and_sell_stock_with_transaction_fee import max_profit


@pytest.mark.parametrize(
    "prices, fee, expected",
    [
        ([1, 3, 2, 8, 4, 9], 2, 8),
        ([1, 3, 7, 5, 10, 3], 3, 6),
    ],
)
def test_max_profit(prices, fee, expected):
    assert max_profit(prices, fee) == expected
