# https://stackoverflow.com/questions/41135033/type-hinting-within-a-class/52631754#52631754
from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: ListNode = None


@dataclass
class DListNode:
    """
    doubly linked list node
    """

    val: int = 0
    prev: DListNode = None
    next: DListNode = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.left = DListNode()
        self.right = DListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self) -> int:
        return len(self.map)

    def push_right(self, val: int) -> None:
        node = DListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val) -> None:
        if val not in self.map:
            return
        node = self.map[val]
        next, prev = node.next, node.prev
        next.prev = prev
        prev.next = next
        del self.map[val]

    def pop_left(self) -> int:
        res = self.left.next.val
        self.pop(res)
        return res

    def update(self, val) -> None:
        self.pop(val)
        self.push_right(val)


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


def connect_linked_list(head: ListNode, start: int, end: int) -> ListNode:
    start_node = None
    end_node = None
    cur = head
    while cur:
        if cur.val == start:
            start_node = cur
        if cur.val == end:
            end_node = cur
        cur = cur.next
    start_node.next = end_node
    return end_node


def linked_list_to_list(head: ListNode) -> list[int]:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


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


def print_matrix(mat):
    for r in range(len(mat)):
        print(mat[r])


if __name__ == "__main__":
    tns = {}
    for i in range(3):
        tns[i] = TreeNode(i)
    tns[0].left = tns[1]
    tns[0].right = tns[2]
    print(tns[1])
