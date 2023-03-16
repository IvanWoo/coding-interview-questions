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


from puzzles.utils import TreeNode


def build_tree(inorder: list[int], postorder: list[int]) -> TreeNode:
    if not inorder or not postorder or len(inorder) != len(postorder):
        return

    def helper(in_start, in_end, post_end):
        if in_start > in_end or post_end < 0:
            return
        val = postorder[post_end]
        idx = inorder.index(val)
        left = helper(in_start, idx - 1, post_end - 1 - (in_end - idx))
        right = helper(idx + 1, in_end, post_end - 1)
        return TreeNode(val, left, right)

    return helper(0, len(inorder) - 1, len(postorder) - 1)
