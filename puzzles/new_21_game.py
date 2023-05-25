# https://leetcode.com/problems/new-21-game/description/
"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, max_pts], where max_pts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

Example 1:
Input: n = 10, k = 1, max_pts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.

Example 2:
Input: n = 6, k = 1, max_pts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.

Example 3:
Input: n = 21, k = 17, max_pts = 10
Output: 0.73278


Constraints:
0 <= k <= n <= 104
1 <= max_pts <= 104
"""
from functools import cache
from random import randint


# brute force: TLE
def new_21_game(n: int, k: int, max_pts: int) -> float:
    total = int(1e4)
    count = 0
    for _ in range(total):
        pts = 0
        while pts < k:
            pts += randint(1, max_pts)
        if pts <= n:
            count += 1
    return count / total


# TLE
def new_21_game(n: int, k: int, max_pts: int) -> float:
    dp = [0.0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for pt in range(1, 1 + max_pts):
            if 0 <= i - pt < k:
                dp[i] += dp[i - pt] / max_pts
    return sum(dp[k:])


def new_21_game(n: int, k: int, max_pts: int) -> float:
    dp = [0.0] * (n + 1)
    dp[0] = 1
    s = 1 if k > 0 else 0
    for i in range(1, n + 1):
        dp[i] = s / max_pts
        if i < k:
            s += dp[i]
        if 0 <= i - max_pts < k:
            s -= dp[i - max_pts]
    return sum(dp[k:])
