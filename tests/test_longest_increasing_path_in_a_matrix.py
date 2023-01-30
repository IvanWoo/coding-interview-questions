import pytest

from puzzles.longest_increasing_path_in_a_matrix import longest_increasing_path


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
        ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
        ([[1]], 1),
    ],
)
def test_longest_increasing_path(matrix, expected):
    assert longest_increasing_path(matrix) == expected
