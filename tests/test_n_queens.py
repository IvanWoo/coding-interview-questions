import pytest
from puzzles.n_queens import solve_n_queens


def test_solve_n_queens():
    assert solve_n_queens(4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]

