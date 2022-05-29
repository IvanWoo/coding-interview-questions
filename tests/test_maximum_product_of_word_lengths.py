import pytest
from puzzles.maximum_product_of_word_lengths import max_product


@pytest.mark.parametrize(
    "words, expected",
    [
        (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16),
        (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4),
        (["a", "aa", "aaa", "aaaa"], 0),
    ],
)
def test_max_product(words, expected):
    assert max_product(words) == expected
