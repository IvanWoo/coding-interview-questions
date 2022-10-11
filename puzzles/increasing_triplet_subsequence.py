# https://leetcode.com/problems/increasing-triplet-subsequence/
"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 
Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
from math import inf
from bisect import bisect_left

# brute force
def increasing_triplet(nums: list[int]) -> bool:
    n = len(nums)
    for k in range(n):
        for j in range(k):
            for i in range(j):
                if nums[i] < nums[j] < nums[k]:
                    return True
    return False


# O(n)
def increasing_triplet(nums: list[int]) -> bool:
    first = second = inf
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False


# similar like https://leetcode.com/problems/longest-increasing-subsequence/
# O(n*logn)
def increasing_triplet(nums: list[int]) -> bool:
    curr = []
    for n in nums:
        i = bisect_left(curr, n)
        if i == len(curr):
            curr.append(n)
        else:
            curr[i] = n
        if len(curr) >= 3:
            return True
    return False
