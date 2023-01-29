# https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""
from heapq import heappop, heappush


def find_kth_largest(nums: list[int], k: int) -> int:
    nums.sort()
    return nums[-k]


def find_kth_largest(nums: list[int], k: int) -> int:
    pq = []
    for num in nums:
        heappush(pq, num)
        if len(pq) > k:
            heappop(pq)
    return heappop(pq)


if __name__ == "__main__":
    find_kth_largest([3, 2, 1, 5, 6, 4], 1)
