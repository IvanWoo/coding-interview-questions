# https://leetcode.com/problems/couples-holding-hands/
"""
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:
Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:
Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.

Note:
len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
"""
from typing import List


def min_swaps_couples(row: List[int]) -> int:
    class UF:
        def __init__(self, n):
            self.count = n
            self.parent = list(range(n))

        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(self, u, v):
            root_u, root_v = self.find(u), self.find(v)
            if root_u == root_v:
                return
            self.parent[root_u] = root_v
            self.count -= 1

    n = len(row) // 2
    uf = UF(n)
    for i in range(n):
        a = row[2 * i]
        b = row[2 * i + 1]
        uf.union(a // 2, b // 2)
    return n - uf.count


if __name__ == "__main__":
    min_swaps_couples([5, 4, 2, 6, 3, 1, 0, 7])
