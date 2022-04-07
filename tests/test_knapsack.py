import pytest
from puzzles.knapsack import max_value


@pytest.mark.parametrize(
    "weights, values, capacity, expected",
    [
        ([1, 3, 4], [15, 20, 30], 4, 35),
    ],
)
def test_max_value(weights, values, capacity, expected):
    assert max_value(weights, values, capacity) == expected
