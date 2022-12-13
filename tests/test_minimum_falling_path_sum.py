import pytest
from puzzles.minimum_falling_path_sum import min_falling_path_sum


@pytest.mark.parametrize(
    "matrix, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 12),
        ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
        ([[-19, 57], [-40, -5]], -59),
    ],
)
def test_min_falling_path_sum(matrix, expected):
    assert min_falling_path_sum(matrix) == expected
