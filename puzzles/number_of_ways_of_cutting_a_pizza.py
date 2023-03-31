# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/
"""
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts.

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

Example 2:
Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:
Input: pizza = ["A..","A..","..."], k = 1
Output: 1

Constraints:
1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""
from functools import cache


def ways(pizza: list[str], k: int) -> int:
    MOD = 10**9 + 7
    rows, cols = len(pizza), len(pizza[0])
    suffix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            suffix_sum[i][j] = (
                suffix_sum[i + 1][j]
                + suffix_sum[i][j + 1]
                - suffix_sum[i + 1][j + 1]
                + (pizza[i][j] == "A")
            )

    @cache
    def dp(x, y, cuts) -> int:
        if cuts == 0:
            return 1

        count = 0
        for i in range(x, rows - 1):
            if suffix_sum[i + 1][y] and suffix_sum[x][y] - suffix_sum[i + 1][y]:
                count += dp(i + 1, y, cuts - 1)

        for j in range(y, cols - 1):
            if suffix_sum[x][j + 1] and suffix_sum[x][y] - suffix_sum[x][j + 1]:
                count += dp(x, j + 1, cuts - 1)

        return count % MOD

    return dp(0, 0, k - 1)
