import pytest
from puzzles.word_search import exist


@pytest.fixture
def board():
    return [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]


def test_exist(board):
    assert exist(board, "ABCCED") == True
    assert exist(board, "SEE") == True
    assert exist(board, "ABCB") == False
