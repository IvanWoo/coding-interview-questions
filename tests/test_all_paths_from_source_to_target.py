from puzzles.all_paths_from_source_to_target import all_paths_source_target


def test_all_paths_source_target():
    assert all_paths_source_target([[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]
    assert all_paths_source_target([[1], []]) == [[0, 1]]
    assert all_paths_source_target([[1, 3], [2], [3], []]) == [[0, 1, 2, 3], [0, 3]]
    assert all_paths_source_target([[1, 2, 3], [2], [3], []]) == [
        [0, 1, 2, 3],
        [0, 2, 3],
        [0, 3],
    ]
    assert all_paths_source_target([[4, 3, 1], [3, 2, 4], [3], [4], []]) == [
        [0, 4],
        [0, 3, 4],
        [0, 1, 3, 4],
        [0, 1, 2, 3, 4],
        [0, 1, 4],
    ]
