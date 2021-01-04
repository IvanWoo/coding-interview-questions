# https://leetcode.com/problems/contiguous-array/
"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
from typing import List

# O(n^2)
def find_max_length(nums: List[int]) -> int:
    n = len(nums)
    prefix_sum = [[0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        prefix_sum[i][0] += prefix_sum[i - 1][0] + (nums[i - 1] == 0)
        prefix_sum[i][1] += prefix_sum[i - 1][1] + (nums[i - 1] == 1)

    res = 0
    for i in range(n, 0, -1):
        for j in range(i):
            if (prefix_sum[i][0] - prefix_sum[j][0]) == (
                prefix_sum[i][1] - prefix_sum[j][1]
            ):
                res = max(res, i - j)
    return res


# O(n)
def find_max_length(nums: List[int]) -> int:
    n = len(nums)
    hashmap = dict()
    hashmap[0] = -1
    count, max_len = 0, 0
    for i in range(n):
        count += -1 if nums[i] == 0 else 1
        if count in hashmap:
            max_len = max(max_len, i - hashmap[count])
        else:
            hashmap[count] = i
    return max_len


if __name__ == "__main__":
    find_max_length([0, 1])
