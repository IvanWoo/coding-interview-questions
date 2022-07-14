# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

from puzzles.utils import TreeNode


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    if (not preorder) or (not inorder) or (len(preorder) != len(inorder)):
        return

    def helper(pre_st: int, in_st: int, in_end: int) -> TreeNode:
        if pre_st > len(preorder) or in_st > in_end:
            return
        root_val = preorder[pre_st]
        root = TreeNode(root_val)
        pivot = inorder.index(root_val)
        root.left = helper(pre_st + 1, in_st, pivot - 1)
        root.right = helper(pre_st + 1 + (pivot - in_st), pivot + 1, in_end)
        return root

    return helper(0, 0, len(inorder) - 1)
