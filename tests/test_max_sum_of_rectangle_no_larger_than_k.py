import pytest

from puzzles.max_sum_of_rectangle_no_larger_than_k import max_sum_submatrix


@pytest.mark.parametrize(
    "matrix, k, expected",
    [
        ([[1, 0, 1], [0, -2, 3]], 2, 2),
        ([[2, 2, -1]], 3, 3),
        ([[2, 2, -1]], 0, -1),
        ([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 10, 10),
        ([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 9, 9),
        ([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 8, 8),
    ],
)
def test_max_sum_submatrix(matrix, k, expected):
    assert max_sum_submatrix(matrix, k) == expected
