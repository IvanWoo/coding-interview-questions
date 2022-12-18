# https://leetcode.com/problems/daily-temperatures/
"""
Given a list of daily temperatures temperatures, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
from math import inf


def daily_temperatures(temperatures: list[int]) -> list[int]:
    futures = dict()
    n = len(temperatures)
    res = [0] * n
    for i in reversed(range(n)):
        t = temperatures[i]
        futures[t] = i
        latest = inf
        for k, v in futures.items():
            if k > t:
                latest = min(latest, v)
        if latest != inf:
            res[i] = latest - i
    return res


def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    ans = [0] * n
    stack = []
    for i in reversed(range(n)):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        ans[i] = stack[-1] - i if stack else 0
        stack.append(i)
    return ans


# monotonic stack: O(n)
def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    ans = [0] * n
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            prev_idx = stack.pop()
            ans[prev_idx] = i - prev_idx
        stack.append(i)
    return ans


if __name__ == "__main__":
    daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])
