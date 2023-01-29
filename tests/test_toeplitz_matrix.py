import pytest

from puzzles.toeplitz_matrix import is_toeplitz_matrix


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True),
        ([[1, 2], [2, 2]], False),
        ([[1]], True),
    ],
)
def test_is_toeplitz_matrix(matrix, expected):
    assert is_toeplitz_matrix(matrix) == expected
