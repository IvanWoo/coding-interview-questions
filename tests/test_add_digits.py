import pytest

from puzzles.add_digits import add_digits


@pytest.mark.parametrize(
    "num, expected",
    [
        (38, 2),
        (0, 0),
    ],
)
def test_add_digits(num, expected):
    assert add_digits(num) == expected
