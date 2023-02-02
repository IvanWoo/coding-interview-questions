import pytest

from puzzles.verifying_an_alien_dictionary import is_alien_sorted


@pytest.mark.parametrize(
    "words, order, expected",
    [
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
        (["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz", True),
    ],
)
def test_is_alien_sorted(words, order, expected):
    assert is_alien_sorted(words, order) == expected
