# https://leetcode.com/problems/similar-string-groups/
"""
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

Example 1:
Input: strs = ["tars","rats","arts","star"]
Output: 2

Example 2:
Input: strs = ["omv","ovm"]
Output: 1

Constraints:
1 <= strs.length <= 100
1 <= strs[i].length <= 1000
sum(strs[i].length) <= 2 * 104
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
"""
from typing import List


def num_similar_groups(strs: List[str]) -> int:
    class UF:
        def __init__(self, n) -> None:
            self.parent = list(range(n))
            self.count = n

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

    def is_similar(s1, s2):
        n = len(s1)
        diff = 0
        for i in range(n):
            if s1[i] != s2[i]:
                diff += 1
        return diff <= 2

    n = len(strs)
    uf = UF(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_similar(strs[i], strs[j]):
                uf.union(i, j)
    return uf.count


if __name__ == "__main__":
    num_similar_groups(["tars", "rats", "arts", "star"])
