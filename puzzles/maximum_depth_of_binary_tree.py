# https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
from collections import deque
from typing import Optional

from puzzles.utils import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    def traverse(node, depth):
        if not node:
            return depth
        return max(
            [
                traverse(node.left, depth + 1),
                traverse(node.right, depth + 1),
            ]
        )

    return traverse(root, 0)


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    q = deque([(root, 1)])
    ans = 0
    while q:
        node, steps = q.popleft()
        ans = max(ans, steps)
        if node.left:
            q.append((node.left, steps + 1))
        if node.right:
            q.append((node.right, steps + 1))
    return ans
