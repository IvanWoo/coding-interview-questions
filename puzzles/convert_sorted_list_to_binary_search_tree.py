# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
height-balanced
 binary search tree.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []


Constraints:
The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
"""
from typing import Optional

from puzzles.utils import ListNode, TreeNode


def sorted_list_to_BST(head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head:
        return
    array = []
    cur = head
    while cur:
        array.append(cur.val)
        cur = cur.next

    def helper(array: Optional[list[int]]):
        if not array:
            return
        mid = len(array) // 2
        left = helper(array[:mid])
        right = helper(array[mid + 1 :])
        return TreeNode(array[mid], left, right)

    return helper(array)
