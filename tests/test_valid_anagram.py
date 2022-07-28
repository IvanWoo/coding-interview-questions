import pytest
from puzzles.valid_anagram import is_anagram


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("a", "", False),
        ("", "a", False),
        ("ab", "ba", True),
    ],
)
def test_is_anagram(s: str, t: str, expected: bool):
    assert is_anagram(s, t) == expected
