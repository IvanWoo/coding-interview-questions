# https://leetcode.com/problems/increasing-subsequences/
"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 
Constraints:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""
from typing import List


def find_subsequences(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = set()

    def helper(i, seq):
        if len(seq) >= 2:
            ans.add(tuple(seq))
        for j in range(i + 1, n):
            if not seq:
                helper(j, [nums[j]])
            elif seq[-1] <= nums[j]:
                helper(j, seq + [nums[j]])

    helper(-1, [])
    return [list(x) for x in ans]
