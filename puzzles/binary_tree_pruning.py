# https://leetcode.com/problems/binary-tree-pruning/
"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]



Note:

The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.
"""

from puzzles.utils import TreeNode


def has_one(node):
    if not node:
        return False
    return node.val == 1 or has_one(node.left) or has_one(node.right)


def prune_tree(root: TreeNode) -> TreeNode:
    if not root:
        return
    root.left = root.left if has_one(root.left) else None
    root.right = root.right if has_one(root.right) else None
    prune_tree(root.left)
    prune_tree(root.right)
    return root


def prune_tree(root: TreeNode) -> TreeNode:
    if not root:
        return
    root.left = prune_tree(root.left)
    root.right = prune_tree(root.right)
    if not root.left and not root.right and root.val == 0:
        return None
    return root


def prune_tree(root: TreeNode) -> TreeNode:
    if not root:
        return
    ans = TreeNode(
        root.val,
        prune_tree(root.left),
        prune_tree(root.right),
    )
    if not ans.val and not ans.left and not ans.right:
        return None
    return ans
