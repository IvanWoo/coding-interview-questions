import pytest
from puzzles.valid_palindrome import valid_palindrome


def test_valid_palindrome():
    assert valid_palindrome("aba") == True
    assert valid_palindrome("abca") == True
    assert valid_palindrome("deeee") == True
    assert valid_palindrome("eeccccbebaeeabebccceea") == False
    assert valid_palindrome("ebcbbececabbacecbbcbe") == True
