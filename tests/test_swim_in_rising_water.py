from puzzles.swim_in_rising_water import swim_in_water


def test_swim_in_water():
    assert swim_in_water([[0, 2], [1, 3]]) == 3
    assert (
        swim_in_water(
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ]
        )
        == 16
    )
