from puzzles.wiggle_subsequence import wiggle_max_length


def test_wiggle_max_length():
    assert wiggle_max_length([1, 7, 4, 9, 2, 5]) == 6
    assert wiggle_max_length([0, 0]) == 1
    assert wiggle_max_length([]) == 0
    assert wiggle_max_length([3, 3, 3, 2, 5]) == 3
    assert wiggle_max_length([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert wiggle_max_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    # fmt: off
    assert (
        wiggle_max_length(
            [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9]
        )
        == 19
    )
    # fmt: on
