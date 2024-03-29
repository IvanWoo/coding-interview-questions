# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
121. Best Time to Buy and Sell Stock
Easy

14453

488

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from math import inf


def max_profit(prices: list[int]) -> int:
    profit = 0
    min_p = inf
    for p in prices:
        min_p = min(min_p, p)
        profit = max(profit, p - min_p)
    return profit


def max_profit(prices: list[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    for i in range(n):
        if i - 1 == -1:
            dp[i][0] = 0
            dp[i][1] = -prices[i]
            continue
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], -prices[i])
    return dp[-1][0]


# based on the template
def max_profit(prices: list[int]) -> int:
    n = len(prices)
    k = 1
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


# states compaction
def max_profit(prices: list[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n + 1)]

    # don't allow any txn, so no profit
    for i in range(n + 1):
        dp[i][1] = -inf

    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
        dp[i][1] = max(dp[i - 1][1], -prices[i - 1])
    return dp[n][0]
