# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.



Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""

from typing import List

from puzzles.utils import TreeNode


def construct(pre: List[int], post: List[int]) -> TreeNode:
    def helper(i0, i1, N):
        if N == 0:
            return
        root = TreeNode(pre[i0])
        if N == 1:
            return root
        for L in range(N):
            if post[i1 + L - 1] == pre[i0 + 1]:
                break

        root.left = helper(i0 + 1, i1, L)
        root.right = helper(i0 + L + 1, i1 + L, N - (L + 1))
        return root

    return helper(0, 0, len(pre))


def construct(pre: List[int], post: List[int]) -> TreeNode:
    if not pre:
        return None
    root = TreeNode(pre[0])
    if len(pre) == 1:
        return root
    L = post.index(pre[1]) + 1
    root.left = construct(pre[1 : L + 1], post[:L])
    root.right = construct(pre[L + 1 :], post[L:-1])
    return root


if __name__ == "__main__":
    pre = [1, 2, 4, 5, 3, 6, 7]
    post = [4, 5, 2, 6, 7, 3, 1]
    print(construct(pre, post))
