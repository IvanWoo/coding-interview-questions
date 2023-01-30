import pytest

from puzzles.find_closest_node_to_given_two_nodes import closest_meeting_node


@pytest.mark.parametrize(
    "edges, node1, node2, expected",
    [
        ([2, 2, 3, -1], 0, 1, 2),
        ([1, 2, -1], 0, 2, 2),
        ([5, -1, 3, 4, 5, 6, -1, -1, 4, 3], 0, 0, 0),
        ([3, 0, 5, -1, 3, 4], 2, 0, 3),
    ],
)
def test_closest_meeting_node(edges, node1, node2, expected):
    assert closest_meeting_node(edges, node1, node2) == expected
