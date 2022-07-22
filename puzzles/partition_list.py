# https://leetcode.com/problems/partition-list/
"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""


from typing import Optional
from puzzles.utils import ListNode, make_linked_list


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    before_dummy = ListNode(42)
    after_dummy = ListNode(42)
    before_pt = before_dummy
    after_pt = after_dummy
    curr = head
    while curr:
        val = curr.val
        if val < x:
            before_pt.next = ListNode(val)
            before_pt = before_pt.next
        else:
            after_pt.next = ListNode(val)
            after_pt = after_pt.next
        curr = curr.next
    before_pt.next = after_dummy.next
    return before_dummy.next


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    dummy = ListNode(42)
    dummy.next = head
    cur = dummy
    while cur.next and cur.next.val < x:
        cur = cur.next

    fast = cur
    while fast and fast.next:
        if fast.next.val >= x:
            fast = fast.next
        else:
            target = fast.next
            fast.next = target.next
            target.next = cur.next
            cur.next = target
            cur = cur.next
    return dummy.next


if __name__ == "__main__":
    partition(make_linked_list([1, 4, 3, 2, 5, 2]), 3)
