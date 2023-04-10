import pytest

from puzzles.valid_parentheses import is_valid


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("[", False),
        ("]", False),
    ],
)
def test_is_valid(s, expected):
    assert is_valid(s) == expected
