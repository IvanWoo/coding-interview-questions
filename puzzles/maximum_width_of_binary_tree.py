# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# It is guaranteed that the answer will in the range of 32-bit signed integer.

# Example 1:

# Input:

#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:

# Input:

#           1
#          /
#         3
#        / \
#       5   3

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input:

#           1
#          / \
#         3   2
#        /
#       5

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input:

#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


# Constraints:

# The given binary tree will have between 1 and 3000 nodes.

from collections import deque

from puzzles.utils import TreeNode


def width_of_binary_tree(root: TreeNode) -> int:
    ans = 1
    stack = deque([(1, root)])
    while stack:
        temp = deque()
        width = {"left": float("inf"), "right": float("-inf")}
        while stack:
            x_axis, cur = stack.popleft()
            if not cur:
                continue
            width["left"] = min(x_axis, width["left"])
            width["right"] = max(x_axis, width["right"])
            temp.extend(deque([(x_axis * 2, cur.left), (x_axis * 2 + 1, cur.right)]))
        ans = max(ans, (width["right"] - width["left"] + 1))
        stack = temp
    return ans
