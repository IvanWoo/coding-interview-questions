# https://leetcode.com/problems/maximum-product-of-word-lengths/
"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".

Example 3:
Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
 
Constraints:

0 <= words.length <= 10^3
0 <= words[i].length <= 10^3
words[i] consists only of lowercase English letters.
"""
from collections import defaultdict

# bit manipulation
def max_product(words: list[str]) -> int:
    d = defaultdict(int)
    for w in words:
        mask = 0
        for c in set(w):
            mask |= 1 << (ord(c) - ord("a"))
        d[mask] = max(d[mask], len(w))
    res = 0
    for x in d:
        for y in d:
            if x & y == 0:
                res = max(res, d[x] * d[y])
    return res
