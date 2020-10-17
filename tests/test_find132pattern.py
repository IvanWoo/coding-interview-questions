from puzzles.find132pattern import find132pattern


def test_find132pattern():
    assert find132pattern([3, 5, 0, 3, 4]) == True
    assert find132pattern([3, 5, 0, 2, 1]) == True
    assert find132pattern([1, 2, 3, 4]) == False
    assert find132pattern([-1, 3, 2, 0]) == True
    assert find132pattern([1, 0, 1, -4, -3]) == False
