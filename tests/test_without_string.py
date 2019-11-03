import pytest
from puzzles.without_string import without_string

def test_without_string():
    assert without_string("Hello there", "llo") == "He there"
    assert without_string("Hello there", "e") == "Hllo thr"
    assert without_string("Hello there", "x") == "Hello there"
