# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""
Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:
Input: [8,3,10,1,6,14,4,7,13]
Output: 7

Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Note:
The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""

from puzzles.utils import TreeNode


def max_ancestor_diff(root: TreeNode) -> int:
    ans = 0

    def traverse(node, lo, hi):
        nonlocal ans
        if not node:
            return
        if hi is None and lo is None:
            hi = lo = node.val
        ans = max(ans, max(hi - node.val, node.val - lo))
        lo, hi = min(lo, node.val), max(hi, node.val)
        traverse(node.left, lo, hi)
        traverse(node.right, lo, hi)

    traverse(root, None, None)
    return ans


def max_ancestor_diff(root: TreeNode) -> int:
    def traverse(node):
        nonlocal ans
        if not node:
            return
        left = traverse(node.left)
        right = traverse(node.right)
        val = node.val
        min_val = max_val = val
        if left is not None:
            min_val = min(min_val, left[0])
            max_val = max(max_val, left[1])
        if right is not None:
            min_val = min(min_val, right[0])
            max_val = max(max_val, right[1])
        ans = max([ans, abs(val - min_val), abs(val - max_val)])
        return min_val, max_val

    ans = 0
    traverse(root)
    return ans
