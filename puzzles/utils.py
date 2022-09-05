# https://stackoverflow.com/questions/41135033/type-hinting-within-a-class/52631754#52631754
from __future__ import annotations
from dataclasses import dataclass, field
from collections import deque
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: ListNode = None


@dataclass
class TreeNode:
    val: int
    left: TreeNode = None
    right: TreeNode = None


@dataclass
class Node:
    val: int
    left: Node = None
    right: Node = None
    next: Node = None


@dataclass
class NaryNode:
    val: int = None
    children: list[NaryNode] = field(default_factory=list)


def make_tree(vals: list[Optional[int]]) -> TreeNode:
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def find_tree(root: TreeNode, target: int) -> TreeNode:
    def traverse(node):
        if not node:
            return
        if node.val == target:
            return node
        left = traverse(node.left)
        right = traverse(node.right)
        return left or right

    return traverse(root)


def make_linked_list(vals: list[Optional[int]]) -> ListNode:
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for i in range(1, len(vals)):
        cur.next = ListNode(vals[i])
        cur = cur.next
    return head


def make_nary_node(vals: list[Optional[int]]) -> Optional[NaryNode]:
    if not vals:
        return
    root = NaryNode(vals[0])
    queue = deque([root])
    i = 2
    while queue:
        node = queue.popleft()
        children = []
        while i < len(vals) and vals[i] is not None:
            new_node = NaryNode(vals[i])
            queue.append(new_node)
            children.append(new_node)
            i += 1
        # use None to split every levels
        i += 1
        node.children = children
    return root


def deep_sort(x: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(x) for x in x)


if __name__ == "__main__":
    tns = {}
    for i in range(3):
        tns[i] = TreeNode(i)
    tns[0].left = tns[1]
    tns[0].right = tns[2]
    print(tns[1])
