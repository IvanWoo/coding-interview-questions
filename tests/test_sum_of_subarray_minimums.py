from puzzles.sum_of_subarray_minimums import sum_subarray_mins


def test_sum_subarray_mins():
    assert sum_subarray_mins([3, 1, 2, 4]) == 17
    assert sum_subarray_mins([1, 1]) == 3
