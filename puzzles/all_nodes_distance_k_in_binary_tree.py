# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""
We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.


Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
from typing import List
from collections import defaultdict
from puzzles.utils import TreeNode


def distance_k(root: TreeNode, target: TreeNode, K: int) -> List[int]:
    # get bidirectional relationship
    hashmap = defaultdict(set)

    def traverse(node, parent):
        if not node:
            return
        if parent:
            hashmap[parent].add(node.val)
            hashmap[node.val].add(parent)
        traverse(node.left, node.val)
        traverse(node.right, node.val)

    traverse(root, None)

    res = []
    visited = set()

    def find(cur, distance):
        if distance == 0:
            res.append(cur)
            return
        visited.add(cur)
        for nxt in hashmap[cur]:
            if nxt not in visited:
                find(nxt, distance - 1)

    find(target.val, K)
    return res
