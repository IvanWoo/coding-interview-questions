# https://leetcode.com/problems/maximum-sum-circular-subarray/
"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)


Example 1:
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 
Note:
-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""
from typing import List

# O(n^2)
def max_subarray_sum_circular(A: List[int]) -> int:
    n = len(A)
    a = A + A
    res = float("-inf")

    prefix_sum = [0] * 2 * n
    prefix_sum[0] = a[0]
    for i in range(1, 2 * n):
        prefix_sum[i] += prefix_sum[i - 1] + a[i]

    for i in range(n):
        for j in range(i, i + n):
            res = max(res, prefix_sum[j + 1] - prefix_sum[i])
    return res


# Kadane’s Algorithm
def max_subarray_sum_circular(A: List[int]):
    ans = 0
    cmin = 0
    cmax = 0
    total = sum(A)
    for x in A:
        cmin = min(0, cmin + x)
        cmax = max(0, cmax + x)
        ans = max([ans, cmax, total - cmin])
    return ans if ans > 0 else max(A)


if __name__ == "__main__":
    max_subarray_sum_circular([-2, -3, -1])
