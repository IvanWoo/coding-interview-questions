# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
"""
from math import inf
from typing import Optional

from puzzles.utils import TreeNode


def min_diff_in_bst(root: Optional[TreeNode]) -> int:
    def traverse(node):
        if not node:
            return []
        return traverse(node.left) + [node.val] + traverse(node.right)

    ans = inf
    vals = traverse(root)
    n = len(vals)
    for i in range(1, n):
        ans = min(ans, vals[i] - vals[i - 1])
    return ans
