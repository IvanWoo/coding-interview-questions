import pytest

from puzzles.reverse_words_in_a_string import reverse_words


@pytest.mark.parametrize(
    "s, expected",
    [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
    ],
)
def test_reverse_words(s, expected):
    assert reverse_words(s) == expected
