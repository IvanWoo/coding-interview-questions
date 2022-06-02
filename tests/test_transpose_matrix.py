import pytest
from puzzles.transpose_matrix import transpose


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
        ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ],
)
def test_transpose(matrix: list[list[int]], expected: list[list[int]]):
    assert transpose(matrix) == expected
