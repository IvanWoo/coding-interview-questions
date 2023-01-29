# https://leetcode.com/problems/single-element-in-a-sorted-array/
"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""
from typing import List


# O(N)
def single_non_duplicate(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res ^= n
    return res


# O(logN)
def single_non_duplicate(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = 2 * ((lo + hi) // 4)
        if nums[mid] == nums[mid + 1]:
            lo = mid + 2
        else:
            hi = mid
    return nums[lo]


if __name__ == "__main__":
    single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
