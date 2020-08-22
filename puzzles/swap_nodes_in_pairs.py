# https://leetcode.com/problems/swap-nodes-in-pairs/
"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

from puzzles.utils import ListNode


def swap_pairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    last = swap_pairs(head.next.next)
    head, head.next = head.next, head
    head.next.next = last
    return head


def swap_pairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    dummy = ListNode()
    pre, cur, nxt = None, head, head.next
    dummy.next = nxt
    while cur and nxt:
        if pre:
            pre.next = nxt
        cur.next, nxt.next = nxt.next, cur

        if cur.next:
            pre, cur, nxt = cur, cur.next, cur.next.next
        else:
            break

    return dummy.next
