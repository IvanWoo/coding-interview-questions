# https://leetcode.com/problems/add-strings/
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
from collections import defaultdict, deque


def add_strings(num1: str, num2: str) -> str:
    i1, i2 = len(num1) - 1, len(num2) - 1
    ans = []
    carry = 0

    while i1 >= 0 or i2 >= 0:
        x1 = ord(num1[i1]) - ord("0") if i1 >= 0 else 0
        x2 = ord(num2[i2]) - ord("0") if i2 >= 0 else 0

        carry, v = divmod(x1 + x2 + carry, 10)
        ans.append(v)
        i1 -= 1
        i2 -= 1

    if carry:
        ans.append(carry)

    return "".join(str(x) for x in ans[::-1])


def add_strings(num1: str, num2: str) -> str:
    def get_val(n: str) -> dict[int, int]:
        ans = defaultdict(int)
        for k, v in enumerate(n):
            ans[k] = int(v)
        return ans

    i1, i2 = len(num1) - 1, len(num2) - 1
    v1, v2 = get_val(num1), get_val(num2)
    carry = 0
    ans = deque()
    while i1 >= 0 or i2 >= 0:
        total = carry + v1[i1] + v2[i2]
        carry, val = divmod(total, 10)
        ans.appendleft(val)
        i1 -= 1
        i2 -= 1
    if carry:
        ans.appendleft(carry)
    return "".join((str(x) for x in ans))


if __name__ == "__main__":
    add_strings("0", "9")
