from puzzles.diagonal_traverse import find_diagonal_order


def test_find_diagonal_order():
    assert find_diagonal_order([]) == []
    assert find_diagonal_order([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        4,
        7,
        5,
        3,
        6,
        8,
        9,
    ]
