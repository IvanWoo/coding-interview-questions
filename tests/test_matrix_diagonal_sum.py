import pytest

from puzzles.matrix_diagonal_sum import diagonal_sum


@pytest.mark.parametrize(
    "mat, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25),
        ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 8),
        ([[5]], 5),
    ],
)
def test_diagonal_sum(mat, expected):
    assert diagonal_sum(mat) == expected
