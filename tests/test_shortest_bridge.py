from puzzles.shortest_bridge import shortest_bridge


def test_shortest_bridge():
    assert shortest_bridge([[0, 1], [1, 0]]) == 1
    assert shortest_bridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2
    assert (
        shortest_bridge(
            [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ]
        )
        == 1
    )
