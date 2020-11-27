from puzzles.subarray_sum_equals_k import subarray_sum


def test_subarray_sum():
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
