from puzzles.contiguous_array import find_max_length


def test_find_max_length():
    assert find_max_length([0]) == 0
    assert find_max_length([0, 1]) == 2
    assert find_max_length([0, 1, 0]) == 2
    assert find_max_length([0, 1, 0, 1, 0, 0, 1]) == 6
    assert find_max_length([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]) == 10
    assert find_max_length([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]) == 10
