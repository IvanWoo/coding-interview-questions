# https://leetcode.com/problems/first-missing-positive/submissions/
"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.
"""
from typing import List

# cycle sort
def first_missing_positive(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        while 0 <= nums[i] - 1 < n and nums[nums[i] - 1] != nums[i]:
            # sequence matters
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
