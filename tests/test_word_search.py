import pytest
from puzzles.word_search import exist


@pytest.mark.parametrize(
    "board, word, expected",
    [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ),
        ([["a", "a"]], "aaa", False),
        ([["a"]], "b", False),
        (
            [
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
            ],
            "AAAAAAAAAAAABAA",
            False,
        ),
    ],
)
def test_exist(board, word, expected):
    assert exist(board, word) == expected
