import pytest

from puzzles.maximum_length_of_a_concatenated_string_with_unique_characters import max_length


@pytest.mark.parametrize(
    "arr, expected",
    [
        (["aa"], 0),
        (["un", "iq", "ue"], 4),
        (["cha", "r", "act", "ers"], 6),
        (["abcdefghijklmnopqrstuvwxyz"], 26),
    ],
)
def test_max_length(arr, expected):
    assert max_length(arr) == expected
