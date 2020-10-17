from puzzles.largest_rectangle_in_histogram import largest_rectangle_area


def test_largest_rectangle_in_histogram():
    assert largest_rectangle_area([1]) == 1
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
