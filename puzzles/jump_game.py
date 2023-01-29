# https://leetcode.com/problems/jump-game/
"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
from collections import deque
from functools import cache


# TLE
def jump_game(nums: list[int]) -> bool:
    n = len(nums)

    @cache()
    def dfs(index):
        if index >= n - 1:
            return True
        return any([dfs(index + i) for i in range(nums[index], 0, -1)])

    return dfs(0)


# TLE: bfs
def jump_game(nums: list[int]) -> bool:
    n = len(nums)
    q = deque([0])
    visited = set([0])
    while q:
        cur = q.popleft()
        if cur == n - 1:
            return True
        for d in reversed(range(1, nums[cur] + 1)):
            nxt = cur + d
            if nxt < n and nxt not in visited:
                q.append(nxt)
                visited.add(nxt)
    return False


def jump_game(nums: list[int]) -> bool:
    n = len(nums)
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        if dp[-1]:
            return True
        if not dp[i]:
            return False
        for j in range(nums[i] + 1):
            if i + j < n:
                dp[i + j] = 1
    return False


def jump_game(nums: list[int]) -> bool:
    i = 0
    n = len(nums)
    reach = 0
    while i < n and i <= reach:
        reach = max(reach, i + nums[i])
        if reach >= n - 1:
            return True
        i += 1
    return False
