# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from math import inf


def max_profit(k: int, prices: list[int]) -> int:
    # dp[i][j][0 or 1]: the profit at i-th day, allow most j txn, hold(1) or no stock(0)
    n = len(prices)
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

    # don't allow any txn, so no profit
    for i in range(n + 1):
        dp[i][0][1] = -inf
    # not start yet, cannot hold stock
    for j in range(k + 1):
        dp[0][j][1] = -inf

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
            dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
    return dp[n][k][0]
