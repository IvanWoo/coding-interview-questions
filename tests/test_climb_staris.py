import pytest

from puzzles.climb_stairs import climb_stairs


def test_climb_stairs():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(35) == 14930352
    assert climb_stairs(100) == 573147844013817084101
