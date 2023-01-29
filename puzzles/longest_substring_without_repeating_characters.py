# https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict


# sliding window: O(n)
def length_of_longest_substring(s: str) -> int:
    lo, hi = 0, 0
    window = defaultdict(int)
    res = 0
    while hi < len(s):
        c1 = s[hi]
        hi += 1
        window[c1] += 1
        while window[c1] > 1:
            c2 = s[lo]
            lo += 1
            window[c2] -= 1
        res = max(res, hi - lo)
    return res


# brute force: O(n^2)
def length_of_longest_substring(s: str) -> int:
    n = len(s)
    res = min(1, n)
    for i in range(n):
        counter = set([s[i]])
        for j in range(i + 1, n):
            char = s[j]
            if char in counter:
                res = max(res, len(counter))
                counter = set()
                break
            counter.add(char)
        res = max(res, len(counter))
    return res
