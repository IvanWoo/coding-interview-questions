import pytest

from puzzles.detect_capital import detect_capital_use


@pytest.mark.parametrize(
    "word, expected",
    [
        ("USA", True),
        ("FlaG", False),
        ("leetcode", True),
        ("A", True),
        ("Aa", True),
        ("mL", False),
    ],
)
def test_detect_capital_use(word, expected):
    assert detect_capital_use(word) == expected
