# https://leetcode.com/problems/basic-calculator/
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

# TLE: too ugly...
def calculate(s: str) -> int:
    n = len(s)
    i = 0
    res = 0
    op = None
    while i < n:
        if s[i] == " ":
            i += 1
        elif s[i] in "-+":
            op = s[i]
            i += 1
        else:
            if s[i] == "(":
                i += 1
                start = i
                balance = -1
                while balance != 0:
                    if s[i] == "(":
                        balance -= 1
                    elif s[i] == ")":
                        balance += 1
                    i += 1
                end = i - 1
                temp_res = calculate(s[start:end])
                i -= 1
            elif s[i].isdigit():
                start = i
                while i < n and s[i].isdigit():
                    i += 1
                temp_res = int(s[start:i])
                i -= 1

            if op:
                new_res = res - temp_res if op == "-" else res + temp_res
                op = None
            else:
                new_res = temp_res
            res = new_res
            i += 1
    return res


def calculate(s: str) -> int:
    res, num, sign, stack = 0, 0, 1, []
    for char in s:
        if char.isdigit():
            num = 10 * num + int(char)
        elif char in "-+":
            res += sign * num
            num = 0
            sign = [-1, 1][char == "+"]
        elif char == "(":
            stack.append(res)
            stack.append(sign)
            sign, res = 1, 0
        elif char == ")":
            res += sign * num
            res *= stack.pop()
            res += stack.pop()
            num = 0
    return res + num * sign


if __name__ == "__main__":
    calculate("1+(4+5+2)-3")
