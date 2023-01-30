import pytest

from puzzles.redundant_connection import find_redundant_connection


def test_find_redundant_connection():
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
