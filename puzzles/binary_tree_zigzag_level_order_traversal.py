# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from collections import defaultdict, deque
from typing import Optional

from puzzles.utils import TreeNode


def zigzag_level_order(root: Optional[TreeNode]) -> list[list[int]]:
    def traverse(node, lvl):
        nonlocal ans
        if not node:
            return
        val = node.val

        ans[lvl].append(val) if lvl % 2 == 0 else ans[lvl].appendleft(val)
        traverse(node.left, lvl + 1)
        traverse(node.right, lvl + 1)

    ans = defaultdict(deque)
    traverse(root, 0)
    return [list(v) for v in ans.values()]
