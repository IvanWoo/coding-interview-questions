import pytest

from puzzles.string_compression import compress


@pytest.mark.parametrize(
    "chars, expected",
    [
        (["a", "a", "b", "b", "c", "c", "c"], ["a", "2", "b", "2", "c", "3"]),
        (["a"], ["a"]),
        (
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
            ["a", "b", "1", "2"],
        ),
    ],
)
def test_compress(chars, expected):
    n = len(expected)
    assert compress(chars) == n
    assert chars[:n] == expected
