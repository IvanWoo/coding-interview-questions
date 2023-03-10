# https://leetcode.com/problems/linked-list-random-node/description/
"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.


Example 1:
Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.


Constraints:
The number of nodes in the linked list will be in the range [1, 104].
-104 <= Node.val <= 104
At most 104 calls will be made to getRandom.


Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?
"""
from functools import partial
from random import randint
from typing import Optional

from puzzles.utils import ListNode


class Solution:
    def __init__(self, head: Optional[ListNode]):
        def get_n(head: Optional[ListNode]) -> None:
            if not head:
                return 0
            cur = head
            n = 0
            while cur:
                n += 1
                cur = cur.next
            return n

        self.head = head
        self.n = get_n(head)
        self.rnd = partial(randint, a=0, b=self.n - 1)

    def get_random(self) -> int:
        steps = self.rnd()
        cur = self.head
        while steps > 0:
            cur = cur.next
            steps -= 1
        return cur.val
