# https://leetcode.com/problems/find-the-duplicate-number/
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""
from typing import List


def find_duplicate(nums: List[int]) -> int:
    # Pigeonhole Principle
    left, right = 1, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        count = 0
        for v in nums:
            if v <= mid:
                count += 1

        if count <= mid:
            left = mid + 1
        else:
            right = mid
    return left


def find_duplicate(nums: List[int]) -> int:
    # fast slow pointers
    # standard way to find a cycle in the linked list
    fast = slow = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast
