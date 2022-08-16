import pytest
from puzzles.first_unique_character_in_a_string import first_uniq_char


@pytest.mark.parametrize(
    "s, expected",
    [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("", -1),
        ("a", 0),
        ("aa", -1),
    ],
)
def test_first_unique_character_in_a_string(s, expected):
    assert first_uniq_char(s) == expected
