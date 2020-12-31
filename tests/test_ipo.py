from puzzles.ipo import find_maximized_capital


def test_find_maximized_capital():
    assert find_maximized_capital(k=2, W=0, Profits=[1, 2, 3], Capital=[0, 1, 1]) == 4
    assert find_maximized_capital(1, 0, [1, 2, 3], [1, 1, 2]) == 0
