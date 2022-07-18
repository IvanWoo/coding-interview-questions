# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
"""
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.


Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0
 

Constraints:
1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""
from collections import defaultdict

# brute force: O(n^6)
def num_submatrix_sum_target(matrix: list[list[int]], target: int) -> int:
    rows, cols = len(matrix), len(matrix[0])
    ans = 0
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    val = 0
                    for r in range(r1, r2):
                        for c in range(c1, c2):
                            val += matrix[r][c]
                    if val == target:
                        ans += 1
    return ans


def num_submatrix_sum_target(matrix: list[list[int]], target: int) -> int:
    rows, cols = len(matrix), len(matrix[0])
    prefix = defaultdict(int)
    for r in range(rows):
        for c in range(cols):
            prefix[r, c] = (
                prefix[r - 1, c]
                + prefix[r, c - 1]
                - prefix[r - 1, c - 1]
                + matrix[r][c]
            )

    ans = 0
    for r1 in range(-1, rows):
        for r2 in range(r1 + 1, rows):
            counts = defaultdict(int)
            for c in range(-1, cols):
                total = prefix[r2, c] - prefix[r1, c]
                offset = total - target
                ans += counts[offset]
                counts[total] += 1
    return ans


if __name__ == "__main__":
    num_submatrix_sum_target([[1, -1], [-1, 1]], 0)
