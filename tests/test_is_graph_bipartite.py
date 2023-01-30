import pytest

from puzzles.is_graph_bipartite import is_bipartite


@pytest.mark.parametrize(
    "graph, expected",
    [
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
        ([[1], [0]], True),
        ([[1], [0], []], True),
        ([[1, 2, 3], [0], [0], [0]], True),
    ],
)
def test_is_bipartite(graph, expected):
    assert is_bipartite(graph) == expected
