# https://leetcode.com/problems/subarray-sum-equals-k/
"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
from collections import defaultdict
from typing import List


# prefix sum
# O(n^2)
def subarray_sum(nums: List[int], k: int) -> int:
    n = len(nums)
    pre_sum = [0] * (n + 1)

    for i in range(n):
        pre_sum[i + 1] = pre_sum[i] + nums[i]

    ans = 0
    for i in range(1, n + 1):
        for j in range(i):
            if pre_sum[i] - pre_sum[j] == k:
                ans += 1
    return ans


# O(n)
def subarray_sum(nums: List[int], k: int) -> int:
    n = len(nums)
    sums = 0
    count = 0

    hashmap = defaultdict(int)
    hashmap[0] = 1

    for i in range(n):
        sums += nums[i]
        count += hashmap[sums - k]
        hashmap[sums] += 1
    return count


if __name__ == "__main__":
    subarray_sum([1, 2, 1, 3], 3)
