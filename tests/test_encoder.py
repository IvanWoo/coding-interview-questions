import pytest
from puzzles.encoder import encoder


def test_encoder():
    assert encoder(["a"], ["1", "2", "3", "4"]) == ["1"]
    assert encoder(["a", "b"], ["1", "2", "3", "4"]) == ["1", "2"]
    assert encoder(["a", "b", "a"], ["1", "2", "3", "4"]) == ["1", "2", "1"]

