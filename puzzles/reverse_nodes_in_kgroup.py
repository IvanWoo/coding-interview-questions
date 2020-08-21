# https://leetcode.com/problems/reverse-nodes-in-k-group/
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

from puzzles.utils import ListNode


def reverse_kgroup(head: ListNode, k: int) -> ListNode:
    count = 0
    cur = head
    while cur:
        cur = cur.next
        count += 1
    if count < k:
        return head

    pre, new_head = reverse(head, k)
    head.next = reverse_kgroup(new_head, k)
    return pre


def reverse(head, count):
    pre, cur = None, head
    while count > 0:
        nxt = cur.next
        cur.next = pre
        pre, cur = cur, nxt
        count -= 1

    return pre, cur
