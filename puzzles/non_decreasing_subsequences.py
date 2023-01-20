# https://leetcode.com/problems/non-decreasing-subsequences/description/
"""
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]
 
Constraints:
1 <= nums.length <= 15
-100 <= nums[i] <= 100
"""


def find_subsequences(nums: list[int]) -> list[list[int]]:
    def dfs(idx, path):
        nonlocal ans
        if len(path) > 1:
            ans.add(path)

        for nxt in range(idx + 1, n):
            if nums[nxt] >= nums[idx]:
                dfs(nxt, (*path, nums[nxt]))

    n = len(nums)
    ans = set()
    for i in range(n - 1):
        dfs(i, (nums[i],))
    return [list(x) for x in ans]
