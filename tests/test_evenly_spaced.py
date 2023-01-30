import pytest

from puzzles.evenly_spaced import evenly_spaced


def test_evenly_spaced():
    assert evenly_spaced(2, 4, 6) == True
    assert evenly_spaced(4, 6, 2) == True
    assert evenly_spaced(4, 6, 3) == False
