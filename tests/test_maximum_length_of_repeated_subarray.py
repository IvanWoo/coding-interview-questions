from puzzles.maximum_length_of_repeated_subarray import find_length


def test_find_length():
    assert find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
    assert find_length([0, 1, 1, 1, 1], [1, 0, 1, 0, 1]) == 2
