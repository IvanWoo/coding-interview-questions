# https://stackoverflow.com/questions/41135033/type-hinting-within-a-class/52631754#52631754
from __future__ import annotations
from dataclasses import dataclass


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


if __name__ == "__main__":
    tns = {}
    for i in range(3):
        tns[i] = TreeNode(i)
    tns[0].left = tns[1]
    tns[0].right = tns[2]
    print(tns[1])

