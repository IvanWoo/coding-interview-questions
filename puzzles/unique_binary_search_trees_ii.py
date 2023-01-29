# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

# Example:

# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Constraints:
# 0 <= n <= 8
from typing import List

from puzzles.utils import TreeNode


# top down dp
def generate_trees(n: int) -> List[TreeNode]:
    def helper(lo, hi):
        res = []
        if lo > hi:
            res.append(None)
            return res

        for rt in range(lo, hi + 1):
            leftlist = helper(lo, rt - 1)
            rightlist = helper(rt + 1, hi)

            for right in rightlist:
                for left in leftlist:
                    root = TreeNode(rt)
                    root.right = right
                    root.left = left
                    res.append(root)
        return res

    if n == 0:
        return []
    return helper(1, n)


if __name__ == "__main__":
    print(generate_trees(3))
