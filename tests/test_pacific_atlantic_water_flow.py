from puzzles.pacific_atlantic_water_flow import pacific_atlantic


def test_pacific_atlantic():
    assert (
        sorted(
            pacific_atlantic(
                [
                    [1, 2, 2, 3, 5],
                    [3, 2, 3, 4, 4],
                    [2, 4, 5, 3, 1],
                    [6, 7, 1, 4, 5],
                    [5, 1, 1, 2, 4],
                ]
            )
        )
        == sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
    )
