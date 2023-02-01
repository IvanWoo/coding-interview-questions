import pytest

from puzzles.greatest_common_divisor_of_strings import gcd_of_strings


@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
    ],
)
def test_gcd_of_strings(str1, str2, expected):
    assert gcd_of_strings(str1, str2) == expected
