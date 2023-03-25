import pytest

from puzzles.count_unreachable_pairs_of_nodes_in_an_undirected_graph import count_pairs


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (3, [[0, 1], [0, 2], [1, 2]], 0),
        (7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]], 14),
        (
            11,
            [
                [5, 0],
                [1, 0],
                [10, 7],
                [9, 8],
                [7, 2],
                [1, 3],
                [0, 2],
                [8, 5],
                [4, 6],
                [4, 2],
            ],
            0,
        ),
        (9628, [], 46344378),
    ],
)
def test_count_pairs(n, edges, expected):
    assert count_pairs(n, edges) == expected
