import pytest

from puzzles.n_queens_ii import total_n_queens


@pytest.mark.parametrize(
    "n, expected",
    [
        (4, 2),
        (1, 1),
    ],
)
def test_total_n_queens(n, expected):
    assert total_n_queens(n) == expected
