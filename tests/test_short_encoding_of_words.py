import pytest
from puzzles.short_encoding_of_words import minimum_length_encoding


@pytest.mark.parametrize(
    "words, expected",
    [
        (["time", "me", "bell"], 10),
        (["t"], 2),
        (["t", "t"], 2),
    ],
)
def test_minimum_length_encoding(words, expected):
    assert minimum_length_encoding(words) == expected
