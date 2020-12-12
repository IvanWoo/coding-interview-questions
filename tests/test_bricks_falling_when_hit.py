from puzzles.bricks_falling_when_hit import hit_bricks


def test_hit_bricks():
    assert hit_bricks([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]]) == [2]
    assert hit_bricks([[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]]) == [0, 3, 0]
    assert hit_bricks([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]]) == [
        0,
        0,
    ]
