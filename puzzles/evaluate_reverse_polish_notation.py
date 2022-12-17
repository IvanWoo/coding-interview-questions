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


def evalRPN(tokens: list[str]) -> int:
    stack = []
    for tk in tokens:
        if tk in ["+", "-", "*", "/"]:
            v2 = stack.pop()
            v1 = stack.pop()
            match tk:
                case "+":
                    res = v1 + v2
                case "-":
                    res = v1 - v2
                case "*":
                    res = v1 * v2
                case "/":
                    res = int(v1 / v2)
            stack.append(res)
            continue
        stack.append(int(tk))
    return stack.pop()
