import pytest

from puzzles.shortest_path_with_alternating_colors import shortest_alternating_paths


@pytest.mark.parametrize(
    "n, red_edges, blue_edges, expected",
    [
        (
            3,
            [[0, 1], [1, 2]],
            [],
            [0, 1, -1],
        ),
        (
            3,
            [[0, 1]],
            [[2, 1]],
            [0, 1, -1],
        ),
        (
            3,
            [[1, 0]],
            [[2, 1]],
            [0, -1, -1],
        ),
        (
            3,
            [[0, 1]],
            [[1, 2]],
            [0, 1, 2],
        ),
        (
            3,
            [[0, 1], [0, 2]],
            [[1, 0]],
            [0, 1, 1],
        ),
        (
            5,
            [[0, 1], [1, 2], [2, 3], [3, 4]],
            [[1, 2], [2, 3], [3, 1]],
            [0, 1, 2, 3, 7],
        ),
        (
            2,
            [[0, 1]],
            [[1, 0]],
            [0, 1],
        ),
    ],
)
def test_shortest_alternating_paths(n, red_edges, blue_edges, expected):
    assert shortest_alternating_paths(n, red_edges, blue_edges) == expected
