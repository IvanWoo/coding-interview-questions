# https://leetcode.com/problems/smallest-string-with-swaps/
"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
You can swap the characters at any pair of indices in the given pairs any number of times.
Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"


Constraints:
1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""
from collections import defaultdict
from typing import List

from puzzles.union_find import UF


def smallest_string_with_swaps(s: str, pairs: List[List[int]]) -> str:
    n = len(s)
    uf = UF(n)
    for u, v in pairs:
        uf.union(u, v)

    groups = defaultdict(list)
    for i in range(n):
        groups[uf.find(i)].append(i)

    res = list(s)
    for _, v in groups.items():
        # because we can swap any number of times
        # we take greedy approach to make sure every group is sorted lexicographically
        temp_res = sorted([s[i] for i in v])
        for _k, _v in enumerate(sorted(v)):
            res[_v] = temp_res[_k]

    return "".join(res)


if __name__ == "__main__":
    smallest_string_with_swaps(s="dcab", pairs=[[0, 3], [1, 2]])
