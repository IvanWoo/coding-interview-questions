# https://leetcode.com/problems/find-and-replace-pattern/
"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 
Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""
from collections import defaultdict


def find_and_replace_pattern(words: list[str], pattern: str) -> list[str]:
    def translate(word):
        dic = defaultdict(int)
        # random big number to hold tokens
        token = iter(range(1, 100))
        res = [0] * len(word)
        for i, c in enumerate(word):
            if not dic[c]:
                dic[c] = next(token)
            res[i] = dic[c]
        return res

    def translate(word):
        return [word.find(c) for c in word]

    return [w for w in words if translate(w) == translate(pattern)]


def find_and_replace_pattern(words: list[str], pattern: str) -> list[str]:
    def match(word):
        m1, m2 = {}, {}
        for w, p in zip(word, pattern):
            if w not in m1:
                m1[w] = p
            if p not in m2:
                m2[p] = w
            if (m1[w], m2[p]) != (p, w):
                return False
        return True

    return list(filter(match, words))
