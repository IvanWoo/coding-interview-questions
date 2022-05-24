# https://leetcode.com/problems/longest-valid-parentheses/
"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

from collections import deque

# stack
def longest_valid_parentheses(s: str) -> int:
    stack = deque()
    leftmost = -1
    ans = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else leftmost))
            else:
                leftmost = i
    return ans


# two pass
# space O(1)
def longest_valid_parentheses(s: str) -> int:
    def count(i, l, r):
        if s[i] == "(":
            l += 1
        elif s[i] == ")":
            r += 1
        return l, r

    n = len(s)
    ans = 0
    # left to right
    l = r = 0
    for i in range(n):
        l, r = count(i, l, r)

        if l == r:
            ans = max(ans, 2 * l)
        elif r > l:
            l = r = 0

    # right to left
    l = r = 0
    for i in reversed(range(n)):
        l, r = count(i, l, r)

        if l == r:
            ans = max(ans, 2 * l)
        elif l > r:
            l = r = 0

    return ans


if __name__ == "__main__":
    longest_valid_parentheses(")()())")
