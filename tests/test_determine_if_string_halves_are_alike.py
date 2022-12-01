import pytest
from puzzles.determine_if_string_halves_are_alike import halves_are_alike


@pytest.mark.parametrize(
    "s, expected",
    [
        ("book", True),
        ("textbook", False),
        ("AbCdEfGh", True),
    ],
)
def test_halves_are_alike(s, expected):
    assert halves_are_alike(s) == expected
