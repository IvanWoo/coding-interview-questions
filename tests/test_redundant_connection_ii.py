from puzzles.redundant_connection_ii import find_redundant_directed_connection


def test_find_redundant_directed_connection():
    assert find_redundant_directed_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert find_redundant_directed_connection([[2, 1], [3, 1], [4, 2], [1, 4]]) == [
        2,
        1,
    ]
    assert find_redundant_directed_connection(
        [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    ) == [4, 1]
