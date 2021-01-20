from puzzles.number_of_longest_increasing_subsequence import find_number_of_LIS


def test_find_number_of_LIS():
    assert find_number_of_LIS([1, 3, 5, 4, 7]) == 2
    assert find_number_of_LIS([2, 2, 2, 2, 2]) == 5
    assert find_number_of_LIS([1, 2, 4, 3, 5, 4, 7, 2]) == 3
