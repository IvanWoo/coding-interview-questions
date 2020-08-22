import pytest

from puzzles.next_greater_elements import next_greater_elements


def test_next_greater_elements():
    assert next_greater_elements([1, 2, 1]) == [2, -1, 2]
    assert next_greater_elements([1, 2, 3, 2, 1]) == [2, 3, -1, 3, 2]
