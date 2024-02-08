from puzzles.combinations import combine


def test_combine():
    assert sorted(combine(4, 2)) == sorted(
        [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]
    )
