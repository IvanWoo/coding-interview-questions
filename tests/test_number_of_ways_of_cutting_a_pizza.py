import pytest

from puzzles.number_of_ways_of_cutting_a_pizza import ways


@pytest.mark.parametrize(
    "pizza, k, expected",
    [
        (["A..", "AAA", "..."], 3, 3),
        (["A..", "AA.", "..."], 3, 1),
        (["A..", "A..", "..."], 1, 1),
    ],
)
def test_ways(pizza, k, expected):
    assert ways(pizza, k) == expected
