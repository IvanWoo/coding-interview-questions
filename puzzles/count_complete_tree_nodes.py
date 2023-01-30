# https://leetcode.com/problems/count-complete-tree-nodes/
"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""
from typing import Optional

from puzzles.utils import TreeNode


# O(n)
def count_nodes(root: Optional[TreeNode]) -> int:
    def traverse(node):
        if not node:
            return 0
        left = traverse(node.left)
        right = traverse(node.right)
        return left + right + 1

    return traverse(root)


# O(log(n)^2)
def count_nodes(root: Optional[TreeNode]) -> int:
    def helper(node):
        left_lvl = 0
        right_lvl = 0
        curr = node
        while curr:
            curr = curr.left
            left_lvl += 1
        curr = node
        while curr:
            curr = curr.right
            right_lvl += 1
        if left_lvl == right_lvl:
            return 2 ** (left_lvl) - 1
        return 1 + helper(node.left) + helper(node.right)

    return helper(root)
