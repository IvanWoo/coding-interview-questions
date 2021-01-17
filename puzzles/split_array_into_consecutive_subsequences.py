# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
"""
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.


Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:
Input: [1,2,3,4,4,5]
Output: False

Constraints:
1 <= nums.length <= 10000
"""
from typing import List
from collections import Counter, defaultdict


# TLE: O(N^2)
def is_possible(nums: List[int]) -> bool:
    n = len(nums)
    res = [None] * (n // 3 + 1)
    counter = 0
    i = 0
    while i < n and counter < len(res):
        allocated = False
        for j in range(counter):
            if res[j][1] + 1 == nums[i] and res[j][0] < 3:
                res[j][0] += 1
                res[j][1] = nums[i]
                allocated = True
                break
        if not allocated:
            for j in range(counter):
                if res[j][1] + 1 == nums[i]:
                    res[j][0] += 1
                    res[j][1] = nums[i]
                    allocated = True
                    break
        if not allocated:
            res[counter] = [1, nums[i]]
            counter += 1
        i += 1
    if i != n:
        return False
    return all([x[0] >= 3 for x in res if x])


# O(N)
def is_possible(nums: List[int]) -> bool:
    left = Counter(nums)
    end = defaultdict(int)
    for val in nums:
        if not left[val]:
            continue
        left[val] -= 1
        if end[val - 1] > 0:
            end[val - 1] -= 1
            end[val] += 1
        elif left[val + 1] and left[val + 2]:
            left[val + 1] -= 1
            left[val + 2] -= 1
            end[val + 2] += 1
        else:
            return False
    return True


if __name__ == "__main__":
    is_possible([1, 2, 3, 3, 4, 4, 5, 5])
