import pytest
from puzzles.best_time_to_buy_and_sell_stock_iv import max_profit


@pytest.mark.parametrize(
    "k, prices, expected",
    [
        (2, [2, 4, 1], 2),
        (2, [3, 2, 6, 5, 0, 3], 7),
    ],
)
def test_max_profit(k, prices, expected):
    assert max_profit(k, prices) == expected
