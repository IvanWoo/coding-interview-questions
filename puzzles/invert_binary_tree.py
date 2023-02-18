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
    def helper(node):
        if not node:
            return
        node.left, node.right = helper(node.right), helper(node.left)
        return node

    return helper(root)
