from puzzles.count_of_range_sum import count_range_sum


def test_count_range_sum():
    assert count_range_sum([-2, 5, -1], -2, 2) == 3
    assert count_range_sum([2147483647, -2147483648, -1, 0], -1, 0) == 4
    assert count_range_sum([2147483647, -2147483647, -1, 0], -1, 0) == 6
