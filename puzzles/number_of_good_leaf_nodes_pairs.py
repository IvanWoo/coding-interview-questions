# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
"""
Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Example 1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

Example 2:
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example 3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Example 4:
Input: root = [100], distance = 1
Output: 0

Example 5:
Input: root = [1,1,1], distance = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 2^10].
Each node's value is between [1, 100].
1 <= distance <= 10
"""

from puzzles.utils import TreeNode


def is_leaf(node):
    return node.val and (node.left is None) and (node.right is None)


def count_pairs(root: TreeNode, distance: int) -> int:
    ans = [0]

    def dfs(node):
        if not node:
            return []
        if is_leaf(node):
            return [1]
        left = dfs(node.left)
        right = dfs(node.right)
        ans[0] += sum(l + r <= distance for l in left for r in right)
        return [n + 1 for n in left + right if n + 1 < distance]

    dfs(root)
    return ans[0]
