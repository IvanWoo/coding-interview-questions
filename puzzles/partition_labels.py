# https://leetcode.com/problems/partition-labels/
"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""

from collections import defaultdict
from dataclasses import dataclass
from typing import List


@dataclass
class Interval:
    start: float = float("inf")
    end: float = float("-inf")


def partition_labels(S: str) -> List[int]:
    ans = []
    intervals = defaultdict(Interval)
    for i, s in enumerate(S):
        intervals[s].start = min(intervals[s].start, i)
        intervals[s].end = max(intervals[s].end, i)
    its = sorted(intervals.values(), key=lambda x: x.start)

    start, end = float("inf"), float("-inf")
    for it in its:
        if it.start > abs(end):
            ans.append(end - start + 1)
            start, end = float("inf"), float("-inf")
        start = min(it.start, start)
        end = max(it.end, end)
    ans.append(end - start + 1)
    return ans


def partition_labels(S: str) -> List[int]:
    last = {c: i for i, c in enumerate(S)}
    ans = []
    start = end = 0
    for i, c in enumerate(S):
        end = max(end, last[c])
        if i == end:
            ans.append(end - start + 1)
            start = i + 1
    return ans
