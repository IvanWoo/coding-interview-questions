import pytest

from puzzles.longest_palindromic_substring import longest_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("babad", ["aba", "bab"]),
        ("cbbd", ["bb"]),
        ("", [""]),
        ("a", ["a"]),
        ("bb", ["bb"]),
        ("aaaa", ["aaaa"]),
    ],
)
def test_longest_palindrome(s, expected):
    assert longest_palindrome(s) in expected
