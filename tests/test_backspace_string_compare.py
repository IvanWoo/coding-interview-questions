import pytest

from puzzles.backspace_string_compare import backspace_compare


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ab#c", "ad#c", True),
        ("ab##", "c#d#", True),
        ("a#c", "b", False),
        ("a##c", "#a#c", True),
    ],
)
def test(s, t, expected):
    assert backspace_compare(s, t) == expected
