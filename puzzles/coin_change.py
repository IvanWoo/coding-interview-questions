# https://leetcode.com/problems/coin-change/
"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0


Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
from functools import cache


def coin_change(coins: list[int], amount: int) -> int:
    @cache
    def helper(coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        res = float("inf")
        for c in coins:
            sub_question = helper(coins, amount - c)
            if sub_question == -1:
                continue
            res = min(res, sub_question + 1)
        return res if res != float("inf") else -1

    return helper(tuple(coins), amount)


def coin_change(coins: list[int], amount: int) -> int:
    n = amount + 1
    dp = [n] * n

    dp[0] = 0
    for i in range(n):
        for coin in coins:
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != n else -1


# top to bottom
def coin_change(coins: list[int], amount: int) -> int:
    @cache
    def helper(amount):
        if amount < 0:
            return float("inf")
        if amount == 0:
            return 0

        return 1 + min([helper(amount - c) for c in coins])

    res = helper(amount)
    if res == float("inf"):
        return -1
    return res
