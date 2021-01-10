from puzzles.single_element_in_a_sorted_array import single_non_duplicate


def test_single_non_duplicate():
    assert single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert single_non_duplicate([3, 3, 7, 7, 10, 11, 11]) == 10
