import pytest
from puzzles.utils import make_tree
from puzzles.leaf_similar_trees import leaf_similar


@pytest.mark.parametrize(
    "root1, root2, expected",
    [
        (
            make_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
            make_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]),
            True,
        ),
        (make_tree([1, 2, 3]), make_tree([1, 3, 2]), False),
    ],
)
def test_leaf_similar(root1, root2, expected):
    assert leaf_similar(root1, root2) == expected
