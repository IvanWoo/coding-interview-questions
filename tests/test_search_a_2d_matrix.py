import pytest
from puzzles.search_a_2d_matrix import search_matrix


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ],
)
def test_search_matrix(matrix: list[list[int]], target: int, expected: bool):
    assert search_matrix(matrix, target) == expected
