import pytest
from puzzles.basic_calculator import calculate


@pytest.mark.parametrize(
    "s, expected",
    [
        ("-2", -2),
        ("42", 42),
        ("1 + 1", 2),
        (" 1+1", 2),
        (" 2-1 + 2 ", 3),
        ("(6+8)", 14),
        ("(4+5- 2)", 7),
        ("1+(4+5+2)-3", 9),
        ("(1+(4+5+2)-3)", 9),
        ("(1+(4+5+2)-3)+(6+8)", 23),
    ],
)
def test_calculate(s, expected):
    assert calculate(s) == expected
