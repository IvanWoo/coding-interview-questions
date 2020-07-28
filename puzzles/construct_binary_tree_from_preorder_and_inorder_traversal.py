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

from typing import List
from puzzles.utils import TreeNode


def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if (not preorder) or (not inorder) or (len(preorder) != len(inorder)):
        return

    def helper(
        preorder: List[int], inorder: List[int], pre_st: int, in_st: int, in_end: int
    ) -> TreeNode:
        if pre_st > len(preorder) or in_st > in_end:
            return
        root = TreeNode(preorder[pre_st])
        ind = inorder.index(preorder[pre_st])
        root.left = helper(preorder, inorder, pre_st + 1, in_st, ind - 1)
        root.right = helper(
            preorder, inorder, pre_st + 1 + (ind - in_st), ind + 1, in_end
        )
        return root

    return helper(preorder, inorder, 0, 0, len(inorder) - 1)


# def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
#     if inorder:
#         ind = inorder.index(preorder.pop(0))
#         root = TreeNode(inorder[ind])
#         root.left = build_tree(preorder, inorder[0:ind])
#         root.right = build_tree(preorder, inorder[ind + 1 :])
#         return root
