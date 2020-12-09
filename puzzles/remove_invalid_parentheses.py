# https://leetcode.com/problems/remove-invalid-parentheses/
"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all potemp_sible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]
"""
from typing import List
from functools import lru_cache


def remove_invalid_parentheses(s: str) -> List[str]:
    def get_max_len():
        diff = 0
        max_len = 0
        for char in s:
            if char == "(":
                diff += 1
            elif char == ")":
                if diff == 0:
                    continue
                diff -= 1
            max_len += 1
        max_len -= diff
        return max_len

    @lru_cache(None)
    def helper(temp_s, i, diff):
        nonlocal res
        n = len(s)
        if len(temp_s) + n - i < max_len:
            return
        if i == n and diff == 0:
            res.add(temp_s)
            return
        for j in range(i, n):
            if s[j] == "(":
                helper(temp_s + s[j], j + 1, diff + 1)
                helper(temp_s, j + 1, diff)
            elif s[j] == ")":
                if diff == 0:
                    helper(temp_s, j + 1, diff)
                else:
                    helper(temp_s + s[j], j + 1, diff - 1)
            else:
                helper(temp_s + s[j], j + 1, diff)
        return

    max_len = get_max_len()
    res = set()
    helper("", 0, 0)

    return list(res)


if __name__ == "__main__":
    remove_invalid_parentheses("()())()")
