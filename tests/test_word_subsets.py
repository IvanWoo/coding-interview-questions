import pytest
from puzzles.word_subsets import word_subsets


@pytest.mark.parametrize(
    "words1, words2, expected",
    [
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["e", "o"],
            ["facebook", "google", "leetcode"],
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["l", "e"],
            ["apple", "google", "leetcode"],
        ),
        (
            ["amazon", "apple", "facebook", "google", "leetcode"],
            ["e", "oo"],
            ["facebook", "google"],
        ),
    ],
)
def test_word_subsets(words1, words2, expected):
    assert word_subsets(words1, words2) == expected
