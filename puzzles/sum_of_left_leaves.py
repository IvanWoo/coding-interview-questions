# https://leetcode.com/problems/sum-of-left-leaves/
# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

from puzzles.utils import TreeNode


def is_leaf(node: TreeNode):
    return node.left is None and node.right is None


def get_left_leaf(node, from_left):
    if not node:
        return 0
    if is_leaf(node) and from_left:
        return node.val
    return get_left_leaf(node.right, False) + get_left_leaf(node.left, True)


def sum_of_left_leaves(root: TreeNode) -> int:
    if not root:
        return 0
    return get_left_leaf(root.left, True) + get_left_leaf(root.right, False)
