# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].

Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""


def find_length(A: list[int], B: list[int]) -> int:
    row, col = len(A), len(B)
    dp = [[0] * (col + 1) for _ in range(row + 1)]
    for r in reversed(range(row)):
        for c in reversed(range(col)):
            if A[r] == B[c]:
                dp[r][c] = dp[r + 1][c + 1] + 1
    return max(max(r) for r in dp)


if __name__ == "__main__":
    find_length([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
