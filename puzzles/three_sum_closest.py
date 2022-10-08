# https://leetcode.com/problems/3sum-closest/
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
from math import inf


# brute force
def three_sum_closest(nums: list[int], target: int) -> int:
    res = inf
    n = len(nums)
    for i in range(n):
        for j in range(i):
            for k in range(j):
                temp = nums[i] + nums[j] + nums[k]
                if abs(temp - target) < abs(res - target):
                    res = temp
    return res


def three_sum_closest(nums: list[int], target: int) -> int:
    nums = sorted(nums)
    res = None
    distance = inf
    n = len(nums)
    for i in range(n):
        if i and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            new_distance = total - target
            if abs(new_distance) < distance:
                res = total
                distance = abs(new_distance)

            if new_distance < 0:
                lo += 1
            elif new_distance > 0:
                hi -= 1
            else:
                return res
    return res
