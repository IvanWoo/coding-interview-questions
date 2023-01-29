# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
from functools import cache
from math import inf


# TLE
def max_profit(prices: list[int]) -> int:
    @cache
    def helper(idx, is_hold, profit):
        if idx >= n:
            return profit
        cur_price = prices[idx]
        res = []
        if not is_hold:
            # buy
            res.append(helper(idx + 1, True, profit - cur_price))
        else:
            # sell
            res.append(helper(idx + 2, False, profit + cur_price))
        # rest
        res.append(helper(idx + 1, is_hold, profit))
        return max(res)

    n = len(prices)
    return helper(0, False, 0)


def max_profit(prices: list[int]) -> int:
    n = len(prices)
    # (rest, hold)
    dp = [[0] * 2 for _ in range(n + 1)]

    dp[0][1] = -inf

    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
        dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1])

    return dp[n][0]
