# https://leetcode.com/problems/add-binary/
"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
from collections import deque


def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


def add_binary(a: str, b: str) -> str:
    carry = 0
    ans = deque()
    a = list(a)
    b = list(b)
    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        carry, curr = divmod(carry, 2)
        ans.appendleft(curr)
    return "".join((str(x) for x in ans))
