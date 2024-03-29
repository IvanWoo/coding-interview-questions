# https://leetcode.com/problems/recover-binary-search-tree/
# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Example 1:

# Input: [1,3,null,null,2]

#    1
#   /
#  3
#   \
#    2

# Output: [3,1,null,null,2]

#    3
#   /
#  1
#   \
#    2
# Example 2:

# Input: [3,1,4,null,null,2]

#   3
#  / \
# 1   4
#    /
#   2

# Output: [2,1,4,null,null,3]

#   2
#  / \
# 1   4
#    /
#   3
# Follow up:

# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?

from puzzles.utils import TreeNode


def recover_tree(root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    def traverse(node):
        nonlocal first, second, pre
        if not node:
            return
        traverse(node.left)
        if not first and node.val < pre.val:
            first = pre
        if first and node.val < pre.val:
            second = node
        pre = node
        traverse(node.right)

    first, second, pre = None, None, TreeNode(float("-inf"))
    traverse(root)

    # swap
    first.val, second.val = second.val, first.val
    return


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(3, None, TreeNode(2)), None)
    recover_tree(root)
    print(root)
