import pytest

from puzzles.longest_valid_parentheses import longest_valid_parentheses


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", 2),
        ("(()", 2),
        (")()())", 4),
        ("()(()))", 6),
        ("))))))", 0),
        ("", 0),
        ("()(()", 2),
    ],
)
def test_longest_valid_parentheses(s, expected):
    assert longest_valid_parentheses(s) == expected
