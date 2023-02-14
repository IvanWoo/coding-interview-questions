import pytest

from puzzles.add_binary import add_binary


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("100", "110010", "110110"),
    ],
)
def test_add_binary(a, b, expected):
    assert add_binary(a, b) == expected
