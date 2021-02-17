# https://leetcode.com/problems/shortest-bridge/
"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:
Input: A = [[0,1],[1,0]]
Output: 1

Example 2:
Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
2 <= A.length == A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""
from typing import List


def print_matrix(mat):
    for r in range(len(mat)):
        print(mat[r])


def shortest_bridge(A: List[List[int]]) -> int:
    def paint(A, r, c):
        row, col = len(A), len(A[0])
        A[r][c] = 2
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r + i, c + j
            if 0 <= new_r < row and 0 <= new_c < col and A[new_r][new_c] == 1:
                paint(A, new_r, new_c)

    row, col = len(A), len(A[0])
    done = False
    for r in range(row):
        for c in range(col):
            if A[r][c]:
                paint(A, r, c)
                done = True
                break
        if done:
            break

    # can generate q while paining, but don't like it
    q = []
    for r in range(row):
        for c in range(col):
            if A[r][c] == 2:
                q.append((r, c))
    while q:
        new_q = []
        while q:
            cur_r, cur_c = q.pop()
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = cur_r + i, cur_c + j
                if 0 <= new_r < row and 0 <= new_c < col:
                    if A[new_r][new_c] == 0:
                        A[new_r][new_c] = A[cur_r][cur_c] + 1
                        new_q.append((new_r, new_c))
                    elif A[new_r][new_c] == 1:
                        return A[cur_r][cur_c] - 2
        q = new_q


if __name__ == "__main__":
    shortest_bridge([[1, 0], [0, 1]])
