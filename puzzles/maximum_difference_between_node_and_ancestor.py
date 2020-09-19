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

    def traverse(node, max_val, min_val):
        nonlocal ans
        if not node:
            return
        if max_val is None and min_val is None:
            max_val = min_val = node.val
        ans = max(ans, max(abs(max_val - node.val), abs(min_val - node.val)))
        max_val, min_val = max(max_val, node.val), min(min_val, node.val)
        traverse(node.left, max_val, min_val)
        traverse(node.right, max_val, min_val)

    traverse(root, None, None)
    return ans
