import pytest

from puzzles.removing_stars_from_a_string import remove_stars


@pytest.mark.parametrize(
    "s, expected",
    [
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
    ],
)
def test_remove_stars(s, expected):
    assert remove_stars(s) == expected
