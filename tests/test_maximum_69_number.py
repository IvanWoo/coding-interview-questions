import pytest

from puzzles.maximum_69_number import maximum_69_number


@pytest.mark.parametrize(
    "num, expected",
    [
        (9669, 9969),
        (9996, 9999),
        (9999, 9999),
    ],
)
def test_maximum_69_number(num, expected):
    assert maximum_69_number(num) == expected
