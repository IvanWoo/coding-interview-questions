import pytest

from puzzles.minimum_cost_for_tickets import mincost_tickets


@pytest.mark.parametrize(
    "days, costs, expected",
    [
        ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
        ([1, 365], [2, 7, 15], 4),
    ],
)
def test_mincost_tickets(days, costs, expected):
    assert mincost_tickets(days, costs) == expected
