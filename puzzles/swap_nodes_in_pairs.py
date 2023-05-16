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
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy

    while curr.next and curr.next.next:
        node1 = curr.next
        node2 = curr.next.next
        curr.next = node2
        node1.next = node2.next
        node2.next = node1
        curr = node1

    return dummy.next


def swap_pairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    second = head.next
    head.next = swap_pairs(second.next)
    second.next = head
    return second
