# https://leetcode.com/problems/odd-even-linked-list/description/
"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 
Constraints:
The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
"""
from typing import Optional
from puzzles.utils import ListNode, make_linked_list, linked_list_to_list

# cheat
def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    vals = []
    while cur:
        vals.append(cur.val)
        cur = cur.next
    odds = [v for i, v in enumerate(vals) if i % 2 == 0]
    evens = [v for i, v in enumerate(vals) if i % 2 == 1]
    res = odds + evens
    return make_linked_list(res)


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    dummy = ListNode(42, head)
    evens_dummy = ListNode(42)
    evens = evens_dummy
    cur, nxt = head, head.next
    while nxt:
        cur.next = nxt.next
        evens.next = nxt
        evens = evens.next
        nxt.next = None
        if cur.next is None:
            break
        cur, nxt = cur.next, cur.next.next
    cur.next = evens_dummy.next
    return dummy.next
