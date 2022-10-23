# https://leetcode.com/problems/set-mismatch/
"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]
 
Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104
"""
from collections import Counter


def find_error_nums(nums: list[int]) -> list[int]:
    n = len(nums)
    c = Counter(nums)
    dup, mis = None, None
    for i in range(1, n + 1):
        # __missing__ for Counter
        # https://github.com/python/cpython/blob/f58631be1148ee5436bb71d175d3993e3e6b4e1e/Lib/collections/__init__.py#L599-L602
        if c[i] == 0:
            mis = i
        elif c[i] == 2:
            dup = i
    return [dup, mis]
