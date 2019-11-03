import pytest
from puzzles.max_span import max_span


def test_max_span():
    assert max_span([1, 2, 1, 1, 3]) == 4
    assert max_span([1, 4, 2, 1, 4, 1, 4]) == 6
    assert max_span([1, 4, 2, 1, 4, 4, 4]) == 6
