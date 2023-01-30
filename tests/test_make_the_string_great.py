import pytest

from puzzles.make_the_string_great import make_good


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abBAcC", ""),
        ("leEeetcode", "leetcode"),
        ("", ""),
        ("s", "s"),
        ("LoOkGood", "LkGood"),
    ],
)
def test_make_good(s, expected):
    assert make_good(s) == expected
