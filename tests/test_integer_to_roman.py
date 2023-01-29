import pytest

from puzzles.integer_to_roman import int_to_roman


@pytest.mark.parametrize(
    "num, expected",
    [
        (3, "III"),
        (8, "VIII"),
        (20, "XX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ],
)
def test_int_to_roman(num, expected):
    assert int_to_roman(num) == expected
