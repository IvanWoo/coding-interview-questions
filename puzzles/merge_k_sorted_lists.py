# https://leetcode.com/problems/merge-k-sorted-lists/
"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
import heapq
from queue import PriorityQueue
from typing import Optional

from puzzles.utils import ListNode


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    pq = []
    dummy = ListNode()
    cur = dummy
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(pq, (l.val, i, l.next))
    while pq:
        val, idx, node = heapq.heappop(pq)
        cur.next = ListNode(val)
        cur = cur.next
        if node:
            heapq.heappush(pq, (node.val, idx, node.next))
    return dummy.next


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    pq = PriorityQueue()
    dummy = ListNode()
    cur = dummy
    for i, l in enumerate(lists):
        if l:
            pq.put((l.val, i, l.next))

    while not pq.empty():
        val, idx, node = pq.get()
        cur.next = ListNode(val)
        cur = cur.next
        if node:
            pq.put((node.val, idx, node.next))
    return dummy.next
