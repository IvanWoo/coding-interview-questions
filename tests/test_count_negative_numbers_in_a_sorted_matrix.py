import pytest

from puzzles.count_negative_numbers_in_a_sorted_matrix import count_negatives


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], 8),
        ([[3, 2], [1, 0]], 0),
        ([[5, 1, 0], [-5, -5, -5]], 3),
    ],
)
def test_count_negatives(grid, expected):
    assert count_negatives(grid) == expected
