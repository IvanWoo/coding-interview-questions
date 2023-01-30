import pytest

from puzzles.binary_tree_cameras import min_camera_cover
from puzzles.utils import TreeNode, make_tree


@pytest.mark.parametrize(
    "root, expected",
    [
        (make_tree([0, 0, None, 0, 0]), 1),
        (make_tree([0, 0, None, 0, None, 0, None, None, 0]), 2),
    ],
)
def test_min_camera_cover(root: TreeNode, expected: int) -> None:
    assert min_camera_cover(root) == expected
