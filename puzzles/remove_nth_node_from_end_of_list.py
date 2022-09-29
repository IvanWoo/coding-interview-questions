# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?
"""
from typing import Optional
from puzzles.utils import ListNode


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(-1)
    dummy.next = head

    total = 0
    cur = head
    while cur:
        total += 1
        cur = cur.next

    cur = dummy
    count = 0
    while count != (total - n):
        count += 1
        cur = cur.next

    cur.next = cur.next.next
    return dummy.next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(-1, head)

    fast, slow = head, head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return dummy.next.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
