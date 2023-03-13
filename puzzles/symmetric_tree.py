# https://leetcode.com/problems/symmetric-tree/description/
"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""
from collections import deque
from typing import Optional

from puzzles.utils import TreeNode


def is_symmetric(root: Optional[TreeNode]) -> bool:
    q = deque([root])
    while q:
        new_q = deque()
        vals = []
        while q:
            cur = q.popleft()
            if cur:
                vals.append(cur.val)
                new_q.extend([cur.left, cur.right])
            else:
                vals.append(None)
        n = len(vals)
        if n > 1:
            mid = n // 2
            if vals[:mid] != vals[mid:][::-1]:
                return False
        q = new_q
    return True


def is_symmetric(root: Optional[TreeNode]) -> bool:
    def helper(left, right) -> list[Optional[int]]:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
            left.val == right.val
            and helper(left.left, right.right)
            and helper(left.right, right.left)
        )

    if not root:
        return False
    return helper(root.left, root.right)
