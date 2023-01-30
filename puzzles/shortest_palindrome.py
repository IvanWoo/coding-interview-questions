# https://leetcode.com/problems/shortest-palindrome/
"""
Given a string s, you can convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"

Constraints:
0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
"""


# TLE
def shortest_palindrome(s: str) -> str:
    def expand(s, left, right):
        if right >= len(s):
            return ""
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                return ""
            left -= 1
            right += 1
        if left >= 0:
            return ""
        return s[right:][::-1] + s

    if not s:
        return ""
    res = None
    n = len(s)

    for i in range(n):
        temp_res = expand(s, i, i)
        if temp_res:
            if not res:
                res = temp_res
            else:
                if len(temp_res) < len(res):
                    res = temp_res
        temp_res = expand(s, i, i + 1)
        if temp_res:
            if not res:
                res = temp_res
            else:
                if len(temp_res) < len(res):
                    res = temp_res
    return res


def shortest_palindrome(s: str) -> str:
    r = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(r[i:]):
            return r[:i] + s


if __name__ == "__main__":
    shortest_palindrome("aacecaaa")
