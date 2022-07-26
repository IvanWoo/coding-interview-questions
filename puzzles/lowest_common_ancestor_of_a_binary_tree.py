# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
from puzzles.utils import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def is_descendant(node, target):
        nonlocal memo
        if not node:
            return False
        memo_key = (node.val, target.val)
        if memo_key in memo:
            return memo[memo_key]
        if node == target:
            return True
        left = is_descendant(node.left, target)
        right = is_descendant(node.right, target)
        ans = left or right
        memo[memo_key] = ans
        return ans

    def dfs(node: TreeNode):
        nonlocal ans
        if not node:
            return
        if is_descendant(node, p) and is_descendant(node, q):
            ans = node
        dfs(node.left)
        dfs(node.right)

    memo = dict()
    ans = None
    dfs(root)
    return ans


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def helper(root, p, q):
        if not root:
            return
        if root == p or root == q:
            return root

        left = helper(root.left, p, q)
        right = helper(root.right, p, q)
        if left and right:
            return root
        return left or right

    return helper(root, p, q)
