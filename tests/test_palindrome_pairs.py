import pytest

from puzzles.palindrome_pairs import palindrome_pairs


@pytest.mark.parametrize(
    "words, expected",
    [
        (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
        (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
        (["a", ""], [[0, 1], [1, 0]]),
    ],
)
def test_palindrome_pairs(words, expected):
    assert sorted(palindrome_pairs(words)) == sorted(expected)
