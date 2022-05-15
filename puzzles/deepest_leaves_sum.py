# https://leetcode.com/problems/deepest-leaves-sum/
"""
Given the root of a binary tree, return the sum of values of its deepest leaves.
 
Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:
The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""
from typing import Optional
from collections import defaultdict
from puzzles.utils import TreeNode


def deepest_leaves_sum(root: Optional[TreeNode]) -> int:
    def traverse(node, lv):
        nonlocal leaves
        if not node:
            return
        leaves[lv].append(node.val)
        traverse(node.left, lv + 1)
        traverse(node.right, lv + 1)

    leaves = defaultdict(list)
    traverse(root, 0)
    return sum(leaves[max(leaves.keys())])
