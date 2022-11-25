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
from math import inf

# O(n^2)
def sum_subarray_mins(A: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(A)
    ans = 0
    for i in range(n):
        cur_min = inf
        for j in range(i, n):
            cur_min = min(cur_min, A[j])
            ans += cur_min
    return ans % MOD


# monotonic stack: O(n)
def sum_subarray_mins(A: list[int]) -> int:
    n = len(A)
    MOD = 10**9 + 7
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


# monotonic stack: O(n)
def sum_subarray_mins(A: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(A)
    res = 0
    stack = []
    for i in range(n + 1):
        while stack and (i == n or A[stack[-1]] >= A[i]):
            mid = stack.pop()
            left = -1 if not stack else stack[-1]
            right = i
            res += (mid - left) * (right - mid) * A[mid]
        stack.append(i)
    return res % MOD


if __name__ == "__main__":
    sum_subarray_mins([3, 1, 2, 4])
