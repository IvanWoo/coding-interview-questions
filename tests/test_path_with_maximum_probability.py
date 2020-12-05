from puzzles.path_with_maximum_probability import max_probability


def test_max_probability():
    assert (
        max_probability(
            n=3,
            edges=[[0, 1], [1, 2], [0, 2]],
            succProb=[0.5, 0.5, 0.2],
            start=0,
            end=2,
        )
        == 0.25
    )
    assert (
        max_probability(
            n=3,
            edges=[[0, 1], [1, 2], [0, 2]],
            succProb=[0.5, 0.5, 0.3],
            start=0,
            end=2,
        )
        == 0.3
    )
    assert max_probability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2) == 0
    assert (
        max_probability(
            5,
            [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
            [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
            3,
            4,
        )
        == 0.21390
    )
