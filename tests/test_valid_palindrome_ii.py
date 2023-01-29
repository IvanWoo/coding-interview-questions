import pytest

from puzzles.valid_palindrome_ii import valid_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aba", True),
        ("abca", True),
        ("abcba", True),
        ("bdbd", True),
        ("bddb", True),
        ("abc", False),
    ],
)
def test_valid_palindrome(s, expected):
    assert valid_palindrome(s) == expected
