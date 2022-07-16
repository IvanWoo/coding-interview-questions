import pytest
from puzzles.out_of_boundary_paths import find_paths


@pytest.mark.parametrize(
    "m, n, N, i, j, expected",
    [
        (2, 2, 2, 0, 0, 6),
        (1, 3, 3, 0, 1, 12),
        (2, 1, 2, 0, 0, 6),
    ],
)
def test_find_paths(m, n, N, i, j, expected):
    assert find_paths(m, n, N, i, j) == expected
