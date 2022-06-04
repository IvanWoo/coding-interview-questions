import pytest
from puzzles.n_queens import solve_n_queens


@pytest.mark.parametrize(
    "n, expected",
    [
        (
            4,
            [
                [".Q..", "...Q", "Q...", "..Q."],
                ["..Q.", "Q...", "...Q", ".Q.."],
            ],
        ),
        (1, [["Q"]]),
    ],
)
def test_solve_n_queens(n, expected):
    assert sorted(solve_n_queens(n)) == sorted(expected)
