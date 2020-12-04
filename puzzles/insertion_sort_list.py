# https://leetcode.com/problems/insertion-sort-list/
"""
Sort a linked list using insertion sort.

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
from puzzles.utils import ListNode


def insertion_sort_list(head: ListNode) -> ListNode:
    def insert(original, node):
        cur = original
        while cur:
            nxt = cur.next
            if not nxt:
                cur.next = node
                break
            if nxt.val >= node.val:
                cur.next, node.next = node, nxt
                break
            cur = nxt

    dummy = ListNode(None)

    cur = head
    while cur:
        nxt = cur.next
        cur.next = None
        insert(dummy, cur)
        cur = nxt

    return dummy.next


if __name__ == "__main__":
    lns = {x: ListNode(x) for x in range(1, 6)}
    lns[1].next = lns[4]
    lns[4].next = lns[3]
    lns[3].next = lns[2]
    lns[2].next = lns[5]

    print(insertion_sort_list(lns[4]))