import pytest
from puzzles.palindrome_partitioning import partition


def test_palindrome_partitioning():
    assert sorted(partition("aab")) == sorted([["aa", "b"], ["a", "a", "b"]])
