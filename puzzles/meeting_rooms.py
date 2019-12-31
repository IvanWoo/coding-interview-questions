"""
252.Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true
"""

from typing import List


def can_attend(intervals: List[List[int]]) -> bool:
    starts = sorted([x[0] for x in intervals])
    ends = sorted([x[1] for x in intervals])
    for i in range(len(intervals) - 1):
        if starts[i + 1] < ends[i]:
            return False
    return True


"""
253.Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
"""


def minimum_rooms(intervals: List[List[int]]) -> int:
    if not intervals or not intervals[0]:
        return 0
    starts = sorted([x[0] for x in intervals])
    ends = sorted([x[1] for x in intervals])
    ans = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        temp = 0
        while i < len(intervals) and starts[i] < ends[j]:
            i += 1
            temp += 1
        ans = max(temp, ans)
        j += 1
    return ans
