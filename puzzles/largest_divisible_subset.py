# https://leetcode.com/problems/largest-divisible-subset/
"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]
"""
from typing import List

# dp: O(n^2)
def largest_divisible_subset(nums: List[int]) -> List[int]:
    n = len(nums)
    if n == 0:
        return []
    sorted_nums = sorted(nums)
    dp = [[sorted_nums[i]] for i in range(n)]
    res = [sorted_nums[0]]
    for i in range(1, n):
        for j in range(i):
            if sorted_nums[i] % sorted_nums[j] == 0:
                t = dp[j] + [sorted_nums[i]]
                if len(t) > len(dp[i]):
                    dp[i] = t[:]
                if len(dp[i]) > len(res):
                    res = dp[i]
    return res


if __name__ == "__main__":
    largest_divisible_subset([2, 3, 4, 9, 8])
