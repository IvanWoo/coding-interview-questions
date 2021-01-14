from puzzles.longest_harmonious_subsequence import find_LHS


def test_find_LHS():
    assert find_LHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5
    assert find_LHS([1, 2, 3, 4]) == 2
    assert find_LHS([1, 1, 1, 1]) == 0
