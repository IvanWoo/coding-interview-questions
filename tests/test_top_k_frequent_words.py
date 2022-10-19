import pytest
from puzzles.top_k_frequent_words import top_k_frequent


@pytest.mark.parametrize(
    "words, k, expected",
    [
        (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
        (["i", "love", "leetcode", "i", "love", "coding"], 3, ["i", "love", "coding"]),
        (
            ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
            4,
            ["the", "is", "sunny", "day"],
        ),
    ],
)
def test_top_k_frequent(words, k, expected):
    assert top_k_frequent(words, k) == expected
