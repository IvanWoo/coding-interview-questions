# https://leetcode.com/problems/longest-increasing-subsequence/
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from bisect import bisect_left


def length_of_LIS(nums: list[int]) -> int:
    if not nums:
        return 0
    ans = 0
    dp = [0] * len(nums)

    for i in range(len(nums)):
        temp = -1
        for j in range(i):
            if nums[j] < nums[i]:
                temp = max(temp, dp[j])
        dp[i] = (temp + 1) if temp != -1 else 0
        ans = max(ans, dp[i])
    return ans + 1


# patience sorting
# O(n*logn)
def length_of_LIS(nums: list[int]) -> int:
    # bisect_left implementation
    def binary_search(sub, num):
        lo, hi = 0, len(sub) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if sub[mid] < num:
                lo = mid + 1
            elif sub[mid] > num:
                hi = mid - 1
            elif sub[mid] == num:
                hi = mid - 1
        return lo

    if not nums:
        return 0

    # sub[i]: the smallest ending number of a subsequence that has length i + 1
    sub = []

    for num in nums:
        i = bisect_left(sub, num)
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
    return len(sub)


# dp: O(n^2)
def length_of_LIS(nums: list[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    # dp[i] means ending at index i, what's the length of longest increasing subsequence
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


if __name__ == "__main__":
    length_of_LIS([7, 7, 7, 7, 7, 7, 7])
