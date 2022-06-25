# https://leetcode.com/problems/non-decreasing-array/
"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:
n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
"""


# brute force: O(n^2)
def check_possibility(nums: list[int]) -> bool:
    def is_valid(nums: list[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                return False
        return True

    for i in range(len(nums)):
        if is_valid(nums[:i] + nums[i + 1 :]):
            return True
    return False


def check_possibility(nums: list[int]) -> bool:
    n = len(nums)
    count = 0

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            if count:
                return False
            count += 1
            if i >= 2 and nums[i - 2] > nums[i]:
                nums[i] = nums[i - 1]
            nums[i - 1] = nums[i]
    return True


if __name__ == "__main__":
    check_possibility([-1, 4, 2, 3])
