import pytest
from puzzles.minimum_cost_for_tickets import mincost_tickets


def test_mincost_tickets():
    assert mincost_tickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11
    assert mincost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17
