# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example 1:
Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:
Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:
Input: root = [9]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 9
"""
from collections import Counter
from functools import cache
from typing import Optional

from puzzles.utils import TreeNode


# MLE
def pseudo_palindromic_paths(root: Optional[TreeNode]) -> int:
    def is_valid(path: list[int]):
        if not path:
            return False
        c = Counter(path)
        n = len(path)
        chance = int(n % 2 == 1)
        for _, v in c.items():
            if v % 2 == 1:
                if chance == 0:
                    return False
                else:
                    chance -= 1
        return True

    def traverse(node, path):
        nonlocal ans
        if not node:
            return
        nxt_path = path + [node.val]
        if node.left:
            traverse(node.left, nxt_path)
        if node.right:
            traverse(node.right, nxt_path)
        if not node.left and not node.right:
            if is_valid(nxt_path):
                ans += 1

    ans = 0
    traverse(root, [])
    return ans


def pseudo_palindromic_paths(root: Optional[TreeNode]) -> int:
    @cache
    def is_valid(nxt_path):
        target = set([0] + [2**n for n in range(10)])
        return nxt_path in target

    def traverse(node, path):
        nonlocal ans
        if not node:
            return
        nxt_path = path ^ (1 << node.val)
        if node.left:
            traverse(node.left, nxt_path)
        if node.right:
            traverse(node.right, nxt_path)
        if not node.left and not node.right:
            if is_valid(nxt_path):
                ans += 1

    ans = 0
    traverse(root, 0)
    return ans
