import pytest

from puzzles.remove_palindromic_subsequences import remove_palindrome_sub


@pytest.mark.parametrize(
    "s, expected",
    [
        ("ababa", 1),
        ("abb", 2),
        ("baabb", 2),
    ],
)
def test_remove_palindrome_sub(s: str, expected: int) -> None:
    assert remove_palindrome_sub(s) == expected
