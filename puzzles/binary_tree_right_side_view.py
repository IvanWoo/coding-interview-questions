# https://leetcode.com/problems/binary-tree-right-side-view/
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from collections import defaultdict
from puzzles.utils import TreeNode
from typing import List


def right_side_view(root: TreeNode) -> List[int]:
    ans = defaultdict(int)

    def traverse(node, lv, ans):
        if not node:
            return
        ans[lv] = node.val
        traverse(node.left, lv + 1, ans)
        traverse(node.right, lv + 1, ans)

    traverse(root, 0, ans)
    return ans.values()
