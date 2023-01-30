# https://leetcode.com/problems/array-nesting/
"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.



Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}


Note:

N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
"""
from typing import List


# TLE: O(N^2)
def array_nesting(nums: List[int]) -> int:
    n = len(nums)
    res = 0
    for num in nums:
        path = set()
        while num not in path:
            path.add(num)
            num = nums[num]
        res = max(res, len(path))
    return res


# O(N)
def array_nesting(nums: List[int]) -> int:
    n = len(nums)
    visited = [False] * n
    res = 0
    for num in nums:
        if not visited[num]:
            path = set()
            while num not in path:
                visited[num] = True
                path.add(num)
                num = nums[num]
            res = max(res, len(path))
    return res


if __name__ == "__main__":
    array_nesting([5, 4, 0, 3, 1, 6, 2])
