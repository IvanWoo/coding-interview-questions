import pytest
from puzzles.evaluate_reverse_polish_notation import evalRPN


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["4", "-2", "/", "2", "-3", "-", "-"], -7),
    ],
)
def test_evalRPN(tokens, expected):
    assert evalRPN(tokens) == expected
