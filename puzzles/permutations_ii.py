# https://leetcode.com/problems/permutations-ii/
"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from collections import deque, Counter


def permute_unique(nums: list[int]) -> list[list[int]]:
    def backtrack():
        nonlocal res, path, visited
        if all(visited):
            res.append(tuple(path))
            return

        for i, v in enumerate(visited):
            if v:
                continue
            path.append(nums[i])
            visited[i] = True
            backtrack()
            path.pop()
            visited[i] = False
        return

    n = len(nums)
    res = []
    visited = [False] * n
    path = []
    backtrack()
    return [list(x) for x in set(res)]


def permute_unique(nums: list[int]) -> list[list[int]]:
    def backtrack(path, counter):
        nonlocal res
        if len(path) == len(nums):
            res.append(path[:])
            return
        for k, v in counter.items():
            if v > 0:
                path.append(k)
                counter[k] -= 1
                backtrack(path, counter)
                path.pop()
                counter[k] += 1

    res = deque()
    backtrack([], Counter(nums))
    return res
