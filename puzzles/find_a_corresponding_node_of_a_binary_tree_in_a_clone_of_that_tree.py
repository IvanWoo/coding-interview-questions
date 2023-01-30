# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.


Example 1:
Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

Example 2:
Input: tree = [7], target =  7
Output: 7

Example 3:
Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4


Constraints:
The number of nodes in the tree is in the range [1, 104].
The values of the nodes of the tree are unique.
target node is a node from the original tree and is not null.

Follow up: Could you solve the problem if repeated values on the tree are allowed?
"""
from puzzles.utils import TreeNode


def get_target_copy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    def traverse(node):
        nonlocal res
        if res:
            return
        if not node:
            return
        if node.val == target.val:
            res = node
            return
        traverse(node.left)
        traverse(node.right)

    res = None
    traverse(cloned)
    return res


def get_target_copy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    def is_same(n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        return (
            n1.val == n2.val
            and is_same(n1.left, n2.left)
            and is_same(n1.right, n2.right)
        )

    def traverse(node):
        nonlocal res
        if res:
            return
        if not node:
            return
        if is_same(node, target):
            res = node
            return
        traverse(node.left)
        traverse(node.right)

    res = None
    traverse(cloned)
    return res
