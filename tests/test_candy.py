from puzzles.candy import candy


def test_candy():
    assert candy([1, 0, 2]) == 5
    assert candy([1, 2, 2]) == 4
    assert candy([1, 2, 87, 87, 87, 2, 1]) == 13
    assert candy([1, 6, 10, 8, 7, 3, 2]) == 18
    assert candy([1, 3, 4, 5, 2]) == 11
