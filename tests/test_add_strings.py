import pytest
from puzzles.add_strings import add_strings


def test_add_strings():
    assert add_strings("0", "0") == "0"
    assert add_strings("9", "0") == "9"
    assert add_strings("3099", "9") == "3108"