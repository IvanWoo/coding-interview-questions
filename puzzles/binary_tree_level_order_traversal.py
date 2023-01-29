# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from collections import defaultdict, deque

from puzzles.utils import TreeNode


def level_order(root: TreeNode) -> list[list[int]]:
    ans = defaultdict(deque)

    def traverse(node, lv, ans):
        if not node:
            return
        ans[lv].append(node.val)
        traverse(node.left, lv + 1, ans)
        traverse(node.right, lv + 1, ans)

    traverse(root, 0, ans)
    return [list(x) for x in ans.values()]


def level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = deque()
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans
