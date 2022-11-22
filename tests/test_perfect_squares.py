import pytest
from puzzles.perfect_squares import num_squares


@pytest.mark.parametrize(
    "n, expected",
    [
        (12, 3),
        (13, 2),
        (7168, 4),
    ],
)
def test_num_squares(n, expected):
    assert num_squares(n) == expected
