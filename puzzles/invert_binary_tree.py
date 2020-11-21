# https://leetcode.com/problems/invert-binary-tree/
# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
from puzzles.utils import TreeNode


def invert_tree(root: TreeNode) -> TreeNode:
    if not root:
        return

    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
