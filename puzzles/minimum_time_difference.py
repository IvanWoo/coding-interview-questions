# https://leetcode.com/problems/minimum-time-difference/
"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""
from typing import List


def find_min_difference(timePoints: List[str]) -> int:
    def parse(tp):
        h, m = tp.split(":")
        return int(h) * 60 + int(m)

    n = len(timePoints)
    if n <= 1:
        return
    tps = sorted([parse(tp) for tp in timePoints])
    res = float("inf")
    for i in range(n):
        res = min(
            res,
            abs(tps[i] - tps[i - 1]),
            24 * 60 - abs(tps[i] - tps[i - 1]),
        )
    return res


if __name__ == "__main__":
    find_min_difference(["23:59", "00:00"])
