# https://leetcode.com/problems/remove-duplicate-letters/
"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""
from collections import Counter


def remove_duplicate_letters(s: str) -> str:
    if not s:
        return ""
    count = Counter(list(s))

    pos = 0
    for i, x in enumerate(s):
        if x < s[pos]:
            pos = i
        count[x] -= 1
        if count[x] == 0:
            break
    return s[pos] + remove_duplicate_letters(s[pos + 1 :].replace(s[pos], ""))


def remove_duplicate_letters(s: str) -> str:
    rindex = {c: i for i, c in enumerate(s)}
    result = ""
    for i, c in enumerate(s):
        if c not in result:
            while c < result[-1:] and i < rindex[result[-1]]:
                result = result[:-1]
            result += c
    return result


if __name__ == "__main__":
    remove_duplicate_letters("cbacdcbc")
