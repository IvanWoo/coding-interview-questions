import pytest
from puzzles.palindrome_partitioning_2 import min_cut


def test_palindrome_partitioning_2():
    assert min_cut("aab") == 1
    assert min_cut("ababababababababababababcbabababababababababababa") == 0
