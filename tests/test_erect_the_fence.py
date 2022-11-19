import pytest
from puzzles.erect_the_fence import outer_trees


@pytest.mark.parametrize(
    "trees, expected",
    [
        (
            [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
            [[1, 1], [2, 0], [3, 3], [2, 4], [4, 2]],
        ),
        ([[1, 2], [2, 2], [4, 2]], [[4, 2], [2, 2], [1, 2]]),
        (
            [[3, 7], [6, 8], [7, 8], [11, 10], [4, 3], [8, 5], [7, 13], [4, 13]],
            [[3, 7], [4, 13], [11, 10], [4, 3], [8, 5], [7, 13]],
        ),
    ],
)
def test_outer_trees(trees, expected):
    assert sorted(outer_trees(trees)) == sorted(expected)
