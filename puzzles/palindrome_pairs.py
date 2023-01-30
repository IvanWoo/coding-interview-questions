# https://leetcode.com/problems/palindrome-pairs/
"""
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:
Input: words = ["a",""]
Output: [[0,1],[1,0]]

Constraints:
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
"""

from __future__ import annotations

from dataclasses import dataclass, field


# TLE
def palindrome_pairs(words: list[str]) -> list[list[int]]:
    def is_palindrome(s):
        return s == s[::-1]

    n = len(words)
    res = []
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            if is_palindrome(words[i] + words[j]):
                res.append([i, j])
    return res


def palindrome_pairs(words: list[str]) -> list[list[int]]:
    @dataclass
    class TrieNode:
        word_idx: int = -1
        children: dict[str, TrieNode] = field(default_factory=dict)
        rest_is_palindrome: list[int] = field(default_factory=list)

    class Trie:
        def __init__(self):
            self.root = TrieNode()

        def is_palindrome(self, word: str, lo: int, hi: int) -> bool:
            while lo <= hi:
                if word[lo] != word[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        def add(self, word: str, idx: int):
            cur = self.root
            # add the word reversely to make the search feasible
            n = len(word)
            for i in reversed(range(n)):
                if self.is_palindrome(word, 0, i):
                    cur.rest_is_palindrome.append(idx)

                char = word[i]
                if char not in cur.children:
                    cur.children[char] = TrieNode()

                cur = cur.children[char]
            cur.word_idx = idx

        def search(self, word: str, idx: int, ans: list):
            cur = self.root
            for i, char in enumerate(word):
                # case 0: xyzll|zyx
                if cur.word_idx != -1 and self.is_palindrome(word, i, len(word) - 1):
                    ans.append([idx, cur.word_idx])

                if char not in cur.children:
                    break

                cur = cur.children[char]
            else:
                # only run when no break happened above
                # case 1: abcd|dcba, aaa
                if cur.word_idx != -1 and cur.word_idx != idx:
                    ans.append([idx, cur.word_idx])

                # case 2: zyx|xyzll
                for k in cur.rest_is_palindrome:
                    ans.append([idx, k])

    t = Trie()
    ans = []

    for i, word in enumerate(words):
        t.add(word, i)

    for i, word in enumerate(words):
        t.search(word, i, ans)

    return ans


def palindrome_pairs(words: list[str]) -> list[list[int]]:
    d = {w: i for i, w in enumerate(words)}
    ans = []
    for i, w in enumerate(words):
        # case 0:
        rev_w = w[::-1]
        if rev_w in d and d[rev_w] != i:
            ans.append([i, d[rev_w]])
        if w != "" and rev_w == w and "" in d:
            ans.append([i, d[""]])
            ans.append([d[""], i])

        for k in range(1, len(w)):
            # case 1:
            s1, s2 = w[:k], w[k:]
            if s1 == s1[::-1] and s2[::-1] in d:
                ans.append([d[s2[::-1]], i])
            # case 2:
            if s2 == s2[::-1] and s1[::-1] in d:
                ans.append([i, d[s1[::-1]]])

    return ans


if __name__ == "__main__":
    palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
