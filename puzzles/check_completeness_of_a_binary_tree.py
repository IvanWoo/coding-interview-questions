# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Constraints:
The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
"""
from collections import defaultdict, deque
from typing import Optional

from puzzles.utils import TreeNode


def is_complete_tree(root: Optional[TreeNode]) -> bool:
    vals = defaultdict(list)
    q = deque([(root, 0)])
    n = 0
    while q:
        cur, lvl = q.popleft()
        n = lvl
        vals[lvl].append(cur.val if cur else None)
        if cur:
            q.append((cur.left, lvl + 1))
            q.append((cur.right, lvl + 1))
    for i in range(n - 1):
        if any(v is None for v in vals[i]):
            return False
    last_row = vals[n - 1]
    idx = 0
    while idx < len(last_row) and last_row[idx] is not None:
        idx += 1
    if any(v is not None for v in last_row[idx:]):
        return False
    return True


def is_complete_tree(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    q = deque([root])
    found_none = False
    while q:
        cur = q.popleft()
        if cur is None:
            found_none = True
        else:
            if found_none:
                return False
            q.append(cur.left)
            q.append(cur.right)
    return True
