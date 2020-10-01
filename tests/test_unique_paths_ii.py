from puzzles.unique_paths_ii import unique_paths_with_obstacles


def test_unique_paths_with_obstacles():
    assert unique_paths_with_obstacles([[0, 0]]) == 1
    assert unique_paths_with_obstacles([[0, 0], [1, 1], [0, 0]]) == 0
    assert unique_paths_with_obstacles([[1, 0]]) == 0
    assert unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
