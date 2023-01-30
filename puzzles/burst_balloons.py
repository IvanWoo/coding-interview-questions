# https://leetcode.com/problems/burst-balloons/
"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
from functools import lru_cache
from typing import List


# TLE: recursion
def max_coins(nums: List[int]) -> int:
    @lru_cache(None)
    def helper(nums):
        if not nums:
            return 0
        candidates = []
        n = len(nums)
        for i in range(n):
            left = nums[i - 1] if i >= 1 else 1
            right = nums[i + 1] if i <= n - 2 else 1
            candidates.append(left * nums[i] * right + helper(nums[:i] + nums[i + 1 :]))
        return max(candidates)

    return helper(tuple(nums))


# DP: O(n ^ 3)
def max_coins(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # at least we have three items
    for gap in range(2, n):
        for left in range(n - gap):
            cur = 0
            right = left + gap
            # i is the last ballon to be bursted
            for i in range(left + 1, right):
                cur = max(cur, dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right])
            dp[left][right] = cur
    return dp[0][n - 1]


if __name__ == "__main__":
    max_coins([3, 1, 5, 8])
