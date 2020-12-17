# https://leetcode.com/problems/wiggle-subsequence/
"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:
Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Example 2:
Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Example 3:
Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""
from typing import List

# brute force: O(2^n), TLE
def wiggle_max_length(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)

    def helper(i, diff, length):
        nonlocal res
        if i != n - 1:
            for j in range(i + 1, n):
                new_diff = nums[j] - nums[i]
                if new_diff == 0:
                    continue
                if diff is None or new_diff * diff < 0:
                    helper(j, new_diff, length + 1)
        res = max(res, length)

    res = 0
    helper(0, None, 1)
    return res


# dp: O(n^2)
def wiggle_max_length(nums: List[int]) -> int:
    """
       1      7      4      9      2     5
    (1, 1) (1, 2) (3, 2) (1, 4) (5, 2) (5, 6)
    """
    if not nums:
        return 0
    n = len(nums)
    dp = [None] * n
    dp[0] = (1, 1)
    for i in range(1, n):
        neg, pos = 1, 1
        for j in range(i):
            if nums[i] - nums[j] < 0:
                neg = max(neg, dp[j][1] + 1)
            elif nums[i] - nums[j] > 0:
                pos = max(pos, dp[j][0] + 1)
        dp[i] = (neg, pos)
    return max(dp[-1])


# linear dp: O(n)
def wiggle_max_length(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    up = [0] * n
    down = [0] * n
    up[0], down[0] = 1, 1
    for i in range(1, n):
        if nums[i] - nums[i - 1] > 0:
            up[i] = down[i - 1] + 1
            down[i] = down[i - 1]
        elif nums[i] - nums[i - 1] < 0:
            down[i] = up[i - 1] + 1
            up[i] = up[i - 1]
        else:
            down[i] = down[i - 1]
            up[i] = up[i - 1]
    return max(up[-1], down[-1])


# space-optimized dp: O(n)
def wiggle_max_length(nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    up, down = 1, 1
    for i in range(1, n):
        if nums[i] - nums[i - 1] > 0:
            up = down + 1
        elif nums[i] - nums[i - 1] < 0:
            down = up + 1
    return max(up, down)


# greedy: O(n)
def wiggle_max_length(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        return n
    prev_diff = nums[1] - nums[0]
    count = 2 if prev_diff != 0 else 1
    for i in range(2, n):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
            count += 1
            prev_diff = diff
    return count


if __name__ == "__main__":
    # fmt: off
    wiggle_max_length([33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9]) 
    # fmt: on
