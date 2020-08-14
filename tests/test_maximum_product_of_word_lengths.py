import pytest
from puzzles.maximum_product_of_word_lengths import max_product


def test_max_product():
    assert max_product(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
    assert max_product(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
    assert max_product(["a", "aa", "aaa", "aaaa"]) == 0
