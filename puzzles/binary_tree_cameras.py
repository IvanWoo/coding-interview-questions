# https://leetcode.com/problems/binary-tree-cameras/
"""
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
Node.val == 0
"""


from typing import Optional

from puzzles.utils import TreeNode


def min_camera_cover(root: Optional[TreeNode]) -> int:
    """
    three states:
    - 0: uncovered
    - 1: no camera but covered
    - 2: has_camera
    """

    def traverse(node: Optional[TreeNode]):
        nonlocal count
        if not node:
            return 1

        left = traverse(node.left)
        right = traverse(node.right)

        if left == 0 or right == 0:
            count += 1
            return 2
        elif left == 2 or right == 2:
            return 1
        else:
            return 0

    count = 0
    if not traverse(root):
        count += 1
    return count
