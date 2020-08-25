import pytest
from puzzles.count_of_smaller_numbers_after_self import count_smaller


def test_count_smaller():
    assert count_smaller([5, 2, 6, 1]) == [2, 1, 1, 0]
