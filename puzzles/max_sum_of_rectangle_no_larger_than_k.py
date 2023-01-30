# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
"""
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
It is guaranteed that there will be a rectangle with a sum no larger than k.


Example 1:
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).\

Example 2:
Input: matrix = [[2,2,-1]], k = 3
Output: 3

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105

Follow up: What if the number of rows is much larger than the number of columns?
"""
import bisect
from copy import deepcopy
from math import inf


# prefix sum: TLE
# O(m^2*n^2)
def max_sum_submatrix(matrix: list[list[int]], k: int) -> int:
    rows, cols = len(matrix), len(matrix[0])
    ps = deepcopy(matrix)
    for r in range(1, rows):
        ps[r][0] += ps[r - 1][0]
    for c in range(1, cols):
        ps[0][c] += ps[0][c - 1]
    for r in range(1, rows):
        for c in range(1, cols):
            ps[r][c] += ps[r - 1][c] + ps[r][c - 1] - ps[r - 1][c - 1]

    vals = set()

    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    s = (
                        ps[r2][c2]
                        - (ps[r1 - 1][c2] if r1 >= 1 else 0)
                        - (ps[r2][c1 - 1] if c1 >= 1 else 0)
                        + (ps[r1 - 1][c1 - 1] if r1 >= 1 and c1 >= 1 else 0)
                    )
                    if s == k:
                        return s
                    vals.add(s)
    return max(v for v in vals if v <= k)


# O(m^2*n*log(n))
def max_sum_submatrix(matrix: list[list[int]], k: int) -> int:
    def get_max_sum(arr: list[int]) -> int:
        sorted_pre_sum = []
        ans = -inf
        running_sum = 0

        for num in arr:
            running_sum += num
            target_sum = running_sum - k
            idx = bisect.bisect_left(sorted_pre_sum, target_sum)
            if not sorted_pre_sum and running_sum <= k:
                ans = max(ans, running_sum)
            if idx < len(sorted_pre_sum):
                ans = max(ans, running_sum - sorted_pre_sum[idx])
            if ans == k:
                break
            bisect.insort(sorted_pre_sum, running_sum)

        return ans

    rows, cols = len(matrix), len(matrix[0])
    ps = []
    # calculate pre sum for each row
    for r in range(rows):
        row_ps = [0] * cols
        for c in range(cols):
            if c == 0:
                row_ps[c] = matrix[r][c]
            else:
                row_ps[c] = matrix[r][c] + row_ps[c - 1]
        ps.append(row_ps)

    ans = -inf

    # loop all of the col pairs
    for c2 in range(cols):
        for c1 in range(c2 + 1):
            # compress the rows between c1 and c2
            curr_arr = []
            for r in range(rows):
                row_sum = ps[r][c2] - (ps[r][c1 - 1] if c1 >= 1 else 0)
                curr_arr.append(row_sum)

            ans = max(ans, get_max_sum(curr_arr))
            if ans == k:
                return k

    return ans


if __name__ == "__main__":
    max_sum_submatrix([[2, 2, -1]], 0)
