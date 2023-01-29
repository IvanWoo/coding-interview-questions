import pytest

from puzzles.sum_of_distances_in_tree import sum_of_distances_in_tree


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        (6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]], [8, 12, 6, 10, 10, 10]),
        (1, [], [0]),
        (2, [[1, 0]], [1, 1]),
    ],
)
def test_sum_of_distances_in_tree(n, edges, expected):
    assert sum_of_distances_in_tree(n, edges) == expected
