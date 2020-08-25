# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
 
Constraints:

0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

from typing import List
from collections import deque


def count_smaller(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n

    def merge(arr1, arr2):
        ans = deque()
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i][1] > arr2[j][1]:
                ans.append(arr1[i])
                res[arr1[i][0]] += len(arr2) - j
                i += 1
            else:
                ans.append(arr2[j])
                j += 1

        ans.extend(arr1[i:] or arr2[j:])
        return list(ans)

    def sort(nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = sort(nums[:mid])
        right = sort(nums[mid:])

        return merge(left, right)

    sort(list(enumerate(nums)))
    return res
