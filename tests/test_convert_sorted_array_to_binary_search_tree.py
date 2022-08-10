import pytest

from puzzles.utils import make_tree, TreeNode
from puzzles.convert_sorted_array_to_binary_search_tree import sorted_array_to_bst


@pytest.mark.parametrize(
    "nums, expected",
    [
        (
            [-10, -3, 0, 5, 9],
            [
                make_tree([0, -3, 9, -10, None, 5]),
                make_tree([0, -10, 5, None, -3, None, 9]),
            ],
        ),
        ([1, 3], [make_tree([3, 1]), make_tree([1, None, 3])]),
    ],
)
def test_sorted_array_to_bst(nums: list[int], expected: list[TreeNode]) -> None:
    assert sorted_array_to_bst(nums) in expected
