# https://leetcode.com/problems/my-calendar-iii/
"""
A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.


Example 1:
Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3


Constraints:
0 <= start < end <= 109
At most 400 calls will be made to book.
"""
from collections import defaultdict

from sortedcontainers import SortedDict


# sweep line algorithm
class MyCalendarThree:
    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = res = 0
        for delta in self.diff.values():
            cur += delta
            res = max(res, cur)
        return res


# segment tree
class MyCalendarThree:
    def __init__(self):
        self.vals = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start: int, end: int, left: int = 0, right: int = 10**9, idx: int = 1) -> None:
        if start > right or end < left:
            return

        if start <= left <= right <= end:
            self.vals[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (left + right) // 2
            self.update(start, end, left, mid, idx * 2)
            self.update(start, end, mid + 1, right, idx * 2 + 1)
            self.vals[idx] = self.lazy[idx] + max(self.vals[idx * 2], self.vals[idx * 2 + 1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1)
        return self.vals[1]
