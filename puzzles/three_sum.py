# https://leetcode.com/problems/3sum/
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from collections import Counter


# O(n^2)
def three_sum(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    res = []
    n = len(nums)
    for i in range(n):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total > 0:
                hi -= 1
            elif total < 0:
                lo += 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                while lo < hi and nums[lo] == nums[lo + 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi - 1]:
                    hi -= 1
                lo += 1
                hi -= 1
    return res


def two_sum(counter, target):
    res = []
    for num in counter:
        if counter[num] == 0:
            continue
        counter[num] -= 1
        left = target - num
        if left in counter and num <= left and counter[left] >= 1:
            res.append([num, left])
        counter[num] += 1
    return res


def three_sum(nums: list[int]) -> list[list[int]]:
    counter = Counter(nums)
    res = []
    for num in nums:
        counter[num] -= 1
        ts_res = two_sum(counter, -num)
        if ts_res:
            temp = [[num] + r for r in ts_res if num <= r[0]]
            for t in temp:
                if t not in res:
                    res.append(t)
        counter[num] += 1
    return res


if __name__ == "__main__":
    three_sum([1, 2, -2, -1])
