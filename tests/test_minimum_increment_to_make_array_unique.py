from puzzles.minimum_increment_to_make_array_unique import min_increment_for_unique


def test_min_increment_for_unique():
    assert min_increment_for_unique([1, 2, 2]) == 1
    assert min_increment_for_unique([3, 2, 1, 2, 1, 7]) == 6
