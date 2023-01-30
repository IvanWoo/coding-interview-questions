# https://leetcode.com/problems/different-ways-to-add-parentheses/
"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1:
Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""
from typing import List


def diff_ways_to_compute(input: str) -> List[int]:
    def helper(input):
        if input not in memo:
            if input.isdigit():
                return [int(input)]
            res = []
            for i, c in enumerate(input):
                if c in "+-*":
                    l = helper(input[:i])
                    r = helper(input[i + 1 :])
                    res.extend(eval(f"{x}{c}{y}") for x in l for y in r)
            memo[input] = res
        return memo[input]

    memo = {}
    return helper(input)


if __name__ == "__main__":
    diff_ways_to_compute("2-1-1")
