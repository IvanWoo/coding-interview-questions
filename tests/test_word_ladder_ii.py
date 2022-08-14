import pytest
from puzzles.word_ladder_ii import find_ladders


@pytest.mark.parametrize(
    "begin_word, end_word, word_list, expected",
    [
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]],
        ),
        ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], []),
    ],
)
def test_find_ladders(begin_word, end_word, word_list, expected):
    assert sorted(find_ladders(begin_word, end_word, word_list)) == sorted(expected)
