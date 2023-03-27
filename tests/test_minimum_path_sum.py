import pytest

from puzzles.minimum_path_sum import min_path_sum


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
    ],
)
def test_min_path_sum(grid, expected):
    assert min_path_sum(grid) == expected
