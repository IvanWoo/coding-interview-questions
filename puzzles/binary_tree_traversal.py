from collections import deque
from typing import List

from puzzles.utils import TreeNode


def inorder_traversal(root: TreeNode) -> List[int]:
    def it(cur, res):
        "it stands for inorder traversal"
        if not cur:
            return
        it(cur.left, res)
        res.append(cur.val)
        it(cur.right, res)

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


def preorder_traversal(root: TreeNode) -> List[int]:
    def prt(cur, res):
        if not cur:
            return
        res.append(cur.val)
        prt(cur.left, res)
        prt(cur.right, res)

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


def preorder_traversal(root: TreeNode) -> List[int]:
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            res.append(cur.val)
            cur = cur.left
        cur = stack.pop()
        cur = cur.right
    return res


def postorder_traversal(root: TreeNode) -> List[int]:
    def pot(cur, res):
        if not cur:
            return
        pot(cur.left, res)
        pot(cur.right, res)
        res.append(cur.val)

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


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if (not p) and (not q):
        return True
    if (not p) or (not q):
        return False
    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
