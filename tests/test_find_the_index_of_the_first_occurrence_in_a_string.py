import pytest

from puzzles.find_the_index_of_the_first_occurrence_in_a_string import str_str


@pytest.mark.parametrize(
    "haystack, needle, expected",
    [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("a", "a", 0),
        ("abc", "c", 2),
    ],
)
def test_str_str(haystack, needle, expected):
    assert str_str(haystack, needle) == expected
