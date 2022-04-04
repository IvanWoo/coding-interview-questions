# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the vals of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
"""
from typing import Optional
from puzzles.utils import ListNode


def swap_nodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def to_list(head):
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals

    def from_list(vals):
        dummy = ListNode()
        curr = dummy
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def swap(vals, i, j):
        vals[i], vals[j] = vals[j], vals[i]

    vals = to_list(head)
    n = len(vals)
    swap(vals, k - 1, n - k)
    return from_list(vals)


def swap_nodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    l = r = head
    # move the left to the kth
    for _ in range(k - 1):
        l = l.next

    tail = l
    # the distance from end to left is n-k
    # so when tail move to the end, right will be at the expected place
    while tail.next:
        r, tail = r.next, tail.next
    l.val, r.val = r.val, l.val
    return head
