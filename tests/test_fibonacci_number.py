import pytest

from puzzles.fibonacci_number import fib


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (30, 832040),
    ],
)
def test_fib(n, expected):
    assert fib(n) == expected
