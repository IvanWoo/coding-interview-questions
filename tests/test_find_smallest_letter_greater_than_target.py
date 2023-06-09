import pytest

from puzzles.find_smallest_letter_greater_than_target import next_greatest_letter


@pytest.mark.parametrize(
    "letters, target, expected",
    [
        (["c", "f", "j"], "a", "c"),
        (["c", "f", "j"], "c", "f"),
        (["x", "x", "y", "y"], "z", "x"),
    ],
)
def test_next_greatest_letter(letters, target, expected):
    assert next_greatest_letter(letters, target) == expected
