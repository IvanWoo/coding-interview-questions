import pytest

from puzzles.sum_numbers import sum_numbers


def test_sum_numbers():
    assert sum_numbers("abc123xyz") == 123
    assert sum_numbers("aa11b33") == 44
    assert sum_numbers("7 11") == 18
