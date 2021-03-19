# https://leetcode.com/problems/largest-sum-of-averages/
"""
We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Note:
1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.
"""
from typing import List
from functools import lru_cache


def largest_sum_of_averages(A: List[int], K: int) -> float:
    def avg(a):
        return sum(a) / len(a)

    @lru_cache(None)
    def helper(start, end, left):
        n = end - start
        if n == 0 or left == 0 or n < left:
            return float("-inf")
        if left == 1:
            return avg(A[start:end])
        if n == left:
            return sum(A[start:end])
        ans = 0
        for i in range(1, n):
            for j in range(left):
                ans = max(
                    [
                        ans,
                        helper(start, start + i, left - j) + helper(start + i, end, j),
                        helper(start, start + i, j) + helper(start + i, end, left - j),
                    ]
                )
        return ans

    return helper(0, len(A), K)


if __name__ == "__main__":
    largest_sum_of_averages([9, 1, 2, 3, 9], 3)
