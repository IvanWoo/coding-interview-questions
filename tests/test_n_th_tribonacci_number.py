import pytest
from puzzles.n_th_tribonacci_number import tribonacci


@pytest.mark.parametrize(
    "n, expected",
    [
        (4, 4),
        (25, 1389537),
    ],
)
def test_tribonacci(n, expected):
    assert tribonacci(n) == expected
