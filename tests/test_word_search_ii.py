import pytest
from puzzles.word_search_ii import find_words


@pytest.mark.parametrize(
    "board, words, expected",
    [
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        ),
        ([["a", "b"], ["c", "d"]], ["abcb"], []),
        ([["a"]], ["a"], "a"),
    ],
)
def test_find_words(board, words, expected):
    assert sorted(find_words(board, words)) == sorted(expected)
