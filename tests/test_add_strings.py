import pytest

from puzzles.add_strings import add_strings


@pytest.mark.parametrize(
    "num1, num2, expected",
    [("0", "0", "0"), ("9", "0", "9"), ("9", "1", "10"), ("3099", "9", "3108")],
)
def test_add_strings(num1, num2, expected):
    assert add_strings(num1, num2) == expected
