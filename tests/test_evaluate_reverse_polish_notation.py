import pytest
from puzzles.evaluate_reverse_polish_notation import evalRPN


def test_evalRPN():
    assert evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert (
        evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        == 22
    )
