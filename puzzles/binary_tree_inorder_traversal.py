# https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional

from puzzles.utils import TreeNode


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    def traverse(node: Optional[TreeNode]) -> None:
        nonlocal ans
        if not node:
            return

        traverse(node.left)
        ans.append(node.val)
        traverse(node.right)

    ans = []
    traverse(root)
    return ans


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    ans = []
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        ans.append(curr.val)
        curr = curr.right

    return ans


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    ans, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if visited:
            ans.append(node.val)
        else:
            # inorder: left -> root -> right
            # stack: LIFO
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))
    return ans
