# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 
Constraints:
The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
"""
from typing import Optional
from puzzles.utils import ListNode


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    def get_len(head):
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        return n

    n = get_len(head)
    idx = 0
    mid = n // 2
    dummy = ListNode(42, head)
    parent = dummy
    cur = head
    while cur:
        if idx == mid:
            parent.next = cur.next
            break
        cur = cur.next
        parent = parent.next
        idx += 1
    return dummy.next


# one pass
def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head
    dummy = ListNode(42, head)
    slow_par = dummy
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        slow_par = slow_par.next

    if fast and fast.next:
        slow = slow.next
        slow_par = slow_par.next
    slow_par.next = slow.next

    return dummy.next
