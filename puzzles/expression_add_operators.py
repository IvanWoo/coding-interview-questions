# https://leetcode.com/problems/expression-add-operators/
"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.


Example 1:
Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:
Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:
Input: num = "3456237490", target = 9191
Output: []
 

Constraints:
0 <= num.length <= 10
num only contain digits.
Accepted
118,040
Submissions
325,350
"""
from functools import lru_cache
from typing import List


def add_operators(num: str, target: int) -> List[str]:
    @lru_cache(None)
    def get_prefix(expression):
        n = len(expression)
        i = n - 1
        while i >= 0:
            if expression[i] in "*+-":
                break
            i -= 1
        return expression[0] if i == 0 else expression[i + 1]

    @lru_cache(None)
    def cal(i, expression):
        if i == len(num):
            if not expression:
                return []
            if eval(expression) == target:
                return [expression]
            else:
                return []

        plus, minus, mul, null = [], [], [], []
        if expression == "" or get_prefix(expression) != "0":
            null = cal(i + 1, expression + num[i])
        if expression:
            plus = cal(i + 1, expression + f"+{num[i]}")
            minus = cal(i + 1, expression + f"-{num[i]}")
            mul = cal(i + 1, expression + f"*{num[i]}")

        return plus + minus + mul + null

    return cal(0, "")


if __name__ == "__main__":
    add_operators(num="232", target=8)
