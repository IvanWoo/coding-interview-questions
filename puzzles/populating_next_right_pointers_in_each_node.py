# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
"""

from puzzles.utils import Node


def connect(root: Node) -> Node:
    level = [root]
    while any(level):
        for i in range(len(level) - 1):
            level[i].next = level[i + 1]
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = temp
    return root


def connect(root: Node) -> Node:
    def helper(node):
        if node and node.left and node.right:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            helper(node.left)
            helper(node.right)

    helper(root)
    return root


def connect(root: Node) -> Node:
    ans = root
    prekid = Node(0)
    kid = prekid
    while root:
        while root:
            if root.left:
                kid.next = root.left
                kid = kid.next
            if root.right:
                kid.next = root.right
                kid = kid.next
            root = root.next
        root, kid = prekid.next, prekid
        # reset the chain for prekid
        kid.next = None
    return ans


if __name__ == "__main__":
    ns = {x: Node(x) for x in range(1, 8)}
    ns[1].left = ns[2]
    ns[1].right = ns[3]
    ns[2].left = ns[4]
    ns[2].right = ns[5]
    ns[3].left = ns[6]
    ns[3].right = ns[7]

    print(connect(ns[1]))
