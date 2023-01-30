import pytest

from puzzles.prefix_and_suffix_search import WordFilter


@pytest.mark.parametrize(
    "words, prefix, suffix, expected",
    [
        (["apple"], "a", "e", 0),
        (["apple", "app"], "a", "e", 0),
        (["apple", "app"], "a", "p", 1),
        (["apple", "app"], "p", "e", -1),
        (["apple", "app"], "p", "p", -1),
        (["apple", "app"], "p", "l", -1),
        (
            [
                "cabaabaaaa",
                "ccbcababac",
                "bacaabccba",
                "bcbbcbacaa",
                "abcaccbcaa",
                "accabaccaa",
                "cabcbbbcca",
                "ababccabcb",
                "caccbbcbab",
                "bccbacbcba",
            ],
            "ab",
            "abcaccbcaa",
            4,
        ),
    ],
)
def test_prefix_and_suffix_search(words, prefix, suffix, expected):
    word_filter = WordFilter(words)
    assert word_filter.f(prefix, suffix) == expected
