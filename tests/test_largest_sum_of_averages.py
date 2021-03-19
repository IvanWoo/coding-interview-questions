from puzzles.largest_sum_of_averages import largest_sum_of_averages


def test_largest_sum_of_averages():
    assert largest_sum_of_averages([9, 1, 2], 3) == 12
    assert largest_sum_of_averages([9, 1, 2, 3, 9], 3) == 20
