# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

from collections import deque
from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    n = len(nums)
    return list(set(range(n)) - set(nums))


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    for num in nums:
        num = abs(num)
        if nums[num - 1] > 0:
            nums[num - 1] *= -1
    ans = deque()
    for i, num in enumerate(nums):
        if num > 0:
            ans.append(i + 1)
    return list(ans)
