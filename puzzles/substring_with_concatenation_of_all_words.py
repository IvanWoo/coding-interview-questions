# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
 
Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""

from collections import Counter
from typing import List


def find_substring(s: str, words: List[str]) -> List[int]:
    l = len(words[0])
    c = Counter(words)
    n = sum([len(word) for word in words])
    ans = []
    for i in range(len(s) - n + 1):
        sub_s = s[i : i + n]
        temp_c = Counter([sub_s[i : i + l] for i in range(0, n, l)])
        if temp_c == c:
            ans.append(i)
    return ans
