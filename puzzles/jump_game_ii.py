# https://leetcode.com/problems/jump-game_ii/
"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.


Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""

from typing import List


def jump_game(nums: List[int]) -> bool:
    n = len(nums)
    jumps, cur_max, next_max = 0, 0, 0
    for i in range(n - 1):
        next_max = max(next_max, i + nums[i])
        if i == cur_max:
            jumps += 1
            cur_max = next_max
        if cur_max >= n - 1:
            break
    return jumps
