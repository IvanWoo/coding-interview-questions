# https://leetcode.com/problems/validate-stack-sequences/
"""
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.


Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Constraints:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""


def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
    n = len(pushed)
    i = 0
    stack = []

    for x in pushed:
        stack.append(x)
        while stack and i < n and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return i == n
