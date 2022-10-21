# https://leetcode.com/problems/contains-duplicate-ii/
"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from collections import deque

# TLE: O(nk)
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    if k == 0:
        return False
    q = deque()
    for num in nums:
        if len(q) > k:
            q.popleft()
        if num in q:
            return True
        q.append(num)
    return False


# O(n)
def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    n = len(nums)
    window = set()
    first, last = 0, 0
    for _ in range(min(k + 1, n)):
        val = nums[last]
        if val in window:
            return True
        window.add(val)
        last += 1

    for _ in range(n - last):
        window.remove(nums[first])
        if nums[last] in window:
            return True
        window.add(nums[last])
        first += 1
        last += 1

    return False


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    dic = {}
    for i, num in enumerate(nums):
        if num in dic and i - dic[num] <= k:
            return True
        dic[num] = i
    return False


if __name__ == "__main__":
    contains_nearby_duplicate([1, 0, 1, 1], 1)
