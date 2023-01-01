import pytest
from puzzles.word_pattern import word_pattern


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("abab", "dog cat cat dog", False),
        ("aaaa", "dog cat cat dog", False),
    ],
)
def test_word_pattern(pattern, s, expected):
    assert word_pattern(pattern, s) == expected
