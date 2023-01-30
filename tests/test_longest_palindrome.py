import pytest

from puzzles.longest_palindrome import longest_palindrome


def test_longest_palindrome():
    assert longest_palindrome("babad") == "bab"
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
