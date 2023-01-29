import pytest

from puzzles.longest_common_subsequence import longest_common_subsequence


@pytest.mark.parametrize(
    "text1, text2, expected",
    [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("bsbininm", "jmjkbkjkv", 1),
    ],
)
def test_longest_common_subsequence(text1, text2, expected):
    assert longest_common_subsequence(text1, text2) == expected
