from puzzles.binary_subarrays_with_sum import num_subarrays_with_sum


def test_num_subarrays_with_sum():
    assert num_subarrays_with_sum([1, 0, 1, 0, 1], 2) == 4
    assert num_subarrays_with_sum([0, 0, 0, 0, 0], 0) == 15
    assert num_subarrays_with_sum([0, 0, 1, 1, 0, 0], 2) == 9
