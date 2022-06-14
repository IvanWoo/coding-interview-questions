import pytest
from puzzles.delete_operation_for_two_strings import min_distance


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("sea", "eat", 2),
        ("leetcode", "etco", 4),
        ("abc", "abd", 2),
    ],
)
def test_min_distance(word1: str, word2: str, expected: int):
    assert min_distance(word1, word2) == expected
