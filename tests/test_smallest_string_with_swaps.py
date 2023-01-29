import pytest

from puzzles.smallest_string_with_swaps import smallest_string_with_swaps


@pytest.mark.parametrize(
    "s, pairs, expected",
    [
        ("dcab", [[0, 3], [1, 2]], "bacd"),
        ("dcab", [[0, 3], [1, 2], [0, 2]], "abcd"),
        ("cba", [[0, 1], [1, 2]], "abc"),
    ],
)
def test_smallest_string_with_swaps(s, pairs, expected):
    assert smallest_string_with_swaps(s, pairs) == expected
