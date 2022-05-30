import pytest
from puzzles.divide_two_integers import divide


@pytest.mark.parametrize(
    "dividend, divisor, expected",
    [
        (10, 3, 3),
        (7, -3, -2),
        (1, 1, 1),
        (1, -1, -1),
        (1, -2, 0),
        (2147483647, 1, 2147483647),
        (-2147483648, -1, 2147483647),
    ],
)
def test_divide(dividend, divisor, expected):
    assert divide(dividend, divisor) == expected
