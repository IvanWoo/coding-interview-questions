from puzzles.first_missing_positive import first_missing_positive


def test_first_missing_positive():
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([11, 3, 5, 6]) == 1
    assert first_missing_positive([0, 1, 2, 3]) == 4
