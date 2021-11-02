from puzzles.online_stock_span import StockSpanner


def test_StockSpanner_1():
    obj = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    spans = [1, 1, 1, 2, 1, 4, 6]
    ans = [0] * len(prices)
    for i, p in enumerate(prices):
        ans[i] = obj.next(p)

    assert ans == spans


def test_StockSpanner_2():
    obj = StockSpanner()
    prices = [31, 41, 48, 59, 79]
    spans = [1, 2, 3, 4, 5]
    ans = [0] * len(prices)
    for i, p in enumerate(prices):
        ans[i] = obj.next(p)

    assert ans == spans
