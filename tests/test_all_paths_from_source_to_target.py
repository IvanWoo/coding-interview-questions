import pytest
from puzzles.all_paths_from_source_to_target import all_paths_source_target


@pytest.mark.parametrize(
    "graph, expected",
    [
        ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]]),
        ([[1], []], [[0, 1]]),
        ([[1, 3], [2], [3], []], [[0, 1, 2, 3], [0, 3]]),
        (
            [[1, 2, 3], [2], [3], []],
            [
                [0, 1, 2, 3],
                [0, 2, 3],
                [0, 3],
            ],
        ),
        (
            [[4, 3, 1], [3, 2, 4], [3], [4], []],
            [
                [0, 4],
                [0, 3, 4],
                [0, 1, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 4],
            ],
        ),
    ],
)
def test_all_paths_source_target(graph, expected):
    assert all_paths_source_target(graph) == expected
