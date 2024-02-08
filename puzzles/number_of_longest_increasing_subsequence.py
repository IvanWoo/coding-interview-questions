# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
"""
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

Constraints:
1 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""
from typing import List


def find_number_of_LIS(nums: List[int]) -> int:
    def backtrack(idx, l):
        nonlocal max_len, res
        if l > max_len:
            max_len = l
            res = 1
        elif l == max_len:
            res += 1
        for i in range(idx, len(nums)):
            if not visited[i] and nums[i] > nums[idx]:
                visited[i] = True
                backtrack(i, l + 1)
                visited[i] = False

    max_len = float("-inf")
    res = 0
    visited = [False] * len(nums)
    for i in range(len(nums)):
        backtrack(i, 1)
    return res


def find_number_of_LIS(nums: List[int]) -> int:
    n = len(nums)
    dp_l = [1] * n
    dp_c = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] <= nums[j]:
                continue
            if dp_l[j] + 1 > dp_l[i]:
                dp_l[i] = dp_l[j] + 1
                dp_c[i] = dp_c[j]
            elif dp_l[j] + 1 == dp_l[i]:
                dp_c[i] += dp_c[j]
    max_l = max(dp_l)
    count = 0
    for l, c in zip(dp_l, dp_c):
        if l == max_l:
            count += c
    return count


if __name__ == "__main__":
    print(find_number_of_LIS([1, 2, 4, 3, 5, 4, 7, 2]))
