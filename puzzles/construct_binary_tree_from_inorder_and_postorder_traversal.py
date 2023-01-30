# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7

from typing import List

from puzzles.utils import TreeNode


def build_tree(inorder: List[int], postorder: List[int]) -> TreeNode:
    if (not inorder) or (not postorder) or (len(inorder) != len(postorder)):
        return

    def helper(inorder, postorder, in_st, in_end, post_end):
        if in_st > in_end or post_end < 0:
            return
        root = TreeNode(postorder[post_end])
        ind = inorder.index(postorder[post_end])
        root.left = helper(
            inorder, postorder, in_st, ind - 1, post_end - 1 - (in_end - ind)
        )
        root.right = helper(inorder, postorder, ind + 1, in_end, post_end - 1)
        return root

    return helper(inorder, postorder, 0, len(inorder) - 1, len(postorder) - 1)
