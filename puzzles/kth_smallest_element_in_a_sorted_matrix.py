# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:
Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""
from heapq import heappop, heappush, heappushpop


# brute force
def kth_smallest(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)
    nums = [matrix[r][c] for r in range(n) for c in range(n)]
    return sorted(nums)[k - 1]


# min heap
def kth_smallest(matrix: list[list[int]], k: int) -> int:
    q = []
    n = len(matrix)
    limit = n**2 - k + 1
    for r in range(n):
        for c in range(n):
            heappush(q, matrix[r][c])
            if len(q) > limit:
                heappop(q)
    return q[0]


# max heap
def kth_smallest(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)
    q = []
    for r in range(n):
        for c in range(n):
            if (r + 1) * (c + 1) > k:
                break
            val = matrix[r][c]
            if len(q) < k:
                heappush(q, -val)
            else:
                if val < -q[0]:
                    heappushpop(q, -val)
    return -q[0]


if __name__ == "__main__":
    kth_smallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 6)
