import pytest

from puzzles.break_a_palindrome import break_palindrome


@pytest.mark.parametrize(
    "palindrome, expected",
    [
        ("abccba", "aaccba"),
        ("a", ""),
        ("aa", "ab"),
        ("aba", "abb"),
    ],
)
def test_break_palindrome(palindrome, expected):
    assert break_palindrome(palindrome) == expected
