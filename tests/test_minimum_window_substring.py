import pytest
from puzzles.minimum_window_substring import min_window


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("", "", ""),
    ],
)
def test_min_window(s, t, expected):
    assert min_window(s, t) == expected
