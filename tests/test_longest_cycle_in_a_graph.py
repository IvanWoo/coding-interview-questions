import pytest

from puzzles.longest_cycle_in_a_graph import longest_cycle


@pytest.mark.parametrize(
    "edges, expected",
    [
        ([3, 3, 4, 2, 3], 3),
        ([2, -1, 3, 1], -1),
    ],
)
def test_longest_cycle(edges, expected):
    assert longest_cycle(edges) == expected
