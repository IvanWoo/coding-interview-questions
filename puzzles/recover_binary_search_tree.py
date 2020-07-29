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
    state = {"first": None, "second": None, "pre": TreeNode(float("-inf"))}

    def traverse(node, state):
        if not node:
            return
        traverse(node.left, state)
        if not state["first"] and node.val < state["pre"].val:
            state["first"] = state["pre"]
        if state["first"] and node.val < state["pre"].val:
            state["second"] = node
        state["pre"] = node
        traverse(node.right, state)

    traverse(root, state)

    # swap
    state["first"].val, state["second"].val = (
        state["second"].val,
        state["first"].val,
    )
    return
