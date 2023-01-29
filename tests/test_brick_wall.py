from puzzles.brick_wall import least_bricks


def test_least_bricks():
    assert least_bricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]) == 2
    assert least_bricks([[100000000], [100000000], [100000000]]) == 3
