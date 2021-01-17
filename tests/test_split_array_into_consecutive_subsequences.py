from puzzles.split_array_into_consecutive_subsequences import is_possible


def test_is_possible():
    assert is_possible([1, 2, 3, 3, 4, 5]) == True
    assert is_possible([1, 2, 3, 3, 4, 4, 5, 5]) == True
    assert is_possible([1, 2, 3, 4, 4, 5]) == False
    assert is_possible([1, 2, 3, 3, 3, 4, 4, 5]) == False
    assert is_possible([1, 2, 3, 3, 4, 5, 9]) == False
    assert is_possible([4, 5, 6, 7, 7, 8, 8, 9, 10, 11]) == True
