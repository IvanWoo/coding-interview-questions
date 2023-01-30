# https://leetcode.com/problems/pascals-triangle/
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30
"""


def generate(num_rows: int) -> list[list[int]]:
    ans = []
    for n in range(num_rows + 1):
        ans.append([1] * n)

    for n in range(3, num_rows + 1):
        for c in range(1, n - 1):
            ans[n][c] = ans[n - 1][c - 1] + ans[n - 1][c]

    return ans[1:]


if __name__ == "__main__":
    generate(5)
