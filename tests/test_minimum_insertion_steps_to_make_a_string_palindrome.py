import pytest

from puzzles.minimum_insertion_steps_to_make_a_string_palindrome import min_insertions


@pytest.mark.parametrize(
    "s, expected",
    [
        ("zzazz", 0),
        ("mbadm", 2),
        ("leetcode", 5),
        ("zjveiiwvc", 5),
        ("dyyuyabzkqaybcspq", 12),
    ],
)
def test_min_insertions(s, expected):
    assert min_insertions(s) == expected
