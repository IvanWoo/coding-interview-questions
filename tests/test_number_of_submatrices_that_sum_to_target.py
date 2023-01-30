import pytest

from puzzles.number_of_submatrices_that_sum_to_target import num_submatrix_sum_target


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0, 4),
        ([[1, -1], [-1, 1]], 0, 5),
        ([[904]], 0, 0),
    ],
)
def test_num_submatrix_sum_target(matrix, target, expected):
    assert num_submatrix_sum_target(matrix, target) == expected
