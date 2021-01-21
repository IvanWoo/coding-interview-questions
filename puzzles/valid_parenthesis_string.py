# https://leetcode.com/problems/valid-parenthesis-string/
"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True
Note:

The string size will be in the range [1, 100].
"""
from functools import lru_cache


def check_valid_string(s: str) -> bool:
    @lru_cache(None)
    def helper(s, idx, open):
        if idx == len(s):
            return open == 0
        if s[idx] == "(":
            return helper(s, idx + 1, open + 1)
        elif s[idx] == ")":
            return open != 0 and helper(s, idx + 1, open - 1)
        elif s[idx] == "*":
            return any(
                [
                    helper(s, idx + 1, open),
                    helper(s, idx + 1, open + 1),
                    open != 0 and helper(s, idx + 1, open - 1),
                ]
            )

    return helper(s, 0, 0)


if __name__ == "__main__":
    check_valid_string("((*)")
