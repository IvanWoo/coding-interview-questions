# https://leetcode.com/problems/degree-of-an-array/
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:

Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""
from collections import Counter
from typing import List


def get_len(nums: List[int], item: int) -> int:
    return len(nums) - nums[::-1].index(item) - nums.index(item)


def find_shortest_sub_array(nums: List[int]) -> int:
    ct = Counter(nums)
    max_f = -1
    min_l = float("inf")
    for item, f in ct.most_common():
        if f >= max_f:
            max_f = f
            l = get_len(nums, item)
            if l < min_l:
                min_l = l
    return min_l


def find_shortest_sub_array(nums: List[int]) -> int:
    first, count, res, degree = {}, {}, 0, 0
    for i, num in enumerate(nums):
        first.setdefault(num, i)
        count[num] = count.get(num, 0) + 1
        if count[num] > degree:
            degree = count[num]
            res = i - first[num] + 1
        elif count[num] == degree:
            res = min(res, i - first[num] + 1)
    return res
