import pytest
from puzzles.insert_interval import insert


def test_insert():
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
