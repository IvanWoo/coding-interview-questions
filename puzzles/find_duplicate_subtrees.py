# https://leetcode.com/problems/find-duplicate-subtrees/
"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Constraints:
The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200
"""

from collections import Counter, deque
from typing import Optional

from puzzles.utils import TreeNode


def find_duplicate_subtrees(root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
    def collect(node):
        nonlocal c, ans
        if not node:
            return "#"
        serial = f"{node.val},{collect(node.left)},{collect(node.right)}"
        c[serial] += 1
        if c[serial] == 2:
            ans.append(node)
        return serial

    c = Counter()
    ans = []
    collect(root)
    return ans


def find_duplicate_subtrees(root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
    def traverse(node):
        nonlocal ans, visited
        if not node:
            return
        if node in visited and node not in ans:
            ans.append(node)
        visited.append(node)
        traverse(node.left)
        traverse(node.right)

    visited = []
    ans = []
    traverse(root)
    return ans


def find_duplicate_subtrees(root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
    def serialize(node: Optional[TreeNode]) -> list[Optional[int]]:
        def traverse(node):
            nonlocal ret
            if not node:
                ret.append(None)
                return
            ret.append(node.val)
            traverse(node.left)
            traverse(node.right)

        ret = []
        traverse(node)
        return tuple(ret)

    q = deque([(root, serialize(root))])
    visited, included = set(), set()
    ans = []
    while q:
        (cur_node, node_s) = q.popleft()
        if not cur_node:
            continue
        if node_s in visited and node_s not in included:
            ans.append(cur_node)
            included.add(node_s)
        visited.add(node_s)
        q.append((cur_node.left, serialize(cur_node.left)))
        q.append((cur_node.right, serialize(cur_node.right)))
    return ans
