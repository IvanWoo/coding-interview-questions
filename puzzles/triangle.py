# https://leetcode.com/problems/triangle/
"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""

from copy import deepcopy

# space: O(n!)
def minimum_total(triangle: list[list[int]]) -> int:
    n = len(triangle)
    dp = deepcopy(triangle)
    for row in range(1, n):
        dp[row][0] += dp[row - 1][0]
        dp[row][-1] += dp[row - 1][-1]

    for row in range(1, n):
        for i in range(1, row):
            dp[row][i] += min(dp[row - 1][i], dp[row - 1][i - 1])
    return min(dp[-1])


# space: O(n)
def minimum_total(triangle: list[list[int]]) -> int:
    n = len(triangle)
    dp = [0] * n
    dp[0] = triangle[0][0]
    for row in range(1, n):
        new_dp = [0] * n
        new_dp[0] = triangle[row][0] + dp[0]
        for i in range(1, row):
            new_dp[i] = triangle[row][i] + min(dp[i], dp[i - 1])
        new_dp[row] = triangle[row][row] + dp[row - 1]
        dp = new_dp[:]
    return min(dp)


def minimum_total(triangle: list[list[int]]) -> int:
    n = len(triangle)
    dp = [0] * (n + 1)
    for row in triangle[::-1]:
        for i in range(len(row)):
            dp[i] = row[i] + min(dp[i], dp[i + 1])
    return dp[0]


if __name__ == "__main__":
    minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
