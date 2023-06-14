# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""
from math import inf
from typing import Optional

from puzzles.utils import TreeNode


def get_minimum_difference(root: Optional[TreeNode]) -> int:
    def traverse(node):
        nonlocal ret
        if not node:
            return inf, -inf
        val = node.val
        left_lo, left_hi = traverse(node.left)
        right_lo, right_hi = traverse(node.right)
        ret = min([ret, abs(val - left_hi), abs(right_lo - val)])
        return min(left_lo, val), max(right_hi, val)

    ret = inf
    traverse(root)
    return ret


def get_minimum_difference(root: Optional[TreeNode]) -> int:
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        seq.append(node.val)
        traverse(node.right)

    seq = []
    traverse(root)
    ret = inf
    for i in range(1, len(seq)):
        ret = min(ret, seq[i] - seq[i - 1])
    return ret
