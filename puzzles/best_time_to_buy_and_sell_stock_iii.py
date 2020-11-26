# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:
Input: prices = [1]
Output: 0

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
"""
from typing import List


# O(n^2): TLE
def max_profit(prices: List[int]) -> int:
    def max_profit_one(prices):
        res = 0
        min_price = float("inf")
        for p in prices:
            min_price = min(min_price, p)
            res = max(res, p - min_price)
        return res

    res = 0
    for i in range(len(prices)):
        left = max_profit_one(prices[:i])
        right = max_profit_one(prices[i:])
        res = max(res, left + right)
    return res


# dp
def max_profit(prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0

    p1 = [0] * n
    res = 0
    min_price = float("inf")
    for i in range(n):
        p = prices[i]
        min_price = min(min_price, p)
        res = max(res, p - min_price)
        p1[i] = res

    p2 = [0] * n
    res = 0
    max_price = float("-inf")
    for i in reversed(range(n)):
        p = prices[i]
        max_price = max(max_price, p)
        res = max(res, max_price - p)
        p2[i] = res

    return max(p1[i] + p2[i] for i in range(n))


if __name__ == "__main__":
    max_profit([1, 2, 3, 4, 5])
