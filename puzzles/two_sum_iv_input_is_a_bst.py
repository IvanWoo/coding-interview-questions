# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
"""
from typing import Optional

from puzzles.utils import TreeNode


def find_target(root: Optional[TreeNode], k: int) -> bool:
    def find(node: Optional[TreeNode], q: set) -> bool:
        if not node:
            return False
        if k - node.val in q:
            return True
        q.add(node.val)
        return find(node.left, q) or find(node.right, q)

    return find(root, set())
