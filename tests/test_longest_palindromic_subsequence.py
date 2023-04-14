import pytest

from puzzles.longest_palindromic_subsequence import longest_palindrome_subseq


@pytest.mark.parametrize(
    "s, expected",
    [
        ("bbbab", 4),
        ("babab", 5),
        ("cbbd", 2),
    ],
)
def test_longest_palindrome_subseq(s, expected):
    assert longest_palindrome_subseq(s) == expected
