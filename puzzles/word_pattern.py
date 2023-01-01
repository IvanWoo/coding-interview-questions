# https://leetcode.com/problems/word-pattern/
"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


def word_pattern(pattern: str, s: str) -> bool:
    def get_idx(m, target):
        for i, v in enumerate(m):
            if v == target:
                return i
        return -1

    s_list = s.split()
    np, ns = len(pattern), len(s_list)
    if np != ns:
        return False
    map_p, map_s = [], []
    for i in range(np):
        cur_p, cur_s = pattern[i], s_list[i]
        i_p, i_s = get_idx(map_p, cur_p), get_idx(map_s, cur_s)
        if i_p != i_s:
            return False
        if i_p == -1:
            map_p.append(cur_p)
            map_s.append(cur_s)
    return True


def word_pattern(pattern: str, s: str) -> bool:
    s_list = s.split()
    np, ns = len(pattern), len(s_list)
    if np != ns:
        return False

    mp, ms = {}, {}
    for p, c in zip(pattern, s_list):
        if p not in mp:
            mp[p] = c
        if c not in ms:
            ms[c] = p
        if (mp[p], ms[c]) != (c, p):
            return False
    return True
