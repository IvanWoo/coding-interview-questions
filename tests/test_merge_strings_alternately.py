import pytest

from puzzles.merge_strings_alternately import merge_alternately


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
    ],
)
def test_merge_alternately(word1, word2, expected):
    assert merge_alternately(word1, word2) == expected
