# https://leetcode.com/problems/sum-of-subarray-minimums/
"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

Note:
1 <= A.length <= 30000
1 <= A[i] <= 30000
"""
from typing import List


# O(n^2)
def sum_subarray_mins(A: List[int]) -> int:
    n = len(A)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ans += min(A[i : j + 1])
    return ans


# monotonic stack: O(n)
def sum_subarray_mins(A: List[int]) -> int:
    n = len(A)
    MOD = 1e9 + 7
    left, right = [0] * n, [0] * n
    s1, s2 = [], []
    for i in range(n):
        count = 1
        while s1 and s1[-1][0] > A[i]:
            count += s1.pop()[1]
        left[i] = count
        s1.append([A[i], count])
    for i in reversed(range(n)):
        count = 1
        while s2 and s2[-1][0] >= A[i]:
            count += s2.pop()[1]
        right[i] = count
        s2.append([A[i], count])
    return sum(a * l * r for a, l, r in zip(A, left, right)) % MOD


def sum_subarray_mins(A: List[int]) -> int:
    MOD = 1e9 + 7
    res = 0
    s = []
    A = [0] + A + [0]
    for i, x in enumerate(A):
        while s and A[s[-1]] > x:
            j = s.pop()
            k = s[-1]
            res += A[j] * (i - j) * (j - k)
        s.append(i)
    return res % MOD


if __name__ == "__main__":
    sum_subarray_mins([3, 1, 2, 4])
