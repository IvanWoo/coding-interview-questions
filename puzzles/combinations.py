# https://leetcode.com/problems/combinations/
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
from collections import deque
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    ans = deque()

    def backtrack(path):
        if len(path) == k:
            ans.append(path)
            return
        start = path[-1] if path else 1
        for i in range(start, n + 1):
            if i in path:
                continue
            backtrack(path + [i])

    backtrack([])
    return ans
