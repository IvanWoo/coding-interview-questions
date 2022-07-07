import pytest
from puzzles.interleaving_string import is_interleave


@pytest.mark.parametrize(
    "s1, s2, s3, expected",
    [
        ("a", "b", "ab", True),
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("", "", "", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
    ],
)
def test_is_interleave(s1, s2, s3, expected):
    assert is_interleave(s1, s2, s3) == expected
