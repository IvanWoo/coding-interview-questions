# https://leetcode.com/problems/coin-change-2/
"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10] 
Output: 1
 
Note:
You can assume that
0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
"""
from typing import List
from functools import lru_cache

# TLE
def change(amount: int, coins: List[int]) -> int:
    def helper(total, i):
        nonlocal res
        if total < 0:
            return
        elif total == 0:
            res += 1
            return
        for j in range(i, len(coins)):
            helper(total - coins[j], j)

    coins = sorted(coins, reverse=True)
    res = 0
    helper(amount, 0)
    return res


def change(amount: int, coins: List[int]) -> int:
    @lru_cache(None)
    def helper(total, i):
        if total < 0:
            return 0
        elif total == 0:
            return 1
        res = 0
        for j in range(i, len(coins)):
            res += helper(total - coins[j], j)
        return res

    coins = sorted(coins, reverse=True)
    return helper(amount, 0)
