import pytest

from puzzles.online_stock_span import StockSpanner


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6]),
        ([31, 41, 48, 59, 79], [1, 2, 3, 4, 5]),
    ],
)
def test_stock_spanner(prices, expected):
    obj = StockSpanner()
    ans = [obj.next(p) for p in prices]
    assert ans == expected
