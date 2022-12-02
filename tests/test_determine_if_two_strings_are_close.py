import pytest
from puzzles.determine_if_two_strings_are_close import close_strings


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        ("abc", "bca", True),
        ("a", "aa", False),
        ("cabbba", "abbccc", True),
        ("uau", "ssx", False),
    ],
)
def test_close_strings(word1, word2, expected):
    assert close_strings(word1, word2) == expected
