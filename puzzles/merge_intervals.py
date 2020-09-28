# https://leetcode.com/problems/merge-intervals/
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 0:
        return []
    ans = []
    for s, e in sorted(intervals):
        if not ans or s > ans[-1][1]:
            ans.append([s, e])
        else:
            ans[-1][1] = max(ans[-1][1], e)
    return ans


from collections import deque


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) == 0:
        return []
    sorted_intervals = deque(sorted(intervals))
    ans = []
    prev = sorted_intervals[0]
    while sorted_intervals:
        cur = sorted_intervals.popleft()
        if prev[1] >= cur[0]:
            prev = [prev[0], max(prev[1], cur[1])]
        else:
            ans.append(prev)
            prev = cur
    ans.append(prev)
    return ans
