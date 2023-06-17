# https://leetcode.com/problems/make-array-strictly-increasing/description/
"""
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

Example 1:
Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].

Example 2:
Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].

Example 3:
Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.

Constraints:
1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
"""
from bisect import bisect_right
from collections import defaultdict
from math import inf


def make_array_increasing(arr1: list[int], arr2: list[int]) -> int:
    arr2.sort()
    n = len(arr2)
    dp = {-1: 0}

    for i in range(len(arr1)):
        new_dp = defaultdict(lambda: inf)
        for prev in dp:
            if arr1[i] > prev:
                new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
            idx = bisect_right(arr2, prev)
            if idx < n:
                new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])
        dp = new_dp

    return min(dp.values()) if dp else -1
