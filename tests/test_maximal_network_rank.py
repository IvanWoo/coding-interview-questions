from puzzles.maximal_network_rank import maximal_network_rank


def test_maximal_network_rank():
    assert maximal_network_rank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]) == 4
    assert (
        maximal_network_rank(
            n=5, roads=[[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
        )
        == 5
    )
    assert (
        maximal_network_rank(
            n=8, roads=[[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
        )
        == 5
    )
