# https://stackoverflow.com/questions/41135033/type-hinting-within-a-class/52631754#52631754
from __future__ import annotations
from dataclasses import dataclass
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


def make_linked_list(vals: list[Optional[int]]) -> ListNode:
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for i in range(1, len(vals)):
        cur.next = ListNode(vals[i])
        cur = cur.next
    return head


if __name__ == "__main__":
    tns = {}
    for i in range(3):
        tns[i] = TreeNode(i)
    tns[0].left = tns[1]
    tns[0].right = tns[2]
    print(tns[1])
