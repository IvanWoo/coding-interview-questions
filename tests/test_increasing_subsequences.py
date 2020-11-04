from puzzles.increasing_subsequences import find_subsequences


def test_find_subsequences():
    assert find_subsequences([4, 3, 2, 1]) == []
    assert sorted(find_subsequences([4, 6, 7, 7])) == sorted(
        [
            [4, 6],
            [4, 7],
            [4, 6, 7],
            [4, 6, 7, 7],
            [6, 7],
            [6, 7, 7],
            [7, 7],
            [4, 7, 7],
        ]
    )
