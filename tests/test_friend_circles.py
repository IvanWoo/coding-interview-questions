from puzzles.friend_circles import find_circle_num


def test_find_circle_num():
    assert find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert find_circle_num([[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1
