# https://leetcode.com/problems/add-two-numbers/
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

from puzzles.utils import ListNode


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    curr = dummy
    p1, p2 = l1, l2
    carrier = 0
    while p1 or p2:
        x = p1.val if p1 else 0
        y = p2.val if p2 else 0
        carrier, val = divmod(x + y + carrier, 10)
        curr.next = ListNode(val)
        curr = curr.next
        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next

    if carrier > 0:
        curr.next = ListNode(carrier)

    return dummy.next
