import pytest
from puzzles.remove_k_digits import remove_k_digits


def test_remove_k_digits():
    assert remove_k_digits("5337", 2) == "33"
    assert remove_k_digits("5337", 0) == "5337"
    assert remove_k_digits("5337", 5) == "0"
    assert remove_k_digits("5337", 4) == "0"
    assert remove_k_digits("1432219", 5) == "11"
    assert remove_k_digits("1432219", 1) == "132219"
    assert remove_k_digits("1432219", 3) == "1219"
    assert remove_k_digits("10200", 1) == "200"
    assert remove_k_digits("1111111", 3) == "1111"