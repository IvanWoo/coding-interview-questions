import pytest

from puzzles.spiral_matrix_ii import generate_matrix


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [[1]]),
        (2, [[1, 2], [4, 3]]),
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
    ],
)
def test_generate_matrix(n, expected):
    assert generate_matrix(n) == expected
