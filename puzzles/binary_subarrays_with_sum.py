# https://leetcode.com/problems/binary-subarrays-with-sum/
"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:
Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 
Note:
A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""
from typing import List
from collections import defaultdict


# O(n^2)
def num_subarrays_with_sum(A: List[int], S: int) -> int:
    n = len(A)
    prefix_sum = [0] + A[:]
    for i in range(1, n + 1):
        prefix_sum[i] += prefix_sum[i - 1]

    res = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if (prefix_sum[j] - prefix_sum[i]) == S:
                res += 1
    return res


def num_subarrays_with_sum(A: List[int], S: int) -> int:
    count = defaultdict(int)
    count[0] = 1
    psum = res = 0
    for x in A:
        psum += x
        res += count[psum - S]
        count[psum] += 1
    return res


if __name__ == "__main__":
    num_subarrays_with_sum([0, 0, 0, 0, 0], 0)
