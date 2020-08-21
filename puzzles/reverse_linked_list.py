# https://leetcode.com/problems/reverse-linked-list/
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

from puzzles.utils import ListNode


def reverse_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    last = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return last


def reverse_list(head: ListNode) -> ListNode:
    pre, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre, cur = cur, nxt
    return pre
