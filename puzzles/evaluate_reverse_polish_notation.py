# https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operator may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

from collections import deque
from typing import List


def cal(operator, a, b):
    a, b = int(a), int(b)
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return int(float(a) / b)


def isdigit(x):
    return x not in set("+-*/")


def evalRPN(tokens: List[str]) -> int:
    stack = deque()

    while stack or tokens:
        if len(stack) >= 3 and isdigit(stack[-1]) and isdigit(stack[-2]):
            a = stack.pop()
            b = stack.pop()
            operator = stack.pop()

            val = cal(operator, a, b)
            stack.append(str(val))
            continue
        if tokens:
            cur_token = tokens.pop()
            stack.append(cur_token)
        if len(stack) == 1 and isdigit(stack[0]):
            return int(stack[0])
