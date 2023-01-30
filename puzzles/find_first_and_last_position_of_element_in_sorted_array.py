# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]


Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from bisect import bisect_left, bisect_right


def bisect_left(a, x):
    n = len(a)
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_right(a, x):
    n = len(a)
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def search_range(nums: list[int], target: int) -> list[int]:
    l = bisect_left(nums, target)
    if l >= len(nums) or nums[l] != target:
        return [-1, -1]
    r = bisect_right(nums, target) - 1
    return [l, r]
