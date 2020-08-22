# https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

"""

from puzzles.utils import TreeNode
from typing import List


class FindModes:
    def __init__(self):
        self.modes = []
        self.prev = None
        self.count = 0
        self.max_count = 0

    def find_modes(self, root: TreeNode) -> List[int]:
        self.traversal(root)
        return self.modes

    def traversal(self, node):
        if not node:
            return
        self.traversal(node.left)
        if self.prev != node.val:
            self.count = 1
        else:
            self.count += 1

        if self.count == self.max_count:
            self.modes.append(node.val)
        elif self.count > self.max_count:
            self.max_count = self.count
            self.modes = [node.val]
        self.prev = node.val
        self.traversal(node.right)
