import pytest
from puzzles.surrounded_regions import solve


@pytest.fixture
def board():
    return [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]


@pytest.fixture
def ans():
    return [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]


def test_solve(board, ans):
    solve(board)
    assert board == ans
