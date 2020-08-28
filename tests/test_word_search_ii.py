import pytest
from puzzles.word_search_ii import find_words


def test_find_words():
    assert (
        find_words(
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
        )
        == ["oath", "eat"]
    )
