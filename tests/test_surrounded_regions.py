import pytest
from puzzles.surrounded_regions import solve


@pytest.fixture
def board1():
    return [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]


@pytest.fixture
def ans1():
    return [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]


@pytest.fixture
def board2():
    return [
        ["X", "O", "X", "O", "X", "O", "O", "O", "X", "O"],
        ["X", "O", "O", "X", "X", "X", "O", "O", "O", "X"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
        ["O", "O", "O", "O", "O", "O", "X", "O", "O", "X"],
        ["O", "O", "X", "X", "O", "X", "X", "O", "O", "O"],
        ["X", "O", "O", "X", "X", "X", "O", "X", "X", "O"],
        ["X", "O", "X", "O", "O", "X", "X", "O", "X", "O"],
        ["X", "X", "O", "X", "X", "O", "X", "O", "O", "X"],
        ["O", "O", "O", "O", "X", "O", "X", "O", "X", "O"],
        ["X", "X", "O", "X", "X", "X", "X", "O", "O", "O"],
    ]


@pytest.fixture
def ans2():
    return [
        ["X", "O", "X", "O", "X", "O", "O", "O", "X", "O"],
        ["X", "O", "O", "X", "X", "X", "O", "O", "O", "X"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
        ["O", "O", "O", "O", "O", "O", "X", "O", "O", "X"],
        ["O", "O", "X", "X", "O", "X", "X", "O", "O", "O"],
        ["X", "O", "O", "X", "X", "X", "X", "X", "X", "O"],
        ["X", "O", "X", "X", "X", "X", "X", "O", "X", "O"],
        ["X", "X", "O", "X", "X", "X", "X", "O", "O", "X"],
        ["O", "O", "O", "O", "X", "X", "X", "O", "X", "O"],
        ["X", "X", "O", "X", "X", "X", "X", "O", "O", "O"],
    ]


def test_solve_1(board1, ans1):
    solve(board1)
    assert board1 == ans1


def test_solve_2(board2, ans2):
    solve(board2)
    assert board2 == ans2
