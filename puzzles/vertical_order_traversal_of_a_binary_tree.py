# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""
Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

Example 1:

Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).

Example 2:

Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 
Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
"""

from collections import defaultdict, deque
from heapq import heappop, heappush
from puzzles.utils import TreeNode
from typing import List


def vertical_traversal(root: TreeNode) -> List[List[int]]:
    ans = defaultdict(list)
    stack = deque([(0, 0, root)])
    while stack:
        x_axis, y_axis, node = stack.popleft()
        if node:
            ans[x_axis].append((y_axis, node.val))
            stack.extend(
                deque(
                    [
                        (x_axis - 1, y_axis + 1, node.left),
                        (x_axis + 1, y_axis + 1, node.right),
                    ]
                )
            )
    ans = [sorted(vy) for _, vy in sorted(ans.items())]
    res = [[]] * len(ans)
    for i, yvs in enumerate(ans):
        res[i] = [v for y, v in yvs]
    return res


if __name__ == "__main__":
    ts = {x: TreeNode(x) for x in range(12)}
    ts[0].left = ts[2]
    ts[0].right = ts[1]

    ts[2].left = ts[3]

    ts[3].left = ts[4]
    ts[3].right = ts[5]

    ts[4].right = ts[7]
    ts[7].left = ts[10]
    ts[7].right = ts[8]

    ts[5].left = ts[6]
    ts[6].left = ts[11]
    ts[6].right = ts[9]

    vertical_traversal(ts[0])
