# https://leetcode.com/problems/maximum-erasure-value/
"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""

from collections import defaultdict


# TLE: O(n^2)
def maximum_unique_subarray(nums: list[int]) -> int:
    def is_unique(window: dict[int, int]) -> bool:
        return all([v <= 1 for _, v in window.items()])

    def total(window: dict[int, int]) -> int:
        return sum([k for k, v in window.items() if v == 1])

    n = len(nums)
    lo, hi, res = 0, 0, 0
    window = defaultdict(int)
    while hi < n:
        n1 = nums[hi]
        hi += 1
        window[n1] += 1
        while not is_unique(window):
            n2 = nums[lo]
            lo += 1
            window[n2] -= 1
        res = max(res, total(window))
    return res


# sliding window
def maximum_unique_subarray(nums: list[int]) -> int:
    n = len(nums)
    lo, hi, res, total = 0, 0, 0, 0
    window = set()
    while hi < n:
        n1 = nums[hi]
        hi += 1
        while n1 in window:
            n2 = nums[lo]
            lo += 1
            window.remove(n2)
            total -= n2
        window.add(n1)
        total += n1
        res = max(res, total)
    return res


def maximum_unique_subarray(nums: list[int]) -> int:
    n = len(nums)
    lo, hi, res, total = 0, 0, 0, 0
    window = defaultdict(int)
    while hi < n:
        n1 = nums[hi]
        hi += 1
        window[n1] += 1
        total += n1
        while window[n1] > 1:
            n2 = nums[lo]
            lo += 1
            window[n2] -= 1
            total -= n2
        res = max(res, total)
    return res
