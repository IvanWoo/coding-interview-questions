import pytest

from puzzles.longest_palindrome_by_concatenating_two_letter_words import longest_palindrome


@pytest.mark.parametrize(
    "words, expected",
    [
        (["lc", "cl", "gg"], 6),
        (["ab", "ty", "yt", "lc", "cl", "ab"], 8),
        (["cc", "ll", "xx"], 2),
    ],
)
def test_longest_palindrome(words, expected):
    assert longest_palindrome(words) == expected
