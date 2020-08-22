import pytest
from puzzles.is_palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("a") == True
    assert is_palindrome("aba") == True
    assert is_palindrome("bba") == False
