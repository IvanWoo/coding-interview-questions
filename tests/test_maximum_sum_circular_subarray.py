from puzzles.maximum_sum_circular_subarray import max_subarray_sum_circular


def test_max_subarray_sum_circular():
    assert max_subarray_sum_circular([1, -2, 3, -2]) == 3
    assert max_subarray_sum_circular([5, -3, 5]) == 10
    assert max_subarray_sum_circular([3, -1, 2, -1]) == 4
    assert max_subarray_sum_circular([3, -2, 2, -3]) == 3
    assert max_subarray_sum_circular([-2, -3, -1]) == -1
