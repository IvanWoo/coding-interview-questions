# https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

from typing import List


def find_duplicates(nums: List[int]) -> List[int]:
    res = []
    for i in nums:
        if nums[abs(i) - 1] < 0:
            res.append(abs(i))
        else:
            nums[abs(i) - 1] *= -1
    return res
