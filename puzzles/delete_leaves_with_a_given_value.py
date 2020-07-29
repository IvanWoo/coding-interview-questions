# https://leetcode.com/problems/delete-leaves-with-a-given-value/
# Given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you can't).

# Constraints:

# 1 <= target <= 1000
# The given binary tree will have between 1 and 3000 nodes.
# Each node's value is between [1, 1000].

from puzzles.utils import TreeNode


def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


def remove_leaf_nodes(root: TreeNode, target: int) -> TreeNode:
    if root:
        root.left = remove_leaf_nodes(root.left, target)
        root.right = remove_leaf_nodes(root.right, target)
        if root.val == target and is_leaf(root):
            return None
        return root
