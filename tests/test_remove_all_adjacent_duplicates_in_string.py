import pytest

from puzzles.remove_all_adjacent_duplicates_in_string import remove_duplicates


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
    ],
)
def test_remove_duplicates(s, expected):
    assert remove_duplicates(s) == expected
