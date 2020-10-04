from puzzles.edit_distance import min_distance


def test_min_distance():
    assert min_distance("intention", "execution") == 5
    assert min_distance("horse", "ros") == 3
    assert min_distance("", "") == 0
