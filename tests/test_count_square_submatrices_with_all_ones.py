from puzzles.count_square_submatrices_with_all_ones import count_squares


def test_count_squares():
    assert count_squares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]) == 15
    assert count_squares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]) == 7
