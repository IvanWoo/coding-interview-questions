import pytest

from puzzles.clone_graph import clone_graph


@pytest.mark.parametrize(
    "node, expected",
    [
        (None, None),
    ],
)
def test_clone_graph(node, expected):
    assert clone_graph(node) == expected
