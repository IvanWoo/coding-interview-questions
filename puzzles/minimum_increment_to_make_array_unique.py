# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
"""
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

Example 1:
Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].

Example 2:
Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

Note:
0 <= A.length <= 40000
0 <= A[i] < 40000
"""
from collections import Counter
from typing import List


def min_increment_for_unique(A: List[int]) -> int:
    ans = 0
    c = Counter(A)
    for i in range(80000):
        if i in c and c[i] > 1:
            ans += c[i] - 1
            c[i + 1] += c[i] - 1
    return ans


def min_increment_for_unique(A: List[int]) -> int:
    ans = 0
    need = 0
    for i in sorted(A):
        ans += max(need - i, 0)
        need = max(need, i) + 1
    return ans


if __name__ == "__main__":
    min_increment_for_unique([3, 2, 1, 2, 1, 7])
