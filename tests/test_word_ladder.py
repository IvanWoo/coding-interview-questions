import pytest

from puzzles.word_ladder import ladder_length


def test_ladder_length():
    assert ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
