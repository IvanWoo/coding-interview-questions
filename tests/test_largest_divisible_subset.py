from puzzles.largest_divisible_subset import largest_divisible_subset


def test_largest_divisible_subset():
    assert largest_divisible_subset([1, 2, 3]) == [1, 2]
    assert largest_divisible_subset([1, 2, 4, 8]) == [1, 2, 4, 8]
    assert largest_divisible_subset([4, 8, 10, 240]) == [4, 8, 240]
    assert largest_divisible_subset([2, 3, 4, 9, 8]) == [2, 4, 8]
