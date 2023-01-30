import pytest

from puzzles.substring_with_concatenation_of_all_words import find_substring


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "good"], [8]),
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ],
)
def test_find_substring(s: str, words: list[str], expected: list[int]) -> None:
    assert sorted(find_substring(s, words)) == sorted(expected)
