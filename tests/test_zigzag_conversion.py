import pytest

from puzzles.zigzag_conversion import convert


@pytest.mark.parametrize(
    "s, num_rows, expected",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("ABC", 1, "ABC"),
    ],
)
def test_convert(s, num_rows, expected):
    assert convert(s, num_rows) == expected
