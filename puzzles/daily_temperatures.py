# https://leetcode.com/problems/daily-temperatures/
"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

from typing import List


def daily_temperatures(T: List[int]) -> List[int]:
    n = len(T)
    ans = [0] * n
    stack = []
    for i in reversed(range(n)):
        while stack and T[stack[-1]] <= T[i]:
            stack.pop()
        ans[i] = stack[-1] - i if stack else 0
        stack.append(i)
    return ans


def daily_temperatures(T: List[int]) -> List[int]:
    n = len(T)
    ans = [0] * n
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            prev_idx = stack.pop()
            ans[prev_idx] = i - prev_idx
        stack.append(i)
    return ans


if __name__ == "__main__":
    daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
