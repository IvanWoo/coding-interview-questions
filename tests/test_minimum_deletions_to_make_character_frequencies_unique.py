import pytest

from puzzles.minimum_deletions_to_make_character_frequencies_unique import min_deletions


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aab", 0),
        ("abcabc", 3),
        ("bbcebab", 2),
        ("aaabbbcc", 2),
        ("ceabaacb", 2),
    ],
)
def test_min_deletions(s, expected):
    assert min_deletions(s) == expected
