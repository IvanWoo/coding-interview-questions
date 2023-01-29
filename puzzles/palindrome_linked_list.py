# https://leetcode.com/problems/palindrome-linked-list/
"""
Given the head of a singly linked list, return true if it is a palindrome.


Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?
"""
from typing import Optional

from puzzles.utils import ListNode


def is_palindrome(head: Optional[ListNode]) -> bool:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]


def is_palindrome(head: Optional[ListNode]) -> bool:
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        rev = rev.next
        slow = slow.next
    return rev is None
