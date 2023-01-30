# https://leetcode.com/problems/multiply-strings/
"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


def multiply(num1: str, num2: str) -> str:
    m, n = len(num1), len(num2)
    if not m or not n or num1 == "0" or num2 == "0":
        return "0"

    res = [0] * (m + n)
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            sum = mul + res[p2]
            res[p2] = sum % 10
            res[p1] += sum // 10

    i = 0
    for i in range(m + n):
        if i != 0:
            break
    return "".join([str(x) for x in res[i:]])


if __name__ == "__main__":
    multiply("123", "456")
