# https://leetcode.com/problems/132-pattern/
"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

Constraints:

n == nums.length
1 <= n <= 3 * 104
-109 <= nums[i] <= 109
"""
from typing import List


# O(n^2)
def find132pattern(nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n):
        _max = float("-inf")
        for j in range(i + 1, n):
            _max = max(_max, nums[j])
            if _max > nums[j] > nums[i]:
                return True
    return False


def find132pattern(nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False
    min_list = [0] * n
    min_list[0] = nums[0]
    for i in range(1, n):
        min_list[i] = min(min_list[i - 1], nums[i])

    stack = []

    for i in reversed(range(n)):
        if nums[i] > min_list[i]:
            while stack and stack[-1] <= min_list[i]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
    return False


def find132pattern(nums: List[int]) -> bool:
    stack = []
    s3 = float("-inf")
    for num in reversed(nums):
        if num < s3:
            return True
        while stack and stack[-1] < num:
            s3 = stack.pop()
        stack.append(num)
    return False


if __name__ == "__main__":
    find132pattern([3, 5, 0, 3, 4])
