from puzzles.longest_consecutive_sequence import longest_consecutive


def test_longest_consecutive():
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([1, 2, 0, 1]) == 3
    assert longest_consecutive([]) == 0
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
