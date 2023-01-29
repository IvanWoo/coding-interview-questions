from puzzles.shortest_path_with_alternating_colors import shortest_alternating_paths


def test_shortest_alternating_paths():
    assert shortest_alternating_paths(n=3, red_edges=[[0, 1], [1, 2]], blue_edges=[]) == [0, 1, -1]
    assert shortest_alternating_paths(n=3, red_edges=[[0, 1]], blue_edges=[[2, 1]]) == [
        0,
        1,
        -1,
    ]
    assert shortest_alternating_paths(n=3, red_edges=[[1, 0]], blue_edges=[[2, 1]]) == [
        0,
        -1,
        -1,
    ]
    assert shortest_alternating_paths(n=3, red_edges=[[0, 1]], blue_edges=[[1, 2]]) == [
        0,
        1,
        2,
    ]
    assert shortest_alternating_paths(n=3, red_edges=[[0, 1], [0, 2]], blue_edges=[[1, 0]]) == [0, 1, 1]
    assert shortest_alternating_paths(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 2], [2, 3], [3, 1]]) == [0, 1, 2, 3, 7]
