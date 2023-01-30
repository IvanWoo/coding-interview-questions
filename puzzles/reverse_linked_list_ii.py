# https://leetcode.com/problems/reverse-linked-list-ii/
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL


1->2->3->4->5->NULL

1<->2<-3<-4  5->NULL

 ________
|        |
1  2<-3<-4  5->NULL
   |________|
"""
from puzzles.utils import ListNode


def reverse_between(head: ListNode, m: int, n: int) -> ListNode:
    if not head:
        return

    cur, prev = head, None
    while m > 1:
        prev, cur = cur, cur.next
        m -= 1
        n -= 1

    tail, con = cur, prev

    while n:
        cur.next, prev, cur = prev, cur, cur.next
        n -= 1

    if con:
        con.next = prev
    else:
        head = prev
    tail.next = cur
    return head


def reverse_between(head: ListNode, m: int, n: int) -> ListNode:
    successor = None

    def reverse_n(head: ListNode, n: int) -> ListNode:
        nonlocal successor
        if n == 1:
            successor = head.next
            return head
        last = reverse_n(head.next, n - 1)

        head.next.next = head
        head.next = successor
        return last

    if m == 1:
        return reverse_n(head, n)
    head.next = reverse_between(head.next, m - 1, n - 1)
    return head
