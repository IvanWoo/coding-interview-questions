from puzzles.best_time_to_buy_and_sell_stock_iii import max_profit


def test_max_profit():
    assert max_profit([1, 2, 3, 4, 5]) == 4
    assert max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1]) == 0
