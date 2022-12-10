# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/
"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.


Example 1:
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 
Constraints:
The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
"""
from typing import Optional
from math import inf
from puzzles.utils import TreeNode


def max_product(root: Optional[TreeNode]) -> int:
    def traverse(node):
        nonlocal all_sums
        if not node:
            return 0
        left = traverse(node.left)
        right = traverse(node.right)
        curr_sum = node.val + left + right
        all_sums.add(curr_sum)
        return curr_sum

    MOD = 10**9 + 7
    all_sums = set()
    total = traverse(root)
    res = -inf
    for s in all_sums:
        prod = s * (total - s)
        res = max(res, prod)
    return res % MOD
