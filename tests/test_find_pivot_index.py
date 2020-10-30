from puzzles.find_pivot_index import pivot_index


def test_pivot_index():
    assert pivot_index([-1, -1, -1, 0, 1, 1]) == 0
    assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
    assert pivot_index([1, 2, 3]) == -1
    assert pivot_index([-1, -1, 0, 0, -1, -1]) == 2
