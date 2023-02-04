import pytest

from puzzles.permutation_in_string import check_inclusion


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("abc", "bbbca", True),
    ],
)
def test_check_inclusion(s1, s2, expected):
    assert check_inclusion(s1, s2) == expected
