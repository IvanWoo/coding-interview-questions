# https://leetcode.com/problems/validate-binary-search-tree/
"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from math import inf
from typing import Optional
from puzzles.utils import TreeNode, make_tree


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def helper(node: TreeNode, left: int, right: int) -> bool:
        if not node:
            return True
        val = node.val
        if val <= left or val >= right:
            return False
        return helper(node.left, left, val) and helper(node.right, val, right)

    return helper(root, -inf, inf)


if __name__ == "__main__":
    is_valid_bst(make_tree([2, 1, 3]))
