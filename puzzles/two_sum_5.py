# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:

# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 9

# Output: True


# Example 2:

# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Target = 28

# Output: False

from collections import deque

from puzzles.utils import TreeNode


def find_target(root: TreeNode, k: int) -> bool:
    seq = deque()

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        seq.append(node.val)
        traverse(node.right)

    traverse(root)
    seq = list(seq)

    for i, v in enumerate(seq):
        if (k - v) in seq[(i + 1) :]:
            return True

    return False


def find_target(root: TreeNode, k: int) -> bool:
    q = []

    def find(root: TreeNode, k: int, q) -> bool:
        if not root:
            return False
        if (k - root.val) in q:
            return True
        q.append(root.val)
        return find(root.left, k, q) or find(root.right, k, q)

    return find(root, k, q)
