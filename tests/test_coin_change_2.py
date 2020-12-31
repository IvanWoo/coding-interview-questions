from puzzles.coin_change_2 import change


def test_change():
    assert change(amount=5, coins=[1, 2, 5]) == 4
    assert change(amount=3, coins=[2]) == 0
    assert change(amount=10, coins=[10]) == 1
