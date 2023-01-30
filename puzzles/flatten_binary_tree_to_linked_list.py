# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from typing import Optional

from puzzles.utils import TreeNode


def flatten(root: Optional[TreeNode]) -> None:
    def traverse(node: Optional[TreeNode]):
        nonlocal vals
        if not node:
            return
        vals.append(node.val)
        traverse(node.left)
        traverse(node.right)

    vals = []
    traverse(root)
    cur = root
    for val in vals[1:]:
        cur.left = None
        cur.right = TreeNode(val)
        cur = cur.right
    return


def flatten(root: Optional[TreeNode]) -> None:
    def traverse(node: Optional[TreeNode]):
        if not node:
            return
        cur = node
        left = traverse(node.left)
        right = traverse(node.right)
        cur.left = None
        if left:
            cur.right = left
            while left and left.right:
                left = left.right
            left.right = right
        return cur

    traverse(root)
    return


def flatten(root: Optional[TreeNode]) -> None:
    def helper(node: Optional[TreeNode]):
        nonlocal prev
        if not node:
            return
        helper(node.right)
        helper(node.left)
        node.right = prev
        node.left = None
        prev = node

    prev = None
    helper(root)
    return
