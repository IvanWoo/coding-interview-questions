from utils import TreeNode
from typing import List
from collections import deque


def it(cur, ans):
    "it stands for inorder traversal"
    if not cur:
        return
    it(cur.left, ans)
    ans.append(cur.val)
    it(cur.right, ans)


def inorder_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    it(root, res)
    return res


def inorder_traversal(root: TreeNode) -> List[int]:
    res = []
    stack = deque()
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


def prt(cur, res):
    if not cur:
        return
    res.append(cur.val)
    prt(cur.left, res)
    prt(cur.right, res)


def preorder_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    prt(root, res)
    return res


def preorder_traversal(root: TreeNode) -> List[int]:
    stack = deque()
    stack.append(root)
    res = []

    while stack:
        cur = stack.pop()
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            stack.append(cur.left)
    return res


def pot(cur, res):
    if not cur:
        return
    pot(cur.left, res)
    pot(cur.right, res)
    res.append(cur.val)


def postorder_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    pot(root, res)
    return res


def postorder_traversal(root: TreeNode) -> List[int]:
    stack = [(root, False)]
    res = []

    while stack:
        cur, visited = stack.pop()
        if cur:
            if visited:
                res.append(cur.val)
            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
    return res

