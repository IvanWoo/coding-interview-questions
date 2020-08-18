# https://leetcode.com/problems/sort-colors/
# https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
from typing import List


def sort_colors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i, j, k = 0, 0, len(nums)
    while j < k:
        if nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            i += 1
        elif nums[j] == 2:
            k -= 1
            nums[j], nums[k] = nums[k], nums[j]
        else:
            j += 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
